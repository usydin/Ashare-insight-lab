from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from app_core.analytics.history_summary import (
    build_signal_change_summary,
    get_latest_run_pair,
    get_run_snapshot,
)
from app_core.project_info import APP_NAME_CN, VERSION, STAGE
from app_core.storage.file_store import ensure_directory
from app_core.path_utils import get_project_root


def build_dashboard_summary(database_path: str | Path | None = None) -> dict[str, Any]:
    """构建 Dashboard 摘要数据"""
    pair = get_latest_run_pair(database_path)
    latest_run = pair["latest_run"]
    
    if not latest_run:
        return {
            "app": {
                "name": APP_NAME_CN,
                "version": VERSION,
                "stage": STAGE
            },
            "latest_run": None,
            "message": "未发现运行记录"
        }

    latest_run_id = latest_run["id"]
    snapshot = get_run_snapshot(latest_run_id, database_path)
    
    # 1. 信号概览统计
    signal_overview = {
        "index": _count_signals(snapshot["indices"]),
        "sector": _count_signals(snapshot["sectors"]),
        "stock": _count_signals(snapshot["stocks"])
    }

    # 2. 变化摘要 (复用 history_summary)
    change_summary = build_signal_change_summary(latest_run_id=latest_run_id, database_path=database_path)
    
    # 3. 风险项提取
    risk_items = change_summary["risk_items"]
    
    # 4. 数据健康统计
    data_health = {
        "ok_count": (latest_run["index_count"] + latest_run["sector_count"] + latest_run["stock_count"]) - len(risk_items),
        "fetch_failed_count": change_summary["summary"]["fetch_failed_count"],
        "stale_data_count": change_summary["summary"]["stale_data_count"],
        "stale_cache_count": change_summary["summary"].get("stale_cache_count", 0),
        "cache_fallback_count": change_summary["summary"].get("cache_fallback_count", 0),
        "unavailable_count": change_summary["summary"]["unavailable_count"],
        "insufficient_data_count": sum(1 for item in risk_items if item["latest_data_status"] == "insufficient_data"),
        "risk_item_count": len(risk_items)
    }

    # 5. 自选股关注点
    stocks = snapshot["stocks"]
    watchlist_focus = {
        "high_priority": [s for s in stocks if s.get("priority") in ["high", "P1"]],
        "holding": [s for s in stocks if any(kw in (s.get("position_status") or "").lower() for kw in ["holding", "持仓", "in_position"])],
        "watching": [s for s in stocks if any(kw in (s.get("position_status") or "").lower() for kw in ["watch", "观察", "observing"])]
    }

    return {
        "app": {
            "name": APP_NAME_CN,
            "version": VERSION,
            "stage": STAGE
        },
        "latest_run": latest_run,
        "data_health": data_health,
        "signal_overview": signal_overview,
        "changes": {
            "latest_run_id": change_summary["latest_run_id"],
            "previous_run_id": change_summary["previous_run_id"],
            "index_change_count": change_summary["summary"]["index_change_count"],
            "sector_change_count": change_summary["summary"]["sector_change_count"],
            "stock_change_count": change_summary["summary"]["stock_change_count"],
            "risk_item_count": change_summary["summary"]["risk_item_count"],
            "top_changes": (change_summary["index_changes"] + change_summary["sector_changes"] + change_summary["stock_changes"])[:10]
        },
        "risk_items": risk_items,
        "watchlist_focus": watchlist_focus
    }


def write_dashboard_summary_json(
    output_path: str | Path = "data/processed/dashboard_summary.json",
    database_path: str | Path | None = None,
) -> Path:
    """生成并写入 Dashboard 摘要 JSON"""
    summary = build_dashboard_summary(database_path)
    
    path = Path(output_path)
    if not path.is_absolute():
        path = get_project_root() / path
        
    ensure_directory(path.parent)
    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
        
    return path


def _count_signals(records: list[dict[str, Any]]) -> dict[str, int]:
    """统计信号分布"""
    counts = {"bullish": 0, "bearish": 0, "neutral": 0}
    for rec in records:
        sig = rec.get("signal")
        if sig in ["trend_up", "bullish"]:
            counts["bullish"] += 1
        elif sig in ["trend_down", "bearish"]:
            counts["bearish"] += 1
        else:
            counts["neutral"] += 1
    return counts
