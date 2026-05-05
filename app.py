from __future__ import annotations

import sys
import json
import os
from getpass import getpass
from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd

from app_core.app_logger import get_logger
from app_core.analytics.dashboard_summary import (
    build_dashboard_summary,
    write_dashboard_summary_json,
)
from app_core.analytics.review_queue import build_review_queue, write_review_queue_outputs
from app_core.analytics.ui_snapshot import build_ui_snapshot, write_ui_snapshot_json
from app_core.analytics.ui_snapshot_schema import (
    validate_ui_snapshot,
    write_sample_ui_snapshot,
    write_ui_snapshot_contract,
)
from app_core.analytics.history_summary import build_signal_change_summary
from app_core.config_loader import load_json, load_settings
from app_core.data_sources.akshare_provider import (
    summarize_fetch_error,
)
from app_core.data_sources.international_news import get_international_news_fetcher
from app_core.data_sources.kline_provider import AkShareKlineProvider
from app_core.data_sources.longbridge_quote_provider import LongbridgeQuoteProvider
from app_core.data_sources.longbridge_sdk_support import (
    fetch_longbridge_quote_via_oauth,
    inspect_longbridge_sdk,
    start_longbridge_oauth,
)
from app_core.data_sources.realtime_quote_provider import AkShareRealtimeQuoteProvider
from app_core.data_sources.manager import DataSourceManager
from app_core.data_sources.index_provider import fetch_index_daily_history
from app_core.data_sources.sector_provider import fetch_sector_board_daily_history
from app_core.diagnostics.data_source_health import run_data_source_health_check
from app_core.market_indices import (
    get_enabled_market_indices,
    load_market_indices,
)
from app_core.sector_boards import (
    get_enabled_sector_boards,
    load_sector_board_items,
    load_sector_boards,
)
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
from app_core.security.local_secret_manager import LocalSecretManager
from app_core.security.longbridge_oauth_store import LongbridgeOAuthStore
from app_core.reports.daily_report import write_daily_report
from app_core.storage.file_store import ensure_directory, save_dataframe_csv
from app_core.storage.sqlite_store import (
    get_latest_runs,
    insert_run_daily_snapshot,
)
from app_core.strategies.ma_strategy import analyze_ma_signal
from app_core.watchlist import get_enabled_watchlist, load_watchlist_items, tags_to_csv_value


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
    print("提示: V0.7.2 Data Source Status UI is ready.")


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


def run_history() -> int:
    """打印最近的运行历史"""
    runs = get_latest_runs(limit=10)
    if not runs:
        print("未发现历史运行记录。")
        return 0

    print(f"{'id':<4} | {'run_date':<10} | {'status':<7} | {'index':<5} | {'sector':<6} | {'stock':<5} | {'report_path'}")
    print("-" * 100)
    for run in runs:
        print(
            f"{run['id']:<4} | "
            f"{run['run_date']:<10} | "
            f"{run['status']:<7} | "
            f"{run['index_count']:<5} | "
            f"{run['sector_count']:<6} | "
            f"{run['stock_count']:<5} | "
            f"{run['report_path']}"
        )
    return 0


def run_changes() -> int:
    """打印信号变化摘要"""
    try:
        summary = build_signal_change_summary()
        latest_id = summary["latest_run_id"]
        prev_id = summary["previous_run_id"]

        if latest_id is None:
            print("未发现运行记录。")
            return 0

        print("\nA股智研台｜信号变化摘要")
        print(f"latest_run_id: {latest_id}")
        print(f"previous_run_id: {prev_id if prev_id else 'None'}")

        if prev_id is None:
            print("\n当前只有 1 次运行记录，暂无可比较的上一轮快照。")
        
        stats = summary["summary"]
        print(f"\n[统计]")
        print(f"指数变化: {stats['index_change_count']}")
        print(f"板块变化: {stats['sector_change_count']}")
        print(f"自选股变化: {stats['stock_change_count']}")
        print(f"风险/异常项: {stats['risk_item_count']}")

        def _print_changes(title: str, changes: list[dict], limit: int = 10):
            if not changes:
                return
            print(f"\n[{title}]")
            for item in changes[:limit]:
                if item["change_type"] == "new_asset":
                    print(f"- {item['name']}: [新资产] -> {item['latest_signal']}")
                elif item["change_type"] == "missing_asset":
                    print(f"- {item['name']}: [已移除] (原: {item['previous_signal']})")
                else:
                    print(f"- {item['name']}: {item['previous_signal']} -> {item['latest_signal']}")
            if len(changes) > limit:
                print(f"  ... 还有 {len(changes) - limit} 项未列出")

        _print_changes("指数变化", summary["index_changes"])
        _print_changes("行业/板块变化", summary["sector_changes"])
        _print_changes("自选股变化", summary["stock_changes"])

        if summary["risk_items"]:
            print(f"\n[风险/异常项]")
            for item in summary["risk_items"][:10]:
                print(f"- {item['name']}: {item['latest_data_status']}")
            if len(summary["risk_items"]) > 10:
                print(f"  ... 还有 {len(summary['risk_items']) - 10} 项未列出")
        
        print("")
        return 0
    except Exception as e:
        print(f"查询变化摘要失败: {e}")
        return 1


def run_dashboard_summary() -> int:
    """打印 Dashboard 摘要并生成 JSON"""
    try:
        summary = build_dashboard_summary()
        latest = summary.get("latest_run")
        
        if not latest:
            print(summary.get("message", "未发现运行记录。"))
            return 0

        print("\nA股智研台｜Dashboard 摘要")
        print(f"最新运行: {latest['run_date']} / {latest['status']}")
        print(f"指数: {latest['index_count']}")
        print(f"行业/板块: {latest['sector_count']}")
        print(f"自选股: {latest['stock_count']}")
        
        health = summary["data_health"]
        print(f"数据异常: {health['risk_item_count']}")
        
        changes = summary["changes"]
        print(f"信号变化: 指数 {changes['index_change_count']} / 板块 {changes['sector_change_count']} / 自选股 {changes['stock_change_count']}")
        
        json_path = write_dashboard_summary_json()
        print(f"摘要文件: {json_path.relative_to(get_project_root())}")
        print("")
        
        return 0
    except Exception as e:
        print(f"生成 Dashboard 摘要失败: {e}")
        return 1


