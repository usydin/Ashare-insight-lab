from __future__ import annotations

from datetime import datetime, timedelta, timezone
from types import SimpleNamespace

from app_core.data_sources.longbridge_sdk_support import (
    build_oauth_failure_diagnostics,
    fetch_longbridge_quote_via_oauth,
    inspect_longbridge_sdk,
    start_longbridge_oauth,
)
from app_core.security.longbridge_oauth_store import LongbridgeOAuthStore


def test_inspect_longbridge_sdk_missing(monkeypatch) -> None:
    def _boom(name: str):
        raise ModuleNotFoundError(name)

    monkeypatch.setattr("app_core.data_sources.longbridge_sdk_support.importlib.import_module", _boom)

    status = inspect_longbridge_sdk()

    assert status["sdk_importable"] is False
    assert status["available_symbols"]["Config"] is False
    assert status["available_symbols"]["QuoteContext"] is False
    assert status["available_symbols"]["OAuthBuilder"] is False


def test_start_longbridge_oauth_client_id_missing(tmp_path, monkeypatch) -> None:
    store = LongbridgeOAuthStore(project_root=tmp_path)
    monkeypatch.setattr(
        "app_core.data_sources.longbridge_sdk_support.inspect_longbridge_sdk",
        lambda: {
            "sdk_importable": True,
            "sdk_version": "1.0.0",
            "available_symbols": {"Config": True, "QuoteContext": True, "OAuthBuilder": True},
            "openapi_module": SimpleNamespace(),
            "error_message": "",
        },
    )

    result = start_longbridge_oauth(client_id="", store=store)

    assert result["status"] == "oauth_client_id_missing"


def test_start_longbridge_oauth_authorized_saves_metadata(tmp_path, monkeypatch, capsys) -> None:
    class FakeOAuth:
        scope = "quote"
        expires_at = (datetime.now(timezone.utc) + timedelta(days=1)).isoformat(timespec="seconds")

    class FakeOAuthBuilder:
        def __init__(self, client_id: str) -> None:
            self.client_id = client_id

        def build(self, callback):
            callback("https://example.com/oauth?redirect_uri=http%3A%2F%2Flocalhost%3A60355%2Fcallback")
            return FakeOAuth()

    fake_module = SimpleNamespace(
        OAuthBuilder=FakeOAuthBuilder,
        Config=SimpleNamespace,
        QuoteContext=SimpleNamespace,
    )
    store = LongbridgeOAuthStore(project_root=tmp_path)
    monkeypatch.setattr(
        "app_core.data_sources.longbridge_sdk_support.inspect_longbridge_sdk",
        lambda: {
            "sdk_importable": True,
            "sdk_version": "1.0.0",
            "available_symbols": {"Config": True, "QuoteContext": True, "OAuthBuilder": True},
            "openapi_module": fake_module,
            "error_message": "",
        },
    )
    open_calls: list[str] = []
    monkeypatch.setattr(
        "app_core.data_sources.longbridge_sdk_support.webbrowser.open",
        lambda url: open_calls.append(url) or True,
    )

    result = start_longbridge_oauth(client_id="demo-key", store=store)
    captured = capsys.readouterr()
    status = store.get_oauth_token_status()

    assert result["status"] == "authorized"
    assert result["browser_open_requested"] is True
    assert open_calls == ["https://example.com/oauth?redirect_uri=http%3A%2F%2Flocalhost%3A60355%2Fcallback"]
    assert "provider: longbridge" in captured.out
    assert "oauth: waiting_for_browser_authorization" in captured.out
    assert "browser_open_requested: true" in captured.out
    assert "redirect_uri_host: localhost" in captured.out
    assert "quote_only: true" in captured.out
    assert "trade_enabled: false" in captured.out
    assert "https://example.com/oauth" not in captured.out
    assert status["sdk_managed"] is True


