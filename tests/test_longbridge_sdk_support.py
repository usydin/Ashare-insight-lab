from __future__ import annotations

from datetime import datetime, timedelta, timezone
from types import SimpleNamespace

from app_core.data_sources.longbridge_sdk_support import (
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


def test_start_longbridge_oauth_app_key_missing(tmp_path, monkeypatch) -> None:
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

    assert result["status"] == "app_key_missing"


def test_start_longbridge_oauth_authorized_saves_metadata(tmp_path, monkeypatch, capsys) -> None:
    class FakeOAuth:
        scope = "quote"
        expires_at = (datetime.now(timezone.utc) + timedelta(days=1)).isoformat(timespec="seconds")

    class FakeOAuthBuilder:
        def __init__(self, client_id: str) -> None:
            self.client_id = client_id

        def build(self, callback):
            callback("https://example.com/oauth")
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

    result = start_longbridge_oauth(client_id="demo-key", store=store)
    captured = capsys.readouterr()
    status = store.get_oauth_token_status()

    assert result["status"] == "authorized"
    assert "Open this URL to authorize:" in captured.out
    assert status["sdk_managed"] is True
    assert status["token_file"] == "configured"


def test_fetch_longbridge_quote_via_oauth_sdk_missing(tmp_path, monkeypatch) -> None:
    store = LongbridgeOAuthStore(project_root=tmp_path)
    monkeypatch.setattr(
        "app_core.data_sources.longbridge_sdk_support.start_longbridge_oauth",
        lambda client_id, store: {
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
        lambda client_id, store: {
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
