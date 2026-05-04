from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import StrEnum
from typing import Any


class DataSourceCapability(StrEnum):
    STOCK_DAILY = "stock_daily"
    MARKET_INDEX = "market_index"
    SECTOR_BOARD = "sector_board"
    NEWS = "news"
    FINANCIALS = "financials"


@dataclass(slots=True)
class DataSourceRequest:
    symbol: str = ""
    code: str = ""
    market: str = ""
    start_date: str = ""
    end_date: str = ""
    timeout_seconds: int = 10
    extra: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class DataSourceResult:
    source_name: str
    ok: bool
    data: Any = None
    error_message: str = ""
    error_type: str = ""
    elapsed_ms: int = 0
    fetched_at: datetime = field(default_factory=lambda: datetime.now())
    fallback_used: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)