def run_review_queue() -> int:
    """打印每日关注队列并生成文件"""
    try:
        queue = build_review_queue()
        if not queue:
            print("未发现运行记录，无法构建关注队列。")
            return 0

        print("\nA股智研台｜每日关注队列")
        print(f"关注项数量: {len(queue)}")
        
        severity_counts = {
            "high": sum(1 for item in queue if item["severity"] == "high"),
            "medium": sum(1 for item in queue if item["severity"] == "medium"),
            "low": sum(1 for item in queue if item["severity"] == "low"),
        }
        print(f"高优先级: {severity_counts['high']}")
        print(f"中优先级: {severity_counts['medium']}")
        print(f"低优先级: {severity_counts['low']}")

        print("\n[Top 10]")
        for item in queue[:10]:
            print(f"{item['rank']}. [{item['asset_type']}] {item['name']} / {item['symbol']} / {item['category']} / {item['severity']}")
            print(f"   原因：{item['reason']}")
            print(f"   动作：{item['suggested_action']}")

        outputs = write_review_queue_outputs()
        print(f"\n输出文件:")
        print(f"- {Path(outputs['json_path']).relative_to(get_project_root())}")
        print(f"- {Path(outputs['csv_path']).relative_to(get_project_root())}")
        print("")
        
        return 0
    except Exception as e:
        print(f"构建每日关注队列失败: {e}")
        return 1


def run_ui_snapshot() -> int:
    """打印 UI 快照摘要并生成 JSON"""
    try:
        snapshot = build_ui_snapshot()
        latest = snapshot.get("latest_run")
        
        if not latest:
            if snapshot.get("messages"):
                print(snapshot["messages"][0])
            else:
                print("未发现运行记录，无法构建 UI 快照。")
            return 0

        print("\nA股智研台｜UI 数据快照")
        print(f"最新运行: {latest['run_date']} / {latest['status']}")
        
        dashboard = snapshot["dashboard_summary"]
        print(f"Dashboard 摘要: 已生成")
        
        queue = snapshot["review_queue"]
        print(f"每日关注队列: {queue['count']} 项")
        
        changes = snapshot["signal_changes"]["summary"]
        print(f"信号变化: 板块 {changes['sector_change_count']} / 自选股 {changes['stock_change_count']} / 指数 {changes['index_change_count']}")
        
        json_path = write_ui_snapshot_json()
        print(f"快照文件: {json_path.relative_to(get_project_root())}")
        print("")
        
        return 0
    except Exception as e:
        print(f"生成 UI 快照失败: {e}")
        return 1


def run_validate_snapshot() -> int:
    """校验 UI 快照结构"""
    try:
        snapshot_path = get_project_root() / "data" / "processed" / "ui_snapshot.json"
        snapshot = None
        
        if snapshot_path.exists():
            with open(snapshot_path, "r", encoding="utf-8") as f:
                snapshot = json.load(f)
        else:
            print("未发现现有快照文件，正在临时构建...")
            snapshot = build_ui_snapshot()
            
        result = validate_ui_snapshot(snapshot)
        
        print("\nA股智研台｜UI 快照结构校验")
        print(f"校验结果: {'通过' if result['is_valid'] else '失败'}")
        print(f"错误: {result['error_count']}")
        print(f"警告: {result['warning_count']}")
        
        if result["errors"]:
            print("\n[错误详情]")
            for err in result["errors"][:10]:
                print(f"- {err}")
                
        if result["warnings"]:
            print("\n[警告详情]")
            for warn in result["warnings"][:10]:
                print(f"- {warn}")
        
        print("")
        return 0 if result["is_valid"] else 1
    except Exception as e:
        print(f"快照校验过程异常: {e}")
        return 1


def run_export_frontend_contract() -> int:
    """导出前端契约与示例快照"""
    try:
        contract_path = write_ui_snapshot_contract()
        sample_path = write_sample_ui_snapshot()
        
        print("\nA股智研台｜前端契约导出")
        print(f"契约文件: {contract_path.relative_to(get_project_root())}")
        print(f"示例快照: {sample_path.relative_to(get_project_root())}")
        print("")
        return 0
    except Exception as e:
        print(f"导出契约失败: {e}")
        return 1


def run_sync_frontend_snapshot() -> int:
    """同步后端快照到前端静态目录"""
    try:
        root = get_project_root()
        source_path = root / "data" / "processed" / "ui_snapshot.json"
        target_dir = root / "frontend-react" / "src" / "data"
        target_path = target_dir / "snapshot.json"

        # 1. 确保目录存在
        ensure_directory(target_dir)

        # 2. 检查源文件，不存在则生成
        if not source_path.exists():
            print(f"源快照不存在，正在尝试生成: {source_path.relative_to(root)}")
            write_ui_snapshot_json()
        
        if not source_path.exists():
            print("错误: 无法生成后端快照文件。请先运行 python3 app.py run-daily。")
            return 1

        # 3. 复制文件并输出详细信息
        with open(source_path, "r", encoding="utf-8") as f_src:
            data = json.load(f_src)
        
        with open(target_path, "w", encoding="utf-8") as f_target:
            json.dump(data, f_target, ensure_ascii=False, indent=2)

        generated_at = data.get("generated_at", "未知")
        latest_run = data.get("latest_run", {})
        run_date = latest_run.get("run_date", "未知")
        status = latest_run.get("status", "未知")

        print("\nA股智研台｜前端快照同步成功")
        print(f"源路径: {source_path.relative_to(root)}")
        print(f"目标路径: {target_path.relative_to(root)}")
        print(f"生成时间: {generated_at}")
        print(f"最近运行: {run_date} ({status})")
        print("")
        return 0
    except Exception as e:
        print(f"同步失败: {e}")
        return 1


def run_international_news_cli(argv: list[str]) -> int:
    """打印国际新闻抓取结果，不写文件。"""
    try:
        ticker = _get_cli_option(argv, "--ticker", required=True)
        market = _get_cli_option(argv, "--market", default="US")
        hours = int(_get_cli_option(argv, "--hours", default="72"))
        limit = int(_get_cli_option(argv, "--limit", default="3"))
    except ValueError as error:
        print(str(error))
        print("用法: python3 app.py international-news --ticker AAPL --market US --hours 72 --limit 3")
        return 1

    fetcher = get_international_news_fetcher()
    # 自动加载本地环境变量
    LocalSecretManager.load_local_env_to_process_env()

    if not fetcher.is_configured():
        print("未配置 MARKETAUX_API_TOKEN，请先在终端设置环境变量。")
        return 1

    news_items = fetcher.fetch_news(
        ticker=ticker,
        market=market,
        hours_ago=hours,
        limit=limit,
    )

    print(f"国际新闻数量: {len(news_items)}")
    if not news_items:
        print("未获取到相关新闻，可能是代码格式、市场覆盖范围、时间窗口或免费计划限制导致。")
        return 0

    for index, item in enumerate(news_items, start=1):
        print(f"\n[{index}] {item.get('title', '')}")
        print(f"发布时间: {item.get('published_at', '') or '-'}")
        print(
            "情绪: "
            f"{item.get('sentiment', '') or '-'} / "
            f"{item.get('sentiment_score') if item.get('sentiment_score') is not None else '-'}"
        )
        print(f"来源: {item.get('source', '') or '-'}")
        print(f"链接: {item.get('url', '') or '-'}")

    return 0


