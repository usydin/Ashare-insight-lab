from __future__ import annotations

import pandas as pd
from app_core.data_sources.akshare_provider import (
    ak,
    AKSHARE_IMPORT_ERROR,
    normalize_daily_history,
    _supports_timeout_parameter
)


def fetch_index_daily_history(
    symbol: str,
    timeout_seconds: int = 10,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """获取指数历史数据"""
    if ak is None:
        raise ImportError(f"akshare import failed: {AKSHARE_IMPORT_ERROR}") from AKSHARE_IMPORT_ERROR

    request_kwargs = {
        "symbol": symbol,
    }
    
    # 指数采集通常使用 stock_zh_index_daily
    if _supports_timeout_parameter(ak.stock_zh_index_daily):
        request_kwargs["timeout"] = max(1, int(timeout_seconds))

    raw_dataframe = ak.stock_zh_index_daily(**request_kwargs)
    if raw_dataframe is None or raw_dataframe.empty:
        raise ValueError(f"指数 {symbol} 返回了空的历史数据")

    normalized_dataframe = normalize_daily_history(raw_dataframe)
    if normalized_dataframe.empty:
        raise ValueError(f"指数 {symbol} 在标准化后没有可用数据")

    return raw_dataframe, normalized_dataframe
