import sys
from unittest.mock import MagicMock, patch

import app


class DummyInternationalNewsFetcher:
    def __init__(self, *, configured: bool, news_items: list[dict[str, object]] | None = None) -> None:
        self._configured = configured
        self._news_items = news_items or []

    def is_configured(self) -> bool:
        return self._configured

    def fetch_news(
        self,
        ticker: str,
        market: str = "US",
        hours_ago: int = 72,
        limit: int = 3,
    ) -> list[dict[str, object]]:
        del ticker, market, hours_ago, limit
        return self._news_items


def test_main_version_outputs_version_info(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "--version"])

    result = app.main()
    captured = capsys.readouterr()

    assert result == 0
    assert "AShare Insight Lab 0.7.2 (Data Source Status UI)" in captured.out


def test_main_about_outputs_project_metadata(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "about"])
    monkeypatch.setattr(
        app,
        "load_settings",
        lambda: {
            "environment": "development",
        },
    )

    result = app.main()
    captured = capsys.readouterr()

    assert result == 0
    assert "开发者: pL" in captured.out
    assert "维护者: pL" in captured.out
    assert "Copyright © 2026 @B‘lock10STUdio. All rights reserved." in captured.out
    assert "https://github.com/usydin/Ashare-insight-lab" in captured.out
    assert "仅用于研究和模拟盘验证，不构成实盘交易建议。" in captured.out


def test_main_check_data_source_invokes_doctor(monkeypatch) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "check-data-source"])
    monkeypatch.setattr(app, "run_data_source_doctor", lambda: 0)

    assert app.main() == 0


def test_main_doctor_invokes_doctor(monkeypatch) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "doctor"])
    monkeypatch.setattr(app, "run_data_source_doctor", lambda: 0)

    assert app.main() == 0


def test_main_sync_frontend_snapshot_invokes_sync(monkeypatch) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "sync-frontend-snapshot"])
    monkeypatch.setattr(app, "run_sync_frontend_snapshot", lambda: 0)

    assert app.main() == 0


def test_main_international_news_without_token_shows_hint(monkeypatch, capsys, tmp_path) -> None:
    monkeypatch.setattr(
        sys,
        "argv",
        ["app.py", "international-news", "--ticker", "AAPL"],
    )
    monkeypatch.setattr(
        app,
        "get_international_news_fetcher",
        lambda: DummyInternationalNewsFetcher(configured=False),
    )

    with patch("app.get_project_root", return_value=tmp_path):
        with patch("app_core.security.local_secret_manager.get_project_root", return_value=tmp_path):
            result = app.main()
            captured = capsys.readouterr()

            assert result == 1
            assert "未配置 MARKETAUX_API_TOKEN" in captured.out


def test_main_international_news_prints_news_items(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        sys,
        "argv",
        ["app.py", "international-news", "--ticker", "AAPL", "--market", "US", "--hours", "72", "--limit", "3"],
    )
    monkeypatch.setattr(
        app,
        "get_international_news_fetcher",
        lambda: DummyInternationalNewsFetcher(
            configured=True,
            news_items=[
                {
                    "published_at": "2026-05-04T12:00:00Z",
                    "sentiment": "positive",
                    "sentiment_score": 0.88,
                    "source": "Reuters",
                    "title": "Apple expands AI plans",
                    "url": "https://example.com/apple",
                }
            ],
        ),
    )

    result = app.main()
    captured = capsys.readouterr()

    assert result == 0
    assert "国际新闻数量: 1" in captured.out
    assert "Apple expands AI plans" in captured.out
    assert "Reuters" in captured.out


def test_main_international_news_prints_empty_result_hint(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        sys,
        "argv",
        ["app.py", "international-news", "--ticker", "00700.HK"],
    )
    monkeypatch.setattr(
        app,
        "get_international_news_fetcher",
        lambda: DummyInternationalNewsFetcher(configured=True, news_items=[]),
    )

    result = app.main()
    captured = capsys.readouterr()

    assert result == 0
    assert "国际新闻数量: 0" in captured.out
    assert "未获取到相关新闻" in captured.out


def test_main_marketaux_status_without_token(monkeypatch, capsys, tmp_path) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "marketaux-status"])
    monkeypatch.delenv("MARKETAUX_API_TOKEN", raising=False)

    # 模拟项目根目录为空，避免加载真实 .env
    with patch("app.get_project_root", return_value=tmp_path):
        with patch("app_core.security.local_secret_manager.get_project_root", return_value=tmp_path):
            result = app.main()
            captured = capsys.readouterr()

            assert result == 0
            assert "Marketaux 配置状态: 未配置" in captured.out
            assert '设置方式: export MARKETAUX_API_TOKEN="你的 token"' in captured.out


