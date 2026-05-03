from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from app_core.analytics.history_summary import (
    build_signal_change_summary,
    get_run_snapshot,
    get_latest_run_pair,
)
from app_core.path_utils import get_project_root
from app_core.storage.file_store import ensure_directory


def build_review_queue(
    database_path: str | Path | None = None,
    max_items: int = 30,
) -> list[dict[str, Any]]:
    """构建每日关注队列"""
    pair = get_latest_run_pair(database_path)
    latest_run = pair["latest_run"]
    if not latest_run:
        return []

    latest_run_id = latest_run["id"]
    snapshot = get_run_snapshot(latest_run_id, database_path)
    change_summary = build_signal_change_summary(latest_run_id=latest_run_id, database_path=database_path)

    queue = []

    # 1. 数据异常项 (data_risk)
    for risk in change_summary["risk_items"]:
        # 复用 risk_items 逻辑，补充完整信息
        # 注意 history_summary 中的 risk_items 结构较简略
        # 我们需要找到原始记录以获取更多信息
        item_source = _find_original_record(risk, snapshot)
        if not item_source:
            continue
            
        queue.append({
            "asset_type": risk["asset_type"],
            "symbol": risk["symbol"],
            "name": risk["name"],
            "priority": item_source.get("priority", "medium"),
            "severity": "high" if risk["latest_data_status"] in ["fetch_failed", "unavailable"] else "medium",
            "category": "data_risk",
            "reason": f"数据异常: {risk['latest_data_status']}",
            "latest_signal": item_source.get("signal"),
            "latest_signal_level": item_source.get("signal_level"),
            "latest_data_status": risk["latest_data_status"],
            "suggested_action": "检查数据源或人工复核",
            "source": "history_summary"
        })

    # 2. 信号变化项 (signal_change)
    all_changes = (
        change_summary["index_changes"] + 
        change_summary["sector_changes"] + 
        change_summary["stock_changes"]
    )
    for change in all_changes:
        if change["change_type"] not in ["signal_changed", "level_changed", "data_status_changed"]:
            continue
            
        severity = "low"
        latest_sig = change.get("latest_signal")
        latest_level = change.get("latest_signal_level")
        
        if latest_sig in ["bearish", "trend_down"] or latest_level == "warning":
            severity = "high"
        elif latest_sig in ["bullish", "trend_up"] or latest_level == "positive":
            severity = "medium"
            
        queue.append({
            "asset_type": change["asset_type"],
            "symbol": change["symbol"],
            "name": change["name"],
            "priority": "medium", # 默认中，后续可能被覆盖
            "severity": severity,
            "category": "signal_change",
            "reason": f"信号从 {change['previous_signal']} 变为 {change['latest_signal']}",
            "latest_signal": latest_sig,
            "latest_signal_level": latest_level,
            "latest_data_status": change.get("latest_data_status"),
            "suggested_action": "复核信号变化并查看最近数据",
            "source": "history_summary"
        })

    # 3. 高优先级自选股 (high_priority_watchlist)
    for stock in snapshot["stocks"]:
        if stock.get("priority") in ["high", "P1"]:
            # 如果已经因为信号变化或数据风险进入队列，则不重复添加，但可能需要升级 severity
            existing = _find_in_queue(queue, "stock", stock["code"])
            if existing:
                if stock.get("signal_level") == "warning" or stock.get("data_status") != "ok":
                    existing["severity"] = "high"
                continue

            queue.append({
                "asset_type": "stock",
                "symbol": stock["code"],
                "name": stock["name"],
                "priority": "high",
                "severity": "high" if (stock.get("signal_level") == "warning" or stock.get("data_status") != "ok") else "medium",
                "category": "high_priority_watchlist",
                "reason": "高优先级自选股例行观察",
                "latest_signal": stock.get("signal"),
                "latest_signal_level": stock.get("signal_level"),
                "latest_data_status": stock.get("data_status"),
                "suggested_action": "例行观察个股走势",
                "source": "latest_snapshot"
            })

    # 4. 持仓关注项 (holding_risk)
    for stock in snapshot["stocks"]:
        pos_status = (stock.get("position_status") or "").lower()
        if any(kw in pos_status for kw in ["holding", "持仓", "in_position"]):
            if stock.get("signal_level") == "warning" or stock.get("data_status") != "ok":
                existing = _find_in_queue(queue, "stock", stock["code"])
                if existing:
                    existing["category"] = "holding_risk"
                    existing["severity"] = "high"
                    existing["suggested_action"] = "持仓个股出现预警，请人工复核"
                else:
                    queue.append({
                        "asset_type": "stock",
                        "symbol": stock["code"],
                        "name": stock["name"],
                        "priority": stock.get("priority", "medium"),
                        "severity": "high",
                        "category": "holding_risk",
                        "reason": f"持仓个股预警: {stock.get('signal_level') or stock.get('data_status')}",
                        "latest_signal": stock.get("signal"),
                        "latest_signal_level": stock.get("signal_level"),
                        "latest_data_status": stock.get("data_status"),
                        "suggested_action": "持仓个股出现预警，请人工复核",
                        "source": "latest_snapshot"
                    })

    # 5. 重点行业/板块 (sector_focus)
    for sector in snapshot["sectors"]:
        if sector.get("priority") in ["high", "P1"]:
            # 如果有信号变化或非 neutral，进入队列
            has_change = any(c["symbol"] == sector["symbol"] for c in change_summary["sector_changes"])
            is_not_neutral = sector.get("signal_level") != "neutral"
            
            if has_change or is_not_neutral:
                existing = _find_in_queue(queue, "sector", sector["symbol"])
                if existing:
                    if existing["category"] == "signal_change":
                        existing["category"] = "sector_focus"
                    continue
                
                queue.append({
                    "asset_type": "sector",
                    "symbol": sector["symbol"],
                    "name": sector["name"],
                    "priority": "high",
                    "severity": "medium",
                    "category": "sector_focus",
                    "reason": "重点板块走势观察",
                    "latest_signal": sector.get("signal"),
                    "latest_signal_level": sector.get("signal_level"),
                    "latest_data_status": sector.get("data_status"),
                    "suggested_action": "观察板块轮动与强度变化",
                    "source": "latest_snapshot"
                })

    # 排序与 Rank
    # 规则：severity high 优先 > data_risk 优先 > priority high 优先 > signal_change 次之
    def sort_key(item):
        severity_map = {"high": 0, "medium": 1, "low": 2}
        category_map = {"data_risk": 0, "holding_risk": 1, "signal_change": 2, "sector_focus": 3, "high_priority_watchlist": 4}
        priority_map = {"high": 0, "medium": 1, "low": 2, "P1": 0, "P2": 1, "P3": 2}
        
        return (
            severity_map.get(item["severity"], 3),
            category_map.get(item["category"], 5),
            priority_map.get(item["priority"], 3)
        )

    queue.sort(key=sort_key)
    
    # 添加 Rank 并截断
    final_queue = []
    for i, item in enumerate(queue[:max_items], 1):
        item["rank"] = i
        final_queue.append(item)
        
    return final_queue