def test_start_longbridge_oauth_internal_server_error_returns_diagnostics(tmp_path, monkeypatch, capsys) -> None:
    class FakeOAuthBuilder:
        def __init__(self, client_id: str) -> None:
            self.client_id = client_id

        def build(self, callback):
            callback("https://open.longbridgeapp.com/authorize?redirect_uri=http%3A%2F%2Flocalhost%3A3000%2Fcallback&state=hidden")
            raise RuntimeError("OpenApiException: OAuth authorization failed: internal_server_error")

    fake_module = SimpleNamespace(
        OAuthBuilder=FakeOAuthBuilder,
        Config=SimpleNamespace,
        QuoteContext=SimpleNamespace,
    )
    store = LongbridgeOAuthStore(project_root=tmp_path)
    monkeypatch.setattr(
        "app_core.data_sources.longbridge_sdk_support.inspect_longbridge_sdk",
        lambda: {
            "sdk_importable": True,
            "sdk_version": "4.0.5",
            "available_symbols": {"Config": True, "QuoteContext": True, "OAuthBuilder": True},
            "openapi_module": fake_module,
            "error_message": "",
        },
    )
    monkeypatch.setattr(
        "app_core.data_sources.longbridge_sdk_support.webbrowser.open",
        lambda url: True,
    )

    result = start_longbridge_oauth(client_id="demo-key", store=store)
    captured = capsys.readouterr()

    assert result["status"] == "oauth_failed"
    assert result["browser_open_requested"] is True
    assert result["diagnostics"]["error_type"] == "internal_server_error"
    assert result["diagnostics"]["likely_stage"] == "authorization_server"
    assert result["diagnostics"]["redirect_uri_host"] == "localhost"
    assert result["diagnostics"]["redirect_uri_scheme"] == "http"
    assert result["diagnostics"]["browser_open_requested"] is True
    assert "browser_open_requested: true" in captured.out
    assert "state=hidden" not in captured.out
    assert "https://open.longbridgeapp.com" not in captured.out


def test_start_longbridge_oauth_browser_open_false_prints_safe_hint(tmp_path, monkeypatch, capsys) -> None:
    class FakeOAuthBuilder:
        def __init__(self, client_id: str) -> None:
            self.client_id = client_id

        def build(self, callback):
            callback("https://open.longbridgeapp.com/authorize?redirect_uri=http%3A%2F%2Flocalhost%3A60355%2Fcallback&state=hidden")
            raise RuntimeError("OpenApiException: OAuth authorization failed: internal_server_error")

    fake_module = SimpleNamespace(
        OAuthBuilder=FakeOAuthBuilder,
        Config=SimpleNamespace,
        QuoteContext=SimpleNamespace,
    )
    store = LongbridgeOAuthStore(project_root=tmp_path)
    monkeypatch.setattr(
        "app_core.data_sources.longbridge_sdk_support.inspect_longbridge_sdk",
        lambda: {
            "sdk_importable": True,
            "sdk_version": "4.0.5",
            "available_symbols": {"Config": True, "QuoteContext": True, "OAuthBuilder": True},
            "openapi_module": fake_module,
            "error_message": "",
        },
    )
    monkeypatch.setattr(
        "app_core.data_sources.longbridge_sdk_support.webbrowser.open",
        lambda url: False,
    )

    result = start_longbridge_oauth(client_id="demo-key", store=store)
    captured = capsys.readouterr()

    assert result["status"] == "oauth_failed"
    assert result["browser_open_requested"] is False
    assert "browser_open_requested: false" in captured.out
    assert "请检查系统默认浏览器" in captured.out
    assert "state=hidden" not in captured.out


def test_build_oauth_failure_diagnostics_redacts_url_details() -> None:
    diagnostics = build_oauth_failure_diagnostics(
        message="OpenApiException: OAuth authorization failed: internal_server_error",
        sdk_status={
            "sdk_importable": True,
            "sdk_version": "4.0.5",
        },
        client_id_present=True,
        authorization_url="https://open.longbridgeapp.com/authorize?redirect_uri=http%3A%2F%2Flocalhost%3A3000%2Fcallback&state=hidden",
    )

    assert diagnostics["error_type"] == "internal_server_error"
    assert diagnostics["likely_stage"] == "authorization_server"
    assert diagnostics["redirect_uri_host"] == "localhost"
    assert diagnostics["redirect_uri_scheme"] == "http"
    assert diagnostics["quote_only"] is True
    assert diagnostics["trade_enabled"] is False


def test_fetch_longbridge_quote_via_oauth_sdk_missing(tmp_path, monkeypatch) -> None:
    store = LongbridgeOAuthStore(project_root=tmp_path)
    monkeypatch.setattr(
        "app_core.data_sources.longbridge_sdk_support.start_longbridge_oauth",
        lambda client_id, store, open_browser=True, verbose=True: {
            "status": "sdk_missing",
            "message": "sdk missing",
            "authorization_url": "",
        },
    )

    result = fetch_longbridge_quote_via_oauth(
        client_id="demo-key",
        symbol="600519",
        raw_symbol="600519.SH",
        store=store,
    )

    assert result["data_status"] == "sdk_missing"


