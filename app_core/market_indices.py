from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_market_indices(config_path: str | Path) -> list[dict[str, Any]]:
    """从 JSON 文件加载并标准化指数配置"""
    path = Path(config_path)
    if not path.exists():
        return []

    try:
        with open(path, "r", encoding="utf-8") as f:
            raw_items = json.load(f)
    except Exception as e:
        print(f"警告：无法读取指数配置文件 {path}: {e}")
        return []

    if not isinstance(raw_items, list):
        print(f"警告：指数配置格式错误，应为列表: {path}")
        return []

    normalized_items: list[dict[str, Any]] = []
    for raw_item in raw_items:
        if not isinstance(raw_item, dict):
            continue
        normalized_items.append(normalize_market_index(raw_item))
    return normalized_items


def normalize_market_index(item: dict[str, Any]) -> dict[str, Any]:
    """标准化单个指数配置项"""
    symbol = str(item.get("symbol", "")).strip()
    name = str(item.get("name", "")).strip()
    enabled = bool(item.get("enabled", True))

    return {
        "symbol": symbol,
        "name": name,
        "category": str(item.get("category", "未分类")).strip(),
        "enabled": enabled,
    }


def get_enabled_market_indices(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """获取所有启用的指数"""
    return [item for item in items if item.get("enabled") is True]
