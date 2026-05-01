from __future__ import annotations

import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import SplitResult, urlsplit, urlunsplit

from app_core.data_sources.akshare_provider import (
    fetch_stock_daily_history,
    get_akshare_import_error,
    is_akshare_available,
    summarize_fetch_error,
)
from app_core.path_utils import get_project_root
from app_core.project_info import APP_NAME_EN, DEVELOPER, VERSION
from app_core.reports.health_report import write_health_report
from app_core.storage.file_store import ensure_directory


DEFAULT_TEST_URL = "https://push2his.eastmoney.com"
PROXY_ENV_KEYS = [
    "HTTP_PROXY",
    "HTTPS_PROXY",
    "ALL_PROXY",
    "NO_PROXY",
    "http_proxy",
    "https_proxy",
    "all_proxy",
    "no_proxy",
]


def run_data_source_health_check(
    settings: dict[str, Any],
    watchlist_config: dict[str, Any],
    logger: Any,
) -> dict[str, Any]:
    generated_at = datetime.now().isoformat(timespec="seconds")
    timeout_seconds = int(settings.get("network", {}).get("request_timeout_seconds", 10))
    diagnostics_settings = settings.get("diagnostics", {})
    environment = settings.get("environment", "development")
    report_dir = diagnostics_settings.get("health_report_dir", "reports/health")
    default_test_symbol = diagnostics_settings.get("default_test_symbol", "000001")
    enabled_items = [
        item for item in watchlist_config.get("watchlist", []) if item.get("enabled") is True
    ]
    test_symbol = str(enabled_items[0].get("code", default_test_symbol)).strip() if enabled_items else default_test_symbol

    logger.info(
        "data-source health check started app=%s version=%s environment=%s developer=%s timeout=%ss test_symbol=%s",
        APP_NAME_EN,
        VERSION,
        environment,
        DEVELOPER,
        timeout_seconds,
        test_symbol,
    )

    proxy_environment = collect_proxy_environment()
    dependencies = check_dependencies()
    connectivity = check_connectivity(timeout_seconds, logger)
    sample_fetch = check_sample_fetch(test_symbol, timeout_seconds, logger)
    overall_status = determine_health_status(dependencies, sample_fetch)
    suggestions = build_suggestions(proxy_environment, overall_status, dependencies, connectivity, sample_fetch)

    ensure_directory(report_dir)
    report_date = datetime.now().strftime("%Y-%m-%d")

    result = {
        "generated_at": generated_at,
        "environment": environment,
        "python_version": sys.version.replace("\n", " "),
        "project_root": str(get_project_root()),
        "proxy_environment": proxy_environment,
        "dependencies": dependencies,
        "connectivity": connectivity,
        "sample_fetch": sample_fetch,
        "overall_status": overall_status,
        "suggestions": suggestions,
    }

    report_path = write_health_report(result, report_date=report_date, output_path=Path(report_dir) / f"{report_date}_data_source_health.md")
    result["report_path"] = report_path

    logger.info("data-source health report written to %s", report_path)
    logger.info("data-source health check finished with status=%s", overall_status)

    return result


def collect_proxy_environment(environment: dict[str, str] | None = None) -> list[dict[str, Any]]:
    environment = environment or dict(os.environ)
    snapshot: list[dict[str, Any]] = []
    for key in PROXY_ENV_KEYS:
        raw_value = environment.get(key, "")
        snapshot.append(
            {
                "name": key,
                "is_set": bool(raw_value),
                "value": mask_proxy_value(raw_value) if raw_value else "",
            }
        )
    return snapshot


def mask_proxy_value(proxy_value: str) -> str:
    if not proxy_value:
        return ""
    try:
        parts = urlsplit(proxy_value)
    except ValueError:
        return proxy_value

    if not parts.scheme or not parts.netloc:
        return proxy_value

    hostname = parts.hostname or ""
    port = f":{parts.port}" if parts.port else ""
    if parts.username is None and parts.password is None:
        return proxy_value

    masked_auth = "***"
    if parts.password is not None:
        masked_auth = "***:***"

    masked_netloc = f"{masked_auth}@{hostname}{port}"
    masked_parts = SplitResult(parts.scheme, masked_netloc, parts.path, parts.query, parts.fragment)
    return urlunsplit(masked_parts)


