from datetime import datetime
from typing import Any

import pytest

from app_core.data_sources.longbridge_quote_provider import LongbridgeQuoteProvider


@pytest.fixture
def provider() -> LongbridgeQuoteProvider:
    return LongbridgeQuoteProvider()


def test_symbol_mapping_cn(provider: LongbridgeQuoteProvider) -> None:
    assert provider._to_longbridge_symbol("600519", "CN") == "600519.SH"
    assert provider._to_longbridge_symbol("000001", "CN") == "000001.SZ"
    assert provider._to_longbridge_symbol("300750", "CN") == "300750.SZ"
    assert provider._to_longbridge_symbol("600519.SH", "CN") == "600519.SH"
    assert provider._to_longbridge_symbol("600519.sz", "CN") == "600519.SZ"
    assert provider._to_longbridge_symbol("ABC123", "CN") is None


def test_env_status_missing(provider: LongbridgeQuoteProvider, monkeypatch: pytest.MonkeyPatch) -> None:
    for key in ("LONGBRIDGE_APP_KEY", "LONGBRIDGE_APP_SECRET", "LONGBRIDGE_ACCESS_TOKEN"):
        monkeypatch.delenv(key, raising=False)

    status = provider.check_status()
    assert status["env"]["LONGBRIDGE_APP_KEY"] == "missing"
    assert status["env"]["LONGBRIDGE_APP_SECRET"] == "missing"
    assert status["env"]["LONGBRIDGE_ACCESS_TOKEN"] == "missing"


def test_env_status_present(provider: LongbridgeQuoteProvider, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LONGBRIDGE_APP_KEY", "k")
    monkeypatch.setenv("LONGBRIDGE_APP_SECRET", "s")
    monkeypatch.setenv("LONGBRIDGE_ACCESS_TOKEN", "t")
    monkeypatch.setenv("LONGBRIDGE_REGION", "hk")

    status = provider.check_status()
    assert status["env"]["LONGBRIDGE_APP_KEY"] == "present"
    assert status["env"]["LONGBRIDGE_APP_SECRET"] == "present"
    assert status["env"]["LONGBRIDGE_ACCESS_TOKEN"] == "present"
    assert status["optional_env"]["LONGBRIDGE_REGION"] in {"present", "missing"}


def test_fetch_quote_missing_env(provider: LongbridgeQuoteProvider, monkeypatch: pytest.MonkeyPatch) -> None:
    for key in ("LONGBRIDGE_APP_KEY", "LONGBRIDGE_APP_SECRET", "LONGBRIDGE_ACCESS_TOKEN"):
        monkeypatch.delenv(key, raising=False)
    res = provider.fetch_quote("600519", market="CN")
    assert res["data_status"] == "missing_env"


def test_fetch_quote_sdk_missing(provider: LongbridgeQuoteProvider, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LONGBRIDGE_APP_KEY", "k")
    monkeypatch.setenv("LONGBRIDGE_APP_SECRET", "s")
    monkeypatch.setenv("LONGBRIDGE_ACCESS_TOKEN", "t")
    # 模拟 SDK 缺失：将模块变量 lb 设置为 None
    monkeypatch.setattr("app_core.data_sources.longbridge_quote_provider.lb", None, raising=True)
    res = provider.fetch_quote("600519", market="CN")
    assert res["data_status"] == "sdk_missing"


def test_fetch_quote_unknown_symbol(provider: LongbridgeQuoteProvider, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LONGBRIDGE_APP_KEY", "k")
    monkeypatch.setenv("LONGBRIDGE_APP_SECRET", "s")
    monkeypatch.setenv("LONGBRIDGE_ACCESS_TOKEN", "t")
    # 模拟 SDK 可用
    class DummyLB:
        pass
    monkeypatch.setattr("app_core.data_sources.longbridge_quote_provider.lb", DummyLB(), raising=True)
    res = provider.fetch_quote("ABC123", market="CN")
    assert res["data_status"] == "unsupported_symbol"


def test_fetch_quote_success(provider: LongbridgeQuoteProvider, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LONGBRIDGE_APP_KEY", "k")
    monkeypatch.setenv("LONGBRIDGE_APP_SECRET", "s")
    monkeypatch.setenv("LONGBRIDGE_ACCESS_TOKEN", "t")
    class DummyLB:
        pass
    monkeypatch.setattr("app_core.data_sources.longbridge_quote_provider.lb", DummyLB(), raising=True)
    # 模拟底层快照返回
    def fake_snapshot(lb_symbol: str) -> dict[str, Any]:
        assert lb_symbol == "600519.SH"
        return {
            "name": "贵州茅台",
            "current_price": 1650.0,
            "change": 15.5,
            "change_percent": 0.95,
            "open": 1640.0,
            "high": 1660.0,
            "low": 1630.0,
            "prev_close": 1634.5,
            "volume": 12000,
            "turnover": 19800000.0,
            "timestamp": datetime.now().isoformat(timespec="seconds"),
        }
    monkeypatch.setattr(provider, "_fetch_lb_quote_snapshot", fake_snapshot, raising=True)
    res = provider.fetch_quote("600519", market="CN")
    assert res["data_status"] == "ok"
    assert res["raw_symbol"] == "600519.SH"
    assert res["name"] == "贵州茅台"
    assert res["current_price"] == 1650.0


def test_fetch_quote_exception_sanitizes_error(provider: LongbridgeQuoteProvider, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LONGBRIDGE_APP_KEY", "k")
    monkeypatch.setenv("LONGBRIDGE_APP_SECRET", "s")
    monkeypatch.setenv("LONGBRIDGE_ACCESS_TOKEN", "t")
    class DummyLB:
        pass
    monkeypatch.setattr("app_core.data_sources.longbridge_quote_provider.lb", DummyLB(), raising=True)
    def boom(lb_symbol: str) -> dict[str, Any]:
        raise RuntimeError("ACCESS_TOKEN invalid")
    monkeypatch.setattr(provider, "_fetch_lb_quote_snapshot", boom, raising=True)
    res = provider.fetch_quote("600519", market="CN")
    assert res["data_status"] == "fetch_failed"
    assert "ACCESS_TOKEN" not in res["error_message"]
