import json
from pathlib import Path
from app_core.sector_boards import (
    load_sector_boards,
    load_sector_board_items,
    normalize_sector_board,
    get_enabled_sector_boards
)


def test_normalize_sector_board_handles_missing_fields() -> None:
    raw = {"symbol": "人工智能", "name": "人工智能"}
    normalized = normalize_sector_board(raw)
    assert normalized["symbol"] == "人工智能"
    assert normalized["name"] == "人工智能"
    assert normalized["board_type"] == "industry"  # 默认值
    assert normalized["category"] == "未分类"
    assert normalized["priority"] == "medium"
    assert normalized["enabled"] is True


def test_normalize_sector_board_strips_strings() -> None:
    raw = {
        "symbol": " 人工智能 ",
        "name": " 人工智能 ",
        "board_type": " Concept ",
        "category": " Tech ",
    }
    normalized = normalize_sector_board(raw)
    assert normalized["symbol"] == "人工智能"
    assert normalized["name"] == "人工智能"
    assert normalized["board_type"] == "concept"
    assert normalized["category"] == "Tech"


def test_get_enabled_sector_boards_filters_disabled(tmp_path: Path) -> None:
    config = {
        "boards": [
            {"symbol": "S1", "name": "N1", "enabled": True},
            {"symbol": "S2", "name": "N2", "enabled": False},
        ]
    }
    items = load_sector_board_items(config)
    enabled = get_enabled_sector_boards(items)
    assert len(enabled) == 1
    assert enabled[0]["symbol"] == "S1"


def test_load_sector_boards_returns_empty_on_missing_file() -> None:
    assert load_sector_boards("non_existent.json") == {}
