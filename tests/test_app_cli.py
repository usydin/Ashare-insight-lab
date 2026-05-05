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
    monkeypatch.delenv("LONGBRIDGE_OAUTH_CLIENT_ID", raising=False)

    # 模拟项目根目录为空，避免加载真实 .env
    with patch("app.get_project_root", return_value=tmp_path):
        with patch("app_core.security.local_secret_manager.get_project_root", return_value=tmp_path):
            with patch("app_core.security.longbridge_oauth_store.get_project_root", return_value=tmp_path):
                result = app.main()
                captured = capsys.readouterr()

                assert result == 0
                assert "provider: longbridge" in captured.out
                assert "oauth_client:" in captured.out
                assert "client_id: missing" in captured.out
                assert "redirect_uri: http://localhost:60355/callback" in captured.out
                assert "app_key_is_oauth_client_id: false" in captured.out
                assert "env:" in captured.out
                assert "LONGBRIDGE_APP_KEY: missing" in captured.out
                assert "auth_mode_candidate: missing_app_credentials" in captured.out
                assert "token_file: missing" in captured.out
                assert "token_expiry:" in captured.out
                assert "access_token_expiry_status: missing" in captured.out


def test_main_longbridge_sdk_status_sdk_missing(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-sdk-status"])
    monkeypatch.setattr(
        app,
        "inspect_longbridge_sdk",
        lambda: {
            "sdk_importable": False,
            "sdk_version": "unknown",
            "available_symbols": {
                "Config": False,
                "QuoteContext": False,
                "OAuthBuilder": False,
            },
            "error_message": "sdk missing",
        },
    )

    result = app.main()
    captured = capsys.readouterr()

    assert result == 0
    assert "sdk_importable: no" in captured.out
    assert "QuoteContext: no" in captured.out
    assert "OAuthBuilder: no" in captured.out
    assert "sdk missing" in captured.out
    assert "Traceback" not in captured.out

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
    assert "longbridge-oauth-help" in captured.out
    assert "longbridge-oauth-status" in captured.out


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
            "supports_expiry_monitor": True,
            "expires_at_utc": "",
            "days_remaining": None,
            "expiry_status": "not_jwt",
            "expiry_message": "当前 token 不是 JWT-like，需人工维护到期日期",
        }
    ]

    with patch("app.LocalSecretManager", return_value=mock_manager):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert "****1234" in captured.out
        assert "到期等级: not_jwt" in captured.out
        assert "demo-secret-1234" not in captured.out


def test_main_token_expiry_status_outputs_expiry_summary(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "token-expiry-status"])
    mock_manager = MagicMock()
    mock_manager.get_token_expiry_statuses.return_value = [
        {
            "key": "LONGBRIDGE_ACCESS_TOKEN",
            "provider": "Longbridge",
            "display_name": "Longbridge Access Token",
            "status": "configured",
            "masked": "****NcTY",
            "expires_at_utc": "2026-08-03T13:09:05+00:00",
            "days_remaining": 89,
            "expiry_status": "ok",
            "expiry_message": "token 有效",
        }
    ]

    with patch("app.LocalSecretManager", return_value=mock_manager):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert "API Token 到期状态" in captured.out
        assert "Longbridge Access Token" in captured.out
        assert "到期等级: ok" in captured.out
        assert "****NcTY" in captured.out
        assert "LONGBRIDGE_ACCESS_TOKEN=" not in captured.out


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
    assert "token-expiry-status" in captured.out
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
        "LONGBRIDGE_APP_SECRET=auto-secret-2222\n"
        "LONGBRIDGE_OAUTH_CLIENT_ID=\n",
        encoding="utf-8"
    )
    
    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-status"])
    # 确保环境变量缺失
    for key in ("LONGBRIDGE_APP_KEY", "LONGBRIDGE_APP_SECRET"):
        monkeypatch.delenv(key, raising=False)
    monkeypatch.delenv("LONGBRIDGE_OAUTH_CLIENT_ID", raising=False)
    
    with patch("app.get_project_root", return_value=tmp_path):
        with patch("app_core.security.local_secret_manager.get_project_root", return_value=tmp_path):
            with patch("app_core.security.longbridge_oauth_store.get_project_root", return_value=tmp_path):
                with patch("app_core.data_sources.longbridge_quote_provider.inspect_longbridge_sdk", return_value={
                    "sdk_importable": True,
                    "sdk_version": "4.0.5",
                    "available_symbols": {"Config": True, "QuoteContext": True, "OAuthBuilder": True},
                    "error_message": "",
                }):
                    result = app.main()
                    captured = capsys.readouterr()

                    assert result == 0
                    assert "LONGBRIDGE_APP_KEY: present" in captured.out
                    assert "LONGBRIDGE_APP_SECRET: present" in captured.out
                    assert "client_id: missing" in captured.out
                    assert "oauth_client:" in captured.out
                    assert "quote_only: true" in captured.out
                    assert "trade_enabled: false" in captured.out
                    assert "auto-key-1111" not in captured.out
                    assert "auto-secret-2222" not in captured.out


