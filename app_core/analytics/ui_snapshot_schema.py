from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from app_core.path_utils import get_project_root


def get_ui_snapshot_required_schema() -> dict[str, Any]:
    """返回 UI 快照必须包含的字段结构描述"""
    return {
        "root": [
            "app", "generated_at", "latest_run", "dashboard_summary",
            "source_status", "review_queue", "signal_changes", "data_health", "paths", "messages"
        ],
        "app": [
            "name_cn", "name_en", "version", "stage", "developer", "copyright"
        ],
        "source_status": [
            "default_quote_source", "sources"
        ],
        "paths": [
            "database", "daily_report", "dashboard_summary_json",
            "review_queue_json", "review_queue_csv", "signal_changes_csv",
            "ui_snapshot_json"
        ],
        "review_queue": [
            "count", "high_count", "medium_count", "low_count", "items"
        ],
        "signal_changes": [
            "latest_run_id", "previous_run_id", "summary", "top_changes"
        ]
    }


def validate_ui_snapshot(snapshot: dict[str, Any]) -> dict[str, Any]:
    """校验 UI 快照结构是否符合契约"""
    result = {
        "is_valid": True,
        "error_count": 0,
        "warning_count": 0,
        "errors": [],
        "warnings": []
    }

    if not isinstance(snapshot, dict):
        _add_error(result, "Root must be a dictionary")
        return result

    schema = get_ui_snapshot_required_schema()

    # 1. 根节点字段校验
    for field in schema["root"]:
        if field not in snapshot:
            _add_error(result, f"Missing required root field: '{field}'")

    # 如果基础结构都没了，直接返回
    if result["error_count"] > 0:
        result["is_valid"] = False
        return result

    # 2. app 节点校验
    app = snapshot.get("app", {})
    if not isinstance(app, dict):
        _add_error(result, "Field 'app' must be a dictionary")
    else:
        for field in schema["app"]:
            if field not in app:
                _add_error(result, f"Missing required 'app' field: '{field}'")
        if not app.get("version"):
            _add_error(result, "Field 'app.version' must be a non-empty string")

    # 3. paths 节点校验
    source_status = snapshot.get("source_status", {})
    if not isinstance(source_status, dict):
        _add_error(result, "Field 'source_status' must be a dictionary")
    else:
        for field in schema["source_status"]:
            if field not in source_status:
                _add_error(result, f"Missing required 'source_status' field: '{field}'")
        if not isinstance(source_status.get("sources"), list):
            _add_error(result, "Field 'source_status.sources' must be a list")

    # 4. paths 节点校验
    paths = snapshot.get("paths", {})
    if not isinstance(paths, dict):
        _add_error(result, "Field 'paths' must be a dictionary")
    else:
        for field in schema["paths"]:
            if field not in paths:
                _add_error(result, f"Missing required 'paths' field: '{field}'")
        if not paths.get("ui_snapshot_json"):
            _add_error(result, "Field 'paths.ui_snapshot_json' must be a non-empty string")

    # 5. review_queue 节点校验
    review_queue = snapshot.get("review_queue", {})
    if not isinstance(review_queue, dict):
        _add_error(result, "Field 'review_queue' must be a dictionary")
    else:
        for field in schema["review_queue"]:
            if field not in review_queue:
                _add_error(result, f"Missing required 'review_queue' field: '{field}'")
        if not isinstance(review_queue.get("items"), list):
            _add_error(result, "Field 'review_queue.items' must be a list")

    # 6. messages 校验
    if not isinstance(snapshot.get("messages"), list):
        _add_error(result, "Field 'messages' must be a list")

    # 7. latest_run 校验
    latest_run = snapshot.get("latest_run")
    if latest_run is not None:
        if not isinstance(latest_run, dict):
            _add_error(result, "Field 'latest_run' must be a dictionary or None")
        else:
            for field in ["id", "run_date", "status"]:
                if field not in latest_run:
                    _add_error(result, f"Field 'latest_run' missing required property: '{field}'")

    # 8. data_health 校验
    data_health = snapshot.get("data_health", {})
    if not isinstance(data_health, dict):
        _add_warning(result, "Field 'data_health' should be a dictionary")
    else:
        if "risk_item_count" not in data_health and "ok_count" not in data_health:
            _add_warning(result, "Field 'data_health' should contain 'risk_item_count' or 'ok_count'")

    # 9. signal_changes 校验
    signal_changes = snapshot.get("signal_changes", {})
    if not isinstance(signal_changes, dict):
        _add_error(result, "Field 'signal_changes' must be a dictionary")
    else:
        for field in schema["signal_changes"]:
            if field not in signal_changes:
                _add_error(result, f"Missing required 'signal_changes' field: '{field}'")
        if "summary" in signal_changes and not isinstance(signal_changes["summary"], dict):
            _add_error(result, "Field 'signal_changes.summary' must be a dictionary")

    result["is_valid"] = result["error_count"] == 0
    return result


