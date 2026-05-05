from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path
from typing import Any

from app_core.security.longbridge_oauth_store import LongbridgeOAuthStore

try:
    import longbridge as lb  # type: ignore
    LONGBRIDGE_IMPORT_ERROR: BaseException | None = None
except Exception as error:  # pragma: no cover - depends on runtime env
    lb = None  # type: ignore
    LONGBRIDGE_IMPORT_ERROR = error


APP_CREDENTIAL_KEYS = ("LONGBRIDGE_APP_KEY", "LONGBRIDGE_APP_SECRET")
LEGACY_ACCESS_TOKEN_KEY = "LONGBRIDGE_ACCESS_TOKEN"
REQUIRED_ENV_KEYS = (*APP_CREDENTIAL_KEYS, LEGACY_ACCESS_TOKEN_KEY)
OPTIONAL_ENV_KEYS = ("LONGBRIDGE_REGION", "LONGBRIDGE_HTTP_URL", "LONGBRIDGE_QUOTE_WS_URL")


class LongbridgeQuoteProvider:
    """Longbridge 只读实时行情 Provider (候选数据源)。"""

    def __init__(
        self,
        project_root: Path | None = None,
        oauth_store: LongbridgeOAuthStore | None = None,
    ) -> None:
        self.provider_name = "longbridge"
        self.oauth_store = oauth_store or LongbridgeOAuthStore(project_root=project_root)

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
        oauth_status = self.oauth_store.get_oauth_token_status()
        auth_state = self._resolve_auth_state()
        return {
            "provider": self.provider_name,
            "sdk_importable": sdk_importable,
            "auth": {
                "legacy_api_key": "ready" if auth_state["legacy_ready"] else "incomplete",
                "oauth": self._map_oauth_status_for_display(str(oauth_status["status"])),
                "auth_mode_candidate": auth_state["auth_mode"],
            },
            "env": env_status,
            "optional_env": optional_env,
            "local_oauth": {
                "token_file": oauth_status["token_file"],
                "access_token": oauth_status["access_token"],
                "refresh_token": oauth_status["refresh_token"],
                "expires_at": oauth_status["expires_at"],
                "masked": oauth_status["masked_access_token"],
                "status": oauth_status["status"],
            },
            "safety": {
                "quote_only": True,
                "trade_enabled": False,
            },
        }

    def fetch_quote(self, symbol: str, market: str = "CN") -> dict[str, Any]:
        if market.upper() != "CN":
            return self._base_quote(
                symbol=symbol, market=market, data_status="unsupported_market", error_message=f"Unsupported market: {market}"
            )

        auth_state = self._resolve_auth_state()
        auth_mode = str(auth_state["auth_mode"])

        if auth_mode == "missing_app_credentials":
            return self._base_quote(
                symbol=symbol,
                market=market,
                data_status="missing_env",
                error_message="Missing environment variables: LONGBRIDGE_APP_KEY / LONGBRIDGE_APP_SECRET",
                auth_mode=auth_mode,
            )

        if auth_mode == "oauth_required":
            return self._base_quote(
                symbol=symbol,
                market=market,
                data_status="oauth_required",
                error_message=str(auth_state["message"]),
                auth_mode=auth_mode,
            )

        if lb is None:
            return self._base_quote(
                symbol=symbol,
                market=market,
                data_status="sdk_missing",
                error_message=str(LONGBRIDGE_IMPORT_ERROR or "SDK missing"),
                auth_mode=auth_mode,
            )

        mapped = self._to_longbridge_symbol(symbol, "CN")
        if mapped is None:
            return self._base_quote(
                symbol=symbol,
                market=market,
                data_status="unsupported_symbol",
                error_message="Unsupported symbol format",
                auth_mode=auth_mode,
            )

        try:
            snapshot = self._fetch_lb_quote_snapshot(mapped)
            return {
                **self._base_quote(symbol=symbol, market=market, data_status="ok", auth_mode=auth_mode),
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
            return self._base_quote(
                symbol=symbol,
                market=market,
                data_status="fetch_failed",
                error_message=message,
                auth_mode=auth_mode,
            )

    def fetch_quotes(self, symbols: list[str], market: str = "CN") -> list[dict[str, Any]]:
        results: list[dict[str, Any]] = []
        for symbol in symbols:
            results.append(self.fetch_quote(symbol=symbol, market=market))
        return results

    def _fetch_lb_quote_snapshot(self, _lb_symbol: str) -> dict[str, Any]:
        # 真实接入留到后续：此处仅提供测试可替换的占位实现
        # 测试会通过 monkeypatch 覆盖此方法返回模拟数据或抛异常
        raise NotImplementedError("Longbridge SDK call not implemented in prototype")

    def _resolve_auth_state(self) -> dict[str, Any]:
        app_key_present = all(os.getenv(key) for key in APP_CREDENTIAL_KEYS)
        legacy_token_present = bool(os.getenv(LEGACY_ACCESS_TOKEN_KEY))
        oauth_status = self.oauth_store.get_oauth_token_status()
        oauth_state = str(oauth_status.get("status", "missing"))
        oauth_available = oauth_state in {"configured", "unknown_expiry"} and oauth_status.get("access_token") == "present"

        if not app_key_present:
            return {
                "auth_mode": "missing_app_credentials",
                "legacy_ready": False,
                "message": "缺少 LONGBRIDGE_APP_KEY / LONGBRIDGE_APP_SECRET。",
            }

        if legacy_token_present:
            return {
                "auth_mode": "legacy_api_key",
                "legacy_ready": True,
                "message": "",
            }

        if oauth_available:
            return {
                "auth_mode": "oauth2_local_token",
                "legacy_ready": False,
                "message": "",
            }

        if oauth_state == "expired":
            message = "本地 OAuth Token 已过期，请重新授权或执行 longbridge-oauth-help。"
        elif oauth_state == "invalid_json":
            message = "本地 OAuth Token 文件损坏，请执行 longbridge-oauth-clear 后重新设置。"
        else:
            message = "当前账号未提供 legacy Access Token，请执行 longbridge-oauth-help。"

        return {
            "auth_mode": "oauth_required",
            "legacy_ready": False,
            "message": message,
        }

    def _map_oauth_status_for_display(self, status: str) -> str:
        mapping = {
            "configured": "configured",
            "expired": "expired",
            "missing": "missing",
            "invalid_json": "unknown",
            "unknown_expiry": "unknown",
            "unknown": "unknown",
        }
        return mapping.get(status, "unknown")

    def _sanitize_error(self, message: str) -> str:
        # 移除可能包含的敏感信息提示（不读取真实值，仅防御性处理关键字）
        redactions = ["APP_KEY", "APP_SECRET", "ACCESS_TOKEN", "REFRESH_TOKEN", "LONGBRIDGE"]
        lowered = message
        for token in redactions:
            lowered = lowered.replace(token, "***")
        return lowered

    def _to_longbridge_symbol(self, symbol: str, _market: str) -> str | None:
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

    def _base_quote(
        self,
        *,
        symbol: str,
        market: str,
        data_status: str,
        error_message: str = "",
        auth_mode: str = "",
    ) -> dict[str, Any]:
        return {
            "symbol": str(symbol).strip(),
            "market": market,
            "provider": self.provider_name,
            "data_status": data_status,
            "error_message": error_message,
            "auth_mode": auth_mode,
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
