from __future__ import annotations

import base64
import json
from datetime import datetime, timezone
from typing import Any


def analyze_token_expiry(
    token: str,
    *,
    now: datetime | None = None,
) -> dict[str, Any]:
    normalized = str(token or "").strip()
    current_time = now.astimezone(timezone.utc) if now else datetime.now(timezone.utc)

    result = {
        "status": "missing",
        "expires_at_utc": "",
        "issued_at_utc": "",
        "not_before_utc": "",
        "days_remaining": None,
        "seconds_remaining": None,
        "message": "token 缺失",
        "is_jwt_like": False,
        "iss": "",
        "aud": "",
        "scope": "",
        "manual_expires_at": "",
    }

    if not normalized:
        return result

    if normalized.count(".") != 2:
        result["status"] = "not_jwt"
        result["message"] = "当前 token 不是 JWT-like，需人工维护到期日期"
        return result

    result["is_jwt_like"] = True
    parts = normalized.split(".")
    payload_part = parts[1]

    try:
        payload_data = _decode_jwt_payload(payload_part)
    except Exception:
        result["status"] = "invalid"
        result["message"] = "JWT-like token 解析失败"
        return result

    exp_timestamp = _coerce_timestamp(payload_data.get("exp"))
    if exp_timestamp is None:
        result["status"] = "invalid"
        result["message"] = "JWT-like token 缺少可解析的 exp"
        return result

    iat_timestamp = _coerce_timestamp(payload_data.get("iat"))
    nbf_timestamp = _coerce_timestamp(payload_data.get("nbf"))

    expires_at = datetime.fromtimestamp(exp_timestamp, tz=timezone.utc)
    result["expires_at_utc"] = expires_at.isoformat(timespec="seconds")

    if iat_timestamp is not None:
        issued_at = datetime.fromtimestamp(iat_timestamp, tz=timezone.utc)
        result["issued_at_utc"] = issued_at.isoformat(timespec="seconds")

    if nbf_timestamp is not None:
        not_before = datetime.fromtimestamp(nbf_timestamp, tz=timezone.utc)
        result["not_before_utc"] = not_before.isoformat(timespec="seconds")

    result["iss"] = _safe_claim_to_text(payload_data.get("iss"))
    result["aud"] = _safe_claim_to_text(payload_data.get("aud"))
    result["scope"] = _safe_claim_to_text(payload_data.get("scope"))

    seconds_remaining = int((expires_at - current_time).total_seconds())
    result["seconds_remaining"] = seconds_remaining
    result["days_remaining"] = int(seconds_remaining // 86400)

    if seconds_remaining < 0:
        result["status"] = "expired"
        result["message"] = "token 已过期，请立即更新"
    elif seconds_remaining <= 7 * 86400:
        result["status"] = "danger"
        result["message"] = "token 将在 7 天内到期，请尽快更新"
    elif seconds_remaining <= 30 * 86400:
        result["status"] = "warning"
        result["message"] = "token 将在 30 天内到期，请提前更新"
    else:
        result["status"] = "ok"
        result["message"] = "token 有效"

    return result


def _decode_jwt_payload(payload_part: str) -> dict[str, Any]:
    padded = payload_part + "=" * (-len(payload_part) % 4)
    decoded = base64.urlsafe_b64decode(padded.encode("ascii"))
    payload = json.loads(decoded.decode("utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("payload must be an object")
    return payload


def _coerce_timestamp(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    if isinstance(value, str):
        stripped = value.strip()
        if not stripped:
            return None
        try:
            return int(float(stripped))
        except ValueError:
            return None
    return None


def _safe_claim_to_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, list):
        items = [str(item).strip() for item in value if str(item).strip()]
        return ", ".join(items)
    return ""