def test_main_marketaux_status_masks_token(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "marketaux-status"])
    monkeypatch.setenv("MARKETAUX_API_TOKEN", "demo-secret-token-1234")

    result = app.main()
    captured = capsys.readouterr()

    assert result == 0
    assert "Marketaux 配置状态: 已配置" in captured.out
    assert "Token 显示: ****1234" in captured.out
    assert "国际新闻 CLI: 可用" in captured.out
    assert "demo-secret-token-1234" not in captured.out


def test_main_quote_success(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "quote", "--symbol", "600519", "--market", "CN"])
    
    mock_provider = MagicMock()
    mock_provider.fetch_quote.return_value = {
        "symbol": "600519",
        "market": "CN",
        "name": "贵州茅台",
        "price": 1650.0,
        "change": 15.5,
        "pct_change": 0.95,
        "volume": 10000.0,
        "amount": 16500000.0,
        "timestamp": "2026-05-04T15:00:00",
        "data_status": "ok",
        "error_message": ""
    }
    
    with patch("app.AkShareRealtimeQuoteProvider", return_value=mock_provider):
        result = app.main()
        captured = capsys.readouterr()
        
        assert result == 0
        assert "股票代码: 600519" in captured.out
        assert "名称: 贵州茅台" in captured.out
        assert "当前价: 1650.0" in captured.out


def test_main_quote_not_found(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "quote", "--symbol", "999999", "--market", "CN"])
    
    mock_provider = MagicMock()
    mock_provider.fetch_quote.return_value = {
        "symbol": "999999",
        "market": "CN",
        "data_status": "not_found",
        "error_message": "Not found"
    }
    
    with patch("app.AkShareRealtimeQuoteProvider", return_value=mock_provider):
        result = app.main()
        captured = capsys.readouterr()
        
        assert result == 0
        assert "未找到股票代码 999999" in captured.out


def test_main_quote_unsupported(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "quote", "--symbol", "AAPL", "--market", "US"])
    
    mock_provider = MagicMock()
    mock_provider.fetch_quote.return_value = {
        "symbol": "AAPL",
        "market": "US",
        "data_status": "unsupported_market",
        "error_message": "Unsupported"
    }
    
    with patch("app.AkShareRealtimeQuoteProvider", return_value=mock_provider):
        result = app.main()
        captured = capsys.readouterr()
        
        assert result == 0
        assert "暂不支持市场 US" in captured.out


def test_main_quote_batch_success(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        sys,
        "argv",
        ["app.py", "quote-batch", "--symbols", "600519,300750,000001", "--market", "CN"],
    )

    mock_provider = MagicMock()
    mock_provider.fetch_quotes.return_value = [
        {
            "symbol": "600519",
            "name": "贵州茅台",
            "price": 1650.0,
            "pct_change": 0.95,
            "amount": 16500000.0,
            "data_status": "ok",
            "error_message": "",
        },
        {
            "symbol": "300750",
            "name": "宁德时代",
            "price": 198.5,
            "pct_change": -1.15,
            "amount": 992500.0,
            "data_status": "ok",
            "error_message": "",
        },
        {
            "symbol": "000001",
            "name": "上证指数",
            "price": 3050.25,
            "pct_change": 0.41,
            "amount": 8000000.0,
            "data_status": "ok",
            "error_message": "",
        },
    ]

    with patch("app.AkShareRealtimeQuoteProvider", return_value=mock_provider):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert "股票代码: 600519" in captured.out
        assert "查询数量: 3" in captured.out
        assert "ok 数量: 3" in captured.out


def test_main_quote_batch_outputs_summary_with_not_found(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        sys,
        "argv",
        ["app.py", "quote-batch", "--symbols", "600519,999999", "--market", "CN"],
    )

    mock_provider = MagicMock()
    mock_provider.fetch_quotes.return_value = [
        {
            "symbol": "600519",
            "name": "贵州茅台",
            "price": 1650.0,
            "pct_change": 0.95,
            "amount": 16500000.0,
            "data_status": "ok",
            "error_message": "",
        },
        {
            "symbol": "999999",
            "name": "",
            "price": None,
            "pct_change": None,
            "amount": None,
            "data_status": "not_found",
            "error_message": "Symbol 999999 not found",
        },
    ]

    with patch("app.AkShareRealtimeQuoteProvider", return_value=mock_provider):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert "not_found 数量: 1" in captured.out
        assert "ok 数量: 1" in captured.out


def test_main_quote_batch_unsupported_market(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        sys,
        "argv",
        ["app.py", "quote-batch", "--symbols", "AAPL,MSFT", "--market", "US"],
    )

    mock_provider = MagicMock()
    mock_provider.fetch_quotes.return_value = [
        {
            "symbol": "AAPL",
            "name": "",
            "price": None,
            "pct_change": None,
            "amount": None,
            "data_status": "unsupported_market",
            "error_message": "Unsupported market: US",
        },
        {
            "symbol": "MSFT",
            "name": "",
            "price": None,
            "pct_change": None,
            "amount": None,
            "data_status": "unsupported_market",
            "error_message": "Unsupported market: US",
        },
    ]

    with patch("app.AkShareRealtimeQuoteProvider", return_value=mock_provider):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert "unsupported_market 数量: 2" in captured.out
        assert "Unsupported market: US" in captured.out

