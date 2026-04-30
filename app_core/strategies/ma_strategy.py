from __future__ import annotations

from collections.abc import Iterable
from typing import Any

import pandas as pd


CLOSE_COLUMN_ALIASES = ("close", "收盘", "收盘价", "Close", "latest_close")
DATE_COLUMN_ALIASES = ("date", "日期", "Date", "trade_date", "交易日期")


def analyze_ma_signal(dataframe: pd.DataFrame) -> dict[str, Any]:
    """Calculate MA-based signal from a daily history DataFrame."""
    close_column = _find_column(dataframe.columns, CLOSE_COLUMN_ALIASES)
    if close_column is None:
        return {
            "date": "",
            "close": None,
            "ma5": None,
            "ma20": None,
            "signal": "neutral",
            "reason": "未识别到收盘价字段",
            "data_status": "invalid_columns",
            "error_message": "close column not found",
        }

    working_dataframe = dataframe.copy()

    date_column = _find_column(working_dataframe.columns, DATE_COLUMN_ALIASES)
    if date_column is not None:
        working_dataframe["date"] = pd.to_datetime(
            working_dataframe[date_column],
            errors="coerce",
        )
        working_dataframe = working_dataframe.sort_values("date")
    elif "date" not in working_dataframe.columns:
        working_dataframe["date"] = pd.NaT

    working_dataframe["close"] = pd.to_numeric(
        working_dataframe[close_column],
        errors="coerce",
    )
    working_dataframe = working_dataframe.dropna(subset=["close"]).reset_index(drop=True)

    if working_dataframe.empty:
        return {
            "date": "",
            "close": None,
            "ma5": None,
            "ma20": None,
            "signal": "neutral",
            "reason": "无有效收盘价数据",
            "data_status": "empty_data",
            "error_message": "",
        }

    latest_close = round(float(working_dataframe.iloc[-1]["close"]), 4)
    latest_date = _format_date_value(working_dataframe.iloc[-1]["date"])

    if len(working_dataframe) < 20:
        return {
            "date": latest_date,
            "close": latest_close,
            "ma5": None,
            "ma20": None,
            "signal": "neutral",
            "reason": "历史数据不足 20 条，暂不生成均线信号",
            "data_status": "insufficient_data",
            "error_message": "",
        }

    working_dataframe["ma5"] = working_dataframe["close"].rolling(window=5).mean()
    working_dataframe["ma20"] = working_dataframe["close"].rolling(window=20).mean()
    latest_row = working_dataframe.iloc[-1]

    ma5 = round(float(latest_row["ma5"]), 4)
    ma20 = round(float(latest_row["ma20"]), 4)

    if latest_close > ma5 and latest_close > ma20:
        signal = "trend_up"
        reason = "close > ma5 且 close > ma20"
    elif latest_close < ma5 and latest_close < ma20:
        signal = "trend_down"
        reason = "close < ma5 且 close < ma20"
    else:
        signal = "neutral"
        reason = "close 与 ma5/ma20 没有形成同向趋势"

    return {
        "date": latest_date,
        "close": latest_close,
        "ma5": ma5,
        "ma20": ma20,
        "signal": signal,
        "reason": reason,
        "data_status": "ok",
        "error_message": "",
    }


def _find_column(columns: Iterable[object], aliases: tuple[str, ...]) -> str | None:
    alias_lookup = {alias.lower(): alias for alias in aliases}
    for column in columns:
        column_name = str(column)
        if column_name.lower() in alias_lookup:
            return column_name
    return None


def _format_date_value(value: Any) -> str:
    if pd.isna(value):
        return ""
    if hasattr(value, "strftime"):
        return value.strftime("%Y-%m-%d")
    return str(value)
