from __future__ import annotations

from datetime import datetime, timedelta, timezone

from app_core.data_sources.international_news import (
    DEFAULT_FREE_LIMIT,
    DEFAULT_TIMEOUT_SECONDS,
    FreeInternationalNewsFetcher,
    MARKETAUX_NEWS_ENDPOINT,
    get_international_news_fetcher,
)


class DummyResponse:
    def __init__(self, status_code: int, payload: dict, text: str = "") -> None:
        self.status_code = status_code
        self._payload = payload
        self.text = text

    def json(self) -> dict:
        return self._payload


def test_fetcher_is_safe_without_token() -> None:
    fetcher = FreeInternationalNewsFetcher(api_token=None)

    assert fetcher.is_configured() is False
    assert fetcher.fetch_news("AAPL") == []


def test_get_international_news_fetcher_does_not_require_token(monkeypatch) -> None:
    monkeypatch.delenv("MARKETAUX_API_TOKEN", raising=False)

    fetcher = get_international_news_fetcher()

    assert isinstance(fetcher, FreeInternationalNewsFetcher)
    assert fetcher.is_configured() is False


def test_fetch_news_calls_requests_get_with_expected_params(monkeypatch) -> None:
    captured: dict[str, object] = {}

    def fake_get(url: str, *, params: dict[str, object], timeout: int) -> DummyResponse:
        captured["url"] = url
        captured["params"] = params
        captured["timeout"] = timeout
        return DummyResponse(
            200,
            {
                "data": [
                    {
                        "title": "Apple expands AI plans",
                        "description": "desc",
                        "url": "https://example.com/apple",
                        "published_at": "2026-05-04T10:00:00Z",
                        "sentiment": "positive",
                        "sentiment_score": 0.8,
                        "source": "Reuters",
                    }
                ]
            },
        )

    monkeypatch.setattr("app_core.data_sources.international_news.requests.get", fake_get)

    fetcher = FreeInternationalNewsFetcher(api_token="demo-token")
    result = fetcher.fetch_news("AAPL", market="US", hours_ago=12, limit=8)

    assert len(result) == 1
    assert captured["url"] == MARKETAUX_NEWS_ENDPOINT
    assert captured["timeout"] == DEFAULT_TIMEOUT_SECONDS
    assert captured["params"]["api_token"] == "demo-token"
    assert captured["params"]["symbols"] == "AAPL"
    assert captured["params"]["limit"] == DEFAULT_FREE_LIMIT
    assert captured["params"]["language"] == "en,zh"
    assert "sort" not in captured["params"]
    assert "+00:00" not in str(captured["params"]["published_after"])
    assert "." not in str(captured["params"]["published_after"])


def test_fetch_news_uses_cache_on_second_call(monkeypatch) -> None:
    call_count = {"count": 0}

    def fake_get(url: str, *, params: dict[str, object], timeout: int) -> DummyResponse:
        del url, params, timeout
        call_count["count"] += 1
        return DummyResponse(
            200,
            {
                "data": [
                    {
                        "title": "Cached news",
                        "published_at": "2026-05-04T10:00:00Z",
                        "source": "Reuters",
                    }
                ]
            },
        )

    monkeypatch.setattr("app_core.data_sources.international_news.requests.get", fake_get)

    fetcher = FreeInternationalNewsFetcher(api_token="demo-token")
    first = fetcher.fetch_news("MSFT")
    second = fetcher.fetch_news("MSFT")

    assert call_count["count"] == 1
    assert first == second


def test_fetch_news_returns_empty_list_on_non_200(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        "app_core.data_sources.international_news.requests.get",
        lambda url, *, params, timeout: DummyResponse(
            429,
            {"error": {"message": "malformed_parameters"}},
        ),
    )

    fetcher = FreeInternationalNewsFetcher(api_token="demo-token")

    assert fetcher.fetch_news("NVDA") == []
    captured = capsys.readouterr()
    assert "状态码: 429" in captured.out
    assert "错误信息: malformed_parameters" in captured.out
    assert "demo-token" not in captured.out
    assert "***" in captured.out


