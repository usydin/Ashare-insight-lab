from __future__ import annotations

from typing import Any


DEFAULT_PRIORITY = "P3"
DEFAULT_POSITION_STATUS = "watch"
DEFAULT_DATA_SOURCE = "akshare"
VALID_PRIORITIES = {"P1", "P2", "P3"}
VALID_POSITION_STATUSES = {"none", "watch", "simulated", "holding_candidate"}


def load_watchlist_items(watchlist_config: dict[str, Any]) -> list[dict[str, Any]]:
    raw_items = watchlist_config.get("watchlist", [])
    if not isinstance(raw_items, list):
        raise ValueError("watchlist 配置错误：`watchlist` 必须是数组。")

    normalized_items: list[dict[str, Any]] = []
    for raw_item in raw_items:
        if not isinstance(raw_item, dict):
            raise ValueError("watchlist 配置错误：每个股票项都必须是对象。")
        normalized_items.append(normalize_watchlist_item(raw_item))
    return normalized_items


def normalize_watchlist_item(item: dict[str, Any]) -> dict[str, Any]:
    code = str(item.get("code", "")).strip()
    name = str(item.get("name", "")).strip()
    enabled = bool(item.get("enabled", False))

    if enabled and (not code or not name):
        raise ValueError("watchlist 配置错误：enabled=true 的股票至少需要 `code` 和 `name`。")

    priority = str(item.get("priority", DEFAULT_PRIORITY)).strip().upper() or DEFAULT_PRIORITY
    if priority not in VALID_PRIORITIES:
        priority = DEFAULT_PRIORITY

    position_status = str(item.get("position_status", DEFAULT_POSITION_STATUS)).strip().lower()
    if position_status not in VALID_POSITION_STATUSES:
        position_status = DEFAULT_POSITION_STATUS

    tags = _normalize_tags(item.get("tags", []))

    observe_reason = str(
        item.get("observe_reason", item.get("reason", ""))
    ).strip()

    return {
        "code": code,
        "name": name,
        "market": str(item.get("market", "")).strip().upper(),
        "enabled": enabled,
        "industry": str(item.get("industry", "")).strip(),
        "sector": str(item.get("sector", "")).strip(),
        "board": str(item.get("board", "")).strip(),
        "tags": tags,
        "priority": priority,
        "position_status": position_status,
        "observe_reason": observe_reason,
        "risk_note": str(item.get("risk_note", "")).strip(),
        "data_source": str(item.get("data_source", DEFAULT_DATA_SOURCE)).strip() or DEFAULT_DATA_SOURCE,
        "note": str(item.get("note", "")).strip(),
    }


def get_enabled_watchlist(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [item for item in items if item.get("enabled") is True]


def tags_to_csv_value(tags: Any) -> str:
    normalized_tags = _normalize_tags(tags)
    return ",".join(normalized_tags)


def _normalize_tags(tags: Any) -> list[str]:
    if tags is None:
        return []
    if isinstance(tags, list):
        return [str(tag).strip() for tag in tags if str(tag).strip()]
    if isinstance(tags, str):
        return [part.strip() for part in tags.split(",") if part.strip()]
    return [str(tags).strip()] if str(tags).strip() else []
