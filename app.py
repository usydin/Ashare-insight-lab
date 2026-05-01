from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd

from app_core.app_logger import get_logger
from app_core.config_loader import load_json, load_settings
from app_core.data_sources.akshare_provider import (
    fetch_stock_daily_history,
    summarize_fetch_error,
)
from app_core.diagnostics.data_source_health import run_data_source_health_check
from app_core.path_utils import get_project_root
from app_core.project_info import (
    APP_NAME_CN,
    APP_NAME_EN,
    COPYRIGHT_TEXT,
    DEVELOPER,
    MAINTAINER,
    PROJECT_PURPOSE,
    REPOSITORY_URL,
    SAFETY_NOTICE,
    STAGE,
    VERSION,
)
from app_core.reports.daily_report import write_daily_report
from app_core.storage.file_store import ensure_directory, save_dataframe_csv
from app_core.strategies.ma_strategy import analyze_ma_signal


def print_app_info() -> None:
    settings = load_settings()
    project_root = get_project_root()
    current_time = datetime.now().isoformat(timespec="seconds")

    print(f"项目名称: {APP_NAME_CN}")
    print(f"英文名称: {APP_NAME_EN}")
    print(f"版本号: {VERSION}")
    print(f"当前环境: {settings['environment']}")
    print(f"项目根目录: {project_root}")
    print(f"当前时间: {current_time}")
    print(f"开发者: {DEVELOPER}")
    print(f"版权: {COPYRIGHT_TEXT}")
    print(f"仓库地址: {REPOSITORY_URL}")
    print(f"安全提醒: {SAFETY_NOTICE}")
    print("提示: V0.1.3 data source health diagnostics is ready.")


def print_version_info() -> None:
    print(f"{APP_NAME_EN} {VERSION} ({STAGE})")


def print_about_info() -> None:
    settings = load_settings()

    lines = [
        f"项目名称: {APP_NAME_CN}",
        f"英文名称: {APP_NAME_EN}",
        f"当前版本: {VERSION}",
        f"当前阶段: {STAGE}",
        f"当前环境: {settings['environment']}",
        f"开发者: {DEVELOPER}",
        f"维护者: {MAINTAINER}",
        f"项目定位: {PROJECT_PURPOSE}",
        f"版权声明: {COPYRIGHT_TEXT}",
        f"仓库地址: {REPOSITORY_URL}",
        f"安全提醒: {SAFETY_NOTICE}",
    ]
    print("\n".join(lines))


def run_data_source_doctor() -> int:
    logger = get_logger()
    settings = load_settings()
    watchlist_config = load_json("config/watchlist.json")

    result = run_data_source_health_check(settings, watchlist_config, logger)
    report_path = result["report_path"]

    print("数据源健康检查执行完成")
    print(f"诊断结论: {result['overall_status']}")
    print(f"诊断报告: {report_path}")
    print("日志路径: logs/app.log")

    return 0


