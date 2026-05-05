from __future__ import annotations

import importlib
import importlib.metadata
import webbrowser
from datetime import datetime, timezone
from urllib.parse import parse_qs, urlparse
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
    open_browser: bool = True,
    verbose: bool = True,
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
            "status": "oauth_client_id_missing",
            "message": "请先通过 Longbridge /oauth2/register 注册 OAuth Client，并将 client_id 写入 LONGBRIDGE_OAUTH_CLIENT_ID。",
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
    browser_open_requested: bool | None = None

    def _on_authorize(url: str) -> None:
        nonlocal browser_open_requested
        authorization_urls.append(str(url))
        _, redirect_uri_host = _extract_redirect_uri_summary(str(url))
        if open_browser:
            try:
                browser_open_requested = bool(webbrowser.open(str(url)))
            except Exception:  # pragma: no cover - depends on desktop/browser runtime
                browser_open_requested = False
        else:
            browser_open_requested = False

        if verbose:
            print("provider: longbridge")
            print("oauth: waiting_for_browser_authorization")
            print(f"browser_open_requested: {str(bool(browser_open_requested)).lower()}")
            print(f"redirect_uri_host: {redirect_uri_host}")
            print("quote_only: true")
            print("trade_enabled: false")
            if open_browser and not browser_open_requested:
                print("message: 请检查系统默认浏览器，或临时启用 debug 模式获取脱敏排查信息。")

    def _build_failure_result(message: str, status: str = "oauth_failed") -> dict[str, Any]:
        diagnostics = build_oauth_failure_diagnostics(
            message=message,
            sdk_status=sdk_status,
            client_id_present=bool(client_id),
            authorization_url=authorization_urls[-1] if authorization_urls else "",
        )
        diagnostics["browser_open_requested"] = browser_open_requested
        return {
            "status": status,
            "message": diagnostics["message"],
            "sdk_token_cache": "unknown",
            "diagnostics": diagnostics,
            "browser_open_requested": browser_open_requested,
            "redirect_uri_host": diagnostics["redirect_uri_host"],
        }

    try:
        oauth = openapi_module.OAuthBuilder(client_id).build(_on_authorize)
    except Exception as error:  # pragma: no cover - runtime branch
        return _build_failure_result(_sanitize_error(str(error) or "OAuthBuilder failed"))

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
        "sdk_token_cache": "maybe_configured",
        "oauth": oauth,
        "browser_open_requested": browser_open_requested,
        "redirect_uri_host": _extract_redirect_uri_summary(authorization_urls[-1])[1] if authorization_urls else "unknown",
    }


def build_longbridge_quote_context_via_oauth(
    *,
    client_id: str,
    store: LongbridgeOAuthStore,
) -> dict[str, Any]:
    start_result = start_longbridge_oauth(
        client_id=client_id,
        store=store,
        open_browser=False,
        verbose=False,
    )
    if start_result["status"] != "authorized":
        return {
            "status": start_result["status"],
            "message": start_result.get("message", ""),
            "authorization_url": start_result.get("authorization_url", ""),
        }

    sdk_status = inspect_longbridge_sdk()
    openapi_module = sdk_status["openapi_module"]
    if openapi_module is None:
        return {
            "status": "sdk_missing",
            "message": sdk_status["error_message"] or "Longbridge SDK missing",
            "authorization_url": start_result.get("authorization_url", ""),
        }

    try:
        config = openapi_module.Config.from_oauth(start_result["oauth"])
        ctx = openapi_module.QuoteContext(config)
    except Exception as error:  # pragma: no cover - runtime branch
        return {
            "status": "quote_failed",
            "message": _sanitize_error(str(error) or "QuoteContext initialization failed"),
            "authorization_url": start_result.get("authorization_url", ""),
        }

    return {
        "status": "authorized",
        "message": "",
        "authorization_url": start_result.get("authorization_url", ""),
        "ctx": ctx,
    }


