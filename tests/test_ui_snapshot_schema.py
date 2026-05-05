import json
from app_core.analytics.ui_snapshot_schema import (
    validate_ui_snapshot,
    write_ui_snapshot_contract,
    write_sample_ui_snapshot
)

def test_validate_ui_snapshot_valid():
    snapshot = {
        "app": {
            "name_cn": "A股智研台", "name_en": "AShare Insight Lab", "version": "0.7.2",
            "stage": "test", "developer": "pL", "copyright": "test"
        },
        "generated_at": "2026-01-01",
        "latest_run": {"id": 1, "run_date": "2026-01-01", "status": "success"},
        "dashboard_summary": {},
        "source_status": {"default_quote_source": "akshare", "sources": []},
        "realtime_quotes": {"provider": "longbridge", "quote_only": True, "trade_enabled": False, "items": []},
        "review_queue": {"count": 0, "high_count": 0, "medium_count": 0, "low_count": 0, "items": []},
        "signal_changes": {"latest_run_id": 1, "previous_run_id": None, "summary": {}, "top_changes": []},
        "data_health": {"ok_count": 0},
        "paths": {
            "database": "db", "daily_report": "rep", "dashboard_summary_json": "j1",
            "longbridge_quote_snapshot_json": "longbridge_quote_snapshot.json",
            "review_queue_json": "j2", "review_queue_csv": "c1", "signal_changes_csv": "c2",
            "ui_snapshot_json": "j3"
        },
        "messages": []
    }
    result = validate_ui_snapshot(snapshot)
    assert result["is_valid"] is True
    assert result["error_count"] == 0

def test_validate_ui_snapshot_missing_root():
    snapshot = {"app": {}}
    result = validate_ui_snapshot(snapshot)
    assert result["is_valid"] is False
    assert result["error_count"] > 0
    assert any("Missing required root field" in err for err in result["errors"])

def test_validate_ui_snapshot_invalid_types():
    snapshot = {
        "app": {"version": "0.3.5"},
        "generated_at": "...",
        "latest_run": "not_a_dict",
        "dashboard_summary": {},
        "review_queue": {"items": "not_a_list"},
        "signal_changes": {"summary": "not_a_dict"},
        "data_health": "not_a_dict",
        "paths": {"ui_snapshot_json": "path"},
        "messages": "not_a_list"
    }
    # 先补齐 root 必须字段以免第一阶段校验直接返回
    required = ["app", "generated_at", "latest_run", "dashboard_summary", "source_status", "realtime_quotes", "review_queue", "signal_changes", "data_health", "paths", "messages"]
    for r in required:
        if r not in snapshot: snapshot[r] = {}
        
    result = validate_ui_snapshot(snapshot)
    assert result["is_valid"] is False
    assert any("must be a list" in err for err in result["errors"])
    assert any("must be a dictionary" in err for err in result["errors"])

def test_validate_ui_snapshot_latest_run_none():
    snapshot = {
        "app": {"version": "0.3.5", "name_cn": "t", "name_en": "t", "stage": "t", "developer": "t", "copyright": "t"},
        "generated_at": "...",
        "latest_run": None,
        "dashboard_summary": {},
        "source_status": {"default_quote_source": "akshare", "sources": []},
        "realtime_quotes": {"provider": "longbridge", "quote_only": True, "trade_enabled": False, "items": []},
        "review_queue": {"count":0, "high_count":0, "medium_count":0, "low_count":0, "items": []},
        "signal_changes": {"latest_run_id": None, "previous_run_id": None, "summary": {}, "top_changes": []},
        "data_health": {"ok_count": 0},
        "paths": {
            "database": "t", "daily_report": "t", "dashboard_summary_json": "t",
            "longbridge_quote_snapshot_json": "longbridge_quote_snapshot.json",
            "review_queue_json": "t", "review_queue_csv": "t", "signal_changes_csv": "t",
            "ui_snapshot_json": "t"
        },
        "messages": []
    }
    result = validate_ui_snapshot(snapshot)
    assert result["is_valid"] is True

def test_write_contract_and_sample(tmp_path):
    contract_path = tmp_path / "contract.json"
    sample_path = tmp_path / "sample.json"
    
    p1 = write_ui_snapshot_contract(contract_path)
    p2 = write_sample_ui_snapshot(sample_path)
    
    assert p1.exists()
    assert p2.exists()
    
    with open(p2, "r", encoding="utf-8") as f:
        sample_data = json.load(f)
        assert "app" in sample_data
        assert "source_status" in sample_data
        assert "review_queue" in sample_data
        assert validate_ui_snapshot(sample_data)["is_valid"] is True
