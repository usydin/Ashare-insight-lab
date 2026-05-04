from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd

from app_core.data_sources.akshare_provider import normalize_daily_history
from app_core.path_utils import get_project_root
from app_core.storage.file_store import load_dataframe_csv


SOURCE_NAME = "local_cache"


def find_latest_raw_csv(symbol: str) -> Path | None:
    raw_dir = get_project_root() / "data" / "raw"
    preferred_path = raw_dir / f"{symbol}_daily_raw.csv"
    if preferred_path.exists():
        return preferred_path

    candidates = sorted(
        raw_dir.glob(f"{symbol}*_daily_raw.csv"),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )
    return candidates[0] if candidates else None


def load_stock_daily_history_from_cache(symbol: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    cache_path = find_latest_raw_csv(symbol)
    if cache_path is None:
        raise FileNotFoundError(f"local cache unavailable for {symbol}")

    try:
        raw_dataframe = load_dataframe_csv(cache_path)
    except Exception as error:
        raise ValueError(f"failed to read local cache csv for {symbol}: {type(error).__name__}") from error

    if raw_dataframe.empty:
        raise ValueError(f"local cache csv is empty for {symbol}")

    try:
        normalized_dataframe = normalize_daily_history(raw_dataframe)
    except Exception as error:
        raise ValueError(f"invalid local cache csv for {symbol}: {type(error).__name__}") from error

    if normalized_dataframe.empty:
        raise ValueError(f"local cache has no usable rows for {symbol}")

    return raw_dataframe, normalized_dataframe


def get_cache_metadata(symbol: str) -> dict[str, Any]:
    cache_path = find_latest_raw_csv(symbol)
    if cache_path is None:
        return {
            "path": "",
            "modified_at": "",
            "age_seconds": None,
            "row_count": 0,
        }

    stat = cache_path.stat()
    modified_at = datetime.fromtimestamp(stat.st_mtime)
    age_seconds = max(0, int((datetime.now() - modified_at).total_seconds()))

    row_count = 0
    try:
        dataframe = load_dataframe_csv(cache_path)
        row_count = len(dataframe)
    except Exception:
        row_count = 0

    return {
        "path": str(cache_path),
        "modified_at": modified_at.isoformat(timespec="seconds"),
        "age_seconds": age_seconds,
        "row_count": row_count,
    }
