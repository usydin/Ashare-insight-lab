from pathlib import Path

from app_core.reports.daily_report import render_daily_report, write_daily_report


def test_render_daily_report_contains_key_sections() -> None:
    records = [
        {
            "date": "2024-01-31",
            "code": "000001",
            "name": "平安银行",
            "close": 12.34,
            "ma5": 12.1,
            "ma20": 11.8,
            "signal": "trend_up",
            "reason": "close > ma5 且 close > ma20",
            "data_status": "ok",
            "error_message": "",
        }
    ]

    content = render_daily_report(records, generated_at="2024-01-31T18:00:00")

    assert "A股智研台每日观察报告" in content
    assert "V0.1 run-daily" in content
    assert "平安银行" in content


def test_write_daily_report_creates_markdown_file(tmp_path: Path) -> None:
    records = [
        {
            "date": "2024-01-31",
            "code": "600519",
            "name": "贵州茅台",
            "close": 1688.0,
            "ma5": 1660.0,
            "ma20": 1600.0,
            "signal": "trend_up",
            "reason": "close > ma5 且 close > ma20",
            "data_status": "ok",
            "error_message": "",
        }
    ]

    output_path = tmp_path / "2024-01-31_daily_report.md"
    report_path = write_daily_report(records, output_path=output_path)

    assert report_path == output_path
    assert output_path.exists()
    assert "贵州茅台" in output_path.read_text(encoding="utf-8")
