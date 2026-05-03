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
    index_records: list[dict[str, Any]] | None = None,
    sector_records: list[dict[str, Any]] | None = None,
    generated_at: str | None = None,
    *,
    stage_name: str = "V0.2.4 run-daily",
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
        "### 优先级与信号小结",
        "",
        f"- P1 观察数量：{summary['priority_p1_count']}",
        f"- P2 观察数量：{summary['priority_p2_count']}",
        f"- P3 观察数量：{summary['priority_p3_count']}",
        f"- positive 数量：{summary['positive_count']}",
        f"- negative 数量：{summary['negative_count']}",
        f"- neutral(signal_level) 数量：{summary['signal_level_neutral_count']}",
        f"- unavailable 数量：{summary['unavailable_count']}",
        f"- fetch_failed 数量：{summary['fetch_failed_count']}",
        "",
        "## 市场指数观察",
        "",
        "| symbol | name | category | date | close | signal | signal_level | data_status |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]

    if index_records:
        for idx in index_records:
            lines.append(
                (
                    "| {symbol} | {name} | {category} | {date} | {close} | {signal} | {signal_level} | {data_status} |"
                ).format(
                    symbol=idx.get("symbol", ""),
                    name=idx.get("name", ""),
                    category=idx.get("category", ""),
                    date=_display_value(idx.get("date")),
                    close=_display_value(idx.get("close")),
                    signal=idx.get("signal", ""),
                    signal_level=idx.get("signal_level", ""),
                    data_status=idx.get("data_status", ""),
                )
            )
    else:
        lines.append("| - | - | - | - | - | - | - | - |")

    lines.extend(
        [
            "",
            "## 行业/板块观察",
            "",
            "| symbol | name | board_type | category | priority | date | close | signal | signal_level | data_status |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )

    if sector_records:
        for sec in sector_records:
            lines.append(
                (
                    "| {symbol} | {name} | {board_type} | {category} | {priority} | {date} | {close} | {signal} | {signal_level} | {data_status} |"
                ).format(
                    symbol=sec.get("symbol", ""),
                    name=sec.get("name", ""),
                    board_type=sec.get("board_type", ""),
                    category=sec.get("category", ""),
                    priority=sec.get("priority", ""),
                    date=_display_value(sec.get("date")),
                    close=_display_value(sec.get("close")),
                    signal=sec.get("signal", ""),
                    signal_level=sec.get("signal_level", ""),
                    data_status=sec.get("data_status", ""),
                )
            )
    else:
        lines.append("| - | - | - | - | - | - | - | - | - | - |")

    lines.extend(
        [
            "",
            "## 自选股信号表",
            "",
            "| code | name | sector | priority | position_status | latest_trade_date | close | signal | signal_level | data_status | reason |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )

    for record in records:
        lines.append(
            (
                "| {code} | {name} | {sector} | {priority} | {position_status} | {latest_trade_date} | "
                "{close} | {signal} | {signal_level} | {data_status} | {reason} |"
            ).format(
                code=record.get("code", ""),
                name=record.get("name", ""),
                sector=_display_value(record.get("sector")),
                priority=_display_value(record.get("priority")),
                position_status=_display_value(record.get("position_status")),
                latest_trade_date=_display_value(record.get("latest_trade_date")),
                close=_display_value(record.get("close")),
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
    index_records: list[dict[str, Any]] | None = None,
    sector_records: list[dict[str, Any]] | None = None,
    *,
    report_date: str | None = None,
    generated_at: str | None = None,
    output_path: str | Path | None = None,
    stage_name: str = "V0.2.4 run-daily",
    processed_csv_path: str = "data/processed/daily_signals.csv",
    raw_data_dir: str = "data/raw",
    log_path: str = "logs/app.log",
) -> Path:
    """Write the markdown report and return the saved path."""
    report_date = report_date or datetime.now().strftime("%Y-%m-%d")
    relative_output_path = Path(output_path or f"reports/daily/{report_date}_daily_report.md")
    content = render_daily_report(
        records,
        index_records=index_records,
        sector_records=sector_records,
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
    priority_p1_count = sum(1 for record in records if record.get("priority") == "P1")
    priority_p2_count = sum(1 for record in records if record.get("priority") == "P2")
    priority_p3_count = sum(1 for record in records if record.get("priority") == "P3")
    positive_count = sum(1 for record in records if record.get("signal_level") == "positive")
    negative_count = sum(1 for record in records if record.get("signal_level") == "negative")
    signal_level_neutral_count = sum(
        1 for record in records if record.get("signal_level") == "neutral"
    )
    unavailable_count = sum(1 for record in records if record.get("signal_level") == "unavailable")

    return {
        "total_count": total_count,
        "success_count": success_count,
        "failed_count": failed_count,
        "trend_up_count": trend_up_count,
        "trend_down_count": trend_down_count,
        "neutral_count": neutral_count,
        "insufficient_data_count": insufficient_data_count,
        "priority_p1_count": priority_p1_count,
        "priority_p2_count": priority_p2_count,
        "priority_p3_count": priority_p3_count,
        "positive_count": positive_count,
        "negative_count": negative_count,
        "signal_level_neutral_count": signal_level_neutral_count,
        "unavailable_count": unavailable_count,
        "fetch_failed_count": failed_count,
    }


def _display_error_message(record: dict[str, Any]) -> str:
    message = str(record.get("error_message") or record.get("reason") or "未知异常")
    first_line = message.splitlines()[0].strip()
    if "traceback" in first_line.lower():
        return "UnknownError: unexpected fetch error"
    return first_line
