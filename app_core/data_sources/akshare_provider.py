from __future__ import annotations

from collections.abc import Iterable
import inspect

import akshare as ak
import pandas as pd
from requests.exceptions import ConnectionError as RequestsConnectionError
from requests.exceptions import ProxyError


DATE_COLUMN_ALIASES = ("date", "日期", "Date", "trade_date", "交易日期")
CLOSE_COLUMN_ALIASES = ("close", "收盘", "收盘价", "Close", "latest_close")


def fetch_stock_daily_history(
    symbol: str,
    timeout_seconds: int = 10,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Fetch raw and normalized daily stock history from AKShare."""
    request_kwargs = {
        "symbol": symbol,
        "period": "daily",
        "adjust": "",
    }
    if _supports_timeout_parameter(ak.stock_zh_a_hist):
        request_kwargs["timeout"] = max(1, int(timeout_seconds))

    raw_dataframe = ak.stock_zh_a_hist(**request_kwargs)
    if raw_dataframe is None or raw_dataframe.empty:
        raise ValueError(f"{symbol} returned empty daily history")

    normalized_dataframe = normalize_daily_history(raw_dataframe)
    if normalized_dataframe.empty:
        raise ValueError(f"{symbol} has no usable daily rows after normalization")

    return raw_dataframe, normalized_dataframe


def normalize_daily_history(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Normalize date and close fields for downstream strategy use."""
    normalized = dataframe.copy()

    date_column = _find_column(normalized.columns, DATE_COLUMN_ALIASES)
    close_column = _find_column(normalized.columns, CLOSE_COLUMN_ALIASES)

    if date_column is None:
        raise ValueError(f"date column not found in columns: {list(normalized.columns)}")
    if close_column is None:
        raise ValueError(f"close column not found in columns: {list(normalized.columns)}")

    normalized["date"] = pd.to_datetime(normalized[date_column], errors="coerce")
    normalized["close"] = pd.to_numeric(normalized[close_column], errors="coerce")
    normalized = normalized.dropna(subset=["date", "close"]).copy()
    normalized = normalized.sort_values("date").reset_index(drop=True)
    normalized["date"] = normalized["date"].dt.strftime("%Y-%m-%d")

    return normalized


def summarize_fetch_error(error: BaseException, timeout_seconds: int = 10) -> str:
    """Convert network/runtime errors to a short user-facing message."""
    error_type = type(error).__name__
    flattened_message = " ".join(str(error).split())
    lowered_message = flattened_message.lower()

    if "remote end closed connection" in lowered_message:
        return "RemoteDisconnected: remote end closed connection"
    if error_type == "RemoteDisconnected":
        return "RemoteDisconnected: remote end closed connection"
    if error_type in {"ReadTimeout", "ConnectTimeout", "TimeoutError"} or "timed out" in lowered_message:
        return f"TimeoutError: request timed out after {timeout_seconds}s"
    if isinstance(error, ProxyError) or error_type == "ProxyError" or "proxy" in lowered_message:
        return "ProxyError: unable to connect to proxy"
    if (
        isinstance(error, RequestsConnectionError)
        or error_type == "ConnectionError"
        or "connection aborted" in lowered_message
        or "failed to establish a new connection" in lowered_message
        or "connection reset by peer" in lowered_message
    ):
        return "ConnectionError: connection failed"
    if error_type == "KeyboardInterrupt":
        return "KeyboardInterrupt: interrupted by user"

    short_message = flattened_message[:160]
    if len(flattened_message) > 160:
        short_message += "..."

    if short_message:
        return f"UnknownError: {short_message}"
    return "UnknownError: unexpected fetch error"


def _find_column(columns: Iterable[object], aliases: tuple[str, ...]) -> str | None:
    alias_lookup = {alias.lower(): alias for alias in aliases}
    for column in columns:
        column_name = str(column)
        if column_name.lower() in alias_lookup:
            return column_name
    return None


def _supports_timeout_parameter(callable_object: object) -> bool:
    try:
        signature = inspect.signature(callable_object)
    except (TypeError, ValueError):
        return False
    return "timeout" in signature.parameters
