from pathlib import Path

from app_core.reports.daily_report import render_daily_report, write_daily_report


def test_render_daily_report_contains_key_sections() -> None:
    records = [
        {
            "fetch_time": "2024-01-31T17:59:00",
            "date": "2024-01-31",
            "latest_trade_date": "2024-01-31",
            "code": "000001",
            "name": "平安银行",
            "close": 12.34,
            "ma5": 12.1,
            "ma20": 11.8,
            "signal": "trend_up",
            "signal_level": "positive",
            "reason": "close > ma5 且 close > ma20",
            "data_status": "ok",
            "error_message": "",
            "raw_file_path": "data/raw/000001_daily_raw.csv",
        },
        {
            "fetch_time": "2024-01-31T18:00:00",
            "date": "",
            "latest_trade_date": "",
            "code": "600519",
            "name": "贵州茅台",
            "close": None,
            "ma5": None,
            "ma20": None,
            "signal": "neutral",
            "signal_level": "unavailable",
            "reason": "数据采集失败",
            "data_status": "fetch_failed",
            "error_message": "ProxyError: unable to connect to proxy\nTraceback (most recent call last): ...",
            "raw_file_path": "",
        }
    ]

    content = render_daily_report(
        records,
        generated_at="2024-01-31T18:00:00",
        processed_csv_path="data/processed/daily_signals.csv",
        raw_data_dir="data/raw",
        log_path="logs/app.log",
    )

    assert "A股智研台每日观察报告" in content
    assert "A股智研台 / AShare Insight Lab" in content
    assert "当前版本：0.1.4" in content
    assert "开发维护：pL" in content
    assert "Copyright © 2026 @B‘lock10STUdio. All rights reserved." in content
    assert "V0.1.3 run-daily" in content
    assert "平安银行" in content
    assert "## 本次执行摘要" in content
    assert "成功采集数量：1" in content
    assert "失败数量：1" in content
    assert "signal_level" in content
    assert "processed CSV 路径" in content
    assert "ProxyError: unable to connect to proxy" in content
    assert "Traceback (most recent call last)" not in content


def test_write_daily_report_creates_markdown_file(tmp_path: Path) -> None:
    records = [
        {
            "fetch_time": "2024-01-31T18:00:00",
            "date": "2024-01-31",
            "latest_trade_date": "2024-01-31",
            "code": "600519",
            "name": "贵州茅台",
            "close": 1688.0,
            "ma5": 1660.0,
            "ma20": 1600.0,
            "signal": "trend_up",
            "signal_level": "positive",
            "reason": "close > ma5 且 close > ma20",
            "data_status": "ok",
            "error_message": "",
            "raw_file_path": "data/raw/600519_daily_raw.csv",
        }
    ]

    output_path = tmp_path / "2024-01-31_daily_report.md"
    report_path = write_daily_report(records, output_path=output_path)

    assert report_path == output_path
    assert output_path.exists()
    assert "贵州茅台" in output_path.read_text(encoding="utf-8")
