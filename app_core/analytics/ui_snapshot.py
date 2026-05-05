from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime
from typing import Any

from app_core.analytics.dashboard_summary import build_dashboard_summary
from app_core.analytics.review_queue import build_review_queue
from app_core.analytics.history_summary import build_signal_change_summary
from app_core.data_sources.realtime_source_status import build_realtime_source_status
from app_core.project_info import (
    APP_NAME_CN,
    APP_NAME_EN,
    VERSION,
    STAGE,
    DEVELOPER,
    COPYRIGHT_TEXT,
)
from app_core.path_utils import get_project_root
from app_core.storage.file_store import ensure_directory


def build_ui_snapshot(database_path: str | Path | None = None) -> dict[str, Any]:
    """构建统一的 UI 数据快照"""
    # 1. 获取各个摘要数据
    dashboard = build_dashboard_summary(database_path)
    queue = build_review_queue(database_path)
    changes = build_signal_change_summary(database_path=database_path)
    source_status = build_realtime_source_status()
    
    latest_run = dashboard.get("latest_run")
    messages = []
    if not latest_run:
        messages.append(dashboard.get("message", "暂无历史运行记录"))

    # 2. 统计 review_queue
    queue_count = len(queue)
    high_count = sum(1 for item in queue if item["severity"] == "high")
    medium_count = sum(1 for item in queue if item["severity"] == "medium")
    low_count = sum(1 for item in queue if item["severity"] == "low")

    # 3. 构造路径索引
    paths = {
        "database": "data/history/ashare_insight_lab.sqlite3",
        "daily_report": latest_run["report_path"] if latest_run else "",
        "dashboard_summary_json": "data/processed/dashboard_summary.json",
        "review_queue_json": "data/processed/review_queue.json",
        "review_queue_csv": "data/processed/review_queue.csv",
        "signal_changes_csv": "data/processed/signal_changes.csv",
        "ui_snapshot_json": "data/processed/ui_snapshot.json"
    }

    # 4. 组装快照
    snapshot = {
        "app": {
            "name_cn": APP_NAME_CN,
            "name_en": APP_NAME_EN,
            "version": VERSION,
            "stage": STAGE,
            "developer": DEVELOPER,
            "copyright": COPYRIGHT_TEXT
        },
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "latest_run": latest_run,
        "dashboard_summary": dashboard,
        "source_status": {
            "default_quote_source": source_status["default_quote_source"],
            "sources": source_status["sources"],
        },
        "review_queue": {
            "count": queue_count,
            "high_count": high_count,
            "medium_count": medium_count,
            "low_count": low_count,
            "items": queue
        },
        "signal_changes": {
            "latest_run_id": changes["latest_run_id"],
            "previous_run_id": changes["previous_run_id"],
            "summary": changes["summary"],
            "top_changes": (changes["index_changes"] + changes["sector_changes"] + changes["stock_changes"])[:10]
        },
        "data_health": dashboard.get("data_health", {}),
        "paths": paths,
        "messages": messages
    }
    
    return snapshot


def write_ui_snapshot_json(
    output_path: str | Path = "data/processed/ui_snapshot.json",
    database_path: str | Path | None = None,
) -> Path:
    """写出 UI 数据快照到 JSON 文件"""
    snapshot = build_ui_snapshot(database_path)
    
    root = get_project_root()
    path = root / output_path if not Path(output_path).is_absolute() else Path(output_path)
    
    ensure_directory(path.parent)
    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, ensure_ascii=False, indent=2)
        
    return path
