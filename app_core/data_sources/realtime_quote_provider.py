from __future__ import annotations

from datetime import datetime
from typing import Any

import akshare as ak
import pandas as pd

from app_core.app_logger import get_logger

logger = get_logger()


class AkShareRealtimeQuoteProvider:
    """AkShare 实时行情 Provider。"""

    def __init__(self) -> None:
        self.provider_name = "AkShare"
        self.cache_ttl_seconds = 30
        self._cn_snapshot_cache: pd.DataFrame | None = None
        self._cn_snapshot_cache_time: datetime | None = None

    def fetch_quote(self, symbol: str, market: str = "CN") -> dict[str, Any]:
        """抓取单只实时行情快照，不写文件。"""
        if market != "CN":
            return self._build_unsupported_market_quote(symbol=symbol, market=market)

        snapshot = self._get_cn_snapshot()
        if isinstance(snapshot, dict):
            return self._build_base_quote(
                symbol=symbol,
                market=market,
                data_status="fetch_failed",
                error_message=str(snapshot.get("error_message", "")),
            )
        return self._build_quote_from_snapshot(snapshot=snapshot, symbol=symbol, market=market)

    def fetch_quotes(self, symbols: list[str], market: str = "CN") -> list[dict[str, Any]]:
        """批量抓取实时行情快照，对 CN 市场只拉取一次全量快照。"""
        normalized_symbols = [str(symbol).strip() for symbol in symbols if str(symbol).strip()]
        if not normalized_symbols:
            return []

        if market != "CN":
            return [
                self._build_unsupported_market_quote(symbol=symbol, market=market)
                for symbol in normalized_symbols
            ]

        snapshot = self._get_cn_snapshot()
        if isinstance(snapshot, dict):
            return [
                self._build_base_quote(
                    symbol=symbol,
                    market=market,
                    data_status="fetch_failed",
                    error_message=str(snapshot.get("error_message", "")),
                )
                for symbol in normalized_symbols
            ]

        return [
            self._build_quote_from_snapshot(snapshot=snapshot, symbol=symbol, market=market)
            for symbol in normalized_symbols
        ]

    def _get_cn_snapshot(self) -> pd.DataFrame | dict[str, str]:
        now = datetime.now()
        if (
            self._cn_snapshot_cache is not None
            and self._cn_snapshot_cache_time is not None
            and (now - self._cn_snapshot_cache_time).total_seconds() < self.cache_ttl_seconds
        ):
            print("[实时行情] 使用缓存的 A股实时快照。")
            return self._cn_snapshot_cache

        try:
            print("[实时行情] 正在拉取 A股实时快照...")
            dataframe = ak.stock_zh_a_spot_em()
            if dataframe is None or dataframe.empty:
                logger.error("[实时行情] AkShare 返回空数据")
                return {"error_message": "AkShare returned empty data"}

            self._cn_snapshot_cache = dataframe.copy()
            self._cn_snapshot_cache_time = now
            return self._cn_snapshot_cache
        except Exception as error:
            error_message = str(error)
            logger.error("[实时行情] 抓取异常: %s", error_message)
            return {"error_message": error_message}

    def _build_quote_from_snapshot(
        self,
        *,
        snapshot: pd.DataFrame,
        symbol: str,
        market: str,
    ) -> dict[str, Any]:
        code_column = self._pick_column(snapshot, ["代码", "code", "symbol"])
        if not code_column:
            return self._build_base_quote(
                symbol=symbol,
                market=market,
                data_status="fetch_failed",
                error_message="Missing symbol column in realtime snapshot",
            )

        normalized_symbol = str(symbol).strip()
        matched = snapshot[snapshot[code_column].astype(str).str.strip() == normalized_symbol]
        if matched.empty:
            print(f"[实时行情] 未找到代码: {normalized_symbol}")
            return self._build_base_quote(
                symbol=normalized_symbol,
                market=market,
                data_status="not_found",
                error_message=f"Symbol {normalized_symbol} not found in A-share spot data",
            )

        row = matched.iloc[0]
        return {
            **self._build_base_quote(symbol=normalized_symbol, market=market),
            "name": self._to_text(row.get(self._pick_column(snapshot, ["名称", "name"]))),
            "price": self._to_float(row.get(self._pick_column(snapshot, ["最新价", "close", "price"]))),
            "change": self._to_float(row.get(self._pick_column(snapshot, ["涨跌额", "change"]))),
            "pct_change": self._to_float(row.get(self._pick_column(snapshot, ["涨跌幅", "pct_chg", "pct_change"]))),
            "volume": self._to_float(row.get(self._pick_column(snapshot, ["成交量", "volume"]))),
            "amount": self._to_float(row.get(self._pick_column(snapshot, ["成交额", "amount"]))),
        }

    def _build_unsupported_market_quote(self, *, symbol: str, market: str) -> dict[str, Any]:
        print(f"[实时行情] 当前不支持市场: {market}，后续接入。")
        return self._build_base_quote(
            symbol=symbol,
            market=market,
            data_status="unsupported_market",
            error_message=f"Unsupported market: {market}",
        )

    def _build_base_quote(
        self,
        *,
        symbol: str,
        market: str,
        data_status: str = "ok",
        error_message: str = "",
    ) -> dict[str, Any]:
        return {
            "symbol": str(symbol).strip(),
            "market": market,
            "name": "",
            "price": None,
            "change": None,
            "pct_change": None,
            "volume": None,
            "amount": None,
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "provider": self.provider_name,
            "data_status": data_status,
            "error_message": error_message,
        }

    def _pick_column(self, dataframe: pd.DataFrame, candidates: list[str]) -> str | None:
        for candidate in candidates:
            if candidate in dataframe.columns:
                return candidate
        return None

    def _to_float(self, value: Any) -> float | None:
        """安全转换为浮点数。"""
        try:
            if value is None or pd.isna(value):
                return None
            return float(value)
        except (ValueError, TypeError):
            return None

    def _to_text(self, value: Any) -> str:
        if value is None or (not isinstance(value, str) and pd.isna(value)):
            return ""
        return str(value)
