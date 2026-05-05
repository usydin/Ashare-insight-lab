from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

from app_core.analytics.ui_snapshot import build_ui_snapshot


def test_build_ui_snapshot_includes_realtime_quotes(tmp_path):
    """验证 UI 快照包含 realtime_quotes 字段"""
    with patch("app_core.analytics.ui_snapshot.build_dashboard_summary") as mock_dashboard, \
         patch("app_core.analytics.ui_snapshot.build_review_queue") as mock_queue, \
         patch("app_core.analytics.ui_snapshot.build_signal_change_summary") as mock_changes, \
         patch("app_core.analytics.ui_snapshot.build_realtime_source_status") as mock_status, \
         patch("app_core.analytics.ui_snapshot.load_longbridge_realtime_quote_snapshot") as mock_quotes:
        
        mock_dashboard.return_value = {"latest_run": None, "data_health": {}}
        mock_queue.return_value = []
        mock_changes.return_value = {
            "latest_run_id": None,
            "previous_run_id": None,
            "summary": {"index_change_count": 0, "sector_change_count": 0, "stock_change_count": 0},
            "index_changes": [],
            "sector_changes": [],
            "stock_changes": []
        }
        mock_status.return_value = {"default_quote_source": "akshare", "sources": []}
        mock_status.return_value["token_expiry"] = {
            "provider": "longbridge",
            "key": "LONGBRIDGE_ACCESS_TOKEN",
            "status": "ok",
            "expires_at_utc": "2026-08-03T13:09:05+00:00",
            "days_remaining": 89,
            "message": "token 有效",
            "quote_only": True,
            "trade_enabled": False,
        }
        mock_quotes.return_value = {
            "provider": "longbridge",
            "status": "ok",
            "items": [{"symbol": "600519", "data_status": "ok"}]
        }
        
        snapshot = build_ui_snapshot()
        
        assert "realtime_quotes" in snapshot
        assert "token_expiry" in snapshot
        assert snapshot["realtime_quotes"]["provider"] == "longbridge"
        assert snapshot["token_expiry"]["status"] == "ok"
        assert len(snapshot["realtime_quotes"]["items"]) == 1
        assert snapshot["realtime_quotes"]["items"][0]["symbol"] == "600519"
        
        # 验证路径索引也包含新路径
        assert "longbridge_quote_snapshot_json" in snapshot["paths"]
        assert snapshot["paths"]["longbridge_quote_snapshot_json"] == "data/processed/longbridge_quote_snapshot.json"
