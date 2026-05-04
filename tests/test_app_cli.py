import sys

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


def test_main_international_news_without_token_shows_hint(monkeypatch, capsys) -> None:
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
