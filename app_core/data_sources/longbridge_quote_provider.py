from __future__ import annotations

import os
from datetime import datetime
from typing import Any

try:
    import longbridge as lb  # type: ignore
    LONGBRIDGE_IMPORT_ERROR: BaseException | None = None
except Exception as error:  # pragma: no cover - depends on runtime env
    lb = None  # type: ignore
    LONGBRIDGE_IMPORT_ERROR = error


REQUIRED_ENV_KEYS = ("LONGBRIDGE_APP_KEY", "LONGBRIDGE_APP_SECRET", "LONGBRIDGE_ACCESS_TOKEN")
OPTIONAL_ENV_KEYS = ("LONGBRIDGE_REGION", "LONGBRIDGE_HTTP_URL", "LONGBRIDGE_QUOTE_WS_URL")


class LongbridgeQuoteProvider:
    """Longbridge 只读实时行情 Provider (候选数据源)。"""

    def __init__(self) -> None:
        self.provider_name = "longbridge"

    def check_status(self) -> dict[str, Any]:
        sdk_importable = lb is not None and LONGBRIDGE_IMPORT_ERROR is None
        env_status = {
            key: ("present" if os.getenv(key) else "missing")
            for key in REQUIRED_ENV_KEYS
        }
        optional_env = {
            key: ("present" if os.getenv(key) else "missing")
            for key in OPTIONAL_ENV_KEYS
        }
        return {
            "provider": self.provider_name,
            "sdk_importable": sdk_importable,
            "env": env_status,
            "optional_env": optional_env,
        }

    def fetch_quote(self, symbol: str, market: str = "CN") -> dict[str, Any]:
        if market.upper() != "CN":
            return self._base_quote(
                symbol=symbol, market=market, data_status="unsupported_market", error_message=f"Unsupported market: {market}"
            )

        if not self._has_required_env():
            return self._base_quote(symbol=symbol, market=market, data_status="missing_env", error_message="Missing environment variables")

        if lb is None:
            return self._base_quote(
                symbol=symbol, market=market, data_status="sdk_missing", error_message=str(LONGBRIDGE_IMPORT_ERROR or "SDK missing")
            )

        mapped = self._to_longbridge_symbol(symbol, market="CN")
        if mapped is None:
            return self._base_quote(symbol=symbol, market=market, data_status="unsupported_symbol", error_message="Unsupported symbol format")

        try:
            snapshot = self._fetch_lb_quote_snapshot(mapped)
            return {
                **self._base_quote(symbol=symbol, market=market, data_status="ok"),
                "raw_symbol": mapped,
                "name": snapshot.get("name", ""),
                "current_price": snapshot.get("current_price"),
                "change": snapshot.get("change"),
                "change_percent": snapshot.get("change_percent"),
                "open": snapshot.get("open"),
                "high": snapshot.get("high"),
                "low": snapshot.get("low"),
                "prev_close": snapshot.get("prev_close"),
                "volume": snapshot.get("volume"),
                "turnover": snapshot.get("turnover"),
                "timestamp": snapshot.get("timestamp") or datetime.now().isoformat(timespec="seconds"),
            }
        except Exception as error:
            message = self._sanitize_error(str(error))
            return self._base_quote(symbol=symbol, market=market, data_status="fetch_failed", error_message=message)

    def fetch_quotes(self, symbols: list[str], market: str = "CN") -> list[dict[str, Any]]:
        results: list[dict[str, Any]] = []
        for symbol in symbols:
            results.append(self.fetch_quote(symbol=symbol, market=market))
        return results

    def _fetch_lb_quote_snapshot(self, lb_symbol: str) -> dict[str, Any]:
        # 真实接入留到后续：此处仅提供测试可替换的占位实现
        # 测试会通过 monkeypatch 覆盖此方法返回模拟数据或抛异常
        raise NotImplementedError("Longbridge SDK call not implemented in prototype")

    def _has_required_env(self) -> bool:
        return all(os.getenv(key) for key in REQUIRED_ENV_KEYS)

    def _sanitize_error(self, message: str) -> str:
        # 移除可能包含的敏感信息提示（不读取真实值，仅防御性处理关键字）
        redactions = ["APP_KEY", "APP_SECRET", "ACCESS_TOKEN", "LONGBRIDGE"]
        lowered = message
        for token in redactions:
            lowered = lowered.replace(token, "***")
        return lowered

    def _to_longbridge_symbol(self, symbol: str, market: str) -> str | None:
        s = str(symbol).strip().upper()
        if "." in s:
            parts = s.split(".")
            if len(parts) == 2 and parts[1] in {"SH", "SZ"}:
                return f"{parts[0]}.{parts[1]}"
            return None
        if s.startswith(("600", "601", "603", "605", "688", "689")):
            return f"{s}.SH"
        if s.startswith(("000", "001", "002", "003", "300", "301")):
            return f"{s}.SZ"
        return None

    def _base_quote(self, *, symbol: str, market: str, data_status: str, error_message: str = "") -> dict[str, Any]:
        return {
            "symbol": str(symbol).strip(),
            "market": market,
            "provider": self.provider_name,
            "data_status": data_status,
            "error_message": error_message,
            "name": "",
            "current_price": None,
            "change": None,
            "change_percent": None,
            "open": None,
            "high": None,
            "low": None,
            "prev_close": None,
            "volume": None,
            "turnover": None,
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "raw_symbol": "",
        }
