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


def render_daily_report(
    records: list[dict[str, Any]],
    generated_at: str | None = None,
    *,
    stage_name: str = "V0.1.3 run-daily",
    processed_csv_path: str = "data/processed/daily_signals.csv",
    raw_data_dir: str = "data/raw",
    log_path: str = "logs/app.log",
) -> str:
    """Render the daily markdown report content."""
    generated_at = generated_at or datetime.now().isoformat(timespec="seconds")
    summary = _build_summary(records)

    lines = [
        "# A股智研台每日观察报告",
        "",
        f"- 项目名称：{APP_NAME_CN} / {APP_NAME_EN}",
        f"- 当前版本：{VERSION}",
        f"- 开发维护：{DEVELOPER}",
        f"- 版权：{COPYRIGHT_TEXT}",
        f"- 生成时间：{generated_at}",
        f"- 当前阶段：{stage_name}",
        f"- 安全提醒：{SAFETY_NOTICE}",
        "",
        "## 本次执行摘要",
        "",
        f"- 自选股总数：{summary['total_count']}",
        f"- 成功采集数量：{summary['success_count']}",
        f"- 失败数量：{summary['failed_count']}",
        f"- trend_up 数量：{summary['trend_up_count']}",
        f"- trend_down 数量：{summary['trend_down_count']}",
        f"- neutral 数量：{summary['neutral_count']}",
        f"- insufficient_data 数量：{summary['insufficient_data_count']}",
        "",
        "## 自选股信号表",
        "",
        "| code | name | latest_trade_date | close | ma5 | ma20 | signal | signal_level | data_status | reason |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]

    for record in records:
        lines.append(
            (
                "| {code} | {name} | {latest_trade_date} | {close} | {ma5} | {ma20} | "
                "{signal} | {signal_level} | {data_status} | {reason} |"
            ).format(
                code=record.get("code", ""),
                name=record.get("name", ""),
                latest_trade_date=_display_value(record.get("latest_trade_date")),
                close=_display_value(record.get("close")),
                ma5=_display_value(record.get("ma5")),
                ma20=_display_value(record.get("ma20")),
                signal=record.get("signal", ""),
                signal_level=record.get("signal_level", ""),
                data_status=record.get("data_status", ""),
                reason=record.get("reason", ""),
            )
        )

    failures = [
        record
        for record in records
        if record.get("data_status") != "ok" or record.get("signal_level") == "unavailable"
    ]
    lines.extend(["", "## 异常列表", ""])

    if failures:
        for record in failures:
            lines.append(
                f"- {record.get('code', '')} {record.get('name', '')}: "
                f"{_display_error_message(record)}"
            )
    else:
        lines.append("- 无")

    lines.extend(
        [
            "",
            "## 运行产物",
            "",
            f"- processed CSV 路径：`{processed_csv_path}`",
            f"- raw 数据目录：`{raw_data_dir}`",
            f"- 日志路径：`{log_path}`",
            "",
            "## 下一步建议占位",
            "",
            "- 增加更多指标",
            "- 增加模拟盘",
            "- 后续由 OpenClaw 读取日报并生成盘前/盘后摘要",
        ]
    )

    return "\n".join(lines) + "\n"


def write_daily_report(
    records: list[dict[str, Any]],
    *,
    report_date: str | None = None,
    generated_at: str | None = None,
    output_path: str | Path | None = None,
    stage_name: str = "V0.1.3 run-daily",
    processed_csv_path: str = "data/processed/daily_signals.csv",
    raw_data_dir: str = "data/raw",
    log_path: str = "logs/app.log",
) -> Path:
    """Write the markdown report and return the saved path."""
    report_date = report_date or datetime.now().strftime("%Y-%m-%d")
    relative_output_path = Path(output_path or f"reports/daily/{report_date}_daily_report.md")
    content = render_daily_report(
        records,
        generated_at=generated_at,
        stage_name=stage_name,
        processed_csv_path=processed_csv_path,
        raw_data_dir=raw_data_dir,
        log_path=log_path,
    )
    return write_text_file(content, relative_output_path)


def _display_value(value: Any) -> str:
    if value is None or value == "":
        return "-"
    return str(value)


def _build_summary(records: list[dict[str, Any]]) -> dict[str, int]:
    total_count = len(records)
    failed_count = sum(1 for record in records if record.get("data_status") == "fetch_failed")
    insufficient_data_count = sum(
        1 for record in records if record.get("data_status") == "insufficient_data"
    )
    trend_up_count = sum(1 for record in records if record.get("signal") == "trend_up")
    trend_down_count = sum(1 for record in records if record.get("signal") == "trend_down")
    neutral_count = sum(
        1
        for record in records
        if record.get("signal") == "neutral" and record.get("data_status") == "ok"
    )
    success_count = total_count - failed_count

    return {
        "total_count": total_count,
        "success_count": success_count,
        "failed_count": failed_count,
        "trend_up_count": trend_up_count,
        "trend_down_count": trend_down_count,
        "neutral_count": neutral_count,
        "insufficient_data_count": insufficient_data_count,
    }


def _display_error_message(record: dict[str, Any]) -> str:
    message = str(record.get("error_message") or record.get("reason") or "未知异常")
    first_line = message.splitlines()[0].strip()
    if "traceback" in first_line.lower():
        return "UnknownError: unexpected fetch error"
    return first_line
