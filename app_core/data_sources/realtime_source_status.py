from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

from app_core.data_sources.longbridge_quote_provider import LongbridgeQuoteProvider
from app_core.security.local_secret_manager import LocalSecretManager


def build_realtime_source_status(project_root: Path | None = None) -> dict[str, Any]:
    """构建实时行情 / 新闻数据源的脱敏状态摘要。"""
    LocalSecretManager.load_local_env_to_process_env(project_root=project_root)

    manager = LocalSecretManager(project_root=project_root)
    provider = LongbridgeQuoteProvider(project_root=project_root)
    secret_statuses = {item["key"]: item for item in manager.get_secret_statuses()}
    longbridge_status = provider.check_status()

    marketaux_secret = secret_statuses.get("MARKETAUX_API_TOKEN", {})
    tushare_secret = secret_statuses.get("TUSHARE_TOKEN", {})
    longbridge_entry = _build_longbridge_source(longbridge_status)
    marketaux_token_status = _normalize_secret_status(marketaux_secret.get("status", "missing"))
    tushare_token_status = _normalize_secret_status(tushare_secret.get("status", "missing"))

    marketaux_configured = marketaux_token_status == "configured"

    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "default_quote_source": "akshare",
        "sources": [
            {
                "source_id": "akshare",
                "display_name": "AkShare A股实时行情",
                "category": "quote",
                "status": "available",
                "status_label": "可用",
                "priority": "primary",
                "supports": ["CN_quote", "CN_kline"],
                "requires_token": False,
                "token_status": "not_required",
                "note": "当前默认 A股实时行情源",
            },
            longbridge_entry,
            {
                "source_id": "marketaux",
                "display_name": "Marketaux 国际新闻",
                "category": "news",
                "status": "available" if marketaux_configured else "missing_token",
                "status_label": "已配置" if marketaux_configured else "未配置",
                "priority": "news",
                "requires_token": True,
                "token_status": marketaux_token_status,
                "note": "用于国际市场新闻，不作为交易信号",
            },
            {
                "source_id": "tushare",
                "display_name": "Tushare Pro",
                "category": "data",
                "status": "reserved",
                "status_label": "预留",
                "priority": "future",
                "requires_token": True,
                "token_status": tushare_token_status,
                "note": "预留用于 A股历史、财务与基础数据",
            },
        ],
        "safety": {
            "quote_only": True,
            "trade_enabled": False,
            "order_enabled": False,
        },
    }


def _normalize_secret_status(raw_status: Any) -> str:
    status = str(raw_status or "missing").strip() or "missing"
    if status in {"configured", "empty", "missing"}:
        return status
    return "missing"


def _build_longbridge_source(longbridge_status: dict[str, Any]) -> dict[str, Any]:
    raw_auth_mode = str(longbridge_status["auth"].get("auth_mode_candidate", "missing_app_credentials"))
    raw_oauth_status = str(longbridge_status["auth"].get("oauth", "missing"))
    sdk_status = "installed" if bool(longbridge_status.get("sdk_importable")) else "missing"
    auth_mode = _map_longbridge_auth_mode(raw_auth_mode)
    token_status = _map_longbridge_token_status(raw_auth_mode, raw_oauth_status)

    if raw_auth_mode in {"legacy_api_key", "oauth2_local_token"}:
        status = "available"
        status_label = "候选可用"
    else:
        status = "blocked"
        status_label = "待授权"

    if raw_auth_mode == "oauth2_local_token" and raw_oauth_status == "configured":
        note = "Longbridge OAuth 已授权，可读取只读行情；token 由 SDK 托管或本地可用"
    elif raw_auth_mode == "oauth2_local_token":
        note = "Longbridge OAuth 已授权，可读取只读行情；当前采用 SDK 托管 token cache"
    elif raw_auth_mode == "legacy_api_key":
        note = "已检测到 legacy 只读行情凭证，可作为候选行情源"
    elif sdk_status == "missing":
        note = "Longbridge SDK 当前缺失，待安装后再验证 OAuth 只读行情"
    elif raw_auth_mode == "missing_app_credentials":
        note = "缺少 Longbridge App Key / Secret，暂无法进入 OAuthBuilder 授权流程"
    else:
        note = "OAuth 授权当前受 internal_server_error 阻塞，待 Longbridge 配置确认"

    return {
        "source_id": "longbridge",
        "display_name": "Longbridge OpenAPI 只读行情",
        "category": "quote",
        "status": status,
        "status_label": status_label,
        "priority": "candidate",
        "supports": ["CN_quote", "US_quote", "HK_quote"],
        "requires_token": True,
        "token_status": token_status,
        "sdk_status": sdk_status,
        "auth_mode": auth_mode,
        "quote_only": True,
        "trade_enabled": False,
        "note": note,
    }


def _map_longbridge_auth_mode(raw_auth_mode: str) -> str:
    if raw_auth_mode == "oauth2_local_token":
        return "已授权 / 可读取只读行情"
    if raw_auth_mode == "legacy_api_key":
        return "legacy_configured"
    if raw_auth_mode in {"oauthbuilder_required", "oauth_required"}:
        return raw_auth_mode
    if raw_auth_mode == "missing_app_credentials":
        return "missing"
    return raw_auth_mode or "missing"


def _map_longbridge_token_status(raw_auth_mode: str, raw_oauth_status: str) -> str:
    if raw_auth_mode == "legacy_api_key":
        return "configured"
    if raw_oauth_status == "configured":
        return "configured"
    if raw_oauth_status == "expired":
        return "expired"
    if raw_oauth_status == "missing":
        return "missing"
    if raw_oauth_status == "unknown_expiry":
        return "configured"
    return "missing"
