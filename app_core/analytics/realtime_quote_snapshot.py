from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any

from app_core.data_sources.longbridge_quote_provider import LongbridgeQuoteProvider
from app_core.data_sources.longbridge_sdk_support import (
    build_longbridge_quote_context_via_oauth,
    fetch_longbridge_quote_with_context,
)
from app_core.path_utils import get_project_root
from app_core.security.local_secret_manager import LocalSecretManager
from app_core.security.longbridge_oauth_store import LongbridgeOAuthStore
from app_core.storage.file_store import ensure_directory


DEFAULT_LONGBRIDGE_QUOTE_TARGETS = [
    {"symbol": "600519", "market": "CN"},
    {"symbol": "300750", "market": "CN"},
    {"symbol": "000001", "market": "CN"},
    {"symbol": "700", "market": "HK"},
    {"symbol": "AAPL", "market": "US"},
]


def build_longbridge_realtime_quote_snapshot(
    project_root: Path | None = None,
    targets: list[dict[str, str]] | None = None,
) -> dict[str, Any]:
    LocalSecretManager.load_local_env_to_process_env(project_root=project_root)

    provider = LongbridgeQuoteProvider(project_root=project_root)
    store = LongbridgeOAuthStore(project_root=project_root)
    client_id = os.getenv("LONGBRIDGE_OAUTH_CLIENT_ID", "").strip()
    quote_targets = targets or DEFAULT_LONGBRIDGE_QUOTE_TARGETS
    generated_at = datetime.now().isoformat(timespec="seconds")

    snapshot = {
        "provider": "longbridge",
        "generated_at": generated_at,
        "status": "ok",
        "message": "",
        "quote_only": True,
        "trade_enabled": False,
        "items": [],
    }

    context_result = build_longbridge_quote_context_via_oauth(client_id=client_id, store=store)
    if context_result["status"] != "authorized":
        snapshot["status"] = str(context_result["status"])
        snapshot["message"] = str(context_result.get("message", "") or "Longbridge OAuth 未就绪。")
        snapshot["items"] = [
            _build_snapshot_item(
                symbol=target["symbol"],
                market=target["market"],
                longbridge_symbol=provider._to_longbridge_symbol(target["symbol"], target["market"]) or "",
                data_status=str(context_result["status"]),
                message=snapshot["message"],
            )
            for target in quote_targets
        ]
        return snapshot

    ctx = context_result["ctx"]
    items: list[dict[str, Any]] = []
    for target in quote_targets:
        symbol = str(target["symbol"]).strip()
        market = str(target["market"]).strip().upper()
        raw_symbol = provider._to_longbridge_symbol(symbol, market)

        if raw_symbol is None:
            items.append(
                _build_snapshot_item(
                    symbol=symbol,
                    market=market,
                    longbridge_symbol="",
                    data_status="unsupported_symbol",
                    message="股票代码格式不支持",
                )
            )
            continue

        result = fetch_longbridge_quote_with_context(
            ctx=ctx,
            symbol=symbol,
            raw_symbol=raw_symbol,
            authorization_url=context_result.get("authorization_url", ""),
        )
        items.append(
            _build_snapshot_item(
                symbol=symbol,
                market=market,
                longbridge_symbol=raw_symbol,
                data_status=str(result.get("data_status", "fetch_failed")),
                message=_resolve_item_message(
                    market=market,
                    data_status=str(result.get("data_status", "fetch_failed")),
                    message=str(result.get("message", "") or result.get("error_message", "")),
                ),
                name=str(result.get("name", "") or ""),
                price=result.get("current_price"),
                change=result.get("change"),
                change_percent=result.get("change_percent"),
                volume=result.get("volume"),
                turnover=result.get("turnover"),
                quote_time=str(result.get("timestamp", "") or ""),
            )
        )

    snapshot["items"] = items
    if items and not any(item["data_status"] == "ok" for item in items):
        snapshot["status"] = "degraded"
    elif any(item["data_status"] != "ok" for item in items):
        snapshot["status"] = "partial_ok"
    return snapshot


def write_longbridge_realtime_quote_snapshot_json(
    output_path: str | Path = "data/processed/longbridge_quote_snapshot.json",
    project_root: Path | None = None,
    targets: list[dict[str, str]] | None = None,
) -> Path:
    snapshot = build_longbridge_realtime_quote_snapshot(project_root=project_root, targets=targets)
    root = project_root or get_project_root()
    path = root / output_path if not Path(output_path).is_absolute() else Path(output_path)
    ensure_directory(path.parent)
    path.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def load_longbridge_realtime_quote_snapshot(
    input_path: str | Path = "data/processed/longbridge_quote_snapshot.json",
    project_root: Path | None = None,
) -> dict[str, Any]:
    root = project_root or get_project_root()
    path = root / input_path if not Path(input_path).is_absolute() else Path(input_path)
    if not path.exists():
        return _build_empty_snapshot()

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return _build_empty_snapshot(message="Longbridge 行情快照文件损坏。", status="invalid_json")

    if not isinstance(data, dict):
        return _build_empty_snapshot(message="Longbridge 行情快照结构无效。", status="invalid_json")

    return {
        "provider": str(data.get("provider", "longbridge") or "longbridge"),
        "generated_at": str(data.get("generated_at", "") or ""),
        "status": str(data.get("status", "missing") or "missing"),
        "message": str(data.get("message", "") or ""),
        "quote_only": bool(data.get("quote_only", True)),
        "trade_enabled": bool(data.get("trade_enabled", False)),
        "items": list(data.get("items", [])),
    }


def _build_snapshot_item(
    *,
    symbol: str,
    market: str,
    longbridge_symbol: str,
    data_status: str,
    message: str,
    name: str = "",
    price: Any = None,
    change: Any = None,
    change_percent: Any = None,
    volume: Any = None,
    turnover: Any = None,
    quote_time: str = "",
) -> dict[str, Any]:
    return {
        "symbol": symbol,
        "market": market,
        "longbridge_symbol": longbridge_symbol,
        "name": name,
        "price": price,
        "change": change,
        "change_percent": change_percent,
        "volume": volume,
        "turnover": turnover,
        "quote_time": quote_time,
        "data_status": data_status,
        "provider": "longbridge",
        "quote_only": True,
        "trade_enabled": False,
        "message": message,
    }


def _resolve_item_message(*, market: str, data_status: str, message: str) -> str:
    if data_status == "ok" and market == "CN":
        return "A股行情时间可能为最近交易日数据，请结合 quote_time 判断。"
    return message


def _build_empty_snapshot(message: str = "", status: str = "missing") -> dict[str, Any]:
    return {
        "provider": "longbridge",
        "generated_at": "",
        "status": status,
        "message": message,
        "quote_only": True,
        "trade_enabled": False,
        "items": [],
    }