def test_main_longbridge_oauth_help(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-oauth-help"])

    result = app.main()
    captured = capsys.readouterr()

    assert result == 0
    assert "OAuth 2.0" in captured.out
    assert "OAuthBuilder" in captured.out
    assert "QuoteContext" in captured.out
    assert "quote_only: true" in captured.out
    assert ".secrets/longbridge_oauth_token.json" in captured.out
    assert "不接交易" in captured.out
    assert "App Key 不能作为 OAuth client_id 使用" in captured.out
    assert "LONGBRIDGE_OAUTH_CLIENT_ID" in captured.out
    assert "http://localhost:60355/callback" in captured.out


def test_main_longbridge_oauth_status_without_token(monkeypatch, capsys, tmp_path) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-oauth-status"])

    with patch("app_core.security.longbridge_oauth_store.get_project_root", return_value=tmp_path):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert "status: missing" in captured.out
        assert "token_file: missing" in captured.out


def test_main_longbridge_oauth_status_sdk_managed_configured(monkeypatch, capsys, tmp_path) -> None:
    from app_core.security.longbridge_oauth_store import LongbridgeOAuthStore

    store = LongbridgeOAuthStore(project_root=tmp_path)
    store.save_oauth_metadata(
        {
            "scope": "quote",
            "sdk_managed": True,
            "note": "quote only; sdk managed",
        }
    )
    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-oauth-status"])
    with patch("app_core.security.longbridge_oauth_store.get_project_root", return_value=tmp_path):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert "status: sdk_managed_configured" in captured.out
        assert "token_file: configured" in captured.out
        assert "access_token: sdk_managed" in captured.out
        assert "refresh_token: sdk_managed_or_unknown" in captured.out
        assert "quote_only: true" in captured.out
        assert "trade_enabled: false" in captured.out


def test_main_longbridge_oauth_set_masks_output(monkeypatch, capsys, tmp_path) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-oauth-set"])
    getpass_values = iter(["demo_oauth", "demo-refresh-token-5678"])
    input_values = iter(["2030-01-01T00:00:00+00:00", "quote"])
    monkeypatch.setattr(app, "getpass", lambda prompt: next(getpass_values))
    monkeypatch.setattr("builtins.input", lambda prompt: next(input_values))

    with patch("app_core.security.longbridge_oauth_store.get_project_root", return_value=tmp_path):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert "status: configured" in captured.out
        assert "****auth" in captured.out
        assert "demo_oauth" not in captured.out


def test_main_longbridge_oauth_clear(monkeypatch, capsys, tmp_path) -> None:
    from app_core.security.longbridge_oauth_store import LongbridgeOAuthStore

    store = LongbridgeOAuthStore(project_root=tmp_path)
    store.save_oauth_token({"access_token": "demo_oauth"})

    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-oauth-clear"])
    confirmations = iter(["YES", "YES"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(confirmations))

    with patch("app_core.security.longbridge_oauth_store.get_project_root", return_value=tmp_path):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert "status: cleared" in captured.out
        assert not store.token_path.exists()


def test_main_longbridge_oauth_start_sdk_missing(monkeypatch, capsys, tmp_path) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-oauth-start"])
    monkeypatch.setenv("LONGBRIDGE_OAUTH_CLIENT_ID", "demo-client-id")
    monkeypatch.setattr(
        app,
        "start_longbridge_oauth",
        lambda client_id, store: {
            "status": "sdk_missing",
            "message": "Longbridge SDK missing",
            "sdk_token_cache": "unknown",
        },
    )

    with patch("app_core.security.longbridge_oauth_store.get_project_root", return_value=tmp_path):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert "oauth: sdk_missing" in captured.out
        assert "Longbridge SDK missing" in captured.out
        assert "Traceback" not in captured.out


def test_main_longbridge_oauth_start_internal_server_error_diagnostics(monkeypatch, capsys, tmp_path) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-oauth-start"])
    monkeypatch.setenv("LONGBRIDGE_OAUTH_CLIENT_ID", "demo-client-id")
    monkeypatch.setattr(
        app,
        "start_longbridge_oauth",
        lambda client_id, store: {
            "status": "oauth_failed",
            "message": "OpenApiException: OAuth authorization failed: internal_server_error",
            "diagnostics": {
                "error_type": "internal_server_error",
                "likely_stage": "authorization_server",
                "sdk_importable": True,
                "sdk_version": "4.0.5",
                "client_id_present": True,
                "browser_open_requested": True,
                "redirect_uri_host": "localhost",
                "redirect_uri_scheme": "http",
                "quote_only": True,
                "trade_enabled": False,
                "next_steps": [
                    "检查长桥开发者后台是否启用 OAuth 2.0",
                    "通过 /oauth2/register 单独注册 OAuth Client，获得独立 client_id",
                ],
            },
        },
    )
    monkeypatch.setattr(
        app,
        "inspect_longbridge_sdk",
        lambda: {
            "sdk_importable": True,
            "sdk_version": "4.0.5",
            "available_symbols": {"Config": True, "QuoteContext": True, "OAuthBuilder": True},
            "error_message": "",
        },
    )

    with patch("app_core.security.longbridge_oauth_store.get_project_root", return_value=tmp_path):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert "oauth: oauth_failed" in captured.out
        assert "error_type: internal_server_error" in captured.out
        assert "likely_stage: authorization_server" in captured.out
        assert "browser_open_requested: true" in captured.out
        assert "quote_only: true" in captured.out
        assert "trade_enabled: false" in captured.out
        assert "state=" not in captured.out
        assert "token" not in captured.out.lower()
        assert "App Secret" not in captured.out


def test_main_longbridge_oauth_start_app_key_missing(monkeypatch, capsys, tmp_path) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-oauth-start"])
    monkeypatch.delenv("LONGBRIDGE_OAUTH_CLIENT_ID", raising=False)
    monkeypatch.setattr(
        app,
        "start_longbridge_oauth",
        lambda client_id, store: {
            "status": "oauth_client_id_missing",
            "message": "请先通过 Longbridge /oauth2/register 注册 OAuth Client，并将 client_id 写入 LONGBRIDGE_OAUTH_CLIENT_ID。",
            "sdk_token_cache": "unknown",
        },
    )

    with patch("app.get_project_root", return_value=tmp_path):
        with patch("app_core.security.local_secret_manager.get_project_root", return_value=tmp_path):
            with patch("app_core.security.longbridge_oauth_store.get_project_root", return_value=tmp_path):
                result = app.main()
                captured = capsys.readouterr()

                assert result == 0
                assert "oauth: oauth_client_id_missing" in captured.out
                assert "LONGBRIDGE_OAUTH_CLIENT_ID" in captured.out


def test_main_longbridge_oauth_start_authorized_outputs_browser_open_requested(monkeypatch, capsys, tmp_path) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-oauth-start"])
    monkeypatch.setenv("LONGBRIDGE_OAUTH_CLIENT_ID", "demo-client-id")
    monkeypatch.setattr(
        app,
        "start_longbridge_oauth",
        lambda client_id, store: {
            "status": "authorized",
            "message": "",
            "sdk_token_cache": "maybe_configured",
            "browser_open_requested": True,
            "redirect_uri_host": "localhost",
            "oauth": object(),
        },
    )
    monkeypatch.setattr(
        app,
        "inspect_longbridge_sdk",
        lambda: {
            "sdk_importable": True,
            "sdk_version": "4.0.5",
            "available_symbols": {"Config": True, "QuoteContext": True, "OAuthBuilder": True},
            "error_message": "",
        },
    )

    with patch("app_core.security.longbridge_oauth_store.get_project_root", return_value=tmp_path):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert "oauth: authorized" in captured.out
        assert "browser_open_requested: true" in captured.out
        assert "redirect_uri_host: localhost" in captured.out
        assert "demo-client-id" not in captured.out
        assert "state=" not in captured.out
        assert "code=" not in captured.out


def test_main_longbridge_oauth_quote_sdk_missing(monkeypatch, capsys, tmp_path) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-oauth-quote", "--symbol", "600519", "--market", "CN"])
    monkeypatch.setenv("LONGBRIDGE_OAUTH_CLIENT_ID", "demo-client-id")
    monkeypatch.setattr(
        app,
        "fetch_longbridge_quote_via_oauth",
        lambda client_id, symbol, raw_symbol, store: {
            "data_status": "sdk_missing",
            "error_message": "Longbridge SDK missing",
            "symbol": symbol,
            "raw_symbol": raw_symbol,
        },
    )

    with patch("app_core.security.longbridge_oauth_store.get_project_root", return_value=tmp_path):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert "数据状态: sdk_missing" in captured.out
        assert "Longbridge SDK missing" in captured.out
        assert "Traceback" not in captured.out


def test_main_longbridge_oauth_quote_us_mapping_ok(monkeypatch, capsys, tmp_path) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-oauth-quote", "--symbol", "AAPL", "--market", "US"])
    monkeypatch.setenv("LONGBRIDGE_OAUTH_CLIENT_ID", "demo-client-id")

    last_called = {}

    def fake_fetch(client_id, symbol, raw_symbol, store):
        last_called["client_id"] = client_id
        last_called["symbol"] = symbol
        last_called["raw_symbol"] = raw_symbol
        return {
            "data_status": "ok",
            "symbol": symbol,
            "raw_symbol": raw_symbol,
            "name": "Apple Inc.",
            "current_price": 200.5,
            "change": 1.2,
            "change_percent": 0.6,
            "timestamp": "2026-05-05T12:00:00",
        }

    monkeypatch.setattr(app, "fetch_longbridge_quote_via_oauth", fake_fetch)
    with patch("app_core.security.longbridge_oauth_store.get_project_root", return_value=tmp_path):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert last_called["raw_symbol"] == "AAPL.US"
        assert "股票代码: AAPL" in captured.out
        assert "Longbridge代码: AAPL.US" in captured.out
        assert "市场: US" in captured.out
        assert "数据状态: ok" in captured.out
        assert "token" not in captured.out.lower()
        assert "state=" not in captured.out
        assert "code=" not in captured.out


def test_main_longbridge_oauth_quote_hk_mapping_ok(monkeypatch, capsys, tmp_path) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-oauth-quote", "--symbol", "00700", "--market", "HK"])
    monkeypatch.setenv("LONGBRIDGE_OAUTH_CLIENT_ID", "demo-client-id")

    last_called = {}

    def fake_fetch(client_id, symbol, raw_symbol, store):
        last_called["client_id"] = client_id
        last_called["symbol"] = symbol
        last_called["raw_symbol"] = raw_symbol
        return {
            "data_status": "ok",
            "symbol": symbol,
            "raw_symbol": raw_symbol,
            "name": "Tencent",
            "current_price": 350.1,
            "change": 2.3,
            "change_percent": 0.7,
            "timestamp": "2026-05-05T12:00:00",
        }

    monkeypatch.setattr(app, "fetch_longbridge_quote_via_oauth", fake_fetch)
    with patch("app_core.security.longbridge_oauth_store.get_project_root", return_value=tmp_path):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert last_called["raw_symbol"] == "700.HK"
        assert "股票代码: 00700" in captured.out
        assert "Longbridge代码: 700.HK" in captured.out
        assert "市场: HK" in captured.out
        assert "数据状态: ok" in captured.out


def test_main_longbridge_oauth_help_no_tradecontext_runtime_usage(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-oauth-help"])

    result = app.main()
    captured = capsys.readouterr()

    assert result == 0
    assert "QuoteContext" in captured.out
    assert "TradeContext" not in captured.out


def test_main_longbridge_quote_oauth_required(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-quote", "--symbol", "600519", "--market", "CN"])
    mock_provider = MagicMock()
    mock_provider.fetch_quote.return_value = {
        "data_status": "oauth_required",
        "error_message": "当前账号未提供 legacy Access Token，请执行 longbridge-oauth-help",
    }
    with patch("app.LongbridgeQuoteProvider", return_value=mock_provider):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert "longbridge-oauth-help" in captured.out
        assert "Traceback" not in captured.out


def test_main_longbridge_quote_oauthbuilder_required(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-quote", "--symbol", "600519", "--market", "CN"])
    mock_provider = MagicMock()
    mock_provider.fetch_quote.return_value = {
        "data_status": "oauthbuilder_required",
        "error_message": "请先执行 longbridge-oauth-start 或 longbridge-oauth-help。",
    }
    with patch("app.LongbridgeQuoteProvider", return_value=mock_provider):
        result = app.main()
        captured = capsys.readouterr()

        assert result == 0
        assert "longbridge-oauth-start" in captured.out
        assert "Traceback" not in captured.out


def test_main_source_status_outputs_sources(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "source-status"])
    monkeypatch.setattr(
        app,
        "build_realtime_source_status",
        lambda: {
            "generated_at": "2026-05-05T12:00:00",
            "default_quote_source": "akshare",
            "sources": [
                {
                    "source_id": "akshare",
                    "display_name": "AkShare",
                    "category": "quote",
                    "status": "available",
                    "status_label": "可用",
                    "token_status": "not_required",
                    "note": "当前默认 A股实时行情源",
                },
                {
                    "source_id": "longbridge",
                    "display_name": "Longbridge",
                    "category": "quote",
                    "status": "warning",
                    "status_label": "临近到期",
                    "auth_mode": "legacy_configured",
                    "sdk_status": "installed",
                    "token_status": "configured",
                    "token_expiry": {
                        "status": "danger",
                        "expires_at_utc": "2026-08-03T13:09:05+00:00",
                        "days_remaining": 5,
                        "message": "token 将在 7 天内到期，请尽快更新",
                    },
                    "quote_only": True,
                    "trade_enabled": False,
                    "note": "Longbridge Access Token 临近到期，请提前更新 .env 中 LONGBRIDGE_ACCESS_TOKEN",
                },
                {
                    "source_id": "marketaux",
                    "display_name": "Marketaux",
                    "category": "news",
                    "status": "available",
                    "status_label": "已配置",
                    "token_status": "configured",
                    "note": "国际新闻源",
                },
            ],
            "safety": {
                "quote_only": True,
                "trade_enabled": False,
                "order_enabled": False,
            },
        },
    )

    result = app.main()
    captured = capsys.readouterr()

    assert result == 0
    assert "实时行情默认源: akshare" in captured.out
    assert "[AkShare]" in captured.out
    assert "[Longbridge]" in captured.out
    assert "[Marketaux]" in captured.out
    assert "SDK: installed" in captured.out
    assert "OAuth: configured" in captured.out
    assert "Token 到期等级: danger" in captured.out
    assert "Token 到期时间UTC: 2026-08-03T13:09:05+00:00" in captured.out
    assert "quote_only=true, trade_enabled=false" in captured.out


def test_main_source_status_does_not_output_real_token(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "source-status"])
    monkeypatch.setattr(
        app,
        "build_realtime_source_status",
        lambda: {
            "generated_at": "2026-05-05T12:00:00",
            "default_quote_source": "akshare",
            "sources": [
                {
                    "source_id": "longbridge",
                    "display_name": "Longbridge",
                    "category": "quote",
                    "status": "blocked",
                    "status_label": "待授权",
                    "auth_mode": "oauthbuilder_required",
                    "sdk_status": "installed",
                    "token_status": "missing",
                    "quote_only": True,
                    "trade_enabled": False,
                    "note": "no raw token here",
                },
                {
                    "source_id": "marketaux",
                    "display_name": "Marketaux",
                    "category": "news",
                    "status": "available",
                    "status_label": "已配置",
                    "token_status": "configured",
                    "note": "international news only",
                },
            ],
            "safety": {
                "quote_only": True,
                "trade_enabled": False,
                "order_enabled": False,
            },
        },
    )

    result = app.main()
    captured = capsys.readouterr()

    assert result == 0
    assert "demo-secret-token-1234" not in captured.out
    assert "demo-oauth-secret-9876" not in captured.out

def test_main_longbridge_quote_snapshot_success(monkeypatch, capsys, tmp_path):
    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-quote-snapshot"])
    
    mock_snapshot = {
        "status": "ok",
        "items": [{"symbol": "600519", "data_status": "ok"}]
    }
    
    with patch("app.build_longbridge_realtime_quote_snapshot", return_value=mock_snapshot),          patch("app.write_longbridge_realtime_quote_snapshot_json", return_value=tmp_path / "snapshot.json"),          patch("app.get_project_root", return_value=tmp_path):
        
        result = app.main()
        captured = capsys.readouterr()
        
        assert result == 0
        assert "snapshot_status: ok" in captured.out
        assert "ok_items: 1" in captured.out
        assert "quote_only: true" in captured.out

def test_main_longbridge_quote_snapshot_failed(monkeypatch, capsys, tmp_path):
    monkeypatch.setattr(sys, "argv", ["app.py", "longbridge-quote-snapshot"])
    
    with patch("app.build_longbridge_realtime_quote_snapshot", side_effect=RuntimeError("Test error")):
        result = app.main()
        captured = capsys.readouterr()
        
        assert result == 1
        assert "snapshot_status: failed" in captured.out
        assert "message: Test error" in captured.out
