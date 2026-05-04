from __future__ import annotations

import inspect
from typing import Any

import pandas as pd

try:
    import akshare as ak
    AKSHARE_IMPORT_ERROR: BaseException | None = None
except Exception as error:  # pragma: no cover - depends on runtime env
    ak = None
    AKSHARE_IMPORT_ERROR = error


SUPPORTED_PERIODS = {"daily", "weekly", "monthly", "60m", "30m", "15m"}
MINUTE_PERIOD_MAP = {
    "60m": "60",
    "30m": "30",
    "15m": "15",
}


class AkShareKlineProvider:
    """AkShare K 线基础 Provider。"""

    def __init__(self) -> None:
        self.provider_name = "AkShare"

    def fetch_kline(
        self,
        symbol: str,
        market: str = "CN",
        period: str = "daily",
        adjust: str = "qfq",
        limit: int = 120,
    ) -> dict[str, Any]:
        """抓取只读 K 线数据，不写文件。"""
        normalized_symbol = str(symbol).strip()
        normalized_market = str(market).strip().upper()
        normalized_period = str(period).strip().lower()
        normalized_adjust = str(adjust).strip().lower()
        normalized_limit = max(1, int(limit))

        if normalized_market != "CN":
            print(f"[K线] 当前不支持市场: {normalized_market}，后续接入。")
            return self._build_response(
                symbol=normalized_symbol,
                market=normalized_market,
                period=normalized_period,
                adjust=normalized_adjust,
                data_status="unsupported_market",
                error_message=f"Unsupported market: {normalized_market}",
            )

        if normalized_period not in SUPPORTED_PERIODS:
            print(f"[K线] 当前不支持周期: {normalized_period}")
            return self._build_response(
                symbol=normalized_symbol,
                market=normalized_market,
                period=normalized_period,
                adjust=normalized_adjust,
                data_status="unsupported_period",
                error_message=f"Unsupported period: {normalized_period}",
            )

        if ak is None:
            return self._build_response(
                symbol=normalized_symbol,
                market=normalized_market,
                period=normalized_period,
                adjust=normalized_adjust,
                data_status="fetch_failed",
                error_message=f"akshare import failed: {AKSHARE_IMPORT_ERROR}",
            )

        try:
            print(f"[K线] 正在拉取 {normalized_symbol} / {normalized_period} K线...")
            dataframe = self._fetch_raw_dataframe(
                symbol=normalized_symbol,
                period=normalized_period,
                adjust=normalized_adjust,
            )
            if dataframe is None or dataframe.empty:
                print(f"[K线] 未获取到数据: {normalized_symbol}")
                return self._build_response(
                    symbol=normalized_symbol,
                    market=normalized_market,
                    period=normalized_period,
                    adjust=normalized_adjust,
                    data_status="not_found",
                    error_message=f"No kline data found for {normalized_symbol}",
                )

            rows = self._normalize_rows(dataframe.tail(normalized_limit).reset_index(drop=True))
            if not rows:
                return self._build_response(
                    symbol=normalized_symbol,
                    market=normalized_market,
                    period=normalized_period,
                    adjust=normalized_adjust,
                    data_status="not_found",
                    error_message=f"No usable kline rows found for {normalized_symbol}",
                )

            return self._build_response(
                symbol=normalized_symbol,
                market=normalized_market,
                period=normalized_period,
                adjust=normalized_adjust,
                data_status="ok",
                rows=rows,
            )
        except Exception as error:
            print(f"[K线] 抓取异常: {error}")
            return self._build_response(
                symbol=normalized_symbol,
                market=normalized_market,
                period=normalized_period,
                adjust=normalized_adjust,
                data_status="fetch_failed",
                error_message=str(error),
            )

    def _fetch_raw_dataframe(self, *, symbol: str, period: str, adjust: str) -> pd.DataFrame:
        if period in {"daily", "weekly", "monthly"}:
            request_kwargs: dict[str, Any] = {
                "symbol": symbol,
                "period": period,
                "adjust": adjust,
            }
            return ak.stock_zh_a_hist(**request_kwargs)

        minute_period = MINUTE_PERIOD_MAP[period]
        request_kwargs = {
            "symbol": symbol,
            "period": minute_period,
            "adjust": adjust,
        }
        if not _supports_parameter(ak.stock_zh_a_hist_min_em, "adjust"):
            request_kwargs.pop("adjust", None)
        return ak.stock_zh_a_hist_min_em(**request_kwargs)

    def _normalize_rows(self, dataframe: pd.DataFrame) -> list[dict[str, Any]]:
        date_column = _find_column(dataframe.columns, ("日期", "时间", "date", "datetime", "Date", "trade_time"))
        open_column = _find_column(dataframe.columns, ("开盘", "open", "Open"))
        high_column = _find_column(dataframe.columns, ("最高", "high", "High"))
        low_column = _find_column(dataframe.columns, ("最低", "low", "Low"))
        close_column = _find_column(dataframe.columns, ("收盘", "close", "Close"))
        volume_column = _find_column(dataframe.columns, ("成交量", "volume", "Volume"))
        amount_column = _find_column(dataframe.columns, ("成交额", "amount", "Amount"))

        rows: list[dict[str, Any]] = []
        for _, item in dataframe.iterrows():
            rows.append(
                {
                    "date": self._to_text(item.get(date_column) if date_column else ""),
                    "open": self._to_float(item.get(open_column) if open_column else None),
                    "high": self._to_float(item.get(high_column) if high_column else None),
                    "low": self._to_float(item.get(low_column) if low_column else None),
                    "close": self._to_float(item.get(close_column) if close_column else None),
                    "volume": self._to_float(item.get(volume_column) if volume_column else None),
                    "amount": self._to_float(item.get(amount_column) if amount_column else None),
                }
            )
        return rows

    def _build_response(
        self,
        *,
        symbol: str,
        market: str,
        period: str,
        adjust: str,
        data_status: str,
        error_message: str = "",
        rows: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        return {
            "symbol": symbol,
            "market": market,
            "period": period,
            "adjust": adjust,
            "provider": self.provider_name,
            "data_status": data_status,
            "error_message": error_message,
            "rows": rows or [],
        }

    def _to_float(self, value: Any) -> float | None:
        try:
            if value is None or pd.isna(value):
                return None
            return float(value)
        except (TypeError, ValueError):
            return None

    def _to_text(self, value: Any) -> str:
        if value is None:
            return ""
        try:
            if pd.isna(value):
                return ""
        except TypeError:
            pass
        return str(value)


def _find_column(columns: list[Any] | pd.Index, aliases: tuple[str, ...]) -> str | None:
    alias_lookup = {alias.lower() for alias in aliases}
    for column in columns:
        column_name = str(column)
        if column_name.lower() in alias_lookup:
            return column_name
    return None


def _supports_parameter(callable_object: object, parameter_name: str) -> bool:
    try:
        signature = inspect.signature(callable_object)
    except (TypeError, ValueError):
        return False
    return parameter_name in signature.parameters