def run_daily() -> int:
    logger = get_logger()
    try:
        settings = load_settings()
        watchlist_config = load_json("config/watchlist.json")
        run_started_at = datetime.now()
        generated_at = run_started_at.isoformat(timespec="seconds")
        report_date = run_started_at.strftime("%Y-%m-%d")
        timeout_seconds = int(settings.get("network", {}).get("request_timeout_seconds", 10))
        environment = settings.get("environment", "development")
        raw_dir = settings["storage"]["raw_dir"]
        processed_dir = settings["storage"]["processed_dir"]
        log_dir = settings["storage"]["log_dir"]
        log_path = str(Path(log_dir) / "app.log")

        ensure_directory(raw_dir)
        ensure_directory(processed_dir)
        ensure_directory("reports/daily")
        ensure_directory(log_dir)

        all_watchlist_items = watchlist_config.get("watchlist", [])
        enabled_items = [item for item in all_watchlist_items if item.get("enabled") is True]

        logger.info(
            "run-daily started app=%s version=%s environment=%s developer=%s enabled_symbols=%s request_timeout=%ss",
            APP_NAME_EN,
            VERSION,
            environment,
            DEVELOPER,
            len(enabled_items),
            timeout_seconds,
        )

        records: list[dict[str, Any]] = []

        for item in enabled_items:
            code = str(item.get("code", "")).strip()
            name = item.get("name", "")
            fetch_time = datetime.now().isoformat(timespec="seconds")
            logger.info("data collection started for %s %s", code, name)

            try:
                raw_dataframe, normalized_dataframe = fetch_stock_daily_history(
                    code,
                    timeout_seconds=timeout_seconds,
                )
                raw_path = save_dataframe_csv(
                    raw_dataframe,
                    Path(raw_dir) / f"{code}_daily_raw.csv",
                )
                raw_relative_path = str(raw_path.relative_to(get_project_root()))

                strategy_result = analyze_ma_signal(normalized_dataframe)
                record = {
                    "fetch_time": fetch_time,
                    "date": strategy_result["date"],
                    "latest_trade_date": strategy_result["date"],
                    "code": code,
                    "name": name,
                    "market": item.get("market", ""),
                    "industry": item.get("industry", ""),
                    "close": strategy_result["close"],
                    "ma5": strategy_result["ma5"],
                    "ma20": strategy_result["ma20"],
                    "signal": strategy_result["signal"],
                    "signal_level": _determine_signal_level(
                        strategy_result["signal"],
                        strategy_result["data_status"],
                    ),
                    "reason": strategy_result["reason"],
                    "data_status": strategy_result["data_status"],
                    "error_message": strategy_result["error_message"],
                    "raw_file": raw_relative_path,
                    "raw_file_path": raw_relative_path,
                }
                records.append(record)
                logger.info("data collection succeeded for %s %s", code, name)
            except KeyboardInterrupt:
                raise
            except Exception as error:  # pragma: no cover - network/runtime branch
                message = summarize_fetch_error(error, timeout_seconds=timeout_seconds)
                records.append(
                    {
                        "fetch_time": fetch_time,
                        "date": "",
                        "latest_trade_date": "",
                        "code": code,
                        "name": name,
                        "market": item.get("market", ""),
                        "industry": item.get("industry", ""),
                        "close": None,
                        "ma5": None,
                        "ma20": None,
                        "signal": "neutral",
                        "signal_level": "unavailable",
                        "reason": "数据采集失败",
                        "data_status": "fetch_failed",
                        "error_message": message,
                        "raw_file": "",
                        "raw_file_path": "",
                    }
                )
                logger.exception("data collection failed for %s %s: %s", code, name, message)

        summary = summarize_run_daily_records(records)
        processed_dataframe = pd.DataFrame(
            records,
            columns=[
                "fetch_time",
                "date",
                "latest_trade_date",
                "code",
                "name",
                "market",
                "industry",
                "close",
                "ma5",
                "ma20",
                "signal",
                "signal_level",
                "reason",
                "data_status",
                "error_message",
                "raw_file",
                "raw_file_path",
            ],
        )

        processed_path = save_dataframe_csv(
            processed_dataframe,
            Path(processed_dir) / "daily_signals.csv",
        )
        report_path = write_daily_report(
            records,
            report_date=report_date,
            generated_at=generated_at,
            stage_name="V0.1.3 run-daily",
            processed_csv_path=_to_relative_path(processed_path),
            raw_data_dir=raw_dir,
            log_path=log_path,
        )

        logger.info(
            "run-daily summary: success_count=%s failed_count=%s trend_up_count=%s trend_down_count=%s neutral_count=%s",
            summary["success_count"],
            summary["failed_count"],
            summary["trend_up_count"],
            summary["trend_down_count"],
            summary["neutral_count"],
        )
        logger.info("daily signals saved to %s", processed_path)
        logger.info("daily report written to %s", report_path)
        logger.info("run-daily finished")

        print("run-daily 执行完成")
        print(f"已处理股票数: {len(enabled_items)}")
        print(f"处理后数据: {processed_path}")
        print(f"日报路径: {report_path}")
        print("日志路径: logs/app.log")

        return 0
    except KeyboardInterrupt:
        logger.warning("run-daily interrupted by user")
        print("run-daily 已被用户中断")
        return 130


def summarize_run_daily_records(records: list[dict[str, Any]]) -> dict[str, int]:
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


def _determine_signal_level(signal: str, data_status: str) -> str:
    if data_status != "ok":
        return "unavailable"
    if signal == "trend_up":
        return "positive"
    if signal == "trend_down":
        return "negative"
    return "neutral"


def _to_relative_path(path: str | Path) -> str:
    path_object = Path(path)
    if path_object.is_absolute():
        return str(path_object.relative_to(get_project_root()))
    return str(path_object)


def main() -> int:
    if len(sys.argv) == 1:
        print_app_info()
        return 0

    if sys.argv[1] == "--version":
        print_version_info()
        return 0

    if sys.argv[1] == "about":
        print_about_info()
        return 0

    if sys.argv[1] in {"check-data-source", "doctor"}:
        return run_data_source_doctor()

    if sys.argv[1] == "run-daily":
        return run_daily()

    print("用法:")
    print("python app.py")
    print("python app.py --version")
    print("python app.py about")
    print("python app.py check-data-source")
    print("python app.py doctor")
    print("python app.py run-daily")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
