from pathlib import Path

from app_core.diagnostics import data_source_health


def test_mask_proxy_value_hides_credentials() -> None:
    masked = data_source_health.mask_proxy_value("http://user:password@example.com:7890")

    assert masked == "http://***:***@example.com:7890"


def test_determine_health_status_variants() -> None:
    dependencies_ok = {
        "requests": {"available": True, "message": "requests import ok"},
        "akshare": {"available": True, "message": "akshare import ok"},
    }
    dependencies_failed = {
        "requests": {"available": False, "message": "failed"},
        "akshare": {"available": True, "message": "ok"},
    }

    assert (
        data_source_health.determine_health_status(
            dependencies_ok,
            {"status": "success"},
        )
        == "healthy"
    )
    assert (
        data_source_health.determine_health_status(
            dependencies_ok,
            {"status": "success", "fallback_used": True},
        )
        == "degraded"
    )
    assert (
        data_source_health.determine_health_status(
            dependencies_ok,
            {"status": "failed"},
        )
        == "degraded"
    )
    assert (
        data_source_health.determine_health_status(
            dependencies_failed,
            {"status": "failed"},
        )
        == "failed"
    )


def test_run_data_source_health_check_uses_first_enabled_symbol(
    monkeypatch,
    tmp_path: Path,
) -> None:
    logger_messages: list[str] = []

    class DummyLogger:
        def info(self, message: str, *args: object) -> None:
            logger_messages.append(message % args if args else message)

        def exception(self, message: str, *args: object) -> None:
            logger_messages.append(message % args if args else message)

    monkeypatch.setattr(
        data_source_health,
        "collect_proxy_environment",
        lambda environment=None: [],
    )
    monkeypatch.setattr(
        data_source_health,
        "check_dependencies",
        lambda: {
            "requests": {"available": True, "message": "requests import ok"},
            "akshare": {"available": True, "message": "akshare import ok"},
        },
    )
    monkeypatch.setattr(
        data_source_health,
        "check_connectivity",
        lambda timeout_seconds, logger: {
            "url": data_source_health.DEFAULT_TEST_URL,
            "status": "ok",
            "status_code": 200,
            "error_message": "",
        },
    )
    monkeypatch.setattr(
        data_source_health,
        "check_sample_fetch",
        lambda test_symbol, timeout_seconds, logger, manager=None: {
            "code": test_symbol,
            "status": "success",
            "source_name": "akshare",
            "fallback_used": False,
            "rows": 120,
            "latest_trade_date": "2024-01-31",
            "error_type": "",
            "error_message": "",
        },
    )
    monkeypatch.setattr(
        data_source_health,
        "write_health_report",
        lambda result, report_date=None, output_path=None: tmp_path / "health.md",
    )

    result = data_source_health.run_data_source_health_check(
        settings={
            "environment": "development",
            "network": {"request_timeout_seconds": 8},
            "diagnostics": {
                "default_test_symbol": "000001",
                "health_report_dir": "reports/health",
            },
        },
        watchlist_config={
            "watchlist": [
                {"code": "600519", "enabled": False},
                {"code": "000001", "enabled": True},
            ]
        },
        logger=DummyLogger(),
    )

    assert result["overall_status"] == "healthy"
    assert result["sample_fetch"]["code"] == "000001"
    assert result["primary_source"] == "akshare"
    assert result["registered_sources"] == ["akshare", "local_cache"]
    assert result["fallback_order"] == ["akshare", "local_cache"]
    assert result["fallback_enabled"] is True
    assert result["local_cache_status"]["enabled"] is True
    assert result["local_cache_status"]["max_age_days"] == 7
    assert result["report_path"] == tmp_path / "health.md"
    assert any("test_symbol=000001" in message for message in logger_messages)
    assert any("primary_source=akshare" in message for message in logger_messages)


def test_build_suggestions_includes_ssl_hint() -> None:
    suggestions = data_source_health.build_suggestions(
        proxy_environment=[],
        overall_status="degraded",
        dependencies={
            "requests": {"available": True, "message": "requests import ok"},
            "akshare": {"available": True, "message": "akshare import ok"},
        },
        connectivity={
            "status": "failed",
            "error_message": "SSLError: SSL record layer failure",
        },
        sample_fetch={
            "status": "failed",
            "error_message": "SSLError: SSL record layer failure",
        },
    )

    assert any("SSL 连接异常" in suggestion for suggestion in suggestions)