def test_main_longbridge_status_without_env(monkeypatch, capsys, tmp_path) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-status"])
    # 确保环境变量缺失
    for key in ("LONGBRIDGE_APP_KEY", "LONGBRIDGE_APP_SECRET", "LONGBRIDGE_ACCESS_TOKEN"):
        monkeypatch.delenv(key, raising=False)

    # 模拟项目根目录为空，避免加载真实 .env
    with patch("app.get_project_root", return_value=tmp_path):
        with patch("app_core.security.local_secret_manager.get_project_root", return_value=tmp_path):
            result = app.main()
            captured = capsys.readouterr()

            assert result == 0
            assert "provider: longbridge" in captured.out
            assert "env:" in captured.out
            assert "LONGBRIDGE_APP_KEY: missing" in captured.out

def test_main_longbridge_quote_sdk_missing(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-quote", "--symbol", "600519", "--market", "CN"])
    mock_provider = MagicMock()
    mock_provider.fetch_quote.return_value = {
        "data_status": "sdk_missing",
        "error_message": "SDK missing",
    }
    with patch("app.LongbridgeQuoteProvider", return_value=mock_provider):
        result = app.main()
        captured = capsys.readouterr()
        assert result == 0
        assert "SDK 未安装或不可导入" in captured.out

def test_main_longbridge_quote_missing_env(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-quote", "--symbol", "600519", "--market", "CN"])
    mock_provider = MagicMock()
    mock_provider.fetch_quote.return_value = {
        "data_status": "missing_env",
        "error_message": "Missing environment variables",
    }
    with patch("app.LongbridgeQuoteProvider", return_value=mock_provider):
        result = app.main()
        captured = capsys.readouterr()
        assert result == 0
        assert "缺少环境变量" in captured.out

def test_help_contains_longbridge_commands(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "unknown"])
    result = app.main()
    captured = capsys.readouterr()
    assert result == 1
    assert "longbridge-status" in captured.out
    assert "longbridge-quote" in captured.out


def test_main_token_status_does_not_output_real_token(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "token-status"])
    mock_manager = MagicMock()
    mock_manager.get_secret_statuses.return_value = [
        {
            "key": "MARKETAUX_API_TOKEN",
            "provider": "Marketaux",
            "display_name": "Marketaux 新闻 API",
            "status": "configured",
            "source": ".env",
            "masked": "****1234",
            "length": 16,
            "updated_at": "2026-05-05T10:00:00",
            "last_checked_at": "2026-05-05T10:10:00",
            "note": "国际市场新闻",
        }
    ]

    with patch("app.LocalSecretManager", return_value=mock_manager):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert "****1234" in captured.out
        assert "demo-secret-1234" not in captured.out


def test_main_token_set_uses_getpass_and_masks_output(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "token-set", "--key", "MARKETAUX_API_TOKEN"])
    values = iter(["demo-secret-1234", "demo-secret-1234"])
    monkeypatch.setattr(app, "getpass", lambda prompt: next(values))

    mock_manager = MagicMock()
    mock_manager.set_secret.return_value = {
        "key": "MARKETAUX_API_TOKEN",
        "status": "configured",
        "masked": "****1234",
    }

    with patch("app.LocalSecretManager", return_value=mock_manager):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert "****1234" in captured.out
        assert "demo-secret-1234" not in captured.out


def test_main_token_clear_keeps_output_masked(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "token-clear", "--key", "MARKETAUX_API_TOKEN"])
    confirmations = iter(["YES", "YES"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(confirmations))

    mock_manager = MagicMock()
    mock_manager.clear_secret.return_value = {
        "key": "MARKETAUX_API_TOKEN",
        "status": "empty",
        "masked": "",
    }

    with patch("app.LocalSecretManager", return_value=mock_manager):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert "状态: empty" in captured.out


def test_help_contains_token_commands(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "unknown"])
    result = app.main()
    captured = capsys.readouterr()

    assert result == 1
    assert "token-status" in captured.out
    assert "token-set --key MARKETAUX_API_TOKEN" in captured.out
    assert "token-clear --key MARKETAUX_API_TOKEN" in captured.out

