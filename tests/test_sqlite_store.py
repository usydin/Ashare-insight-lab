import pytest
import sqlite3
from pathlib import Path
from app_core.storage.sqlite_store import (
    ensure_database,
    insert_run_daily_snapshot,
    get_latest_runs,
    get_signal_history,
)

@pytest.fixture
def temp_db(tmp_path):
    db_path = tmp_path / "test_ashare.sqlite3"
    return db_path

def test_ensure_database(temp_db):
    path = ensure_database(temp_db)
    assert path.exists()
    
    with sqlite3.connect(path) as conn:
        cursor = conn.cursor()
        # 检查表是否存在
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='daily_runs'")
        assert cursor.fetchone() is not None
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='index_signals_history'")
        assert cursor.fetchone() is not None

def test_insert_and_query_snapshot(temp_db):
    run_metadata = {
        "run_date": "2026-05-03",
        "started_at": "2026-05-03T10:00:00",
        "finished_at": "2026-05-03T10:05:00",
        "app_version": "0.3.0",
        "stage": "Test",
        "status": "success",
        "index_count": 1,
        "sector_count": 1,
        "stock_count": 1,
        "report_path": "reports/daily/2026-05-03.md",
        "processed_csv_path": "data/processed/daily_signals.csv",
        "log_path": "logs/app.log",
    }
    
    index_records = [{
        "fetch_time": "2026-05-03T10:00:01",
        "symbol": "000001.SH",
        "name": "上证指数",
        "category": "market",
        "date": "2026-05-03",
        "close": 3000.0,
        "ma5": 2950.0,
        "ma20": 2900.0,
        "signal": "trend_up",
        "signal_level": "positive",
        "data_status": "ok",
        "error_message": "",
    }]
    
    sector_records = [{
        "fetch_time": "2026-05-03T10:00:02",
        "symbol": "BK0447",
        "name": "半导体",
        "board_type": "industry",
        "category": "tech",
        "priority": "high",
        "observe_reason": "test",
        "risk_note": "none",
        "date": "2026-05-03",
        "close": 1500.0,
        "ma5": 1450.0,
        "ma20": 1400.0,
        "signal": "trend_up",
        "signal_level": "positive",
        "data_status": "ok",
        "error_message": "",
    }]
    
    watchlist_records = [{
        "fetch_time": "2026-05-03T10:00:03",
        "date": "2026-05-03",
        "code": "600519",
        "name": "贵州茅台",
        "market": "SH",
        "industry": "白酒",
        "sector": "消费",
        "board": "主板",
        "tags": ["绩优", "龙头"],
        "priority": "high",
        "position_status": "hold",
        "observe_reason": "test",
        "risk_note": "none",
        "data_source": "akshare",
        "close": 1800.0,
        "ma5": 1750.0,
        "ma20": 1700.0,
        "signal": "trend_up",
        "signal_level": "positive",
        "data_status": "ok",
        "error_message": "",
        "raw_file_path": "data/raw/600519_raw.csv",
    }]
    
    result = insert_run_daily_snapshot(
        run_metadata, index_records, sector_records, watchlist_records, temp_db
    )
    
    assert result["run_id"] == 1
    assert result["index_count"] == 1
    assert result["sector_count"] == 1
    assert result["stock_count"] == 1
    
    # 测试读取运行历史
    runs = get_latest_runs(limit=10, database_path=temp_db)
    assert len(runs) == 1
    assert runs[0]["run_date"] == "2026-05-03"
    
    # 测试读取信号历史
    index_history = get_signal_history("index", "000001.SH", database_path=temp_db)
    assert len(index_history) == 1
    assert index_history[0]["close"] == 3000.0
    
    sector_history = get_signal_history("sector", "BK0447", database_path=temp_db)
    assert len(sector_history) == 1
    assert sector_history[0]["name"] == "半导体"
    
    stock_history = get_signal_history("stock", "600519", database_path=temp_db)
    assert len(stock_history) == 1
    assert stock_history[0]["name"] == "贵州茅台"
    assert stock_history[0]["tags"] == "绩优,龙头"

def test_none_values_safety(temp_db):
    """测试 None 数值不会导致写入崩溃"""
    run_metadata = {
        "run_date": "2026-05-03",
        "status": "success",
    }
    
    index_records = [{
        "symbol": "000001.SH",
        "close": None,
        "ma5": None,
        "ma20": None,
    }]
    
    result = insert_run_daily_snapshot(
        run_metadata, index_records, [], [], temp_db
    )
    assert result["run_id"] is not None
    
    history = get_signal_history("index", "000001.SH", database_path=temp_db)
    assert history[0]["close"] is None

def test_invalid_asset_type(temp_db):
    ensure_database(temp_db)
    with pytest.raises(ValueError, match="不支持的资产类型"):
        get_signal_history("invalid", "123", database_path=temp_db)
