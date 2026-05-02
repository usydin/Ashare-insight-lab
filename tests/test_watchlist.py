from __future__ import annotations

import pytest

from app_core.watchlist import (
    get_enabled_watchlist,
    load_watchlist_items,
    normalize_watchlist_item,
    tags_to_csv_value,
)


def test_normalize_watchlist_item_applies_defaults() -> None:
    item = normalize_watchlist_item(
        {
            "code": "000001",
            "name": "平安银行",
            "market": "sz",
            "enabled": True,
        }
    )

    assert item["market"] == "SZ"
    assert item["priority"] == "P3"
    assert item["position_status"] == "watch"
    assert item["data_source"] == "akshare"
    assert item["tags"] == []


def test_normalize_watchlist_item_converts_tags_safely() -> None:
    item = normalize_watchlist_item(
        {
            "code": "600519",
            "name": "贵州茅台",
            "market": "SH",
            "enabled": True,
            "tags": "核心观察, 高端消费",
        }
    )

    assert item["tags"] == ["核心观察", "高端消费"]
    assert tags_to_csv_value(item["tags"]) == "核心观察,高端消费"


def test_load_watchlist_items_requires_array() -> None:
    with pytest.raises(ValueError, match="watchlist"):
        load_watchlist_items({"watchlist": {}})


def test_enabled_watchlist_requires_code_and_name() -> None:
    with pytest.raises(ValueError, match="code"):
        load_watchlist_items({"watchlist": [{"code": "", "name": "", "enabled": True}]})


def test_get_enabled_watchlist_filters_disabled_items() -> None:
    items = load_watchlist_items(
        {
            "watchlist": [
                {"code": "000001", "name": "平安银行", "enabled": True},
                {"code": "600519", "name": "贵州茅台", "enabled": False},
            ]
        }
    )

    enabled = get_enabled_watchlist(items)
    assert [item["code"] for item in enabled] == ["000001"]
