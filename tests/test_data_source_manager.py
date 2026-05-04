from __future__ import annotations

import pandas as pd

from app_core.data_sources.base import DataSourceResult
from app_core.data_sources.manager import DataSourceManager


def test_manager_registers_akshare_and_local_cache_by_default() -> None:
    manager = DataSourceManager()

    assert manager.list_sources() == ["akshare", "local_cache"]


def test_manager_primary_defaults_to_akshare_when_config_missing() -> None:
    manager = DataSourceManager(settings={})

    assert manager.get_primary_source() == "akshare"
    assert manager.get_fallback_order() == ["akshare", "local_cache"]
    assert manager.is_fallback_enabled() is True


def test_manager_fetch_stock_daily_history_returns_success_result(monkeypatch) -> None:
    raw_dataframe = pd.DataFrame({"日期": ["2024-01-01"], "收盘": [10.0]})
    normalized_dataframe = pd.DataFrame(
        {"日期": ["2024-01-01"], "收盘": [10.0], "date": ["2024-01-01"], "close": [10.0]}
    )

    monkeypatch.setattr(
        "app_core.data_sources.manager.fetch_stock_daily_history",
        lambda symbol, timeout_seconds=10: (raw_dataframe, normalized_dataframe),
    )

    manager = DataSourceManager()
    result = manager.fetch_stock_daily_history("000001", timeout_seconds=6)

    assert isinstance(result, DataSourceResult)
    assert result.ok is True
    assert result.source_name == "akshare"
    assert result.fallback_used is False
    assert result.metadata["row_count"] == 1
    assert result.data["normalized_dataframe"].equals(normalized_dataframe)


def test_manager_fetch_stock_daily_history_uses_local_cache_fallback(monkeypatch) -> None:
    raw_dataframe = pd.DataFrame({"日期": ["2024-01-01"], "收盘": [10.0]})
    normalized_dataframe = pd.DataFrame(
        {"date": ["2024-01-01"], "close": [10.0]}
    )

    monkeypatch.setattr(
        "app_core.data_sources.manager.fetch_stock_daily_history",
        lambda symbol, timeout_seconds=10: (_ for _ in ()).throw(RuntimeError("unexpected response body")),
    )
    monkeypatch.setattr(
        "app_core.data_sources.manager.load_stock_daily_history_from_cache",
        lambda symbol: (raw_dataframe, normalized_dataframe),
    )
    monkeypatch.setattr(
        DataSourceManager,
        "inspect_local_cache",
        lambda self, symbol: {
            "path": "/tmp/000001_daily_raw.csv",
            "modified_at": "2026-05-04T10:00:00",
            "age_seconds": 120,
            "row_count": 1,
            "available": True,
            "enabled": True,
            "max_age_days": 7,
            "allow_stale": True,
            "stale": False,
        },
    )

    manager = DataSourceManager()
    result = manager.fetch_stock_daily_history("000001", timeout_seconds=6)

    assert result.ok is True
    assert result.source_name == "local_cache"
    assert result.fallback_used is True
    assert result.metadata["primary_error_message"] == "UnknownError: unexpected response body"
    assert result.metadata["cache_path"] == "/tmp/000001_daily_raw.csv"
    assert result.metadata["cache_status"] == "cache_fallback"
    assert result.data["normalized_dataframe"].equals(normalized_dataframe)


def test_manager_fetch_stock_daily_history_returns_failure_when_local_cache_unavailable(monkeypatch) -> None:
    monkeypatch.setattr(
        "app_core.data_sources.manager.fetch_stock_daily_history",
        lambda symbol, timeout_seconds=10: (_ for _ in ()).throw(RuntimeError("unexpected response body")),
    )
    monkeypatch.setattr(
        DataSourceManager,
        "inspect_local_cache",
        lambda self, symbol: {
            "path": "",
            "modified_at": "",
            "age_seconds": None,
            "row_count": 0,
            "available": False,
            "enabled": True,
            "max_age_days": 7,
            "allow_stale": True,
            "stale": False,
        },
    )

    manager = DataSourceManager()
    result = manager.fetch_stock_daily_history("000001", timeout_seconds=6)

    assert result.ok is False
    assert result.source_name == "akshare"
    assert result.error_message == "UnknownError: unexpected response body; local cache unavailable"
    assert result.error_type == "UnknownError"
    assert result.fallback_used is False


def test_manager_fallback_order_without_local_cache_does_not_use_local_cache(monkeypatch) -> None:
    monkeypatch.setattr(
        "app_core.data_sources.manager.fetch_stock_daily_history",
        lambda symbol, timeout_seconds=10: (_ for _ in ()).throw(RuntimeError("unexpected response body")),
    )
    monkeypatch.setattr(
        "app_core.data_sources.manager.load_stock_daily_history_from_cache",
        lambda symbol: (_ for _ in ()).throw(AssertionError("local cache should not be used")),
    )

    manager = DataSourceManager(
        settings={
            "data_sources": {
                "primary": "akshare",
                "fallback_order": ["akshare"],
                "enable_fallback": True,
            }
        }
    )

    assert manager.get_fallback_order() == ["akshare"]
    assert manager.is_fallback_enabled() is True
    result = manager.fetch_stock_daily_history("000001", timeout_seconds=6)
    assert isinstance(result, DataSourceResult)
    assert result.ok is False
    assert result.fallback_used is False