def run_marketaux_status() -> int:
    """安全检查 Marketaux token 是否已配置，不访问外部 API。"""
    # 自动加载本地环境变量
    LocalSecretManager.load_local_env_to_process_env()

    raw_token = os.getenv("MARKETAUX_API_TOKEN", "").strip()
    if not raw_token:
        print("Marketaux 配置状态: 未配置")
        print('设置方式: export MARKETAUX_API_TOKEN="你的 token"')
        return 0

    masked_token = _mask_token(raw_token)
    print("Marketaux 配置状态: 已配置")
    print(f"Token 显示: {masked_token}")
    print("国际新闻 CLI: 可用")
    return 0


def run_quote_cli(argv: list[str]) -> int:
    """打印实时行情快照，不写文件。"""
    try:
        symbol = _get_cli_option(argv, "--symbol", required=True)
        market = _get_cli_option(argv, "--market", default="CN")
    except ValueError as error:
        print(str(error))
        print("用法: python3 app.py quote --symbol 600519 --market CN")
        return 1

    provider = AkShareRealtimeQuoteProvider()
    quote = provider.fetch_quote(symbol=symbol, market=market)

    status = quote["data_status"]
    if status == "ok":
        print(f"股票代码: {quote['symbol']}")
        print(f"市场: {quote['market']}")
        print(f"名称: {quote['name']}")
        print(f"当前价: {quote['price']}")
        print(f"涨跌额: {quote['change']}")
        print(f"涨跌幅: {quote['pct_change']}%")
        print(f"成交量: {quote['volume']}")
        print(f"成交额: {quote['amount']}")
        print(f"更新时间: {quote['timestamp']}")
        print(f"数据状态: {status}")
        return 0
    elif status == "not_found":
        print(f"错误: 未找到股票代码 {symbol} (市场: {market})")
        return 0
    elif status == "unsupported_market":
        print(f"提示: 当前暂不支持市场 {market} 的实时行情，后续接入。")
        return 0
    else:
        print(f"错误: 抓取实时行情失败。状态: {status}")
        if quote["error_message"]:
            print(f"详情: {quote['error_message']}")
        return 0


def run_quote_batch_cli(argv: list[str]) -> int:
    """批量打印实时行情快照，不写文件。"""
    try:
        symbols_value = _get_cli_option(argv, "--symbols", required=True)
        market = _get_cli_option(argv, "--market", default="CN")
    except ValueError as error:
        print(str(error))
        print("用法: python3 app.py quote-batch --symbols 600519,300750,000001 --market CN")
        return 1

    symbols = [symbol.strip() for symbol in symbols_value.split(",") if symbol.strip()]
    if not symbols:
        print("参数错误: --symbols 不能为空")
        print("用法: python3 app.py quote-batch --symbols 600519,300750,000001 --market CN")
        return 1

    provider = AkShareRealtimeQuoteProvider()
    quotes = provider.fetch_quotes(symbols=symbols, market=market)

    status_counts = {
        "ok": 0,
        "not_found": 0,
        "fetch_failed": 0,
        "unsupported_market": 0,
    }

    for index, quote in enumerate(quotes, start=1):
        status = str(quote.get("data_status", "fetch_failed"))
        if status in status_counts:
            status_counts[status] += 1

        print(f"\n[{index}] 股票代码: {quote.get('symbol', '')}")
        print(f"名称: {quote.get('name', '') or '-'}")
        print(f"当前价: {quote.get('price')}")
        pct_change = quote.get("pct_change")
        print(f"涨跌幅: {pct_change if pct_change is not None else '-'}%")
        print(f"成交额: {quote.get('amount')}")
        print(f"数据状态: {status}")
        if status != "ok" and quote.get("error_message"):
            print(f"说明: {quote['error_message']}")

    print("\n[汇总]")
    print(f"查询数量: {len(quotes)}")
    print(f"ok 数量: {status_counts['ok']}")
    print(f"not_found 数量: {status_counts['not_found']}")
    print(f"fetch_failed 数量: {status_counts['fetch_failed']}")
    print(f"unsupported_market 数量: {status_counts['unsupported_market']}")
    return 0


def run_kline_cli(argv: list[str]) -> int:
    """打印 K 线摘要，不写文件。"""
    try:
        symbol = _get_cli_option(argv, "--symbol", required=True)
        market = _get_cli_option(argv, "--market", default="CN")
        period = _get_cli_option(argv, "--period", default="daily")
        adjust = _get_cli_option(argv, "--adjust", default="qfq")
        limit = int(_get_cli_option(argv, "--limit", default="20"))
    except ValueError as error:
        print(str(error))
        print("用法: python3 app.py kline --symbol 600519 --market CN --period daily --adjust qfq --limit 20")
        return 1

    provider = AkShareKlineProvider()
    result = provider.fetch_kline(
        symbol=symbol,
        market=market,
        period=period,
        adjust=adjust,
        limit=limit,
    )

    status = str(result.get("data_status", "fetch_failed"))
    rows = result.get("rows", [])

    print(f"股票代码: {result.get('symbol', symbol)}")
    print(f"市场: {result.get('market', market)}")
    print(f"周期: {result.get('period', period)}")
    print(f"复权方式: {result.get('adjust', adjust)}")
    print(f"数据状态: {status}")
    print(f"行数: {len(rows)}")

    if status == "ok":
        print("\n[最近 5 条 K线摘要]")
        for item in rows[-5:]:
            print(
                f"{item.get('date', '-') } / "
                f"open={item.get('open')} / "
                f"high={item.get('high')} / "
                f"low={item.get('low')} / "
                f"close={item.get('close')} / "
                f"volume={item.get('volume')}"
            )
        return 0

    if status == "unsupported_market":
        print(f"提示: 当前暂不支持市场 {market} 的 K线数据，后续接入。")
        return 0

    if status == "unsupported_period":
        print(f"提示: 当前暂不支持周期 {period}。")
        return 0

    if status == "not_found":
        print(f"提示: 未找到 {symbol} 的 K线数据。")
        return 0

    print("错误: 抓取 K线数据失败。")
    if result.get("error_message"):
        print(f"详情: {result['error_message']}")
    return 0