def build_oauth_failure_diagnostics(
    *,
    message: str,
    sdk_status: dict[str, Any],
    client_id_present: bool,
    authorization_url: str = "",
) -> dict[str, Any]:
    safe_message = _sanitize_error(message)
    error_type = _detect_error_type(safe_message)
    redirect_uri_scheme, redirect_uri_host = _extract_redirect_uri_summary(authorization_url)

    likely_stage = "authorization_server" if error_type == "internal_server_error" else "oauth_startup"
    next_steps = [
        "检查长桥开发者后台是否启用 OAuth 2.0",
        "通过 /oauth2/register 单独注册 OAuth Client，获得独立 client_id",
        "在开发者后台登记 redirect_uri（本项目使用 http://localhost:60355/callback）",
        "检查账号地区/权限是否支持 OAuthBuilder",
        "联系 Longbridge OpenAPI 支持并提供 SDK 版本、错误类型和发生阶段",
    ]

    return {
        "message": safe_message,
        "error_type": error_type,
        "likely_stage": likely_stage,
        "sdk_importable": bool(sdk_status.get("sdk_importable")),
        "sdk_version": str(sdk_status.get("sdk_version", "unknown") or "unknown"),
        "client_id_present": client_id_present,
        "redirect_uri_host": redirect_uri_host,
        "redirect_uri_scheme": redirect_uri_scheme,
        "quote_only": True,
        "trade_enabled": False,
        "next_steps": next_steps,
    }


def fetch_longbridge_quote_via_oauth(
    *,
    client_id: str,
    symbol: str,
    raw_symbol: str,
    store: LongbridgeOAuthStore,
) -> dict[str, Any]:
    context_result = build_longbridge_quote_context_via_oauth(client_id=client_id, store=store)
    if context_result["status"] != "authorized":
        return {
            "data_status": context_result["status"],
            "message": context_result.get("message", ""),
            "error_message": context_result.get("message", ""),
            "authorization_url": context_result.get("authorization_url", ""),
            "symbol": symbol,
            "raw_symbol": raw_symbol,
        }

    return fetch_longbridge_quote_with_context(
        ctx=context_result["ctx"],
        symbol=symbol,
        raw_symbol=raw_symbol,
        authorization_url=context_result.get("authorization_url", ""),
    )


def fetch_longbridge_quote_with_context(
    *,
    ctx: Any,
    symbol: str,
    raw_symbol: str,
    authorization_url: str = "",
) -> dict[str, Any]:
    try:
        resp = ctx.quote([raw_symbol])
    except Exception as error:  # pragma: no cover - runtime branch
        safe_message = _sanitize_error(str(error) or "QuoteContext quote failed")
        error_status = _detect_quote_error_status(safe_message)
        return {
            "data_status": error_status,
            "message": (
                "当前账号可能未开通对应市场 OpenAPI 实时行情权限"
                if error_status == "permission_required"
                else ""
            ),
            "error_message": "" if error_status == "permission_required" else safe_message,
            "authorization_url": authorization_url,
            "symbol": symbol,
            "raw_symbol": raw_symbol,
        }

    normalized = _normalize_quote_response(resp)
    if normalized is None:
        return {
            "data_status": "quote_failed",
            "error_message": "QuoteContext 返回空结果。",
            "authorization_url": authorization_url,
            "symbol": symbol,
            "raw_symbol": raw_symbol,
        }

    return {
        "data_status": "ok",
        "message": "",
        "error_message": "",
        "authorization_url": authorization_url,
        "symbol": symbol,
        "raw_symbol": raw_symbol,
        "name": normalized.get("name", ""),
        "current_price": normalized.get("current_price"),
        "change": normalized.get("change"),
        "change_percent": normalized.get("change_percent"),
        "volume": normalized.get("volume"),
        "turnover": normalized.get("turnover"),
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
        "volume": _get(first, "volume"),
        "turnover": _get(first, "turnover", "amount"),
        "timestamp": _get(first, "timestamp", "updated_at"),
    }


def _extract_redirect_uri_summary(authorization_url: str) -> tuple[str, str]:
    if not authorization_url:
        return "unknown", "unknown"

    parsed = urlparse(authorization_url)
    query = parse_qs(parsed.query)
    redirect_uri_values = query.get("redirect_uri", [])
    if not redirect_uri_values:
        return "unknown", "unknown"

    redirect_uri = urlparse(redirect_uri_values[0])
    return redirect_uri.scheme or "unknown", redirect_uri.hostname or "unknown"


def _detect_error_type(message: str) -> str:
    lowered = str(message).lower()
    if "internal_server_error" in lowered:
        return "internal_server_error"
    if "invalid_client" in lowered:
        return "invalid_client"
    if "access_denied" in lowered:
        return "access_denied"
    return "unknown"


def _detect_quote_error_status(message: str) -> str:
    lowered = str(message).lower()
    permission_markers = (
        "permission",
        "authority",
        "not authorized",
        "not subscribed",
        "quote package",
        "行情权限",
        "权限不足",
    )
    for marker in permission_markers:
        if marker in lowered:
            return "permission_required"
    return "fetch_failed"


def _sanitize_error(message: str) -> str:
    lowered = str(message)
    # 替换敏感关键字，防止在错误消息中泄露
    for token in (
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
    ):
        lowered = lowered.replace(token, "***")
    return lowered
