from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path
from typing import Any

from app_core.data_sources.longbridge_sdk_support import inspect_longbridge_sdk
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
OAUTH_CLIENT_ID_KEY = "LONGBRIDGE_OAUTH_CLIENT_ID"
DEFAULT_REDIRECT_URI = "http://localhost:60355/callback"


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
        sdk_status = inspect_longbridge_sdk()
        sdk_importable = bool(sdk_status["sdk_importable"])
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
        client_id_present = bool(os.getenv(OAUTH_CLIENT_ID_KEY))
        return {
            "provider": self.provider_name,
            "sdk_importable": sdk_importable,
            "oauthbuilder_available": bool(sdk_status["available_symbols"].get("OAuthBuilder")),
            "oauth_client": {
                "client_id_present": client_id_present,
                "redirect_uri": DEFAULT_REDIRECT_URI,
                "app_key_is_oauth_client_id": False,
            },
            "auth": {
                "legacy_api_key": "ready" if auth_state["legacy_ready"] else "incomplete",
                "oauth": self._map_oauth_status_for_display(str(oauth_status["status"])),
                "auth_mode_candidate": auth_state["auth_mode"],
                "oauthbuilder": auth_state["oauthbuilder"],
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
        market_code = str(market).strip().upper()
        if market_code not in {"CN", "US", "HK"}:
            return self._base_quote(
                symbol=symbol,
                market=market_code,
                data_status="unsupported_market",
                error_message=f"Unsupported market: {market}",
            )

        auth_state = self._resolve_auth_state()
        auth_mode = str(auth_state["auth_mode"])

        if auth_mode == "missing_app_credentials":
            return self._base_quote(
                symbol=symbol,
                market=market_code,
                data_status="missing_env",
                error_message="Missing environment variables: LONGBRIDGE_APP_KEY / LONGBRIDGE_APP_SECRET",
                auth_mode=auth_mode,
            )

        if auth_mode in {"oauth_required", "oauthbuilder_required", "oauth_client_registration_required"}:
            return self._base_quote(
                symbol=symbol,
                market=market_code,
                data_status=auth_mode,
                error_message=str(auth_state["message"]),
                auth_mode=auth_mode,
            )

        if lb is None:
            return self._base_quote(
                symbol=symbol,
                market=market_code,
                data_status="sdk_missing",
                error_message=str(LONGBRIDGE_IMPORT_ERROR or "SDK missing"),
                auth_mode=auth_mode,
            )

        mapped = self._to_longbridge_symbol(symbol, market_code)
        if mapped is None:
            return self._base_quote(
                symbol=symbol,
                market=market_code,
                data_status="unsupported_symbol",
                error_message="Unsupported symbol format",
                auth_mode=auth_mode,
            )

        try:
            snapshot = self._fetch_lb_quote_snapshot(mapped)
            return {
                **self._base_quote(symbol=symbol, market=market_code, data_status="ok", auth_mode=auth_mode),
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
            data_status = "permission_required" if self._is_permission_error(message) else "fetch_failed"
            return self._base_quote(
                symbol=symbol,
                market=market_code,
                data_status=data_status,
                error_message=(
                    "当前账号可能未开通对应市场 OpenAPI 实时行情权限"
                    if data_status == "permission_required"
                    else message
                ),
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
        oauth_client_id_present = bool(os.getenv(OAUTH_CLIENT_ID_KEY))
        oauth_status = self.oauth_store.get_oauth_token_status()
        oauth_state = str(oauth_status.get("status", "missing"))
        oauth_available = oauth_state in {"configured", "unknown_expiry", "sdk_managed_configured"}
        sdk_status = inspect_longbridge_sdk()
        oauthbuilder_available = bool(sdk_status["available_symbols"].get("OAuthBuilder"))

        if not app_key_present:
            return {
                "auth_mode": "missing_app_credentials",
                "legacy_ready": False,
                "message": "缺少 LONGBRIDGE_APP_KEY / LONGBRIDGE_APP_SECRET。",
                "oauthbuilder": "unknown",
            }

        if legacy_token_present:
            return {
                "auth_mode": "legacy_api_key",
                "legacy_ready": True,
                "message": "",
                "oauthbuilder": "supported" if oauthbuilder_available else "missing_sdk",
            }

        if oauth_available:
            return {
                "auth_mode": "oauth2_local_token",
                "legacy_ready": False,
                "message": "",
                "oauthbuilder": "supported" if oauthbuilder_available else "missing_sdk",
            }

        if not sdk_status["sdk_importable"]:
            return {
                "auth_mode": "oauth_required",
                "legacy_ready": False,
                "message": "Longbridge SDK 未安装或不可导入，无法执行 OAuthBuilder。",
                "oauthbuilder": "missing_sdk",
            }

        if oauthbuilder_available:
            if not oauth_client_id_present:
                return {
                    "auth_mode": "oauth_client_registration_required",
                    "legacy_ready": False,
                    "message": "请先通过 /oauth2/register 注册 OAuth Client，并设置 LONGBRIDGE_OAUTH_CLIENT_ID。",
                    "oauthbuilder": "supported",
                }
            else:
                return {
                    "auth_mode": "oauthbuilder_required",
                    "legacy_ready": False,
                    "message": "请先执行 longbridge-oauth-start 或 longbridge-oauth-help。",
                    "oauthbuilder": "supported",
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
            "oauthbuilder": "unknown",
        }

    def _map_oauth_status_for_display(self, status: str) -> str:
        mapping = {
            "configured": "configured",
            "sdk_managed_configured": "configured",
            "expired": "expired",
            "missing": "missing",
            "invalid_json": "unknown",
            "unknown_expiry": "unknown",
            "unknown": "unknown",
        }
        return mapping.get(status, "unknown")

    def _sanitize_error(self, message: str) -> str:
        # 移除可能包含的敏感信息提示（不读取真实值，仅防御性处理关键字）
        redactions = [
            "APP_KEY",
            "APP_SECRET",
            "ACCESS_TOKEN",
            "REFRESH_TOKEN",
            "app_key",
            "app_secret",
            "access_token",
            "refresh_token",
            "client_id",
            "client_secret",
            "state",
            "code",
            "LONGBRIDGE",
        ]
        lowered = message
        for token in redactions:
            lowered = lowered.replace(token, "***")
        return lowered

    def _is_permission_error(self, message: str) -> bool:
        lowered = str(message).lower()
        markers = (
            "permission",
            "authority",
            "not authorized",
            "not subscribed",
            "quote package",
            "行情权限",
            "权限不足",
        )
        return any(marker in lowered for marker in markers)

    def _to_longbridge_symbol(self, symbol: str, market: str) -> str | None:
        s = str(symbol).strip().upper()
        market_code = str(market).strip().upper()

        if market_code == "US":
            if s.endswith(".US"):
                return s
            if "." in s:
                return None
            if not s or not all(ch.isalnum() or ch in {"-", "_"} for ch in s):
                return None
            return f"{s}.US"

        if market_code == "HK":
            base = s[:-3] if s.endswith(".HK") else s
            if "." in base or not base.isdigit():
                return None
            normalized = base.lstrip("0") or "0"
            return f"{normalized}.HK"

        if market_code != "CN":
            return None

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
