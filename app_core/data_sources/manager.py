from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import time
from typing import Any

from app_core.data_sources.akshare_provider import (
    SOURCE_NAME as AKSHARE_SOURCE_NAME,
    fetch_stock_daily_history,
    summarize_fetch_error,
)
from app_core.data_sources.base import DataSourceCapability, DataSourceRequest, DataSourceResult
from app_core.data_sources.local_cache_provider import (
    SOURCE_NAME as LOCAL_CACHE_SOURCE_NAME,
    get_cache_metadata,
    load_stock_daily_history_from_cache,
)


DEFAULT_PRIMARY_SOURCE = "akshare"
DEFAULT_FALLBACK_ORDER = [AKSHARE_SOURCE_NAME, LOCAL_CACHE_SOURCE_NAME]
DEFAULT_LOCAL_CACHE_MAX_AGE_DAYS = 7


@dataclass(slots=True)
class RegisteredDataSource:
    name: str
    capabilities: tuple[DataSourceCapability, ...]


class DataSourceManager:
    def __init__(self, settings: dict[str, Any] | None = None) -> None:
        self._settings = settings or {}
        self._source_settings = self._normalize_source_settings(self._settings.get("data_sources", {}))
        self._sources: dict[str, RegisteredDataSource] = {}
        self._register_default_sources()

    def list_sources(self) -> list[str]:
        return list(self._sources.keys())

    def get_primary_source(self) -> str:
        configured_primary = str(self._source_settings.get("primary", DEFAULT_PRIMARY_SOURCE)).strip() or DEFAULT_PRIMARY_SOURCE
        if configured_primary in self._sources:
            return configured_primary
        if DEFAULT_PRIMARY_SOURCE in self._sources:
            return DEFAULT_PRIMARY_SOURCE
        return next(iter(self._sources.keys()), DEFAULT_PRIMARY_SOURCE)

    def get_fallback_order(self) -> list[str]:
        order = [
            source
            for source in self._source_settings.get("fallback_order", DEFAULT_FALLBACK_ORDER)
            if source in self._sources
        ]
        if not order:
            return [self.get_primary_source()]
        return order

    def is_fallback_enabled(self) -> bool:
        return bool(self._source_settings.get("enable_fallback", True))

    def get_health_check_symbol(self) -> str:
        raw_value = str(self._source_settings.get("health_check_symbol", "000001")).strip()
        return raw_value or "000001"

    def get_local_cache_settings(self) -> dict[str, Any]:
        return dict(self._source_settings.get("local_cache", {}))

    def is_local_cache_enabled(self) -> bool:
        return bool(self.get_local_cache_settings().get("enabled", True))

    def get_local_cache_max_age_days(self) -> int:
        raw_value = self.get_local_cache_settings().get("max_age_days", DEFAULT_LOCAL_CACHE_MAX_AGE_DAYS)
        try:
            return max(1, int(raw_value))
        except (TypeError, ValueError):
            return DEFAULT_LOCAL_CACHE_MAX_AGE_DAYS

    def is_local_cache_stale(self, age_seconds: int | None) -> bool:
        if age_seconds is None:
            return False
        return age_seconds > self.get_local_cache_max_age_days() * 86400

    def allow_stale_local_cache(self) -> bool:
        return bool(self.get_local_cache_settings().get("allow_stale", True))

    def inspect_local_cache(self, symbol: str) -> dict[str, Any]:
        metadata = get_cache_metadata(symbol)
        metadata["available"] = bool(metadata.get("path"))
        metadata["enabled"] = self.is_local_cache_enabled()
        metadata["max_age_days"] = self.get_local_cache_max_age_days()
        metadata["allow_stale"] = self.allow_stale_local_cache()
        metadata["stale"] = self.is_local_cache_stale(metadata.get("age_seconds"))
        return metadata

    def fetch_stock_daily_history(
        self,
        symbol: str,
        timeout_seconds: int = 10,
    ) -> DataSourceResult:
        request = DataSourceRequest(
            symbol=symbol,
            code=symbol,
            timeout_seconds=timeout_seconds,
        )
        source_name = self.get_primary_source()
        started_at = time.perf_counter()

        try:
            raw_dataframe, normalized_dataframe = fetch_stock_daily_history(
                symbol,
                timeout_seconds=timeout_seconds,
            )
            elapsed_ms = int((time.perf_counter() - started_at) * 1000)
            return DataSourceResult(
                source_name=source_name,
                ok=True,
                data={
                    "raw_dataframe": raw_dataframe,
                    "normalized_dataframe": normalized_dataframe,
                },
                elapsed_ms=elapsed_ms,
                fetched_at=datetime.now(),
                fallback_used=False,
                metadata={
                    "request": request,
                    "primary_source": source_name,
                    "fallback_order": self.get_fallback_order(),
                    "row_count": len(normalized_dataframe),
                },
            )
        except Exception as error:  # pragma: no cover - error path validated via monkeypatch tests
            elapsed_ms = int((time.perf_counter() - started_at) * 1000)
            error_message = summarize_fetch_error(error, timeout_seconds=timeout_seconds)
            error_type = error_message.split(":", maxsplit=1)[0] if ":" in error_message else type(error).__name__

            should_try_local_cache = (
                self.is_fallback_enabled()
                and self.is_local_cache_enabled()
                and LOCAL_CACHE_SOURCE_NAME in self.get_fallback_order()
            )
            if should_try_local_cache:
                cache_metadata = self.inspect_local_cache(symbol)
                if not cache_metadata.get("available"):
                    error_message = f"{error_message}; local cache unavailable"
                elif cache_metadata.get("stale") and not cache_metadata.get("allow_stale", True):
                    error_message = f"{error_message}; local cache stale and disabled"
                else:
                    try:
                        raw_dataframe, normalized_dataframe = load_stock_daily_history_from_cache(symbol)
                        cache_status = "stale_cache" if cache_metadata.get("stale") else "cache_fallback"
                        fallback_message = f"{error_message}; using local cache fallback"
                        return DataSourceResult(
                            source_name=LOCAL_CACHE_SOURCE_NAME,
                            ok=True,
                            data={
                                "raw_dataframe": raw_dataframe,
                                "normalized_dataframe": normalized_dataframe,
                            },
                            error_message=fallback_message,
                            error_type=error_type,
                            elapsed_ms=elapsed_ms,
                            fetched_at=datetime.now(),
                            fallback_used=True,
                            metadata={
                                "request": request,
                                "primary_source": source_name,
                                "fallback_order": self.get_fallback_order(),
                                "primary_error_message": error_message,
                                "cache_path": cache_metadata.get("path", ""),
                                "cache_modified_at": cache_metadata.get("modified_at", ""),
                                "cache_age_seconds": cache_metadata.get("age_seconds"),
                                "cache_row_count": cache_metadata.get("row_count", 0),
                                "cache_status": cache_status,
                                "max_age_days": cache_metadata.get("max_age_days"),
                                "allow_stale": cache_metadata.get("allow_stale"),
                                "stale": cache_metadata.get("stale", False),
                            },
                        )
                    except Exception as cache_error:
                        cache_message = str(cache_error).strip() or "invalid local cache"
                        error_message = f"{error_message}; {cache_message}"

            return DataSourceResult(
                source_name=source_name,
                ok=False,
                data=None,
                error_message=error_message,
                error_type=error_type,
                elapsed_ms=elapsed_ms,
                fetched_at=datetime.now(),
                fallback_used=False,
                metadata={
                    "request": request,
                    "primary_source": source_name,
                    "fallback_order": self.get_fallback_order(),
                    "registered_sources": self.list_sources(),
                },
            )

    def _register_default_sources(self) -> None:
        self._sources[AKSHARE_SOURCE_NAME] = RegisteredDataSource(
            name=AKSHARE_SOURCE_NAME,
            capabilities=(
                DataSourceCapability.STOCK_DAILY,
                DataSourceCapability.MARKET_INDEX,
                DataSourceCapability.SECTOR_BOARD,
            ),
        )
        self._sources[LOCAL_CACHE_SOURCE_NAME] = RegisteredDataSource(
            name=LOCAL_CACHE_SOURCE_NAME,
            capabilities=(DataSourceCapability.STOCK_DAILY,),
        )

    @staticmethod
    def _normalize_source_settings(raw_settings: dict[str, Any]) -> dict[str, Any]:
        fallback_order = raw_settings.get("fallback_order")
        if not isinstance(fallback_order, list) or not fallback_order:
            fallback_order = list(DEFAULT_FALLBACK_ORDER)

        return {
            "primary": raw_settings.get("primary", DEFAULT_PRIMARY_SOURCE),
            "fallback_order": [str(item).strip() for item in fallback_order if str(item).strip()],
            "enable_fallback": raw_settings.get("enable_fallback", True),
            "health_check_symbol": raw_settings.get("health_check_symbol", "000001"),
            "local_cache": {
                "enabled": raw_settings.get("local_cache", {}).get("enabled", True),
                "max_age_days": raw_settings.get("local_cache", {}).get("max_age_days", DEFAULT_LOCAL_CACHE_MAX_AGE_DAYS),
                "allow_stale": raw_settings.get("local_cache", {}).get("allow_stale", True),
            },
        }