def test_main_kline_success(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        sys,
        "argv",
        ["app.py", "kline", "--symbol", "600519", "--market", "CN", "--period", "daily", "--adjust", "qfq", "--limit", "20"],
    )

    mock_provider = MagicMock()
    mock_provider.fetch_kline.return_value = {
        "symbol": "600519",
        "market": "CN",
        "period": "daily",
        "adjust": "qfq",
        "provider": "AkShare",
        "data_status": "ok",
        "error_message": "",
        "rows": [
            {"date": "2024-01-01", "open": 10.0, "high": 10.5, "low": 9.8, "close": 10.3, "volume": 1000, "amount": 100000},
            {"date": "2024-01-02", "open": 10.2, "high": 10.8, "low": 10.1, "close": 10.6, "volume": 1200, "amount": 125000},
        ],
    }

    with patch("app.AkShareKlineProvider", return_value=mock_provider):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert "股票代码: 600519" in captured.out
        assert "周期: daily" in captured.out
        assert "行数: 2" in captured.out
        assert "2024-01-01 / open=10.0" in captured.out


def test_main_kline_unsupported_market(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        sys,
        "argv",
        ["app.py", "kline", "--symbol", "AAPL", "--market", "US", "--period", "daily"],
    )

    mock_provider = MagicMock()
    mock_provider.fetch_kline.return_value = {
        "symbol": "AAPL",
        "market": "US",
        "period": "daily",
        "adjust": "qfq",
        "provider": "AkShare",
        "data_status": "unsupported_market",
        "error_message": "Unsupported market: US",
        "rows": [],
    }

    with patch("app.AkShareKlineProvider", return_value=mock_provider):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert "暂不支持市场 US 的 K线数据" in captured.out


def test_main_kline_unsupported_period(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        sys,
        "argv",
        ["app.py", "kline", "--symbol", "600519", "--market", "CN", "--period", "5m"],
    )

    mock_provider = MagicMock()
    mock_provider.fetch_kline.return_value = {
        "symbol": "600519",
        "market": "CN",
        "period": "5m",
        "adjust": "qfq",
        "provider": "AkShare",
        "data_status": "unsupported_period",
        "error_message": "Unsupported period: 5m",
        "rows": [],
    }

    with patch("app.AkShareKlineProvider", return_value=mock_provider):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert "暂不支持周期 5m" in captured.out


def test_main_kline_fetch_failed(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        sys,
        "argv",
        ["app.py", "kline", "--symbol", "600519", "--market", "CN", "--period", "daily"],
    )

    mock_provider = MagicMock()
    mock_provider.fetch_kline.return_value = {
        "symbol": "600519",
        "market": "CN",
        "period": "daily",
        "adjust": "qfq",
        "provider": "AkShare",
        "data_status": "fetch_failed",
        "error_message": "network down",
        "rows": [],
    }

    with patch("app.AkShareKlineProvider", return_value=mock_provider):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert "抓取 K线数据失败" in captured.out
        assert "network down" in captured.out
        assert "Traceback" not in captured.out


def test_main_marketaux_status_auto_loads_env(monkeypatch, capsys, tmp_path) -> None:
    # 模拟项目根目录 .env
    env_path = tmp_path / ".env"
    env_path.write_text("MARKETAUX_API_TOKEN=auto-loaded-token-9999\n", encoding="utf-8")
    
    monkeypatch.setattr(sys, "argv", ["app.py", "marketaux-status"])
    # 确保环境变量缺失
    monkeypatch.delenv("MARKETAUX_API_TOKEN", raising=False)
    
    # 模拟 get_project_root 返回 tmp_path
    from pathlib import Path
    with patch("app.get_project_root", return_value=tmp_path):
        # 还需要 mock LocalSecretManager 内部的 get_project_root 或者直接 patch LocalSecretManager
        with patch("app_core.security.local_secret_manager.get_project_root", return_value=tmp_path):
            result = app.main()
            captured = capsys.readouterr()

            assert result == 0
            assert "Marketaux 配置状态: 已配置" in captured.out
            assert "Token 显示: ****9999" in captured.out


def test_main_longbridge_status_auto_loads_env(monkeypatch, capsys, tmp_path) -> None:
    # 模拟项目根目录 .env
    env_path = tmp_path / ".env"
    env_path.write_text(
        "LONGBRIDGE_APP_KEY=auto-key-1111\n"
        "LONGBRIDGE_APP_SECRET=auto-secret-2222\n",
        encoding="utf-8"
    )
    
    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-status"])
    # 确保环境变量缺失
    for key in ("LONGBRIDGE_APP_KEY", "LONGBRIDGE_APP_SECRET"):
        monkeypatch.delenv(key, raising=False)
    
    with patch("app.get_project_root", return_value=tmp_path):
        with patch("app_core.security.local_secret_manager.get_project_root", return_value=tmp_path):
            result = app.main()
            captured = capsys.readouterr()

            assert result == 0
            assert "LONGBRIDGE_APP_KEY: present" in captured.out
            assert "LONGBRIDGE_APP_SECRET: present" in captured.out
