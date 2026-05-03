import pandas as pd
import pytest
from app_core.data_sources.sector_provider import normalize_sector_history


def test_normalize_sector_history_handles_chinese_columns() -> None:
    df = pd.DataFrame({
        "日期": ["2024-01-01", "2024-01-02"],
        "开盘": [10.0, 11.0],
        "收盘": [10.5, 11.5],
        "最高": [10.8, 11.8],
        "最低": [9.8, 10.8],
        "成交量": [1000, 1100],
        "成交额": [10000, 12000]
    })
    
    normalized = normalize_sector_history(df)
    
    assert list(normalized.columns) == ["date", "open", "close", "high", "low", "volume", "amount"]
    assert normalized.iloc[0]["date"] == "2024-01-01"
    assert normalized.iloc[0]["close"] == 10.5
    assert normalized.iloc[1]["volume"] == 1100


def test_normalize_sector_history_raises_on_missing_required_columns() -> None:
    df = pd.DataFrame({
        "日期": ["2024-01-01"],
        "成交量": [1000]
    })
    with pytest.raises(ValueError, match="必需字段"):
        normalize_sector_history(df)


def test_normalize_sector_history_sorts_by_date() -> None:
    df = pd.DataFrame({
        "日期": ["2024-01-02", "2024-01-03", "2024-01-01"],
        "收盘": [11.5, 12.0, 10.5]
    })
    normalized = normalize_sector_history(df)
    assert len(normalized) == 3
    assert normalized.iloc[0]["date"] == "2024-01-01"
    assert normalized.iloc[1]["date"] == "2024-01-02"
    assert normalized.iloc[2]["date"] == "2024-01-03"
    assert normalized.iloc[-1]["date"] == "2024-01-03"


def test_normalize_sector_history_drops_invalid_rows() -> None:
    df = pd.DataFrame({
        "日期": ["2024-01-01", None, "invalid-date"],
        "收盘": [10.5, 11.5, 12.5]
    })
    normalized = normalize_sector_history(df)
    assert len(normalized) == 1
    assert normalized.iloc[0]["date"] == "2024-01-01"