def test_fetch_longbridge_quote_via_oauth_success(tmp_path, monkeypatch) -> None:
    class FakeConfig:
        @staticmethod
        def from_oauth(oauth):
            return {"oauth": oauth}

    class FakeQuoteContext:
        def __init__(self, config):
            self.config = config

        def quote(self, symbols):
            assert symbols == ["600519.SH"]
            return [
                {
                    "name": "贵州茅台",
                    "current_price": 1650.0,
                    "change": 15.5,
                    "change_percent": 0.95,
                    "timestamp": "2026-05-05T12:00:00",
                }
            ]

    fake_module = SimpleNamespace(
        Config=FakeConfig,
        QuoteContext=FakeQuoteContext,
        OAuthBuilder=SimpleNamespace,
    )
    store = LongbridgeOAuthStore(project_root=tmp_path)
    monkeypatch.setattr(
        "app_core.data_sources.longbridge_sdk_support.start_longbridge_oauth",
        lambda client_id, store, open_browser=True, verbose=True: {
            "status": "authorized",
            "message": "",
            "authorization_url": "https://example.com/oauth",
            "oauth": object(),
        },
    )
    monkeypatch.setattr(
        "app_core.data_sources.longbridge_sdk_support.inspect_longbridge_sdk",
        lambda: {
            "sdk_importable": True,
            "sdk_version": "1.0.0",
            "available_symbols": {"Config": True, "QuoteContext": True, "OAuthBuilder": True},
            "openapi_module": fake_module,
            "error_message": "",
        },
    )

    result = fetch_longbridge_quote_via_oauth(
        client_id="demo-key",
        symbol="600519",
        raw_symbol="600519.SH",
        store=store,
    )

    assert result["data_status"] == "ok"
    assert result["raw_symbol"] == "600519.SH"
    assert result["name"] == "贵州茅台"


def test_fetch_longbridge_quote_via_oauth_permission_required(tmp_path, monkeypatch) -> None:
    class FakeConfig:
        @staticmethod
        def from_oauth(oauth):
            return {"oauth": oauth}

    class FakeQuoteContext:
        def __init__(self, config):
            self.config = config

        def quote(self, symbols):
            assert symbols == ["AAPL.US"]
            raise RuntimeError("permission denied for quote package")

    fake_module = SimpleNamespace(
        Config=FakeConfig,
        QuoteContext=FakeQuoteContext,
        OAuthBuilder=SimpleNamespace,
    )
    store = LongbridgeOAuthStore(project_root=tmp_path)
    monkeypatch.setattr(
        "app_core.data_sources.longbridge_sdk_support.start_longbridge_oauth",
        lambda client_id, store, open_browser=True, verbose=True: {
            "status": "authorized",
            "message": "",
            "authorization_url": "",
            "oauth": object(),
        },
    )
    monkeypatch.setattr(
        "app_core.data_sources.longbridge_sdk_support.inspect_longbridge_sdk",
        lambda: {
            "sdk_importable": True,
            "sdk_version": "1.0.0",
            "available_symbols": {"Config": True, "QuoteContext": True, "OAuthBuilder": True},
            "openapi_module": fake_module,
            "error_message": "",
        },
    )

    result = fetch_longbridge_quote_via_oauth(
        client_id="demo-key",
        symbol="AAPL",
        raw_symbol="AAPL.US",
        store=store,
    )

    assert result["data_status"] == "permission_required"
    assert result["message"] == "当前账号可能未开通对应市场 OpenAPI 实时行情权限"
    assert result["error_message"] == ""


def test_sanitize_error_redacts_sensitive_info() -> None:
    from app_core.data_sources.longbridge_sdk_support import _sanitize_error

    msg = "Error: client_id=123, client_secret=abc, state=xyz, code=456, APP_KEY=key, APP_SECRET=secret"
    sanitized = _sanitize_error(msg)

    assert "123" in sanitized  # Values are not redacted by this simple replacer, only keywords
    assert "client_id" not in sanitized
    assert "client_secret" not in sanitized
    assert "state" not in sanitized
    assert "code" not in sanitized
    assert "APP_KEY" not in sanitized
    assert "APP_SECRET" not in sanitized
    assert "***" in sanitized
