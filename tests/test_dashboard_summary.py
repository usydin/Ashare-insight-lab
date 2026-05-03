import pytest
import json
from pathlib import Path
from app_core.storage.sqlite_store import ensure_database, insert_run_daily_snapshot
from app_core.analytics.dashboard_summary import build_dashboard_summary, write_dashboard_summary_json

@pytest.fixture
def temp_db(tmp_path):
    return tmp_path / "test_dashboard.sqlite3"

def test_build_dashboard_summary_empty(temp_db):
    ensure_database(temp_db)
    summary = build_dashboard_summary(database_path=temp_db)
    assert summary["latest_run"] is None
    assert "未发现运行记录" in summary["message"]

def test_build_dashboard_summary_with_data(temp_db):
    ensure_database(temp_db)
    
    # 模拟一次运行
    run_metadata = {
        "run_date": "2026-05-03",
        "status": "success",
        "index_count": 1,
        "sector_count": 1,
        "stock_count": 2
    }
    indices = [{"symbol": "IDX1", "name": "Index 1", "signal": "trend_up", "signal_level": "positive", "data_status": "ok"}]
    sectors = [{"symbol": "SEC1", "name": "Sector 1", "signal": "neutral", "signal_level": "neutral", "data_status": "stale_data"}]
    stocks = [
        {"code": "STK1", "name": "Stock 1", "signal": "trend_down", "signal_level": "negative", "data_status": "ok", "priority": "high", "position_status": "holding"},
        {"code": "STK2", "name": "Stock 2", "signal": "neutral", "signal_level": "neutral", "data_status": "ok", "priority": "low", "position_status": "watch"}
    ]
    
    insert_run_daily_snapshot(run_metadata, indices, sectors, stocks, temp_db)
    
    summary = build_dashboard_summary(database_path=temp_db)
    
    assert summary["latest_run"]["run_date"] == "2026-05-03"
    assert summary["data_health"]["risk_item_count"] == 1
    assert summary["data_health"]["stale_data_count"] == 1
    
    # 信号统计
    assert summary["signal_overview"]["index"]["bullish"] == 1
    assert summary["signal_overview"]["sector"]["neutral"] == 1
    assert summary["signal_overview"]["stock"]["bearish"] == 1
    
    # 自选股关注
    assert len(summary["watchlist_focus"]["high_priority"]) == 1
    assert summary["watchlist_focus"]["high_priority"][0]["code"] == "STK1"
    assert len(summary["watchlist_focus"]["holding"]) == 1
    assert len(summary["watchlist_focus"]["watching"]) == 1

def test_write_dashboard_summary_json(temp_db, tmp_path):
    ensure_database(temp_db)
    # 写入一些数据
    insert_run_daily_snapshot({"run_date": "2026-05-03", "status": "success", "index_count": 0, "sector_count": 0, "stock_count": 0}, [], [], [], temp_db)
    
    json_path = tmp_path / "summary.json"
    result_path = write_dashboard_summary_json(output_path=json_path, database_path=temp_db)
    
    assert result_path.exists()
    with open(result_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["app"]["name"] == "A股智研台"
        assert data["latest_run"]["run_date"] == "2026-05-03"
