from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

from app_core.storage.file_store import write_text_file


def render_daily_report(
    records: list[dict[str, Any]],
    generated_at: str | None = None,
) -> str:
    """Render the daily markdown report content."""
    generated_at = generated_at or datetime.now().isoformat(timespec="seconds")

    lines = [
        "# A股智研台每日观察报告",
        "",
        f"- 生成时间：{generated_at}",
        "- 当前阶段说明：V0.1 run-daily",
        "- 安全边界提醒：本报告仅用于研究和模拟盘，不构成实盘交易建议",
        "",
        "## 自选股摘要表",
        "",
        "| 代码 | 名称 | 最新收盘价 | MA5 | MA20 | 策略信号 | 数据状态 |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]

    for record in records:
        lines.append(
            "| {code} | {name} | {close} | {ma5} | {ma20} | {signal} | {data_status} |".format(
                code=record.get("code", ""),
                name=record.get("name", ""),
                close=_display_value(record.get("close")),
                ma5=_display_value(record.get("ma5")),
                ma20=_display_value(record.get("ma20")),
                signal=record.get("signal", ""),
                data_status=record.get("data_status", ""),
            )
        )

    lines.extend(["", "## 个股明细", ""])

    for record in records:
        lines.extend(
            [
                f"### {record.get('code', '')} {record.get('name', '')}",
                "",
                f"- 代码：{record.get('code', '')}",
                f"- 名称：{record.get('name', '')}",
                f"- 最新收盘价：{_display_value(record.get('close'))}",
                f"- MA5：{_display_value(record.get('ma5'))}",
                f"- MA20：{_display_value(record.get('ma20'))}",
                f"- 策略信号：{record.get('signal', '')}",
                f"- 简要原因：{record.get('reason', '')}",
                f"- 数据状态：{record.get('data_status', '')}",
                "",
            ]
        )

    failures = [record for record in records if record.get("data_status") != "ok"]
    lines.extend(["## 失败或异常列表", ""])

    if failures:
        for record in failures:
            lines.append(
                f"- {record.get('code', '')} {record.get('name', '')}: "
                f"{record.get('error_message') or record.get('reason', '未知异常')}"
            )
    else:
        lines.append("- 无")

    lines.extend(
        [
            "",
            "## 下一步建议占位",
            "",
            "- 观察趋势信号是否连续出现",
            "- 后续补充更完整的日报结构与异常说明",
        ]
    )

    return "\n".join(lines) + "\n"


def write_daily_report(
    records: list[dict[str, Any]],
    *,
    report_date: str | None = None,
    generated_at: str | None = None,
    output_path: str | Path | None = None,
) -> Path:
    """Write the markdown report and return the saved path."""
    report_date = report_date or datetime.now().strftime("%Y-%m-%d")
    relative_output_path = Path(output_path or f"reports/daily/{report_date}_daily_report.md")
    content = render_daily_report(records, generated_at=generated_at)
    return write_text_file(content, relative_output_path)


def _display_value(value: Any) -> str:
    if value is None or value == "":
        return "-"
    return str(value)
