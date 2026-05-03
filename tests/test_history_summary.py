import pytest
from pathlib import Path
from app_core.storage.sqlite_store import ensure_database, insert_run_daily_snapshot
from app_core.analytics.history_summary import build_signal_change_summary, get_latest_run_pair

@pytest.fixture
def temp_db(tmp_path):
    return tmp_path / "test_summary.sqlite3"

def test_build_signal_change_summary_single_run(temp_db):
    ensure_database(temp_db)
    run_metadata = {"run_date": "2026-05-01", "status": "success", "index_count": 1, "sector_count": 0, "stock_count": 0}
    indices = [{"symbol": "SH000001", "name": "上证指数", "signal": "neutral", "signal_level": "neutral", "data_status": "ok"}]
    
    insert_run_daily_snapshot(run_metadata, indices, [], [], temp_db)
    
    summary = build_signal_change_summary(database_path=temp_db)
    assert summary["latest_run_id"] == 1
    assert summary["previous_run_id"] is None
    assert summary["index_changes"] == []
    assert summary["summary"]["index_change_count"] == 0

def test_build_signal_change_summary_two_runs(temp_db):
    ensure_database(temp_db)
    
    # Run 1
    run1 = {"run_date": "2026-05-01", "status": "success", "index_count": 1, "sector_count": 1, "stock_count": 1}
    idx1 = [{"symbol": "IDX1", "name": "Index 1", "signal": "neutral", "signal_level": "neutral", "data_status": "ok"}]
    sec1 = [{"symbol": "SEC1", "name": "Sector 1", "signal": "neutral", "signal_level": "neutral", "data_status": "ok"}]
    stk1 = [{"code": "STK1", "name": "Stock 1", "signal": "neutral", "signal_level": "neutral", "data_status": "ok"}]
    insert_run_daily_snapshot(run1, idx1, sec1, stk1, temp_db)
    
    # Run 2
    run2 = {"run_date": "2026-05-02", "status": "success", "index_count": 1, "sector_count": 1, "stock_count": 1}
    idx2 = [{"symbol": "IDX1", "name": "Index 1", "signal": "trend_up", "signal_level": "positive", "data_status": "ok"}] # Signal Changed
    sec2 = [{"symbol": "SEC1", "name": "Sector 1", "signal": "neutral", "signal_level": "neutral", "data_status": "stale_data"}] # Data Status Changed (Risk)
    stk2 = [{"code": "STK2", "name": "Stock 2", "signal": "neutral", "signal_level": "neutral", "data_status": "ok"}] # New Asset (STK1 missing)
    insert_run_daily_snapshot(run2, idx2, sec2, stk2, temp_db)
    
    summary = build_signal_change_summary(database_path=temp_db)
    assert summary["latest_run_id"] == 2
    assert summary["previous_run_id"] == 1
    
    # 检查指数变化
    assert len(summary["index_changes"]) == 1
    assert summary["index_changes"][0]["change_type"] == "signal_changed"
    
    # 检查板块变化
    assert len(summary["sector_changes"]) == 1
    assert summary["sector_changes"][0]["change_type"] == "data_status_changed"
    
    # 检查个股变化
    stk_changes = {c["symbol"]: c["change_type"] for c in summary["stock_changes"]}
    assert stk_changes["STK2"] == "new_asset"
    assert stk_changes["STK1"] == "missing_asset"
    
    # 检查风险项
    assert len(summary["risk_items"]) == 1
    assert summary["risk_items"][0]["symbol"] == "SEC1"
    assert summary["risk_items"][0]["latest_data_status"] == "stale_data"

def test_get_latest_run_pair_empty(temp_db):
    pair = get_latest_run_pair(temp_db)
    assert pair["latest_run"] is None
    assert pair["previous_run"] is None
