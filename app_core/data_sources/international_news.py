from __future__ import annotations

from datetime import datetime, timedelta, timezone
import os
from typing import Any

import requests


MARKETAUX_NEWS_ENDPOINT = "https://api.marketaux.com/v1/news/all"
DEFAULT_FREE_LIMIT = 3
DEFAULT_TIMEOUT_SECONDS = 10
CACHE_TTL_SECONDS = 3600


class FreeInternationalNewsFetcher:
    """Marketaux 国际新闻免费版适配器。

    该类只提供轻量封装，不在 import 阶段要求必须存在 token。
    如果没有配置 token，`fetch_news()` 会直接返回空列表。
    """

    def __init__(self, api_token: str | None = None, free_limit: int | None = None) -> None:
        self.api_token = (api_token or os.getenv("MARKETAUX_API_TOKEN", "")).strip()
        self.free_limit = self._normalize_free_limit(
            free_limit if free_limit is not None else os.getenv("MARKETAUX_FREE_LIMIT")
        )
        self._cache: dict[str, tuple[datetime, list[dict[str, Any]]]] = {}

    def is_configured(self) -> bool:
        """返回当前是否已配置 API token。"""
        return bool(self.api_token)

    def fetch_news(
        self,
        ticker: str,
        market: str = "US",
        hours_ago: int = 24,
        limit: int = 3,
    ) -> list[dict[str, Any]]:
        """获取指定 ticker 的国际新闻。

        失败时返回空列表，不向上抛异常。
        """
        normalized_ticker = str(ticker).strip().upper()
        normalized_market = str(market).strip().upper() or "US"
        normalized_hours_ago = max(1, int(hours_ago))
        normalized_limit = min(max(1, int(limit)), self.free_limit)

        if not normalized_ticker:
            print("[国际新闻] ticker 为空，跳过请求")
            return []

        if not self.is_configured():
            print("[国际新闻] 未配置 MARKETAUX_API_TOKEN，返回空结果")
            return []

        cache_key = self._build_cache_key(
            normalized_ticker,
            normalized_market,
            normalized_hours_ago,
            normalized_limit,
        )
        cached_news = self._get_cached_news(cache_key)
        if cached_news is not None:
            print(f"[国际新闻] 命中 1 小时缓存: {cache_key}")
            return cached_news

        published_after = (
            datetime.now(timezone.utc) - timedelta(hours=normalized_hours_ago)
        ).replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%S")

        params = {
            "api_token": self.api_token,
            "symbols": normalized_ticker,
            "limit": normalized_limit,
            "published_after": published_after,
            "language": "en,zh",
        }

        try:
            response = requests.get(
                MARKETAUX_NEWS_ENDPOINT,
                params=params,
                timeout=DEFAULT_TIMEOUT_SECONDS,
            )
            if response.status_code != 200:
                print(f"[国际新闻] 请求失败，状态码: {response.status_code}")
                print(f"[国际新闻] 参数摘要: {self._safe_params_for_log(params)}")
                self._log_error_response(response)
                return []

            payload = response.json()
            articles = payload.get("data")
            if not isinstance(articles, list):
                print("[国际新闻] 返回数据中未找到 data 列表")
                return []

            normalized_news = self._normalize_articles(
                articles,
                ticker=normalized_ticker,
                market=normalized_market,
            )
            self._cache[cache_key] = (datetime.now(timezone.utc), normalized_news)
            return normalized_news
        except Exception as error:
            print(f"[国际新闻] 获取新闻失败: {type(error).__name__}")
            return []

    @staticmethod
    def _normalize_free_limit(raw_value: object) -> int:
        try:
            normalized = int(raw_value) if raw_value is not None else DEFAULT_FREE_LIMIT
        except (TypeError, ValueError):
            normalized = DEFAULT_FREE_LIMIT
        return max(1, normalized)

    @staticmethod
    def _build_cache_key(ticker: str, market: str, hours_ago: int, limit: int) -> str:
        return f"{ticker}|{market}|{hours_ago}|{limit}"

    @staticmethod
    def _safe_params_for_log(params: dict[str, Any]) -> dict[str, Any]:
        safe_params = dict(params)
        if "api_token" in safe_params:
            safe_params["api_token"] = "***"
        return safe_params

    def _get_cached_news(self, cache_key: str) -> list[dict[str, Any]] | None:
        cached_item = self._cache.get(cache_key)
        if cached_item is None:
            return None

        cached_at, cached_news = cached_item
        age_seconds = (datetime.now(timezone.utc) - cached_at).total_seconds()
        if age_seconds > CACHE_TTL_SECONDS:
            self._cache.pop(cache_key, None)
            return None
        return cached_news

    def _normalize_articles(
        self,
        articles: list[dict[str, Any]],
        *,
        ticker: str,
        market: str,
    ) -> list[dict[str, Any]]:
        normalized_items: list[dict[str, Any]] = []
        for article in articles:
            if not isinstance(article, dict):
                continue

            title = str(article.get("title") or "").strip()
            if not title:
                continue

            sentiment_label, sentiment_score = self._extract_sentiment(article)
            normalized_items.append(
                {
                    "title": title,
                    "description": str(article.get("description") or ""),
                    "url": str(article.get("url") or ""),
                    "published_at": str(article.get("published_at") or ""),
                    "sentiment": sentiment_label,
                    "sentiment_score": sentiment_score,
                    "source": self._extract_source(article.get("source")),
                    "market": market,
                    "ticker": ticker,
                }
            )
        return normalized_items

    @staticmethod
    def _extract_source(raw_source: object) -> str:
        if isinstance(raw_source, str):
            return raw_source
        if isinstance(raw_source, dict):
            for key in ("name", "title", "domain"):
                value = raw_source.get(key)
                if value:
                    return str(value)
        return ""

    def _extract_sentiment(self, article: dict[str, Any]) -> tuple[str, float | None]:
        top_level_label = str(article.get("sentiment") or "").strip().lower()
        top_level_score = self._to_float(article.get("sentiment_score"))
        if top_level_label:
            return top_level_label, top_level_score

        entities = article.get("entities")
        if isinstance(entities, list):
            for entity in entities:
                if not isinstance(entity, dict):
                    continue
                entity_label = str(entity.get("sentiment") or "").strip().lower()
                entity_score = self._to_float(
                    entity.get("sentiment_score", entity.get("score"))
                )
                if entity_label:
                    return entity_label, entity_score
                if entity_score is not None:
                    return self._score_to_sentiment(entity_score), entity_score

        score = self._to_float(article.get("score"))
        if score is not None:
            return self._score_to_sentiment(score), score

        return "neutral", None

    @staticmethod
    def _score_to_sentiment(score: float) -> str:
        if score > 0.05:
            return "positive"
        if score < -0.05:
            return "negative"
        return "neutral"

    @staticmethod
    def _to_float(raw_value: object) -> float | None:
        try:
            if raw_value is None or raw_value == "":
                return None
            return float(raw_value)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def _log_error_response(response: Any) -> None:
        try:
            payload = response.json()
        except Exception:
            response_text = str(getattr(response, "text", "") or "")
            if response_text:
                print(f"[国际新闻] 错误响应: {response_text[:300]}")
            return

        if not isinstance(payload, dict):
            return

        error_data = payload.get("error")
        if isinstance(error_data, dict):
            error_message = str(error_data.get("message") or "").strip()
            if error_message:
                print(f"[国际新闻] 错误信息: {error_message}")
                return

        fallback_message = str(payload.get("message") or "").strip()
        if fallback_message:
            print(f"[国际新闻] 错误信息: {fallback_message}")


def get_international_news_fetcher() -> FreeInternationalNewsFetcher:
    """延迟创建国际新闻抓取器，避免 import 阶段依赖环境变量。"""
    return FreeInternationalNewsFetcher()