def check_dependencies() -> dict[str, dict[str, Any]]:
    requests_available = True
    requests_message = "requests import ok"
    try:
        __import__("requests")
    except Exception as error:  # pragma: no cover - import failure depends on runtime env
        requests_available = False
        requests_message = summarize_fetch_error(error)

    akshare_available = is_akshare_available()
    akshare_message = "akshare import ok"
    if not akshare_available:
        import_error = get_akshare_import_error()
        akshare_message = summarize_fetch_error(import_error) if import_error else "UnknownError: akshare import failed"

    return {
        "requests": {
            "available": requests_available,
            "message": requests_message,
        },
        "akshare": {
            "available": akshare_available,
            "message": akshare_message,
        },
    }


def check_connectivity(timeout_seconds: int, logger: Any) -> dict[str, Any]:
    try:
        import requests
    except Exception as error:  # pragma: no cover - import failure depends on runtime env
        message = summarize_fetch_error(error, timeout_seconds=timeout_seconds)
        return {
            "url": DEFAULT_TEST_URL,
            "status": "failed",
            "status_code": None,
            "error_message": message,
        }

    try:
        response = requests.get(DEFAULT_TEST_URL, timeout=timeout_seconds)
        return {
            "url": DEFAULT_TEST_URL,
            "status": "ok",
            "status_code": response.status_code,
            "error_message": "",
        }
    except Exception as error:  # pragma: no cover - network branch
        message = summarize_fetch_error(error, timeout_seconds=timeout_seconds)
        logger.exception("data-source connectivity check failed: %s", message)
        return {
            "url": DEFAULT_TEST_URL,
            "status": "failed",
            "status_code": None,
            "error_message": message,
        }


def check_sample_fetch(test_symbol: str, timeout_seconds: int, logger: Any) -> dict[str, Any]:
    try:
        _, normalized_dataframe = fetch_stock_daily_history(
            test_symbol,
            timeout_seconds=timeout_seconds,
        )
        latest_trade_date = ""
        if not normalized_dataframe.empty and "date" in normalized_dataframe.columns:
            latest_trade_date = str(normalized_dataframe.iloc[-1]["date"])
        return {
            "code": test_symbol,
            "status": "success",
            "rows": len(normalized_dataframe),
            "latest_trade_date": latest_trade_date,
            "error_type": "",
            "error_message": "",
        }
    except Exception as error:  # pragma: no cover - network/runtime branch
        message = summarize_fetch_error(error, timeout_seconds=timeout_seconds)
        logger.exception("data-source sample fetch failed for %s: %s", test_symbol, message)
        return {
            "code": test_symbol,
            "status": "failed",
            "rows": None,
            "latest_trade_date": "",
            "error_type": message.split(":", maxsplit=1)[0],
            "error_message": message,
        }


def determine_health_status(
    dependencies: dict[str, dict[str, Any]],
    sample_fetch: dict[str, Any],
) -> str:
    if not dependencies.get("akshare", {}).get("available") or not dependencies.get("requests", {}).get("available"):
        return "failed"
    if sample_fetch.get("status") == "success":
        return "healthy"
    return "degraded"


def build_suggestions(
    proxy_environment: list[dict[str, Any]],
    overall_status: str,
    dependencies: dict[str, dict[str, Any]],
    connectivity: dict[str, Any],
    sample_fetch: dict[str, Any],
) -> list[str]:
    suggestions: list[str] = []
    has_proxy = any(item.get("is_set") for item in proxy_environment)

    if has_proxy:
        suggestions.append(
            "当前终端环境检测到代理变量，若 AKShare 连接异常，可尝试临时 unset HTTP_PROXY / HTTPS_PROXY / ALL_PROXY 后重试。"
        )
        suggestions.append(
            "如果使用代理，应确认代理对 push2his.eastmoney.com 可用。"
        )

    ssl_related = any(
        "SSLError" in str(item.get("error_message", ""))
        for item in (connectivity, sample_fetch)
    )
    if ssl_related:
        suggestions.append(
            "检测到 SSL 连接异常，可尝试切换网络、关闭/调整代理、重试 AKShare/Eastmoney 访问。"
        )

    if not dependencies.get("requests", {}).get("available"):
        suggestions.append("requests 依赖不可用，请先确认当前虚拟环境依赖安装是否完整。")
    if not dependencies.get("akshare", {}).get("available"):
        suggestions.append("AKShare 依赖不可用，请先确认当前虚拟环境依赖安装是否完整。")
    if overall_status == "degraded":
        suggestions.append("示例股票采集失败，可先运行 doctor 再检查代理、网络和东方财富连通性。")
    if overall_status == "healthy":
        suggestions.append("数据源检查通过，可以继续执行 run-daily。")
    if connectivity.get("status") == "failed" and sample_fetch.get("status") == "failed":
        suggestions.append("当前连通性与示例股票采集均失败，建议优先检查网络出口、代理配置或临时关闭代理后重试。")

    return suggestions
