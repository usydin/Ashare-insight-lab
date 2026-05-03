from __future__ import annotations

from datetime import datetime
import pandas as pd
from typing import Any
from app_core.data_sources.akshare_provider import (
    ak,
    AKSHARE_IMPORT_ERROR,
    _supports_timeout_parameter,
    _find_column,
    DATE_COLUMN_ALIASES,
    CLOSE_COLUMN_ALIASES,
)

# 新增板块特有的列名别名
OPEN_COLUMN_ALIASES = ("open", "开盘", "开盘价", "Open")
HIGH_COLUMN_ALIASES = ("high", "最高", "最高价", "High")
LOW_COLUMN_ALIASES = ("low", "最低", "最低价", "Low")
VOLUME_COLUMN_ALIASES = ("volume", "成交量", "Volume")
AMOUNT_COLUMN_ALIASES = ("amount", "成交额", "Amount")


def fetch_sector_board_daily_history(
    symbol: str,
    board_type: str,
    timeout_seconds: int = 15,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """获取行业或概念板块的历史数据"""
    if ak is None:
        raise ImportError(f"akshare import failed: {AKSHARE_IMPORT_ERROR}") from AKSHARE_IMPORT_ERROR

    # 根据 board_type 选择不同的接口和周期参数
    if board_type == "concept":
        api_func = ak.stock_board_concept_hist_em
        period_val = "daily"
    else:  # 默认为 industry
        api_func = ak.stock_board_industry_hist_em
        period_val = "日k"

    # 显式提供日期范围，避免 AKShare 默认值过旧 (某些接口默认 end_date 是 2022 年)
    # start_date 设为 2020 年以确保有足够的历史数据进行 MA 计算
    current_date_str = datetime.now().strftime("%Y%m%d")
    request_kwargs = {
        "symbol": symbol,
        "period": period_val,
        "start_date": "20200101",
        "end_date": current_date_str,
        "adjust": "",
    }

    # 尝试设置超时（如果接口支持）
    if _supports_timeout_parameter(api_func):
        request_kwargs["timeout"] = max(1, int(timeout_seconds))

    try:
        raw_dataframe = api_func(**request_kwargs)
    except TypeError:
        # 如果是因为不支持某个参数导致的 TypeError，尝试不带 timeout
        if "timeout" in request_kwargs:
            del request_kwargs["timeout"]
            raw_dataframe = api_func(**request_kwargs)
        else:
            raise

    if raw_dataframe is None or raw_dataframe.empty:
        raise ValueError(f"板块 {symbol} ({board_type}) 返回了空的历史数据")

    normalized_dataframe = normalize_sector_history(raw_dataframe)
    if normalized_dataframe.empty:
        raise ValueError(f"板块 {symbol} 在标准化后没有可用数据")

    return raw_dataframe, normalized_dataframe


def normalize_sector_history(dataframe: pd.DataFrame) -> pd.DataFrame:
    """标准化板块历史数据字段，确保最后一行是最新日期"""
    normalized = dataframe.copy()

    # 查找各列
    date_col = _find_column(normalized.columns, DATE_COLUMN_ALIASES)
    open_col = _find_column(normalized.columns, OPEN_COLUMN_ALIASES)
    close_col = _find_column(normalized.columns, CLOSE_COLUMN_ALIASES)
    high_col = _find_column(normalized.columns, HIGH_COLUMN_ALIASES)
    low_col = _find_column(normalized.columns, LOW_COLUMN_ALIASES)
    vol_col = _find_column(normalized.columns, VOLUME_COLUMN_ALIASES)
    amount_col = _find_column(normalized.columns, AMOUNT_COLUMN_ALIASES)

    if not date_col or not close_col:
        raise ValueError(f"必需字段 (date, close) 缺失。现有列: {list(normalized.columns)}")

    # 转换日期为 datetime 格式以便排序
    normalized["date_dt"] = pd.to_datetime(normalized[date_col], errors="coerce")
    
    # 转换数值列
    mapping = {
        close_col: "close",
        open_col: "open",
        high_col: "high",
        low_col: "low",
        vol_col: "volume",
        amount_col: "amount",
    }

    for src, dest in mapping.items():
        if src:
            normalized[dest] = pd.to_numeric(normalized[src], errors="coerce")
        else:
            normalized[dest] = None

    # 清洗：删除日期为空或收盘价为空的行
    normalized = normalized.dropna(subset=["date_dt", "close"]).copy()
    
    # 排序：按日期升序排列，确保最后一行是最新日期
    normalized = normalized.sort_values("date_dt").reset_index(drop=True)
    
    # 将日期转换回 YYYY-MM-DD 字符串格式用于输出
    normalized["date"] = normalized["date_dt"].dt.strftime("%Y-%m-%d")

    # 只保留需要的列，确保列存在
    keep_cols = ["date", "open", "close", "high", "low", "volume", "amount"]
    actual_cols = [c for c in keep_cols if c in normalized.columns]
    return normalized[actual_cols]