def write_ui_snapshot_contract(
    output_path: str | Path = "config/frontend_snapshot_contract.json",
) -> Path:
    """写出前端快照契约文件"""
    schema = get_ui_snapshot_required_schema()
    
    root = get_project_root()
    path = root / output_path if not Path(output_path).is_absolute() else Path(output_path)
    
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(schema, f, ensure_ascii=False, indent=2)
        
    return path


def write_sample_ui_snapshot(
    output_path: str | Path = "config/sample_ui_snapshot.json",
) -> Path:
    """写出示例 UI 数据快照"""
    sample = {
        "app": {
            "name_cn": "A股智研台",
            "name_en": "AShare Insight Lab",
            "version": "0.3.5",
            "stage": "Frontend Snapshot Schema Guard",
            "developer": "pL",
            "copyright": "Copyright © 2026 @B‘lock10STUdio. All rights reserved."
        },
        "generated_at": "2026-05-03T13:30:00",
        "latest_run": {
            "id": 1,
            "run_date": "2026-05-03",
            "status": "success",
            "index_count": 1,
            "sector_count": 1,
            "stock_count": 1,
            "report_path": "reports/daily/2026-05-03_daily_report.md"
        },
        "dashboard_summary": {
            "signal_overview": {
                "index": {"bullish": 0, "bearish": 0, "neutral": 1},
                "sector": {"bullish": 1, "bearish": 0, "neutral": 0},
                "stock": {"bullish": 0, "bearish": 1, "neutral": 0}
            }
        },
        "source_status": {
            "default_quote_source": "akshare",
            "sources": [
                {
                    "source_id": "akshare",
                    "display_name": "AkShare A股实时行情",
                    "category": "quote",
                    "status": "available",
                    "status_label": "可用",
                    "priority": "primary",
                    "supports": ["CN_quote", "CN_kline"],
                    "requires_token": False,
                    "token_status": "not_required",
                    "note": "当前默认 A股实时行情源"
                }
            ]
        },
        "review_queue": {
            "count": 1,
            "high_count": 1,
            "medium_count": 0,
            "low_count": 0,
            "items": [
                {
                    "rank": 1,
                    "asset_type": "stock",
                    "symbol": "600519",
                    "name": "贵州茅台",
                    "priority": "high",
                    "severity": "high",
                    "category": "signal_change",
                    "reason": "信号从 neutral 变为 bearish",
                    "latest_signal": "bearish",
                    "suggested_action": "复核信号变化并查看最近数据",
                    "source": "changes"
                }
            ]
        },
        "signal_changes": {
            "latest_run_id": 1,
            "previous_run_id": None,
            "summary": {
                "index_change_count": 0,
                "sector_change_count": 0,
                "stock_change_count": 1
            },
            "top_changes": []
        },
        "data_health": {
            "ok_count": 3,
            "risk_item_count": 0
        },
        "paths": {
            "database": "data/history/ashare_insight_lab.sqlite3",
            "daily_report": "reports/daily/2026-05-03_daily_report.md",
            "dashboard_summary_json": "data/processed/dashboard_summary.json",
            "review_queue_json": "data/processed/review_queue.json",
            "review_queue_csv": "data/processed/review_queue.csv",
            "signal_changes_csv": "data/processed/signal_changes.csv",
            "ui_snapshot_json": "data/processed/ui_snapshot.json"
        },
        "messages": ["这是一份示例快照数据"]
    }
    
    root = get_project_root()
    path = root / output_path if not Path(output_path).is_absolute() else Path(output_path)
    
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(sample, f, ensure_ascii=False, indent=2)
        
    return path


def _add_error(result: dict[str, Any], message: str) -> None:
    result["error_count"] += 1
    result["errors"].append(message)


def _add_warning(result: dict[str, Any], message: str) -> None:
    result["warning_count"] += 1
    result["warnings"].append(message)
