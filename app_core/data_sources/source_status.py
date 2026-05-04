from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import StrEnum


class SourceHealthStatus(StrEnum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNAVAILABLE = "unavailable"
    UNKNOWN = "unknown"


@dataclass(slots=True)
class SourceHealthRecord:
    source_name: str
    status: SourceHealthStatus = SourceHealthStatus.UNKNOWN
    checked_at: datetime = field(default_factory=lambda: datetime.now())
    latency_ms: int | None = None
    error_type: str = ""
    error_message: str = ""
    suggestion: str = ""
