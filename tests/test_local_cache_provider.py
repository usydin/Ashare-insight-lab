from __future__ import annotations

from pathlib import Path

import pandas as pd

from app_core.data_sources import local_cache_provider


def test_find_latest_raw_csv_returns_symbol_raw_file(monkeypatch, tmp_path: Path) -> None:
    raw_dir = tmp_path / "data" / "raw"
    raw_dir.mkdir(parents=True)
    cache_path = raw_dir / "000001_daily_raw.csv"
    cache_path.write_text("日期,收盘\n2024-01-01,10.0\n", encoding="utf-8")

    monkeypatch.setattr(local_cache_provider, "get_project_root", lambda: tmp_path)

    assert local_cache_provider.find_latest_raw_csv("000001") == cache_path


def test_find_latest_raw_csv_returns_none_when_missing(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.setattr(local_cache_provider, "get_project_root", lambda: tmp_path)

    assert local_cache_provider.find_latest_raw_csv("000001") is None


def test_load_stock_daily_history_from_cache_returns_dataframes(monkeypatch, tmp_path: Path) -> None:
    raw_dir = tmp_path / "data" / "raw"
    raw_dir.mkdir(parents=True)
    cache_path = raw_dir / "000001_daily_raw.csv"
    dataframe = pd.DataFrame(
        {
            "日期": ["2024-01-01", "2024-01-02"],
            "收盘": [10.0, 10.5],
        }
    )
    dataframe.to_csv(cache_path, index=False, encoding="utf-8-sig")

    monkeypatch.setattr(local_cache_provider, "get_project_root", lambda: tmp_path)

    raw_dataframe, normalized_dataframe = local_cache_provider.load_stock_daily_history_from_cache("000001")

    assert len(raw_dataframe) == 2
    assert list(normalized_dataframe["date"]) == ["2024-01-01", "2024-01-02"]
    assert list(normalized_dataframe["close"]) == [10.0, 10.5]


def test_load_stock_daily_history_from_cache_raises_controlled_error_for_bad_csv(
    monkeypatch,
    tmp_path: Path,
) -> None:
    raw_dir = tmp_path / "data" / "raw"
    raw_dir.mkdir(parents=True)
    cache_path = raw_dir / "000001_daily_raw.csv"
    pd.DataFrame({"foo": [1], "bar": [2]}).to_csv(cache_path, index=False, encoding="utf-8-sig")

    monkeypatch.setattr(local_cache_provider, "get_project_root", lambda: tmp_path)

    try:
        local_cache_provider.load_stock_daily_history_from_cache("000001")
    except ValueError as error:
        assert str(error).startswith("invalid local cache csv for 000001")
    else:  # pragma: no cover
        raise AssertionError("expected ValueError for invalid local cache csv")


def test_get_cache_metadata_contains_path_mtime_age_and_row_count(
    monkeypatch,
    tmp_path: Path,
) -> None:
    raw_dir = tmp_path / "data" / "raw"
    raw_dir.mkdir(parents=True)
    cache_path = raw_dir / "000001_daily_raw.csv"
    pd.DataFrame(
        {
            "日期": ["2024-01-01", "2024-01-02"],
            "收盘": [10.0, 10.5],
        }
    ).to_csv(cache_path, index=False, encoding="utf-8-sig")

    monkeypatch.setattr(local_cache_provider, "get_project_root", lambda: tmp_path)

    metadata = local_cache_provider.get_cache_metadata("000001")

    assert metadata["path"] == str(cache_path)
    assert metadata["modified_at"]
    assert isinstance(metadata["age_seconds"], int)
    assert metadata["age_seconds"] >= 0
    assert metadata["row_count"] == 2
