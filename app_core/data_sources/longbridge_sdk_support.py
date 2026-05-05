from __future__ import annotations

import importlib
import importlib.metadata
from datetime import datetime, timezone
from typing import Any

from app_core.security.longbridge_oauth_store import LongbridgeOAuthStore


def inspect_longbridge_sdk() -> dict[str, Any]:
    try:
        openapi_module = importlib.import_module("longbridge.openapi")
    except Exception as error:  # pragma: no cover - runtime branch
        return {
            "sdk_importable": False,
            "sdk_version": "unknown",
            "available_symbols": {
                "Config": False,
                "QuoteContext": False,
                "OAuthBuilder": False,
            },
            "openapi_module": None,
            "error_message": _sanitize_error(str(error) or "SDK missing"),
        }

    try:
        sdk_version = importlib.metadata.version("longbridge")
    except importlib.metadata.PackageNotFoundError:
        sdk_version = str(getattr(openapi_module, "__version__", "unknown"))

    return {
        "sdk_importable": True,
        "sdk_version": sdk_version or "unknown",
        "available_symbols": {
            "Config": hasattr(openapi_module, "Config"),
            "QuoteContext": hasattr(openapi_module, "QuoteContext"),
            "OAuthBuilder": hasattr(openapi_module, "OAuthBuilder"),
        },
        "openapi_module": openapi_module,
        "error_message": "",
    }


def start_longbridge_oauth(
    *,
    client_id: str,
    store: LongbridgeOAuthStore,
) -> dict[str, Any]:
    sdk_status = inspect_longbridge_sdk()
    if not sdk_status["sdk_importable"]:
        return {
            "status": "sdk_missing",
            "message": sdk_status["error_message"] or "Longbridge SDK missing",
            "authorization_url": "",
            "sdk_token_cache": "unknown",
        }

    if not client_id:
        return {
            "status": "app_key_missing",
            "message": "缺少 LONGBRIDGE_APP_KEY。",
            "authorization_url": "",
            "sdk_token_cache": "unknown",
        }

    openapi_module = sdk_status["openapi_module"]
    if openapi_module is None or not sdk_status["available_symbols"]["OAuthBuilder"]:
        return {
            "status": "sdk_missing",
            "message": "Longbridge SDK 未提供 OAuthBuilder。",
            "authorization_url": "",
            "sdk_token_cache": "unknown",
        }

    authorization_urls: list[str] = []

    def _on_authorize(url: str) -> None:
        authorization_urls.append(str(url))
        print(f"Open this URL to authorize: {url}")

    try:
        oauth = openapi_module.OAuthBuilder(client_id).build(_on_authorize)
    except Exception as error:  # pragma: no cover - runtime branch
        return {
            "status": "oauth_failed",
            "message": _sanitize_error(str(error) or "OAuthBuilder failed"),
            "authorization_url": authorization_urls[-1] if authorization_urls else "",
            "sdk_token_cache": "unknown",
        }

    safe_metadata = {
        "provider": "longbridge",
        "auth_type": "oauth2",
        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "updated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "note": "quote only; sdk managed",
        "sdk_managed": True,
    }
    for field_name in ("expires_at", "scope"):
        field_value = getattr(oauth, field_name, "")
        if field_value:
            safe_metadata[field_name] = str(field_value)
    store.save_oauth_metadata(safe_metadata)

    return {
        "status": "authorized",
        "message": "",
        "authorization_url": authorization_urls[-1] if authorization_urls else "",
        "sdk_token_cache": "maybe_configured",
        "oauth": oauth,
    }


def fetch_longbridge_quote_via_oauth(
    *,
    client_id: str,
    symbol: str,
    raw_symbol: str,
    store: LongbridgeOAuthStore,
) -> dict[str, Any]:
    start_result = start_longbridge_oauth(client_id=client_id, store=store)
    if start_result["status"] != "authorized":
        return {
            "data_status": start_result["status"],
            "error_message": start_result["message"],
            "authorization_url": start_result.get("authorization_url", ""),
            "symbol": symbol,
            "raw_symbol": raw_symbol,
        }

    sdk_status = inspect_longbridge_sdk()
    openapi_module = sdk_status["openapi_module"]
    if openapi_module is None:
        return {
            "data_status": "sdk_missing",
            "error_message": sdk_status["error_message"] or "Longbridge SDK missing",
            "authorization_url": start_result.get("authorization_url", ""),
            "symbol": symbol,
            "raw_symbol": raw_symbol,
        }

    try:
        config = openapi_module.Config.from_oauth(start_result["oauth"])
        ctx = openapi_module.QuoteContext(config)
        resp = ctx.quote([raw_symbol])
    except Exception as error:  # pragma: no cover - runtime branch
        return {
            "data_status": "quote_failed",
            "error_message": _sanitize_error(str(error) or "QuoteContext quote failed"),
            "authorization_url": start_result.get("authorization_url", ""),
            "symbol": symbol,
            "raw_symbol": raw_symbol,
        }

    normalized = _normalize_quote_response(resp)
    if normalized is None:
        return {
            "data_status": "quote_failed",
            "error_message": "QuoteContext 返回空结果。",
            "authorization_url": start_result.get("authorization_url", ""),
            "symbol": symbol,
            "raw_symbol": raw_symbol,
        }

    return {
        "data_status": "ok",
        "error_message": "",
        "authorization_url": start_result.get("authorization_url", ""),
        "symbol": symbol,
        "raw_symbol": raw_symbol,
        "name": normalized.get("name", ""),
        "current_price": normalized.get("current_price"),
        "change": normalized.get("change"),
        "change_percent": normalized.get("change_percent"),
        "timestamp": normalized.get("timestamp") or datetime.now().isoformat(timespec="seconds"),
    }


def _normalize_quote_response(resp: Any) -> dict[str, Any] | None:
    if resp is None:
        return None

    first: Any
    if isinstance(resp, list):
        if not resp:
            return None
        first = resp[0]
    elif hasattr(resp, "__iter__") and not isinstance(resp, (str, bytes, dict)):
        items = list(resp)
        if not items:
            return None
        first = items[0]
    else:
        first = resp

    def _get(item: Any, *names: str) -> Any:
        for name in names:
            if isinstance(item, dict) and name in item:
                return item.get(name)
            if hasattr(item, name):
                return getattr(item, name)
        return None

    return {
        "name": _get(first, "name"),
        "current_price": _get(first, "current_price", "last_done", "price"),
        "change": _get(first, "change"),
        "change_percent": _get(first, "change_percent"),
        "timestamp": _get(first, "timestamp", "updated_at"),
    }


def _sanitize_error(message: str) -> str:
    lowered = str(message)
    for token in ("APP_KEY", "APP_SECRET", "ACCESS_TOKEN", "REFRESH_TOKEN", "LONGBRIDGE"):
        lowered = lowered.replace(token, "***")
    return lowered
