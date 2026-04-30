from http.client import RemoteDisconnected

import pandas as pd
from requests.exceptions import ProxyError, ReadTimeout

from app_core.data_sources import akshare_provider


def test_fetch_stock_daily_history_passes_timeout_when_supported(monkeypatch) -> None:
    captured_kwargs: dict[str, object] = {}

    def fake_stock_zh_a_hist(symbol: str, period: str, adjust: str, timeout: int) -> pd.DataFrame:
        captured_kwargs.update(
            {
                "symbol": symbol,
                "period": period,
                "adjust": adjust,
                "timeout": timeout,
            }
        )
        return pd.DataFrame(
            {
                "日期": ["2024-01-01", "2024-01-02"],
                "收盘": [10.0, 10.5],
            }
        )

    monkeypatch.setattr(akshare_provider.ak, "stock_zh_a_hist", fake_stock_zh_a_hist)

    raw_dataframe, normalized_dataframe = akshare_provider.fetch_stock_daily_history(
        "600519",
        timeout_seconds=8,
    )

    assert not raw_dataframe.empty
    assert list(normalized_dataframe.columns) == ["日期", "收盘", "date", "close"]
    assert captured_kwargs == {
        "symbol": "600519",
        "period": "daily",
        "adjust": "",
        "timeout": 8,
    }


def test_fetch_stock_daily_history_skips_timeout_when_not_supported(monkeypatch) -> None:
    captured_kwargs: dict[str, object] = {}

    def fake_stock_zh_a_hist(symbol: str, period: str, adjust: str) -> pd.DataFrame:
        captured_kwargs.update(
            {
                "symbol": symbol,
                "period": period,
                "adjust": adjust,
            }
        )
        return pd.DataFrame(
            {
                "日期": ["2024-01-01", "2024-01-02"],
                "收盘": [10.0, 10.5],
            }
        )

    monkeypatch.setattr(akshare_provider.ak, "stock_zh_a_hist", fake_stock_zh_a_hist)

    akshare_provider.fetch_stock_daily_history("000001", timeout_seconds=10)

    assert captured_kwargs == {
        "symbol": "000001",
        "period": "daily",
        "adjust": "",
    }


def test_summarize_fetch_error_distinguishes_common_network_errors() -> None:
    assert (
        akshare_provider.summarize_fetch_error(RemoteDisconnected("Remote end closed connection"))
        == "RemoteDisconnected: remote end closed connection"
    )
    assert (
        akshare_provider.summarize_fetch_error(ProxyError("proxy error"))
        == "ProxyError: unable to connect to proxy"
    )
    assert (
        akshare_provider.summarize_fetch_error(ReadTimeout("timed out"), timeout_seconds=10)
        == "TimeoutError: request timed out after 10s"
    )
