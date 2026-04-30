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
from app_core.path_utils import get_project_root
from app_core.reports.daily_report import write_daily_report
from app_core.storage.file_store import ensure_directory, save_dataframe_csv
from app_core.strategies.ma_strategy import analyze_ma_signal


def print_app_info() -> None:
    settings = load_settings()
    project_root = get_project_root()
    current_time = datetime.now().isoformat(timespec="seconds")

    print(f"项目名称: {settings['project_name']}")
    print(f"英文名称: {settings['project_name_en']}")
    print(f"版本号: {settings['version']}")
    print(f"当前环境: {settings['environment']}")
    print(f"项目根目录: {project_root}")
    print(f"当前时间: {current_time}")
    print("提示: V0.1 dev skeleton is ready.")


def run_daily() -> int:
    logger = get_logger()
    try:
        settings = load_settings()
        watchlist_config = load_json("config/watchlist.json")
        run_started_at = datetime.now()
        generated_at = run_started_at.isoformat(timespec="seconds")
        report_date = run_started_at.strftime("%Y-%m-%d")
        timeout_seconds = int(settings.get("network", {}).get("request_timeout_seconds", 10))

        ensure_directory(settings["storage"]["raw_dir"])
        ensure_directory(settings["storage"]["processed_dir"])
        ensure_directory("reports/daily")
        ensure_directory(settings["storage"]["log_dir"])

        all_watchlist_items = watchlist_config.get("watchlist", [])
        enabled_items = [item for item in all_watchlist_items if item.get("enabled") is True]

        logger.info(
            "run-daily started with %s enabled symbols, request timeout=%ss",
            len(enabled_items),
            timeout_seconds,
        )

        records: list[dict[str, Any]] = []

        for item in enabled_items:
            code = str(item.get("code", "")).strip()
            name = item.get("name", "")
            logger.info("data collection started for %s %s", code, name)

            try:
                raw_dataframe, normalized_dataframe = fetch_stock_daily_history(
                    code,
                    timeout_seconds=timeout_seconds,
                )
                raw_path = save_dataframe_csv(
                    raw_dataframe,
                    Path(settings["storage"]["raw_dir"]) / f"{code}_daily_raw.csv",
                )

                strategy_result = analyze_ma_signal(normalized_dataframe)
                record = {
                    "date": strategy_result["date"],
                    "code": code,
                    "name": name,
                    "market": item.get("market", ""),
                    "industry": item.get("industry", ""),
                    "close": strategy_result["close"],
                    "ma5": strategy_result["ma5"],
                    "ma20": strategy_result["ma20"],
                    "signal": strategy_result["signal"],
                    "reason": strategy_result["reason"],
                    "data_status": strategy_result["data_status"],
                    "error_message": strategy_result["error_message"],
                    "raw_file": str(raw_path.relative_to(get_project_root())),
                }
                records.append(record)
                logger.info("data collection succeeded for %s %s", code, name)
            except KeyboardInterrupt:
                raise
            except Exception as error:  # pragma: no cover - network/runtime branch
                message = summarize_fetch_error(error, timeout_seconds=timeout_seconds)
                records.append(
                    {
                        "date": "",
                        "code": code,
                        "name": name,
                        "market": item.get("market", ""),
                        "industry": item.get("industry", ""),
                        "close": None,
                        "ma5": None,
                        "ma20": None,
                        "signal": "neutral",
                        "reason": "数据采集失败",
                        "data_status": "fetch_failed",
                        "error_message": message,
                        "raw_file": "",
                    }
                )
                logger.exception("data collection failed for %s %s: %s", code, name, message)

        processed_dataframe = pd.DataFrame(
            records,
            columns=[
                "date",
                "code",
                "name",
                "market",
                "industry",
                "close",
                "ma5",
                "ma20",
                "signal",
                "reason",
                "data_status",
                "error_message",
            ],
        )

        processed_path = save_dataframe_csv(
            processed_dataframe,
            Path(settings["storage"]["processed_dir"]) / "daily_signals.csv",
        )
        report_path = write_daily_report(
            records,
            report_date=report_date,
            generated_at=generated_at,
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


def main() -> int:
    if len(sys.argv) == 1:
        print_app_info()
        return 0

    if sys.argv[1] == "run-daily":
        return run_daily()

    print("用法:")
    print("python app.py")
    print("python app.py run-daily")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
