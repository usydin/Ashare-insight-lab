from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

from app_core.analytics.realtime_quote_snapshot import (
    build_longbridge_realtime_quote_snapshot,
    load_longbridge_realtime_quote_snapshot,
    write_longbridge_realtime_quote_snapshot_json,
)


def test_build_longbridge_realtime_quote_snapshot_unauthorized(tmp_path):
    """测试在未授权状态下构建快照"""
    with patch("app_core.analytics.realtime_quote_snapshot.build_longbridge_quote_context_via_oauth") as mock_build:
        mock_build.return_value = {"status": "oauth_required", "message": "Auth required"}
        
        snapshot = build_longbridge_realtime_quote_snapshot(project_root=tmp_path)
        
        assert snapshot["status"] == "oauth_required"
        assert snapshot["message"] == "Auth required"
        assert len(snapshot["items"]) > 0
        for item in snapshot["items"]:
            assert item["data_status"] == "oauth_required"


def test_build_longbridge_realtime_quote_snapshot_success(tmp_path):
    """测试在成功获取 Context 后构建快照"""
    with patch("app_core.analytics.realtime_quote_snapshot.build_longbridge_quote_context_via_oauth") as mock_build, \
         patch("app_core.analytics.realtime_quote_snapshot.fetch_longbridge_quote_with_context") as mock_fetch:
        
        mock_build.return_value = {"status": "authorized", "ctx": MagicMock()}
        mock_fetch.return_value = {
            "data_status": "ok",
            "name": "Test Stock",
            "current_price": 100.0,
            "change": 1.0,
            "change_percent": 1.0,
            "timestamp": "2026-05-05T10:00:00",
        }
        
        snapshot = build_longbridge_realtime_quote_snapshot(project_root=tmp_path)
        
        assert snapshot["status"] == "ok"
        assert len(snapshot["items"]) > 0
        assert snapshot["items"][0]["data_status"] == "ok"
        assert snapshot["items"][0]["name"] == "Test Stock"


def test_write_and_load_longbridge_realtime_quote_snapshot(tmp_path):
    """测试写入和加载快照文件"""
    snapshot_data = {
        "provider": "longbridge",
        "generated_at": "2026-05-05T10:00:00",
        "status": "ok",
        "message": "",
        "quote_only": True,
        "trade_enabled": False,
        "items": [
            {
                "symbol": "600519",
                "market": "CN",
                "longbridge_symbol": "600519.SH",
                "name": "贵州茅台",
                "price": 1500.0,
                "data_status": "ok",
                "message": "",
            }
        ],
    }
    
    with patch("app_core.analytics.realtime_quote_snapshot.build_longbridge_realtime_quote_snapshot") as mock_build:
        mock_build.return_value = snapshot_data
        
        output_rel_path = "data/processed/test_snapshot.json"
        full_path = write_longbridge_realtime_quote_snapshot_json(
            output_path=output_rel_path,
            project_root=tmp_path
        )
        
        assert full_path.exists()
        
        loaded_snapshot = load_longbridge_realtime_quote_snapshot(
            input_path=output_rel_path,
            project_root=tmp_path
        )
        
        assert loaded_snapshot["provider"] == "longbridge"
        assert loaded_snapshot["status"] == "ok"
        assert len(loaded_snapshot["items"]) == 1
        assert loaded_snapshot["items"][0]["symbol"] == "600519"


def test_load_non_existent_snapshot(tmp_path):
    """测试加载不存在的快照文件"""
    loaded_snapshot = load_longbridge_realtime_quote_snapshot(
        input_path="non_existent.json",
        project_root=tmp_path
    )
    
    assert loaded_snapshot["status"] == "missing"
    assert len(loaded_snapshot["items"]) == 0
