import pandas as pd

from app_core.strategies.ma_strategy import analyze_ma_signal


def test_analyze_ma_signal_returns_trend_up() -> None:
    dataframe = pd.DataFrame(
        {
            "日期": pd.date_range("2024-01-01", periods=25, freq="D"),
            "收盘": list(range(1, 26)),
        }
    )

    result = analyze_ma_signal(dataframe)

    assert result["data_status"] == "ok"
    assert result["signal"] == "trend_up"
    assert result["ma5"] is not None
    assert result["ma20"] is not None


def test_analyze_ma_signal_returns_insufficient_data() -> None:
    dataframe = pd.DataFrame(
        {
            "date": pd.date_range("2024-01-01", periods=10, freq="D"),
            "close": list(range(10, 20)),
        }
    )

    result = analyze_ma_signal(dataframe)

    assert result["data_status"] == "insufficient_data"
    assert result["signal"] == "neutral"
    assert result["ma20"] is None
