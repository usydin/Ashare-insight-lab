from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any

from app_core.storage.sqlite_store import get_default_database_path


def get_latest_run_pair(database_path: str | Path | None = None) -> dict[str, Any]:
    """返回最近两次成功运行的记录"""
    path = Path(database_path) if database_path else get_default_database_path()
    if not path.exists():
        return {"latest_run": None, "previous_run": None}

    with sqlite3.connect(path) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        # 只取状态为 success 的运行
        cursor.execute(
            "SELECT * FROM daily_runs WHERE status = 'success' ORDER BY id DESC LIMIT 2"
        )
        rows = cursor.fetchall()
        
        latest = dict(rows[0]) if len(rows) > 0 else None
        previous = dict(rows[1]) if len(rows) > 1 else None
        
        return {
            "latest_run": latest,
            "previous_run": previous
        }


def get_run_snapshot(run_id: int, database_path: str | Path | None = None) -> dict[str, Any]:
    """返回指定 run_id 下的三类记录"""
    path = Path(database_path) if database_path else get_default_database_path()
    if not path.exists():
        return {"run": None, "indices": [], "sectors": [], "stocks": []}

    with sqlite3.connect(path) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # 1. 获取运行元信息
        cursor.execute("SELECT * FROM daily_runs WHERE id = ?", (run_id,))
        run_row = cursor.fetchone()
        if not run_row:
            return {"run": None, "indices": [], "sectors": [], "stocks": []}
        
        # 2. 获取指数信号
        cursor.execute("SELECT * FROM index_signals_history WHERE run_id = ?", (run_id,))
        indices = [dict(row) for row in cursor.fetchall()]
        
        # 3. 获取板块信号
        cursor.execute("SELECT * FROM sector_signals_history WHERE run_id = ?", (run_id,))
        sectors = [dict(row) for row in cursor.fetchall()]
        
        # 4. 获取个股信号
        cursor.execute("SELECT * FROM stock_signals_history WHERE run_id = ?", (run_id,))
        stocks = [dict(row) for row in cursor.fetchall()]
        
        return {
            "run": dict(run_row),
            "indices": indices,
            "sectors": sectors,
            "stocks": stocks
        }


def build_signal_change_summary(
    latest_run_id: int | None = None,
    previous_run_id: int | None = None,
    database_path: str | Path | None = None,
) -> dict[str, Any]:
    """对比两次运行并生成信号变化摘要"""
    if latest_run_id is None:
        pair = get_latest_run_pair(database_path)
        if not pair["latest_run"]:
            return {
                "latest_run_id": None,
                "previous_run_id": None,
                "index_changes": [],
                "sector_changes": [],
                "stock_changes": [],
                "risk_items": [],
                "summary": _empty_summary()
            }
        latest_run_id = pair["latest_run"]["id"]
        previous_run_id = pair["previous_run"]["id"] if pair["previous_run"] else None

    latest_snapshot = get_run_snapshot(latest_run_id, database_path)
    previous_snapshot = (
        get_run_snapshot(previous_run_id, database_path)
        if previous_run_id else {"indices": [], "sectors": [], "stocks": []}
    )

    index_changes = _compare_records(
        latest_snapshot["indices"], previous_snapshot["indices"], "index", "symbol"
    )
    sector_changes = _compare_records(
        latest_snapshot["sectors"], previous_snapshot["sectors"], "sector", "symbol"
    )
    stock_changes = _compare_records(
        latest_snapshot["stocks"], previous_snapshot["stocks"], "stock", "code"
    )

    risk_items = _extract_risk_items(
        latest_snapshot["indices"], latest_snapshot["sectors"], latest_snapshot["stocks"]
    )

    summary = {
        "index_change_count": len(index_changes),
        "sector_change_count": len(sector_changes),
        "stock_change_count": len(stock_changes),
        "risk_item_count": len(risk_items),
        "fetch_failed_count": sum(1 for item in risk_items if item["latest_data_status"] == "fetch_failed"),
        "stale_data_count": sum(1 for item in risk_items if item["latest_data_status"] == "stale_data"),
        "unavailable_count": sum(1 for item in risk_items if item["latest_data_status"] == "unavailable"),
    }

    return {
        "latest_run_id": latest_run_id,
        "previous_run_id": previous_run_id,
        "index_changes": index_changes,
        "sector_changes": sector_changes,
        "stock_changes": stock_changes,
        "risk_items": risk_items,
        "summary": summary
    }


def _compare_records(
    latest_list: list[dict], 
    previous_list: list[dict], 
    asset_type: str, 
    id_key: str
) -> list[dict]:
    """对比两组记录"""
    changes = []
    prev_map = {item[id_key]: item for item in previous_list}
    latest_map = {item[id_key]: item for item in latest_list}

    # 如果没有上一轮，则返回 no_previous_run
    if not previous_list and latest_list:
        # 这里可以选择不返回所有资产，或者只返回概要
        # 根据指令要求，如果没有上一轮，则友好提示
        return []

    for key, latest in latest_map.items():
        if key not in prev_map:
            changes.append(_build_change_item(asset_type, latest, None, "new_asset"))
            continue
        
        previous = prev_map[key]
        
        # 检查信号变化
        if latest["signal"] != previous["signal"]:
            changes.append(_build_change_item(asset_type, latest, previous, "signal_changed"))
        # 检查强度变化
        elif latest["signal_level"] != previous["signal_level"]:
            changes.append(_build_change_item(asset_type, latest, previous, "level_changed"))
        # 检查数据状态变化
        elif latest["data_status"] != previous["data_status"]:
            changes.append(_build_change_item(asset_type, latest, previous, "data_status_changed"))

    # 检查缺失资产
    for key, previous in prev_map.items():
        if key not in latest_map:
            changes.append(_build_change_item(asset_type, None, previous, "missing_asset"))

    return changes


def _build_change_item(asset_type: str, latest: dict | None, previous: dict | None, change_type: str) -> dict:
    """构造变化项"""
    ref = latest if latest else previous
    return {
        "asset_type": asset_type,
        "symbol": ref.get("symbol") or ref.get("code"),
        "name": ref.get("name"),
        "previous_signal": previous.get("signal") if previous else None,
        "latest_signal": latest.get("signal") if latest else None,
        "previous_signal_level": previous.get("signal_level") if previous else None,
        "latest_signal_level": latest.get("signal_level") if latest else None,
        "previous_data_status": previous.get("data_status") if previous else None,
        "latest_data_status": latest.get("data_status") if latest else None,
        "date": latest.get("date") if latest else (previous.get("date") if previous else None),
        "change_type": change_type
    }


def _extract_risk_items(indices: list[dict], sectors: list[dict], stocks: list[dict]) -> list[dict]:
    """提取风险项"""
    risks = []
    all_items = []
    for item in indices:
        item["asset_type"] = "index"
        all_items.append(item)
    for item in sectors:
        item["asset_type"] = "sector"
        all_items.append(item)
    for item in stocks:
        item["asset_type"] = "stock"
        all_items.append(item)

    for item in all_items:
        if item.get("data_status") != "ok":
            risks.append({
                "asset_type": item["asset_type"],
                "symbol": item.get("symbol") or item.get("code"),
                "name": item.get("name"),
                "latest_data_status": item.get("data_status"),
                "error_message": item.get("error_message"),
                "change_type": "risk_status"
            })
    return risks


def _empty_summary() -> dict[str, int]:
    return {
        "index_change_count": 0,
        "sector_change_count": 0,
        "stock_change_count": 0,
        "risk_item_count": 0,
        "fetch_failed_count": 0,
        "stale_data_count": 0,
        "unavailable_count": 0,
    }
