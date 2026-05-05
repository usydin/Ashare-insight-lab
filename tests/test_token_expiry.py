from __future__ import annotations

import base64
import json
from datetime import datetime, timedelta, timezone

from app_core.security.token_expiry import analyze_token_expiry


def _build_jwt(payload: dict[str, object]) -> str:
    header = {"alg": "HS256", "typ": "JWT"}
    encoded_header = base64.urlsafe_b64encode(json.dumps(header).encode("utf-8")).decode("ascii").rstrip("=")
    encoded_payload = base64.urlsafe_b64encode(json.dumps(payload).encode("utf-8")).decode("ascii").rstrip("=")
    return f"{encoded_header}.{encoded_payload}.signature"


def test_analyze_token_expiry_parses_jwt_exp() -> None:
    now = datetime(2026, 5, 1, 0, 0, 0, tzinfo=timezone.utc)
    token = _build_jwt(
        {
            "exp": int((now + timedelta(days=90)).timestamp()),
            "iat": int(now.timestamp()),
            "iss": "longbridge",
            "aud": "quote",
            "scope": "quote.read",
        }
    )

    result = analyze_token_expiry(token, now=now)

    assert result["status"] == "ok"
    assert result["expires_at_utc"] == "2026-07-30T00:00:00+00:00"
    assert result["issued_at_utc"] == "2026-05-01T00:00:00+00:00"
    assert result["iss"] == "longbridge"
    assert result["aud"] == "quote"
    assert result["scope"] == "quote.read"


def test_analyze_token_expiry_returns_expired() -> None:
    now = datetime(2026, 5, 1, 0, 0, 0, tzinfo=timezone.utc)
    token = _build_jwt({"exp": int((now - timedelta(days=1)).timestamp())})

    result = analyze_token_expiry(token, now=now)

    assert result["status"] == "expired"
    assert result["seconds_remaining"] < 0


def test_analyze_token_expiry_returns_danger_within_7_days() -> None:
    now = datetime(2026, 5, 1, 0, 0, 0, tzinfo=timezone.utc)
    token = _build_jwt({"exp": int((now + timedelta(days=5)).timestamp())})

    result = analyze_token_expiry(token, now=now)

    assert result["status"] == "danger"


def test_analyze_token_expiry_returns_warning_within_30_days() -> None:
    now = datetime(2026, 5, 1, 0, 0, 0, tzinfo=timezone.utc)
    token = _build_jwt({"exp": int((now + timedelta(days=20)).timestamp())})

    result = analyze_token_expiry(token, now=now)

    assert result["status"] == "warning"


def test_analyze_token_expiry_returns_not_jwt_for_opaque_token() -> None:
    result = analyze_token_expiry("opaque-token-value")

    assert result["status"] == "not_jwt"
    assert "JWT-like" in result["message"]


def test_analyze_token_expiry_returns_missing_for_empty_token() -> None:
    result = analyze_token_expiry("")

    assert result["status"] == "missing"


def test_analyze_token_expiry_returns_invalid_for_broken_payload() -> None:
    result = analyze_token_expiry("aaa.bbb.ccc")

    assert result["status"] == "invalid"


def test_analyze_token_expiry_does_not_leak_token_value() -> None:
    now = datetime(2026, 5, 1, 0, 0, 0, tzinfo=timezone.utc)
    token = _build_jwt({"exp": int((now + timedelta(days=90)).timestamp())})

    result = analyze_token_expiry(token, now=now)

    assert token not in json.dumps(result, ensure_ascii=False)
