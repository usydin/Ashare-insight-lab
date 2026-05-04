from datetime import timedelta
from unittest.mock import patch

import pandas as pd
import pytest

from app_core.data_sources.realtime_quote_provider import AkShareRealtimeQuoteProvider


@pytest.fixture
def provider() -> AkShareRealtimeQuoteProvider:
    return AkShareRealtimeQuoteProvider()


@pytest.fixture
def cn_snapshot() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "代码": "600519",
                "名称": "贵州茅台",
                "最新价": 1650.0,
                "涨跌额": 15.5,
                "涨跌幅": 0.95,
                "成交量": 10000.0,
                "成交额": 16500000.0,
            },
            {
                "代码": "300750",
                "名称": "宁德时代",
                "最新价": 198.5,
                "涨跌额": -2.3,
                "涨跌幅": -1.15,
                "成交量": 5000.0,
                "成交额": 992500.0,
            },
            {
                "代码": "000001",
                "名称": "上证指数",
                "最新价": 3050.25,
                "涨跌额": 12.45,
                "涨跌幅": 0.41,
                "成交量": 3200.0,
                "成交额": 8000000.0,
            },
        ]
    )


def test_fetch_quote_unsupported_market(provider: AkShareRealtimeQuoteProvider) -> None:
    result = provider.fetch_quote("AAPL", market="US")
    assert result["data_status"] == "unsupported_market"
    assert "Unsupported market" in result["error_message"]


@patch("app_core.data_sources.realtime_quote_provider.ak.stock_zh_a_spot_em")
def test_fetch_quote_cn_success(
    mock_spot,
    provider: AkShareRealtimeQuoteProvider,
    cn_snapshot: pd.DataFrame,
) -> None:
    mock_spot.return_value = cn_snapshot

    result = provider.fetch_quote("600519", market="CN")

    assert result["data_status"] == "ok"
    assert result["symbol"] == "600519"
    assert result["name"] == "贵州茅台"
    assert result["price"] == 1650.0
    assert result["change"] == 15.5
    assert result["pct_change"] == 0.95
    assert result["volume"] == 10000.0
    assert result["amount"] == 16500000.0
    assert "timestamp" in result


@patch("app_core.data_sources.realtime_quote_provider.ak.stock_zh_a_spot_em")
def test_fetch_quote_cn_missing_fields_does_not_crash(
    mock_spot,
    provider: AkShareRealtimeQuoteProvider,
) -> None:
    mock_spot.return_value = pd.DataFrame(
        [{"代码": "600519", "名称": "贵州茅台"}]
    )

    result = provider.fetch_quote("600519", market="CN")

    assert result["data_status"] == "ok"
    assert result["name"] == "贵州茅台"
    assert result["price"] is None
    assert result["amount"] is None


@patch("app_core.data_sources.realtime_quote_provider.ak.stock_zh_a_spot_em")
def test_fetch_quote_cn_not_found(
    mock_spot,
    provider: AkShareRealtimeQuoteProvider,
    cn_snapshot: pd.DataFrame,
) -> None:
    mock_spot.return_value = cn_snapshot

    result = provider.fetch_quote("999999", market="CN")
    assert result["data_status"] == "not_found"
    assert "not found" in result["error_message"].lower()


@patch("app_core.data_sources.realtime_quote_provider.ak.stock_zh_a_spot_em")
def test_fetch_quote_cn_fetch_failed_empty(
    mock_spot,
    provider: AkShareRealtimeQuoteProvider,
) -> None:
    mock_spot.return_value = pd.DataFrame()

    result = provider.fetch_quote("600519", market="CN")
    assert result["data_status"] == "fetch_failed"


@patch("app_core.data_sources.realtime_quote_provider.ak.stock_zh_a_spot_em")
def test_fetch_quote_cn_exception(
    mock_spot,
    provider: AkShareRealtimeQuoteProvider,
) -> None:
    mock_spot.side_effect = Exception("Network error")

    result = provider.fetch_quote("600519", market="CN")
    assert result["data_status"] == "fetch_failed"
    assert "Network error" in result["error_message"]


@patch("app_core.data_sources.realtime_quote_provider.ak.stock_zh_a_spot_em")
def test_fetch_quotes_cn_batch_calls_akshare_once(
    mock_spot,
    provider: AkShareRealtimeQuoteProvider,
    cn_snapshot: pd.DataFrame,
) -> None:
    mock_spot.return_value = cn_snapshot

    results = provider.fetch_quotes(["600519", "300750", "000001"], market="CN")

    assert mock_spot.call_count == 1
    assert len(results) == 3
    assert [item["data_status"] for item in results] == ["ok", "ok", "ok"]


@patch("app_core.data_sources.realtime_quote_provider.ak.stock_zh_a_spot_em")
def test_fetch_quotes_cn_one_symbol_not_found(
    mock_spot,
    provider: AkShareRealtimeQuoteProvider,
    cn_snapshot: pd.DataFrame,
) -> None:
    mock_spot.return_value = cn_snapshot

    results = provider.fetch_quotes(["600519", "999999", "300750"], market="CN")

    assert results[0]["data_status"] == "ok"
    assert results[1]["data_status"] == "not_found"
    assert results[2]["data_status"] == "ok"


@patch("app_core.data_sources.realtime_quote_provider.ak.stock_zh_a_spot_em")
def test_fetch_quote_reuses_cache_within_ttl(
    mock_spot,
    provider: AkShareRealtimeQuoteProvider,
    cn_snapshot: pd.DataFrame,
) -> None:
    mock_spot.return_value = cn_snapshot

    first = provider.fetch_quote("600519", market="CN")
    second = provider.fetch_quote("300750", market="CN")

    assert first["data_status"] == "ok"
    assert second["data_status"] == "ok"
    assert mock_spot.call_count == 1


@patch("app_core.data_sources.realtime_quote_provider.ak.stock_zh_a_spot_em")
def test_fetch_quote_refreshes_cache_after_ttl(
    mock_spot,
    provider: AkShareRealtimeQuoteProvider,
    cn_snapshot: pd.DataFrame,
) -> None:
    mock_spot.return_value = cn_snapshot

    provider.fetch_quote("600519", market="CN")
    assert provider._cn_snapshot_cache_time is not None
    provider._cn_snapshot_cache_time = provider._cn_snapshot_cache_time - timedelta(seconds=31)

    provider.fetch_quote("300750", market="CN")

    assert mock_spot.call_count == 2


def test_fetch_quotes_unsupported_market(provider: AkShareRealtimeQuoteProvider) -> None:
    results = provider.fetch_quotes(["AAPL", "MSFT"], market="US")
    assert len(results) == 2
    assert all(item["data_status"] == "unsupported_market" for item in results)


def test_to_float_safety(provider: AkShareRealtimeQuoteProvider) -> None:
    assert provider._to_float(10.5) == 10.5
    assert provider._to_float("10.5") == 10.5
    assert provider._to_float(None) is None
    assert provider._to_float("abc") is None