def test_fetch_news_supports_string_and_object_source(monkeypatch) -> None:
    monkeypatch.setattr(
        "app_core.data_sources.international_news.requests.get",
        lambda url, *, params, timeout: DummyResponse(
            200,
            {
                "data": [
                    {
                        "title": "Source string",
                        "published_at": "2026-05-04T10:00:00Z",
                        "source": "Reuters",
                    },
                    {
                        "title": "Source object",
                        "published_at": "2026-05-04T11:00:00Z",
                        "source": {"name": "Bloomberg"},
                    },
                ]
            },
        ),
    )

    fetcher = FreeInternationalNewsFetcher(api_token="demo-token")
    result = fetcher.fetch_news("TSLA")

    assert result[0]["source"] == "Reuters"
    assert result[1]["source"] == "Bloomberg"


def test_fetch_news_normalizes_sentiment_from_scores(monkeypatch) -> None:
    monkeypatch.setattr(
        "app_core.data_sources.international_news.requests.get",
        lambda url, *, params, timeout: DummyResponse(
            200,
            {
                "data": [
                    {
                        "title": "Positive score",
                        "published_at": "2026-05-04T10:00:00Z",
                        "score": 0.2,
                        "source": "Reuters",
                    },
                    {
                        "title": "Negative entity score",
                        "published_at": "2026-05-04T11:00:00Z",
                        "entities": [{"score": -0.2}],
                        "source": "Reuters",
                    },
                    {
                        "title": "Neutral article",
                        "published_at": "2026-05-04T12:00:00Z",
                        "score": 0.01,
                        "source": "Reuters",
                    },
                ]
            },
        ),
    )

    fetcher = FreeInternationalNewsFetcher(api_token="demo-token")
    result = fetcher.fetch_news("META")

    assert result[0]["sentiment"] == "positive"
    assert result[0]["sentiment_score"] == 0.2
    assert result[1]["sentiment"] == "negative"
    assert result[1]["sentiment_score"] == -0.2
    assert result[2]["sentiment"] == "neutral"
    assert result[2]["sentiment_score"] == 0.01


def test_fetch_news_skips_items_without_title(monkeypatch) -> None:
    monkeypatch.setattr(
        "app_core.data_sources.international_news.requests.get",
        lambda url, *, params, timeout: DummyResponse(
            200,
            {
                "data": [
                    {"published_at": "2026-05-04T10:00:00Z", "source": "Reuters"},
                    {"title": "Valid title", "published_at": "2026-05-04T11:00:00Z", "source": "Reuters"},
                ]
            },
        ),
    )

    fetcher = FreeInternationalNewsFetcher(api_token="demo-token")
    result = fetcher.fetch_news("AMZN")

    assert len(result) == 1
    assert result[0]["title"] == "Valid title"


def test_cache_expires_after_one_hour(monkeypatch) -> None:
    call_count = {"count": 0}

    def fake_get(url: str, *, params: dict[str, object], timeout: int) -> DummyResponse:
        del url, params, timeout
        call_count["count"] += 1
        return DummyResponse(
            200,
            {"data": [{"title": "Cached news", "published_at": "2026-05-04T10:00:00Z", "source": "Reuters"}]},
        )

    monkeypatch.setattr("app_core.data_sources.international_news.requests.get", fake_get)

    fetcher = FreeInternationalNewsFetcher(api_token="demo-token")
    fetcher.fetch_news("GOOGL")
    cache_key = fetcher._build_cache_key("GOOGL", "US", 24, 3)
    fetcher._cache[cache_key] = (
        datetime.now(timezone.utc) - timedelta(seconds=3601),
        fetcher._cache[cache_key][1],
    )
    fetcher.fetch_news("GOOGL")

    assert call_count["count"] == 2


def test_safe_params_for_log_masks_api_token() -> None:
    fetcher = FreeInternationalNewsFetcher(api_token="demo-token")

    safe_params = fetcher._safe_params_for_log(
        {
            "api_token": "demo-token",
            "symbols": "AAPL",
            "limit": 3,
        }
    )

    assert safe_params["api_token"] == "***"
    assert safe_params["symbols"] == "AAPL"


def test_fetch_news_handles_non_json_error_response_without_leaking_token(monkeypatch, capsys) -> None:
    class NonJsonResponse(DummyResponse):
        def json(self) -> dict:
            raise ValueError("not json")

    monkeypatch.setattr(
        "app_core.data_sources.international_news.requests.get",
        lambda url, *, params, timeout: NonJsonResponse(
            400,
            {},
            text="bad request payload from upstream",
        ),
    )

    fetcher = FreeInternationalNewsFetcher(api_token="demo-token")

    assert fetcher.fetch_news("AAPL") == []
    captured = capsys.readouterr()
    assert "bad request payload from upstream" in captured.out
    assert "demo-token" not in captured.out