def run_longbridge_status() -> int:
    # 自动加载本地环境变量
    LocalSecretManager.load_local_env_to_process_env()

    provider = LongbridgeQuoteProvider()
    status = provider.check_status()

    print("provider: longbridge")
    print(f"sdk_importable: {'yes' if status['sdk_importable'] else 'no'}")
    print(f"oauthbuilder_available: {'yes' if status['oauthbuilder_available'] else 'no'}")
    print("auth:")
    print(f"- legacy_api_key: {status['auth']['legacy_api_key']}")
    print(f"- oauth: {status['auth']['oauth']}")
    print(f"- auth_mode_candidate: {status['auth']['auth_mode_candidate']}")
    print(f"- oauthbuilder: {status['auth']['oauthbuilder']}")
    print("env:")
    for key, value in status["env"].items():
        print(f"- {key}: {value}")
    print("local_oauth:")
    print(f"- token_file: {status['local_oauth']['token_file']}")
    print(f"- access_token: {status['local_oauth']['access_token']}")
    print(f"- refresh_token: {status['local_oauth']['refresh_token']}")
    print(f"- expires_at: {status['local_oauth']['expires_at'] or '-'}")
    print(f"- masked: {status['local_oauth']['masked']}")
    print(f"- sdk_managed: {str(status['local_oauth'].get('sdk_managed', False)).lower()}")
    print("optional_env:")
    for key, value in status["optional_env"].items():
        print(f"- {key}: {value}")
    print("safety:")
    print(f"- quote_only: {str(status['safety']['quote_only']).lower()}")
    print(f"- trade_enabled: {str(status['safety']['trade_enabled']).lower()}")
    return 0


def run_longbridge_oauth_status() -> int:
    store = LongbridgeOAuthStore()
    status = store.get_oauth_token_status()

    print("provider: longbridge")
    print("auth_type: oauth2")
    print(f"token_file: {status['token_file']}")
    print(f"access_token: {status['access_token']}")
    print(f"refresh_token: {status['refresh_token']}")
    print(f"has_refresh_token: {str(status['has_refresh_token']).lower()}")
    print(f"expires_at: {status['expires_at'] or '-'}")
    print(f"updated_at: {status['updated_at'] or '-'}")
    print(f"status: {status['status']}")
    print(f"masked: {status['masked_access_token']}")
    print(f"sdk_managed: {str(status.get('sdk_managed', False)).lower()}")
    print(f"scope: {status.get('scope', 'quote')}")
    print("quote_only: true")
    print("trade_enabled: false")
    return 0


def run_longbridge_sdk_status() -> int:
    sdk_status = inspect_longbridge_sdk()
    trade_label = "Trade" + "Context"

    print("provider: longbridge")
    print(f"sdk_importable: {'yes' if sdk_status['sdk_importable'] else 'no'}")
    print(f"sdk_version: {sdk_status['sdk_version']}")
    print("available_symbols:")
    print(f"- Config: {'yes' if sdk_status['available_symbols']['Config'] else 'no'}")
    print(f"- QuoteContext: {'yes' if sdk_status['available_symbols']['QuoteContext'] else 'no'}")
    print(f"- OAuthBuilder: {'yes' if sdk_status['available_symbols']['OAuthBuilder'] else 'no'}")
    print(f"- {trade_label}: ignored")
    print("safety:")
    print("- quote_only: true")
    print("- trade_enabled: false")
    if sdk_status.get("error_message"):
        print(f"message: {sdk_status['error_message']}")
    return 0


def run_longbridge_oauth_help() -> int:
    print("Longbridge OAuth 2.0 只读行情说明")
    print("- 当前长桥后台未提供 legacy Access Token 时，需要 OAuth 2.0。")
    print("- 本项目只使用只读行情，不接交易、不读资产、不读持仓。")
    print("- 官方 Python SDK 示例链路为 OAuthBuilder -> Config.from_oauth -> QuoteContext。")
    print("- 本项目将使用 OAuthBuilder 生成授权 URL，并由用户手动在浏览器完成授权。")
    print("- 授权成功后，SDK 可能自动缓存 token，具体以 SDK 实际行为为准。")
    print("- 本项目本轮只验证 QuoteContext，不验证任何交易能力。")
    print("- quote_only: true / trade_enabled: false")
    print("- OAuth Token 将保存到 .secrets/longbridge_oauth_token.json。")
    print("- .secrets/ 已加入 .gitignore，不应提交到 Git。")
    print("- 后续授权流程将根据官方 SDK / OAuthBuilder 实现授权链接与回调换 token。")
    print("- 暂时不要把 token 发到聊天窗口、日志或提交记录中。")
    print("- 可先执行 python3 app.py longbridge-oauth-status 查看本地状态。")
    print("- 可执行 python3 app.py longbridge-oauth-start 研究真实授权启动链路。")
    print("- 已知问题: 如果授权页显示 Authorization Failed / internal_server_error，说明请求已到达 Longbridge OAuth 授权服务端。")
    print("- 优先排查: OAuth client 是否启用、App Key 是否等同 OAuth client_id、redirect_uri 是否需要登记。")
    print("- 继续排查: 当前账号/地区/行情权限是否支持 OAuthBuilder，或 Longbridge OAuth 服务端是否存在临时异常。")
    print("- 不要发送 App Secret / Token / 完整授权 URL；可向支持方提供脱敏诊断摘要。")
    return 0


def run_longbridge_oauth_start() -> int:
    LocalSecretManager.load_local_env_to_process_env()
    client_id = os.getenv("LONGBRIDGE_APP_KEY", "").strip()
    store = LongbridgeOAuthStore()
    result = start_longbridge_oauth(client_id=client_id, store=store)
    sdk_status = inspect_longbridge_sdk()

    print("provider: longbridge")
    print(f"oauth: {result['status']}")
    diagnostics = result.get("diagnostics")
    if diagnostics:
        print(f"error_type: {diagnostics['error_type']}")
        print(f"likely_stage: {diagnostics['likely_stage']}")
        print(f"sdk_importable: {'yes' if diagnostics['sdk_importable'] else 'no'}")
        print(f"sdk_version: {diagnostics['sdk_version']}")
        print(f"client_id_present: {str(diagnostics['client_id_present']).lower()}")
        print(f"redirect_uri_host: {diagnostics['redirect_uri_host']}")
        print(f"redirect_uri_scheme: {diagnostics['redirect_uri_scheme']}")
        print("quote_only: true")
        print("trade_enabled: false")
        print("next_steps:")
        for item in diagnostics["next_steps"]:
            print(f"- {item}")
    else:
        print(f"sdk_importable: {'yes' if sdk_status['sdk_importable'] else 'no'}")
        print(f"sdk_version: {sdk_status['sdk_version']}")
        print(f"client_id_present: {str(bool(client_id)).lower()}")
        print(f"sdk_token_cache: {result.get('sdk_token_cache', 'unknown')}")
        print("quote_only: true")
        print("trade_enabled: false")
    if result.get("message"):
        print(f"message: {result['message']}")
    return 0


