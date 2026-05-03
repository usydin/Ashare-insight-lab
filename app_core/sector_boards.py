from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_sector_boards(config_path: str | Path = "config/sector_boards.json") -> dict[str, Any]:
    """从 JSON 文件加载行业/板块配置"""
    path = Path(config_path)
    if not path.exists():
        return {}

    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"警告：无法读取行业/板块配置文件 {path}: {e}")
        return {}


def load_sector_board_items(config: dict[str, Any]) -> list[dict[str, Any]]:
    """从配置对象中提取并标准化板块项"""
    raw_items = config.get("boards", [])
    if not isinstance(raw_items, list):
        print("警告：行业/板块配置格式错误，`boards` 应为列表")
        return []

    normalized_items: list[dict[str, Any]] = []
    for raw_item in raw_items:
        if not isinstance(raw_item, dict):
            continue
        normalized_items.append(normalize_sector_board(raw_item))
    return normalized_items


def normalize_sector_board(item: dict[str, Any]) -> dict[str, Any]:
    """标准化单个行业/板块配置项"""
    symbol = str(item.get("symbol", "")).strip()
    name = str(item.get("name", "")).strip()
    board_type = str(item.get("board_type", "industry")).strip().lower()
    category = str(item.get("category", "未分类")).strip()
    priority = str(item.get("priority", "medium")).strip().lower()
    enabled = bool(item.get("enabled", True))
    observe_reason = str(item.get("observe_reason", "")).strip()
    risk_note = str(item.get("risk_note", "")).strip()

    return {
        "symbol": symbol,
        "name": name,
        "board_type": board_type,
        "category": category,
        "priority": priority,
        "enabled": enabled,
        "observe_reason": observe_reason,
        "risk_note": risk_note,
    }


def get_enabled_sector_boards(items_or_config: list[dict[str, Any]] | dict[str, Any]) -> list[dict[str, Any]]:
    """获取所有启用的行业/板块"""
    if isinstance(items_or_config, dict):
        items = load_sector_board_items(items_or_config)
    else:
        items = items_or_config
    
    return [item for item in items if item.get("enabled") is True]
