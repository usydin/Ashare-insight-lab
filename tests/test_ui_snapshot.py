import pytest
import json
from app_core.storage.sqlite_store import ensure_database, insert_run_daily_snapshot
from app_core.analytics.ui_snapshot import build_ui_snapshot, write_ui_snapshot_json

@pytest.fixture
def temp_db(tmp_path):
    return tmp_path / "test_ui.sqlite3"

def test_build_ui_snapshot_empty(temp_db):
    ensure_database(temp_db)
    snapshot = build_ui_snapshot(database_path=temp_db)
    assert snapshot["latest_run"] is None
    assert any("运行记录" in msg for msg in snapshot["messages"])
    app = snapshot["app"]
    assert app["version"] == "0.7.2"
    assert app["developer"] == "pL"
    assert snapshot["source_status"]["default_quote_source"] == "akshare"
    assert isinstance(snapshot["source_status"]["sources"], list)

def test_build_ui_snapshot_with_data(temp_db):
    ensure_database(temp_db)
    
    # 模拟一次运行
    run_metadata = {
        "run_date": "2026-05-03",
        "status": "success",
        "index_count": 1,
        "sector_count": 1,
        "stock_count": 1,
        "report_path": "reports/daily/2026-05-03_report.md"
    }
    indices = [{"symbol": "IDX1", "name": "Index 1", "signal": "neutral", "signal_level": "neutral", "data_status": "ok"}]
    sectors = [{"symbol": "SEC1", "name": "Sector 1", "signal": "trend_up", "signal_level": "positive", "data_status": "ok", "priority": "high"}]
    stocks = [{"code": "STK1", "name": "Stock 1", "signal": "trend_down", "signal_level": "negative", "data_status": "ok", "priority": "high", "position_status": "holding"}]
    
    insert_run_daily_snapshot(run_metadata, indices, sectors, stocks, temp_db)
    
    snapshot = build_ui_snapshot(database_path=temp_db)
    
    assert snapshot["latest_run"]["run_date"] == "2026-05-03"
    assert snapshot["dashboard_summary"]["latest_run"]["id"] is not None
    assert snapshot["review_queue"]["count"] > 0
    assert snapshot["paths"]["ui_snapshot_json"] == "data/processed/ui_snapshot.json"
    assert snapshot["paths"]["daily_report"] == "reports/daily/2026-05-03_report.md"
    assert snapshot["source_status"]["default_quote_source"] == "akshare"

def test_write_ui_snapshot_json(temp_db, tmp_path):
    ensure_database(temp_db)
    insert_run_daily_snapshot({"run_date": "2026-05-03", "status": "success", "index_count": 0, "sector_count": 0, "stock_count": 0}, [], [], [], temp_db)
    
    json_path = tmp_path / "ui_snapshot.json"
    result_path = write_ui_snapshot_json(output_path=json_path, database_path=temp_db)
    
    assert result_path.exists()
    with open(result_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data["app"]["name_cn"] == "A股智研台"
        assert data["latest_run"]["run_date"] == "2026-05-03"
        assert "dashboard_summary" in data
        assert "review_queue" in data
        assert "source_status" in data
        assert "demo-secret-token-1234" not in json.dumps(data, ensure_ascii=False)