def write_review_queue_outputs(
    output_json_path: str | Path = "data/processed/review_queue.json",
    output_csv_path: str | Path = "data/processed/review_queue.csv",
    database_path: str | Path | None = None,
) -> dict[str, str]:
    """写出关注队列到 JSON 和 CSV"""
    queue = build_review_queue(database_path)
    
    root = get_project_root()
    json_path = root / output_json_path
    csv_path = root / output_csv_path
    
    ensure_directory(json_path.parent)
    
    # 写入 JSON
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(queue, f, ensure_ascii=False, indent=2)
        
    # 写入 CSV
    if queue:
        keys = queue[0].keys()
        with open(csv_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(queue)
            
    return {
        "json_path": str(json_path),
        "csv_path": str(csv_path),
        "count": len(queue)
    }


def _find_original_record(risk: dict, snapshot: dict) -> dict | None:
    asset_type = risk["asset_type"]
    symbol = risk["symbol"]
    
    if asset_type == "index":
        target_list = snapshot["indices"]
        key = "symbol"
    elif asset_type == "sector":
        target_list = snapshot["sectors"]
        key = "symbol"
    else:
        target_list = snapshot["stocks"]
        key = "code"
        
    for item in target_list:
        if item.get(key) == symbol:
            return item
    return None


def _find_in_queue(queue: list[dict], asset_type: str, symbol: str) -> dict | None:
    for item in queue:
        if item["asset_type"] == asset_type and item["symbol"] == symbol:
            return item
    return None
