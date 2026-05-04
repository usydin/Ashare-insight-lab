import pandas as pd

from app_core.data_sources import kline_provider
from app_core.data_sources.kline_provider import AkShareKlineProvider


def test_fetch_kline_unsupported_market() -> None:
    provider = AkShareKlineProvider()

    result = provider.fetch_kline("AAPL", market="US")

    assert result["data_status"] == "unsupported_market"
    assert result["rows"] == []


def test_fetch_kline_unsupported_period() -> None:
    provider = AkShareKlineProvider()

    result = provider.fetch_kline("600519", market="CN", period="5m")

    assert result["data_status"] == "unsupported_period"
    assert "Unsupported period" in result["error_message"]


def test_fetch_kline_cn_daily_success(monkeypatch) -> None:
    provider = AkShareKlineProvider()

    def fake_stock_zh_a_hist(symbol: str, period: str, adjust: str) -> pd.DataFrame:
        assert symbol == "600519"
        assert period == "daily"
        assert adjust == "qfq"
        return pd.DataFrame(
            {
                "日期": ["2024-01-01", "2024-01-02"],
                "开盘": [10.0, 10.2],
                "最高": [10.5, 10.8],
                "最低": [9.8, 10.1],
                "收盘": [10.3, 10.6],
                "成交量": [1000, 1200],
                "成交额": [100000, 125000],
            }
        )

    monkeypatch.setattr(kline_provider.ak, "stock_zh_a_hist", fake_stock_zh_a_hist)

    result = provider.fetch_kline("600519", period="daily", adjust="qfq", limit=120)

    assert result["data_status"] == "ok"
    assert len(result["rows"]) == 2
    assert result["rows"][0]["date"] == "2024-01-01"
    assert result["rows"][0]["open"] == 10.0
    assert result["rows"][0]["close"] == 10.3


def test_fetch_kline_limit_only_returns_last_n_rows(monkeypatch) -> None:
    provider = AkShareKlineProvider()

    def fake_stock_zh_a_hist(symbol: str, period: str, adjust: str) -> pd.DataFrame:
        del symbol, period, adjust
        return pd.DataFrame(
            {
                "日期": ["2024-01-01", "2024-01-02", "2024-01-03"],
                "开盘": [10.0, 10.2, 10.4],
                "最高": [10.5, 10.8, 11.0],
                "最低": [9.8, 10.1, 10.3],
                "收盘": [10.3, 10.6, 10.9],
                "成交量": [1000, 1200, 1500],
                "成交额": [100000, 125000, 150000],
            }
        )

    monkeypatch.setattr(kline_provider.ak, "stock_zh_a_hist", fake_stock_zh_a_hist)

    result = provider.fetch_kline("600519", period="daily", limit=2)

    assert result["data_status"] == "ok"
    assert len(result["rows"]) == 2
    assert result["rows"][0]["date"] == "2024-01-02"
    assert result["rows"][1]["date"] == "2024-01-03"


def test_fetch_kline_missing_fields_does_not_crash(monkeypatch) -> None:
    provider = AkShareKlineProvider()

    def fake_stock_zh_a_hist(symbol: str, period: str, adjust: str) -> pd.DataFrame:
        del symbol, period, adjust
        return pd.DataFrame(
            {
                "日期": ["2024-01-01"],
                "收盘": [10.3],
            }
        )

    monkeypatch.setattr(kline_provider.ak, "stock_zh_a_hist", fake_stock_zh_a_hist)

    result = provider.fetch_kline("600519")

    assert result["data_status"] == "ok"
    assert result["rows"][0]["open"] is None
    assert result["rows"][0]["close"] == 10.3
    assert result["rows"][0]["amount"] is None


def test_fetch_kline_exception_returns_fetch_failed(monkeypatch) -> None:
    provider = AkShareKlineProvider()

    def fake_stock_zh_a_hist(symbol: str, period: str, adjust: str) -> pd.DataFrame:
        del symbol, period, adjust
        raise RuntimeError("boom")

    monkeypatch.setattr(kline_provider.ak, "stock_zh_a_hist", fake_stock_zh_a_hist)

    result = provider.fetch_kline("600519")

    assert result["data_status"] == "fetch_failed"
    assert "boom" in result["error_message"]


def test_fetch_kline_empty_dataframe_returns_not_found(monkeypatch) -> None:
    provider = AkShareKlineProvider()

    def fake_stock_zh_a_hist(symbol: str, period: str, adjust: str) -> pd.DataFrame:
        del symbol, period, adjust
        return pd.DataFrame()

    monkeypatch.setattr(kline_provider.ak, "stock_zh_a_hist", fake_stock_zh_a_hist)

    result = provider.fetch_kline("600519")

    assert result["data_status"] == "not_found"


def test_fetch_kline_minute_period_uses_minute_interface(monkeypatch) -> None:
    provider = AkShareKlineProvider()
    captured_kwargs: dict[str, object] = {}

    def fake_stock_zh_a_hist_min_em(symbol: str, period: str, adjust: str) -> pd.DataFrame:
        captured_kwargs.update({"symbol": symbol, "period": period, "adjust": adjust})
        return pd.DataFrame(
            {
                "时间": ["2024-01-02 10:00:00"],
                "开盘": [10.0],
                "最高": [10.2],
                "最低": [9.9],
                "收盘": [10.1],
                "成交量": [200],
                "成交额": [20000],
            }
        )

    monkeypatch.setattr(kline_provider.ak, "stock_zh_a_hist_min_em", fake_stock_zh_a_hist_min_em)

    result = provider.fetch_kline("600519", period="60m", adjust="qfq")

    assert result["data_status"] == "ok"
    assert captured_kwargs == {"symbol": "600519", "period": "60", "adjust": "qfq"}
