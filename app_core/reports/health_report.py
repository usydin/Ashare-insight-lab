from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

from app_core.project_info import (
    APP_NAME_CN,
    APP_NAME_EN,
    COPYRIGHT_TEXT,
    DEVELOPER,
    SAFETY_NOTICE,
    VERSION,
)
from app_core.storage.file_store import write_text_file


def render_health_report(result: dict[str, Any]) -> str:
    generated_at = result.get("generated_at") or datetime.now().isoformat(timespec="seconds")
    proxies: list[dict[str, Any]] = result.get("proxy_environment", [])
    dependencies: dict[str, dict[str, Any]] = result.get("dependencies", {})
    connectivity: dict[str, Any] = result.get("connectivity", {})
    sample_fetch: dict[str, Any] = result.get("sample_fetch", {})
    suggestions: list[str] = result.get("suggestions", [])
    local_cache_status: dict[str, Any] = result.get("local_cache_status", {})

    lines = [
        "# A股智研台数据源健康检查报告",
        "",
        f"- 生成时间：{generated_at}",
        f"- 项目名称：{APP_NAME_CN} / {APP_NAME_EN}",
        f"- 当前版本：{VERSION}",
        f"- 开发者：{DEVELOPER}",
        f"- 版权：{COPYRIGHT_TEXT}",
        f"- 安全提醒：{SAFETY_NOTICE}",
        f"- 当前环境：{result.get('environment', '-')}",
        f"- Python 版本：{result.get('python_version', '-')}",
        f"- 项目根目录：{result.get('project_root', '-')}",
        "",
        "## 代理环境变量检查结果",
        "",
    ]

    if proxies:
        for item in proxies:
            status = "已设置" if item.get("is_set") else "未设置"
            lines.append(f"- {item.get('name')}: {status} {item.get('value', '')}".rstrip())
    else:
        lines.append("- 无")

    lines.extend(["", "## 依赖检查结果", ""])
    for dependency_name in ("requests", "akshare"):
        dependency = dependencies.get(dependency_name, {})
        status = "ok" if dependency.get("available") else "failed"
        lines.append(
            f"- {dependency_name}: {status} | {dependency.get('message', '-')}"
        )

    lines.extend(
        [
            "",
            "## 数据源管理器状态",
            "",
            f"- 主数据源：{result.get('primary_source', '-')}",
            f"- 注册数据源：{', '.join(result.get('registered_sources', [])) or '-'}",
            f"- fallback 顺序：{' -> '.join(result.get('fallback_order', [])) or '-'}",
            f"- fallback 开关：{'enabled' if result.get('fallback_enabled') else 'disabled'}",
        ]
    )

    lines.extend(["", "## 本地缓存兜底状态", ""])
    if local_cache_status:
        lines.append(f"- enabled：{local_cache_status.get('enabled', False)}")
        lines.append(f"- available：{local_cache_status.get('available', False)}")
        lines.append(f"- max_age_days：{local_cache_status.get('max_age_days', '-')}")
        lines.append(f"- allow_stale：{local_cache_status.get('allow_stale', '-')}")
        lines.append(f"- stale：{local_cache_status.get('stale', False)}")
        if local_cache_status.get("path"):
            lines.append(f"- cache_path：{local_cache_status.get('path')}")
        if local_cache_status.get("modified_at"):
            lines.append(f"- cache_modified_at：{local_cache_status.get('modified_at')}")
        if local_cache_status.get("age_seconds") is not None:
            lines.append(f"- cache_age_seconds：{local_cache_status.get('age_seconds')}")
        lines.append(f"- cache_row_count：{local_cache_status.get('row_count', 0)}")
    else:
        lines.append("- 无")

    lines.extend(["", "## 数据源连通性检查结果", ""])
    if connectivity:
        lines.append(f"- 检测地址：{connectivity.get('url', '-')}")
        lines.append(f"- 结果：{connectivity.get('status', '-')}")
        if connectivity.get("status_code") is not None:
            lines.append(f"- HTTP 状态：{connectivity.get('status_code')}")
        if connectivity.get("error_message"):
            lines.append(f"- 错误摘要：{connectivity.get('error_message')}")
    else:
        lines.append("- 无")

    lines.extend(["", "## 示例股票采集结果", ""])
    if sample_fetch:
        lines.append(f"- 测试股票：{sample_fetch.get('code', '-')}")
        lines.append(f"- 结果：{sample_fetch.get('status', '-')}")
        if sample_fetch.get("source_name"):
            lines.append(f"- source_name：{sample_fetch.get('source_name')}")
        lines.append(f"- fallback_used：{sample_fetch.get('fallback_used', False)}")
        if sample_fetch.get("rows") is not None:
            lines.append(f"- rows：{sample_fetch.get('rows')}")
        if sample_fetch.get("latest_trade_date"):
            lines.append(f"- latest_trade_date：{sample_fetch.get('latest_trade_date')}")
        if sample_fetch.get("error_type"):
            lines.append(f"- error_type：{sample_fetch.get('error_type')}")
        if sample_fetch.get("error_message"):
            lines.append(f"- error_message：{sample_fetch.get('error_message')}")
    else:
        lines.append("- 无")

    lines.extend(
        [
            "",
            "## 总体诊断结论",
            "",
            f"- 结论：{result.get('overall_status', '-')}",
            "",
            "## 建议动作",
            "",
        ]
    )

    if suggestions:
        for suggestion in suggestions:
            lines.append(f"- {suggestion}")
    else:
        lines.append("- 无")

    return "\n".join(lines) + "\n"


def write_health_report(
    result: dict[str, Any],
    *,
    report_date: str | None = None,
    output_path: str | Path | None = None,
) -> Path:
    report_date = report_date or datetime.now().strftime("%Y-%m-%d")
    relative_output_path = Path(output_path or f"reports/health/{report_date}_data_source_health.md")
    content = render_health_report(result)
    return write_text_file(content, relative_output_path)
