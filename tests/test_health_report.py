from pathlib import Path

from app_core.reports.health_report import render_health_report, write_health_report


def test_render_health_report_contains_key_sections() -> None:
    result = {
        "generated_at": "2026-05-01T11:00:00",
        "environment": "development",
        "python_version": "3.12.13",
        "project_root": "/tmp/project",
        "primary_source": "akshare",
        "registered_sources": ["akshare", "local_cache"],
        "fallback_order": ["akshare", "local_cache"],
        "fallback_enabled": True,
        "local_cache_status": {
            "enabled": True,
            "available": True,
            "max_age_days": 7,
            "allow_stale": True,
            "stale": False,
            "path": "/tmp/project/data/raw/000001_daily_raw.csv",
            "modified_at": "2026-05-01T10:59:00",
            "age_seconds": 60,
            "row_count": 120,
        },
        "proxy_environment": [
            {"name": "HTTP_PROXY", "is_set": True, "value": "http://***:***@proxy.example.com:7890"}
        ],
        "dependencies": {
            "requests": {"available": True, "message": "requests import ok"},
            "akshare": {"available": True, "message": "akshare import ok"},
        },
        "connectivity": {
            "url": "https://push2his.eastmoney.com",
            "status": "failed",
            "status_code": None,
            "error_message": "ProxyError: unable to connect to proxy",
        },
        "sample_fetch": {
            "code": "000001",
            "status": "failed",
            "rows": None,
            "latest_trade_date": "",
            "error_type": "ProxyError",
            "error_message": "ProxyError: unable to connect to proxy",
        },
        "overall_status": "degraded",
        "suggestions": ["当前终端环境检测到代理变量，若 AKShare 连接异常，可尝试临时 unset HTTP_PROXY / HTTPS_PROXY / ALL_PROXY 后重试。"],
    }

    content = render_health_report(result)

    assert "A股智研台数据源健康检查报告" in content
    assert "代理环境变量检查结果" in content
    assert "本地缓存兜底状态" in content
    assert "akshare -> local_cache" in content
    assert "总体诊断结论" in content
    assert "degraded" in content
    assert "ProxyError: unable to connect to proxy" in content


def test_write_health_report_creates_markdown_file(tmp_path: Path) -> None:
    result = {
        "generated_at": "2026-05-01T11:00:00",
        "environment": "development",
        "python_version": "3.12.13",
        "project_root": "/tmp/project",
        "primary_source": "akshare",
        "registered_sources": ["akshare", "local_cache"],
        "fallback_order": ["akshare", "local_cache"],
        "fallback_enabled": True,
        "local_cache_status": {
            "enabled": True,
            "available": False,
            "max_age_days": 7,
            "allow_stale": True,
            "stale": False,
            "path": "",
            "modified_at": "",
            "age_seconds": None,
            "row_count": 0,
        },
        "proxy_environment": [],
        "dependencies": {
            "requests": {"available": True, "message": "requests import ok"},
            "akshare": {"available": True, "message": "akshare import ok"},
        },
        "connectivity": {
            "url": "https://push2his.eastmoney.com",
            "status": "ok",
            "status_code": 200,
            "error_message": "",
        },
        "sample_fetch": {
            "code": "000001",
            "status": "success",
            "rows": 120,
            "latest_trade_date": "2024-01-31",
            "error_type": "",
            "error_message": "",
        },
        "overall_status": "healthy",
        "suggestions": ["数据源检查通过，可以继续执行 run-daily。"],
    }

    output_path = tmp_path / "health.md"
    report_path = write_health_report(result, output_path=output_path)

    assert report_path == output_path
    assert output_path.exists()
    assert "healthy" in output_path.read_text(encoding="utf-8")
