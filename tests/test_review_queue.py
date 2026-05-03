import pytest
import json
import csv
from pathlib import Path
from app_core.storage.sqlite_store import ensure_database, insert_run_daily_snapshot
from app_core.analytics.review_queue import build_review_queue, write_review_queue_outputs

@pytest.fixture
def temp_db(tmp_path):
    return tmp_path / "test_review.sqlite3"

def test_build_review_queue_empty(temp_db):
    ensure_database(temp_db)
    queue = build_review_queue(database_path=temp_db)
    assert queue == []

def test_build_review_queue_with_various_items(temp_db):
    ensure_database(temp_db)
    
    # 模拟两次运行以触发信号变化
    # Run 1
    run1 = {"run_date": "2026-05-01", "status": "success", "index_count": 1, "sector_count": 1, "stock_count": 3}
    idx1 = [{"symbol": "IDX1", "name": "Index 1", "signal": "neutral", "signal_level": "neutral", "data_status": "ok"}]
    sec1 = [{"symbol": "SEC1", "name": "Sector 1", "signal": "neutral", "signal_level": "neutral", "data_status": "ok", "priority": "high"}]
    stk1 = [
        {"code": "STK1", "name": "Stock 1", "signal": "neutral", "signal_level": "neutral", "data_status": "ok", "priority": "high", "position_status": "holding"},
        {"code": "STK2", "name": "Stock 2", "signal": "neutral", "signal_level": "neutral", "data_status": "ok", "priority": "low", "position_status": "watch"},
        {"code": "STK3", "name": "Stock 3", "signal": "neutral", "signal_level": "neutral", "data_status": "ok", "priority": "low", "position_status": "none"}
    ]
    insert_run_daily_snapshot(run1, idx1, sec1, stk1, temp_db)
    
    # Run 2
    run2 = {"run_date": "2026-05-02", "status": "success", "index_count": 1, "sector_count": 1, "stock_count": 3}
    idx2 = [{"symbol": "IDX1", "name": "Index 1", "signal": "trend_down", "signal_level": "warning", "data_status": "ok"}] # signal_change -> severity high
    sec2 = [{"symbol": "SEC1", "name": "Sector 1", "signal": "trend_up", "signal_level": "positive", "data_status": "ok", "priority": "high"}] # sector_focus + signal_change
    stk2 = [
        {"code": "STK1", "name": "Stock 1", "signal": "neutral", "signal_level": "warning", "data_status": "ok", "priority": "high", "position_status": "holding"}, # holding_risk -> severity high
        {"code": "STK2", "name": "Stock 2", "signal": "neutral", "signal_level": "neutral", "data_status": "stale_data", "priority": "low", "position_status": "watch"}, # data_risk -> severity medium
        {"code": "STK3", "name": "Stock 3", "signal": "trend_up", "signal_level": "positive", "data_status": "ok", "priority": "low", "position_status": "none"} # signal_change -> severity medium
    ]
    insert_run_daily_snapshot(run2, idx2, sec2, stk2, temp_db)
    
    queue = build_review_queue(database_path=temp_db)
    
    assert len(queue) > 0
    assert queue[0]["rank"] == 1
    
    # 验证分类
    categories = [item["category"] for item in queue]
    assert "data_risk" in categories
    assert "signal_change" in categories
    assert "holding_risk" in categories
    assert "sector_focus" in categories
    
    # 验证 severity
    high_items = [item for item in queue if item["severity"] == "high"]
    assert len(high_items) >= 2 # IDX1 and STK1
    
    # 验证 Suggested Action
    for item in queue:
        assert "suggested_action" in item
        assert item["suggested_action"] != ""

def test_write_review_queue_outputs(temp_db, tmp_path):
    ensure_database(temp_db)
    # 写入一些数据
    insert_run_daily_snapshot({"run_date": "2026-05-03", "status": "success", "index_count": 0, "sector_count": 0, "stock_count": 0}, [], [], [], temp_db)
    
    json_path = tmp_path / "review.json"
    csv_path = tmp_path / "review.csv"
    
    outputs = write_review_queue_outputs(output_json_path=json_path, output_csv_path=csv_path, database_path=temp_db)
    
    assert Path(outputs["json_path"]).exists()
    # 虽然队列可能为空（取决于模拟数据），但文件应该生成（JSON 为 []）
    with open(outputs["json_path"], "r", encoding="utf-8") as f:
        data = json.load(f)
        assert isinstance(data, list)