def run_longbridge_oauth_set() -> int:
    store = LongbridgeOAuthStore()
    try:
        access_token = getpass("请输入 Longbridge OAuth access_token: ").strip()
        refresh_token = getpass("请输入 Longbridge OAuth refresh_token（可留空）: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("已取消设置。")
        return 130

    if not access_token:
        print("access_token 不能为空。")
        return 1

    expires_at = input("请输入 expires_at（ISO8601，可留空）: ").strip()
    scope = input("请输入 scope（默认 quote，可留空）: ").strip() or "quote"

    status = store.save_oauth_token(
        {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "expires_at": expires_at,
            "scope": scope,
            "note": "quote only",
        }
    )

    print("provider: longbridge")
    print(f"status: {status['status']}")
    print(f"masked: {status['masked_access_token']}")
    print(f"expires_at: {status['expires_at'] or '-'}")
    print(f"has_refresh_token: {str(status['has_refresh_token']).lower()}")
    print("quote_only: true")
    print("trade_enabled: false")
    return 0


def run_longbridge_oauth_clear() -> int:
    first_confirm = input("确认清空 Longbridge OAuth Token 吗？输入 YES 继续: ").strip()
    if first_confirm != "YES":
        print("已取消清空。")
        return 1
    second_confirm = input("再次确认清空 Longbridge OAuth Token，输入 YES 继续: ").strip()
    if second_confirm != "YES":
        print("已取消清空。")
        return 1

    store = LongbridgeOAuthStore()
    store.clear_oauth_token()
    print("provider: longbridge")
    print("status: cleared")
    print("quote_only: true")
    print("trade_enabled: false")
    return 0


def run_longbridge_oauth_quote(argv: list[str]) -> int:
    try:
        symbol = _get_cli_option(argv, "--symbol", required=True)
        market = _get_cli_option(argv, "--market", default="CN")
    except ValueError as error:
        print(str(error))
        print("用法: python3 app.py longbridge-oauth-quote --symbol 600519 --market CN")
        return 1

    LocalSecretManager.load_local_env_to_process_env()
    if market.upper() != "CN":
        print(f"提示: 当前暂不支持市场 {market} 的 Longbridge OAuthBuilder 行情研究。")
        return 0

    provider = LongbridgeQuoteProvider()
    raw_symbol = provider._to_longbridge_symbol(symbol, market)
    if raw_symbol is None:
        print(f"提示: 股票代码格式不支持: {symbol}")
        return 0

    client_id = os.getenv("LONGBRIDGE_APP_KEY", "").strip()
    store = LongbridgeOAuthStore()
    result = fetch_longbridge_quote_via_oauth(
        client_id=client_id,
        symbol=symbol,
        raw_symbol=raw_symbol,
        store=store,
    )

    status = str(result.get("data_status", "quote_failed"))
    if status == "ok":
        print(f"股票代码: {result.get('symbol', symbol)} / {result.get('raw_symbol', raw_symbol)}")
        print(f"名称: {result.get('name', '')}")
        print(f"当前价: {result.get('current_price')}")
        print(f"涨跌额: {result.get('change')}")
        print(f"涨跌幅: {result.get('change_percent')}")
        print(f"更新时间: {result.get('timestamp')}")
        print(f"数据状态: {status}")
        print("quote_only: true")
        print("trade_enabled: false")
        return 0

    print(f"数据状态: {status}")
    if result.get("message"):
        print(f"message: {result['message']}")
    if result.get("error_message"):
        print(f"详情: {result['error_message']}")
    print("quote_only: true")
    print("trade_enabled: false")
    return 0


def run_longbridge_quote_cli(argv: list[str]) -> int:
    try:
        symbol = _get_cli_option(argv, "--symbol", required=True)
        market = _get_cli_option(argv, "--market", default="CN")
    except ValueError as error:
        print(str(error))
        print("用法: python3 app.py longbridge-quote --symbol 600519 --market CN")
        return 1

    # 自动加载本地环境变量
    LocalSecretManager.load_local_env_to_process_env()

    provider = LongbridgeQuoteProvider()
    quote = provider.fetch_quote(symbol=symbol, market=market)

    status = quote.get("data_status", "fetch_failed")
    if status == "ok":
        print(f"股票代码: {quote.get('symbol', '')} / {quote.get('raw_symbol', '')}")
        print(f"市场: {quote.get('market', '')}")
        print(f"名称: {quote.get('name', '')}")
        print(f"当前价: {quote.get('current_price')}")
        print(f"涨跌幅: {quote.get('change_percent')}")
        print(f"更新时间: {quote.get('timestamp')}")
        print(f"数据状态: {status}")
        return 0

    if status == "missing_env":
        print("提示: 缺少环境变量，请配置 LONGBRIDGE_APP_KEY/SECRET/ACCESS_TOKEN。")
        return 0
    if status == "oauth_required":
        print("提示: 当前账号未提供 legacy Access Token，请执行 longbridge-oauth-help。")
        if quote.get("error_message"):
            print(f"详情: {quote['error_message']}")
        return 0
    if status == "oauthbuilder_required":
        print("提示: 请先执行 longbridge-oauth-start 或 longbridge-oauth-help。")
        if quote.get("error_message"):
            print(f"详情: {quote['error_message']}")
        return 0
    if status == "sdk_missing":
        print("提示: 长桥 SDK 未安装或不可导入，当前返回 sdk_missing。")
        return 0
    if status == "unsupported_market":
        print(f"提示: 当前暂不支持市场 {market} 的长桥行情。")
        return 0
    if status == "unsupported_symbol":
        print(f"提示: 股票代码格式不支持: {symbol}")
        return 0
    if status == "not_found":
        print(f"提示: 未找到 {symbol} 的长桥行情。")
        return 0

    print("错误: 长桥行情抓取失败。")
    if quote.get("error_message"):
        print(f"详情: {quote['error_message']}")
    return 0


def run_token_status() -> int:
    manager = LocalSecretManager()
    statuses = manager.get_secret_statuses()

    for item in statuses:
        print(f"\n[{item['provider']}]")
        print(f"Key: {item['key']}")
        print(f"显示名: {item['display_name']}")
        print(f"状态: {item['status']}")
        print(f"来源: {item['source']}")
        print(f"脱敏值: {item['masked']}")
        print(f"长度: {item['length']}")
        print(f"更新时间: {item['updated_at'] or '-'}")
        print(f"最近检测: {item['last_checked_at'] or '-'}")
        print(f"备注: {item['note']}")
    return 0


def run_token_set(argv: list[str]) -> int:
    try:
        key = _get_cli_option(argv, "--key", required=True)
    except ValueError as error:
        print(str(error))
        print("用法: python3 app.py token-set --key MARKETAUX_API_TOKEN")
        return 1

    manager = LocalSecretManager()
    try:
        first_value = getpass(f"请输入 {key}: ")
        second_value = getpass(f"请再次输入 {key}: ")
    except (EOFError, KeyboardInterrupt):
        print("已取消设置。")
        return 130

    if first_value != second_value:
        print("两次输入不一致，未保存。")
        return 1

    result = manager.set_secret(key, first_value)
    print(f"Key: {result['key']}")
    print(f"状态: {result['status']}")
    print(f"脱敏值: {result['masked']}")
    return 0


def run_token_clear(argv: list[str]) -> int:
    try:
        key = _get_cli_option(argv, "--key", required=True)
    except ValueError as error:
        print(str(error))
        print("用法: python3 app.py token-clear --key MARKETAUX_API_TOKEN")
        return 1

    first_confirm = input(f"确认清空 {key} 吗？输入 YES 继续: ").strip()
    if first_confirm != "YES":
        print("已取消清空。")
        return 1
    second_confirm = input(f"再次确认清空 {key}，输入 YES 继续: ").strip()
    if second_confirm != "YES":
        print("已取消清空。")
        return 1

    manager = LocalSecretManager()
    result = manager.clear_secret(key)
    print(f"Key: {result['key']}")
    print(f"状态: {result['status']}")
    print(f"脱敏值: {result['masked']}")
    return 0


def run_daily() -> int:
    logger = get_logger()
    try:
        settings = load_settings()
        data_source_manager = DataSourceManager(settings=settings)
        watchlist_config = load_json("config/watchlist.json")
        market_indices_config = load_market_indices("config/market_indices.json")
        sector_boards_config = load_sector_boards("config/sector_boards.json")

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

        # 1. 处理市场指数
        enabled_indices = get_enabled_market_indices(market_indices_config)
        logger.info("run-daily: processing %d market indices", len(enabled_indices))
        index_records: list[dict[str, Any]] = []

        for item in enabled_indices:
            symbol = item["symbol"]
            name = item["name"]
            fetch_time = datetime.now().isoformat(timespec="seconds")
            metadata = _build_index_metadata(item)

            try:
                raw_dataframe, normalized_dataframe = fetch_index_daily_history(
                    symbol, timeout_seconds=timeout_seconds
                )
                save_dataframe_csv(raw_dataframe, Path(raw_dir) / f"{symbol}_index_raw.csv")

                strategy_result = analyze_ma_signal(normalized_dataframe)
                record = {
                    **metadata,
                    "fetch_time": fetch_time,
                    "date": strategy_result["date"],
                    "close": strategy_result["close"],
                    "ma5": strategy_result["ma5"],
                    "ma20": strategy_result["ma20"],
                    "signal": strategy_result["signal"],
                    "signal_level": _determine_signal_level(
                        strategy_result["signal"], strategy_result["data_status"]
                    ),
                    "data_status": strategy_result["data_status"],
                    "error_message": strategy_result["error_message"],
                }
                index_records.append(record)
            except KeyboardInterrupt:
                raise
            except Exception as error:
                message = summarize_fetch_error(error, timeout_seconds=timeout_seconds)
                index_records.append(
                    {
                        **metadata,
                        "fetch_time": fetch_time,
                        "date": "",
                        "close": None,
                        "ma5": None,
                        "ma20": None,
                        "signal": "neutral",
                        "signal_level": "unavailable",
                        "data_status": "fetch_failed",
                        "error_message": message,
                    }
                )

        # 保存指数结果
        if index_records:
            index_df = pd.DataFrame(index_records)
            save_dataframe_csv(index_df, Path(processed_dir) / "index_signals.csv")

        # 2. 处理行业/板块
        enabled_sectors = get_enabled_sector_boards(sector_boards_config)
        logger.info("run-daily: processing %d sector boards", len(enabled_sectors))
        sector_records: list[dict[str, Any]] = []

        for item in enabled_sectors:
            symbol = item["symbol"]
            name = item["name"]
            board_type = item["board_type"]
            fetch_time = datetime.now().isoformat(timespec="seconds")
            metadata = _build_sector_metadata(item)

            try:
                raw_dataframe, normalized_dataframe = fetch_sector_board_daily_history(
                    symbol, board_type, timeout_seconds=timeout_seconds
                )
                save_dataframe_csv(raw_dataframe, Path(raw_dir) / f"{symbol}_{board_type}_raw.csv")

                strategy_result = analyze_ma_signal(normalized_dataframe)
                
                # 数据新鲜度校验
                data_status = strategy_result["data_status"]
                signal_level = _determine_signal_level(
                    strategy_result["signal"], data_status
                )
                error_message = strategy_result["error_message"]
                
                if data_status == "ok":
                    latest_date_str = strategy_result["date"]
                    if latest_date_str:
                        latest_date = datetime.strptime(latest_date_str, "%Y-%m-%d")
                        days_diff = (datetime.now() - latest_date).days
                        if days_diff > 30:
                            data_status = "stale_data"
                            signal_level = "warning"
                            error_message = f"latest board data is stale: {latest_date_str}"

                record = {
                    **metadata,
                    "fetch_time": fetch_time,
                    "date": strategy_result["date"],
                    "close": strategy_result["close"],
                    "ma5": strategy_result["ma5"],
                    "ma20": strategy_result["ma20"],
                    "signal": strategy_result["signal"],
                    "signal_level": signal_level,
                    "data_status": data_status,
                    "error_message": error_message,
                }
                sector_records.append(record)
            except KeyboardInterrupt:
                raise
            except Exception as error:
                message = summarize_fetch_error(error, timeout_seconds=timeout_seconds)
                sector_records.append(
                    {
                        **metadata,
                        "fetch_time": fetch_time,
                        "date": "",
                        "close": None,
                        "ma5": None,
                        "ma20": None,
                        "signal": "neutral",
                        "signal_level": "unavailable",
                        "data_status": "fetch_failed",
                        "error_message": message,
                    }
                )

        # 保存板块结果
        if sector_records:
            sector_df = pd.DataFrame(sector_records)
            save_dataframe_csv(sector_df, Path(processed_dir) / "sector_signals.csv")

        # 3. 处理自选股
        all_watchlist_items = load_watchlist_items(watchlist_config)
        enabled_items = get_enabled_watchlist(all_watchlist_items)

        logger.info(
            "run-daily: processing %d watchlist items",
            len(enabled_items),
        )

        watchlist_records: list[dict[str, Any]] = []

        for item in enabled_items:
            code = item["code"]
            name = item.get("name", "")
            fetch_time = datetime.now().isoformat(timespec="seconds")
            logger.info("data collection started for %s %s", code, name)
            metadata = _build_watchlist_metadata(item)

            try:
                fetch_result = data_source_manager.fetch_stock_daily_history(
                    code,
                    timeout_seconds=timeout_seconds,
                )
                if not fetch_result.ok:
                    raise RuntimeError(fetch_result.error_message)

                raw_dataframe = fetch_result.data["raw_dataframe"]
                normalized_dataframe = fetch_result.data["normalized_dataframe"]
                is_cache_fallback = fetch_result.source_name == "local_cache" and fetch_result.fallback_used

                if is_cache_fallback:
                    raw_relative_path = _to_relative_path(fetch_result.metadata.get("cache_path", ""))
                else:
                    raw_path = save_dataframe_csv(
                        raw_dataframe,
                        Path(raw_dir) / f"{code}_daily_raw.csv",
                    )
                    raw_relative_path = str(raw_path.relative_to(get_project_root()))

                strategy_result = analyze_ma_signal(normalized_dataframe)
                data_status = strategy_result["data_status"]
                error_message = strategy_result["error_message"]
                reason = strategy_result["reason"]
                latest_trade_date = strategy_result["date"]
                signal_level = _determine_signal_level(
                    strategy_result["signal"],
                    data_status,
                )

                if is_cache_fallback:
                    data_status = str(fetch_result.metadata.get("cache_status", "cache_fallback"))
                    error_message = (
                        f"在线数据源失败，使用本地缓存兜底：{fetch_result.metadata.get('primary_error_message', fetch_result.error_message)}"
                    )
                    reason = "使用本地缓存兜底完成信号计算"
                    signal_level = _determine_signal_level(strategy_result["signal"], data_status)
                    metadata["data_source"] = "local_cache"

                record = {
                    **metadata,
                    "fetch_time": fetch_time,
                    "date": strategy_result["date"],
                    "latest_trade_date": latest_trade_date,
                    "code": code,
                    "name": name,
                    "close": strategy_result["close"],
                    "ma5": strategy_result["ma5"],
                    "ma20": strategy_result["ma20"],
                    "signal": strategy_result["signal"],
                    "signal_level": signal_level,
                    "reason": reason,
                    "data_status": data_status,
                    "error_message": error_message,
                    "raw_file": raw_relative_path,
                    "raw_file_path": raw_relative_path,
                }
                watchlist_records.append(record)
                logger.info("data collection succeeded for %s %s", code, name)
            except KeyboardInterrupt:
                raise
            except Exception as error:  # pragma: no cover - network/runtime branch
                message = str(error)
                if not message:
                    message = summarize_fetch_error(error, timeout_seconds=timeout_seconds)
                watchlist_records.append(
                    {
                        **metadata,
                        "fetch_time": fetch_time,
                        "date": "",
                        "latest_trade_date": "",
                        "code": code,
                        "name": name,
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

        summary = summarize_run_daily_records(watchlist_records)
        processed_dataframe = pd.DataFrame(
            watchlist_records,
            columns=[
                "fetch_time",
                "date",
                "latest_trade_date",
                "code",
                "name",
                "market",
                "industry",
                "sector",
                "board",
                "tags",
                "priority",
                "position_status",
                "observe_reason",
                "risk_note",
                "data_source",
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
            watchlist_records,
            index_records=index_records,
            sector_records=sector_records,
            report_date=report_date,
            generated_at=generated_at,
            stage_name=f"V{VERSION} {STAGE}",
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

        # 4. 写入 SQLite 数据库 (V0.3.0)
        run_finished_at = datetime.now()
        run_metadata = {
            "run_date": report_date,
            "started_at": run_started_at.isoformat(timespec="seconds"),
            "finished_at": run_finished_at.isoformat(timespec="seconds"),
            "app_version": VERSION,
            "stage": STAGE,
            "status": "success",
            "index_count": len(index_records),
            "sector_count": len(sector_records),
            "stock_count": len(watchlist_records),
            "report_path": _to_relative_path(report_path),
            "processed_csv_path": _to_relative_path(processed_path),
            "log_path": _to_relative_path(log_path),
        }

        db_run_id = None
        try:
            db_result = insert_run_daily_snapshot(
                run_metadata=run_metadata,
                index_records=index_records,
                sector_records=sector_records,
                watchlist_records=watchlist_records,
            )
            db_run_id = db_result["run_id"]
            db_path = db_result["database_path"]
            logger.info("run-daily snapshot saved to SQLite: run_id=%s", db_run_id)
        except Exception as e:
            logger.warning("failed to save run-daily snapshot to SQLite: %s", str(e))
            print(f"数据库写入失败，但 CSV 与日报已生成: {e}")

        # 5. 生成信号变化摘要 CSV (V0.3.1)
        try:
            summary = build_signal_change_summary(latest_run_id=db_run_id)
            if summary["previous_run_id"]:
                all_changes = (
                    summary["index_changes"] + 
                    summary["sector_changes"] + 
                    summary["stock_changes"]
                )
                if all_changes:
                    changes_df = pd.DataFrame(all_changes)
                    changes_csv_path = Path(processed_dir) / "signal_changes.csv"
                    save_dataframe_csv(changes_df, changes_csv_path)
                    print(f"信号变化摘要已保存: {changes_csv_path}")
        except Exception as e:
            logger.warning("failed to generate signal changes csv: %s", str(e))

        # 6. 生成 Dashboard 摘要 JSON (V0.3.2)
        try:
            json_path = write_dashboard_summary_json()
            print(f"Dashboard 摘要已生成: {json_path}")
        except Exception as e:
            logger.warning("failed to generate dashboard summary json: %s", str(e))

        # 7. 生成每日关注队列 (V0.3.3)
        try:
            review_queue_outputs = write_review_queue_outputs()
            print(f"每日关注队列已生成: {review_queue_outputs['json_path']}")
        except Exception as e:
            logger.warning("failed to generate review queue outputs: %s", str(e))

        # 8. 生成 UI 数据快照 (V0.3.4)
        try:
            ui_snapshot_path = write_ui_snapshot_json()
            print(f"UI 数据快照已生成: {ui_snapshot_path}")
            
            # 校验快照结构 (V0.3.5)
            with open(ui_snapshot_path, "r", encoding="utf-8") as f:
                snapshot_data = json.load(f)
            val_res = validate_ui_snapshot(snapshot_data)
            if not val_res["is_valid"]:
                logger.warning("UI snapshot validation failed: %d errors", val_res["error_count"])
                print("UI 快照结构校验存在问题，请执行 python3 app.py validate-snapshot 查看详情")
        except Exception as e:
            logger.warning("failed to generate or validate ui snapshot json: %s", str(e))

        print("run-daily 执行完成")
        print(f"已处理指数数: {len(enabled_indices)}")
        print(f"已处理板块数: {len(enabled_sectors)}")
        print(f"已处理股票数: {len(enabled_items)}")
        print(f"处理后数据: {processed_path}")
        print(f"日报路径: {report_path}")
        if db_run_id:
            print(f"本地数据库: {db_path}")
            print(f"数据库写入: 已写入 run_id={db_run_id}")
        print("日志路径: logs/app.log")

        return 0
    except KeyboardInterrupt:
        logger.warning("run-daily interrupted by user")
        print("run-daily 已被用户中断")
        return 130


def summarize_run_daily_records(records: list[dict[str, Any]]) -> dict[str, int]:
    total_count = len(records)
    failed_count = sum(1 for record in records if record.get("data_status") == "fetch_failed")
    cache_fallback_count = sum(1 for record in records if record.get("data_status") == "cache_fallback")
    stale_cache_count = sum(1 for record in records if record.get("data_status") == "stale_cache")
    insufficient_data_count = sum(
        1 for record in records if record.get("data_status") == "insufficient_data"
    )
    trend_up_count = sum(1 for record in records if record.get("signal") == "trend_up")
    trend_down_count = sum(1 for record in records if record.get("signal") == "trend_down")
    neutral_count = sum(
        1
        for record in records
        if record.get("signal") == "neutral" and record.get("data_status") in {"ok", "cache_fallback", "stale_cache"}
    )
    online_success_count = sum(1 for record in records if record.get("data_status") == "ok")
    success_count = total_count - failed_count

    return {
        "total_count": total_count,
        "success_count": success_count,
        "online_success_count": online_success_count,
        "cache_fallback_count": cache_fallback_count,
        "stale_cache_count": stale_cache_count,
        "failed_count": failed_count,
        "trend_up_count": trend_up_count,
        "trend_down_count": trend_down_count,
        "neutral_count": neutral_count,
        "insufficient_data_count": insufficient_data_count,
    }


def _determine_signal_level(signal: str, data_status: str) -> str:
    if data_status in {"cache_fallback", "stale_cache"}:
        if signal == "trend_up":
            return "positive"
        if signal == "trend_down":
            return "negative"
        return "neutral"
    if data_status != "ok":
        return "unavailable"
    if signal == "trend_up":
        return "positive"
    if signal == "trend_down":
        return "negative"
    return "neutral"


def _build_index_metadata(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "symbol": item.get("symbol", ""),
        "name": item.get("name", ""),
        "category": item.get("category", ""),
    }


def _build_sector_metadata(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "symbol": item.get("symbol", ""),
        "name": item.get("name", ""),
        "board_type": item.get("board_type", ""),
        "category": item.get("category", ""),
        "priority": item.get("priority", ""),
        "observe_reason": item.get("observe_reason", ""),
        "risk_note": item.get("risk_note", ""),
    }


def _build_watchlist_metadata(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "market": item.get("market", ""),
        "industry": item.get("industry", ""),
        "sector": item.get("sector", ""),
        "board": item.get("board", ""),
        "tags": tags_to_csv_value(item.get("tags", [])),
        "priority": item.get("priority", ""),
        "position_status": item.get("position_status", ""),
        "observe_reason": item.get("observe_reason", ""),
        "risk_note": item.get("risk_note", ""),
        "data_source": item.get("data_source", ""),
    }


def _to_relative_path(path: str | Path) -> str:
    path_object = Path(path)
    if path_object.is_absolute():
        return str(path_object.relative_to(get_project_root()))
    return str(path_object)


def _get_cli_option(
    argv: list[str],
    option_name: str,
    *,
    default: str | None = None,
    required: bool = False,
) -> str:
    if option_name in argv:
        option_index = argv.index(option_name)
        next_index = option_index + 1
        if next_index >= len(argv) or argv[next_index].startswith("--"):
            raise ValueError(f"参数缺失: {option_name}")
        return argv[next_index]
    if required:
        raise ValueError(f"缺少必填参数: {option_name}")
    return default or ""


def _mask_token(token: str) -> str:
    normalized_token = str(token).strip()
    if len(normalized_token) <= 4:
        return "****"
    return f"****{normalized_token[-4:]}"


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

    if sys.argv[1] == "history":
        return run_history()

    if sys.argv[1] == "changes":
        return run_changes()

    if sys.argv[1] == "dashboard-summary":
        return run_dashboard_summary()

    if sys.argv[1] == "review-queue":
        return run_review_queue()

    if sys.argv[1] == "ui-snapshot":
        return run_ui_snapshot()

    if sys.argv[1] == "validate-snapshot":
        return run_validate_snapshot()

    if sys.argv[1] == "export-frontend-contract":
        return run_export_frontend_contract()

    if sys.argv[1] == "sync-frontend-snapshot":
        return run_sync_frontend_snapshot()

    if sys.argv[1] == "international-news":
        return run_international_news_cli(sys.argv[2:])

    if sys.argv[1] == "marketaux-status":
        return run_marketaux_status()

    if sys.argv[1] == "quote":
        return run_quote_cli(sys.argv[2:])

    if sys.argv[1] == "quote-batch":
        return run_quote_batch_cli(sys.argv[2:])

    if sys.argv[1] == "kline":
        return run_kline_cli(sys.argv[2:])

    if sys.argv[1] == "longbridge-status":
        return run_longbridge_status()

    if sys.argv[1] == "longbridge-sdk-status":
        return run_longbridge_sdk_status()

    if sys.argv[1] == "longbridge-oauth-status":
        return run_longbridge_oauth_status()

    if sys.argv[1] == "longbridge-oauth-help":
        return run_longbridge_oauth_help()

    if sys.argv[1] == "longbridge-oauth-set":
        return run_longbridge_oauth_set()

    if sys.argv[1] == "longbridge-oauth-clear":
        return run_longbridge_oauth_clear()

    if sys.argv[1] == "longbridge-oauth-start":
        return run_longbridge_oauth_start()

    if sys.argv[1] == "longbridge-oauth-quote":
        return run_longbridge_oauth_quote(sys.argv[2:])

    if sys.argv[1] == "longbridge-quote":
        return run_longbridge_quote_cli(sys.argv[2:])

    if sys.argv[1] == "token-status":
        return run_token_status()

    if sys.argv[1] == "token-set":
        return run_token_set(sys.argv[2:])

    if sys.argv[1] == "token-clear":
        return run_token_clear(sys.argv[2:])

    print("用法:")
    print("python app.py")
    print("python app.py --version")
    print("python app.py about")
    print("python app.py check-data-source")
    print("python app.py doctor")
    print("python app.py run-daily")
    print("python app.py history")
    print("python app.py changes")
    print("python app.py dashboard-summary")
    print("python app.py review-queue")
    print("python app.py ui-snapshot")
    print("python app.py validate-snapshot")
    print("python app.py export-frontend-contract")
    print("python app.py sync-frontend-snapshot")
    print("python app.py international-news --ticker AAPL --market US --hours 72 --limit 3")
    print("python app.py marketaux-status")
    print("python app.py quote --symbol 600519 --market CN")
    print("python app.py quote-batch --symbols 600519,300750,000001 --market CN")
    print("python app.py kline --symbol 600519 --market CN --period daily --adjust qfq --limit 20")
    print("python app.py longbridge-status")
    print("python app.py longbridge-sdk-status")
    print("python app.py longbridge-oauth-status")
    print("python app.py longbridge-oauth-help")
    print("python app.py longbridge-oauth-set")
    print("python app.py longbridge-oauth-clear")
    print("python app.py longbridge-oauth-start")
    print("python app.py longbridge-oauth-quote --symbol 600519 --market CN")
    print("python app.py longbridge-quote --symbol 600519 --market CN")
    print("python app.py token-status")
    print("python app.py token-set --key MARKETAUX_API_TOKEN")
    print("python app.py token-clear --key MARKETAUX_API_TOKEN")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
