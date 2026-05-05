from __future__ import annotations

from typing import Any

from app_core.data_sources.realtime_source_status import build_realtime_source_status
from app_core.security.longbridge_oauth_store import LongbridgeOAuthStore


def _mock_sdk_available() -> dict[str, Any]:
    return {
        "sdk_importable": True,
        "available_symbols": {"OAuthBuilder": True},
    }


def _source_map(summary: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["source_id"]: item for item in summary["sources"]}


def test_akshare_default_available(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(
        "app_core.data_sources.longbridge_quote_provider.inspect_longbridge_sdk",
        lambda: _mock_sdk_available(),
    )
    monkeypatch.delenv("MARKETAUX_API_TOKEN", raising=False)
    monkeypatch.delenv("TUSHARE_TOKEN", raising=False)
    monkeypatch.delenv("LONGBRIDGE_APP_KEY", raising=False)
    monkeypatch.delenv("LONGBRIDGE_APP_SECRET", raising=False)
    monkeypatch.delenv("LONGBRIDGE_ACCESS_TOKEN", raising=False)

    summary = build_realtime_source_status(project_root=tmp_path)
    akshare = _source_map(summary)["akshare"]

    assert summary["default_quote_source"] == "akshare"
    assert akshare["status"] == "available"
    assert akshare["token_status"] == "not_required"


def test_longbridge_without_oauth_token_is_blocked_candidate(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(
        "app_core.data_sources.longbridge_quote_provider.inspect_longbridge_sdk",
        lambda: _mock_sdk_available(),
    )
    monkeypatch.setenv("LONGBRIDGE_APP_KEY", "demo-key")
    monkeypatch.setenv("LONGBRIDGE_APP_SECRET", "demo-secret")
    monkeypatch.delenv("LONGBRIDGE_ACCESS_TOKEN", raising=False)

    summary = build_realtime_source_status(project_root=tmp_path)
    longbridge = _source_map(summary)["longbridge"]

    assert longbridge["status"] == "blocked"
    assert longbridge["priority"] == "candidate"
    assert longbridge["auth_mode"] == "oauthbuilder_required"
    assert longbridge["token_status"] == "missing"
    assert longbridge["sdk_status"] == "installed"
    assert longbridge["quote_only"] is True
    assert longbridge["trade_enabled"] is False


def test_marketaux_present_is_available(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(
        "app_core.data_sources.longbridge_quote_provider.inspect_longbridge_sdk",
        lambda: _mock_sdk_available(),
    )
    monkeypatch.setenv("MARKETAUX_API_TOKEN", "demo-marketaux-1234")

    summary = build_realtime_source_status(project_root=tmp_path)
    marketaux = _source_map(summary)["marketaux"]

    assert marketaux["status"] == "available"
    assert marketaux["token_status"] == "configured"


def test_marketaux_missing_is_missing_token(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(
        "app_core.data_sources.longbridge_quote_provider.inspect_longbridge_sdk",
        lambda: _mock_sdk_available(),
    )
    monkeypatch.delenv("MARKETAUX_API_TOKEN", raising=False)

    summary = build_realtime_source_status(project_root=tmp_path)
    marketaux = _source_map(summary)["marketaux"]

    assert marketaux["status"] == "missing_token"
    assert marketaux["token_status"] == "missing"


def test_tushare_default_reserved(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(
        "app_core.data_sources.longbridge_quote_provider.inspect_longbridge_sdk",
        lambda: _mock_sdk_available(),
    )
    monkeypatch.delenv("TUSHARE_TOKEN", raising=False)

    summary = build_realtime_source_status(project_root=tmp_path)
    tushare = _source_map(summary)["tushare"]

    assert tushare["status"] == "reserved"
    assert tushare["status_label"] == "预留"
    assert tushare["token_status"] == "missing"


def test_output_does_not_include_real_tokens(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(
        "app_core.data_sources.longbridge_quote_provider.inspect_longbridge_sdk",
        lambda: _mock_sdk_available(),
    )
    monkeypatch.setenv("MARKETAUX_API_TOKEN", "demo-marketaux-1234")
    monkeypatch.setenv("LONGBRIDGE_APP_KEY", "demo-key")
    monkeypatch.setenv("LONGBRIDGE_APP_SECRET", "demo-secret")
    store = LongbridgeOAuthStore(project_root=tmp_path)
    store.save_oauth_token(
        {
            "access_token": "demo_oauth",
            "refresh_token": "refresh_demo",
            "expires_at": "2030-01-01T00:00:00+00:00",
            "scope": "quote",
        }
    )

    summary = build_realtime_source_status(project_root=tmp_path)
    payload = str(summary)

    assert "demo-marketaux-1234" not in payload
    assert "demo_oauth" not in payload
    assert "refresh_demo" not in payload


def test_safety_trade_enabled_is_false(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(
        "app_core.data_sources.longbridge_quote_provider.inspect_longbridge_sdk",
        lambda: _mock_sdk_available(),
    )

    summary = build_realtime_source_status(project_root=tmp_path)

    assert summary["safety"]["quote_only"] is True
    assert summary["safety"]["trade_enabled"] is False
    assert summary["safety"]["order_enabled"] is False
