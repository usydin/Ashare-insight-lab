from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from app_core.path_utils import get_project_root
from app_core.security.local_secret_manager import LocalSecretManager


class LongbridgeOAuthStore:
    """本地 Longbridge OAuth token 存储，仅用于只读行情准备层。"""

    def __init__(self, project_root: Path | None = None) -> None:
        self.project_root = project_root or get_project_root()
        self.secrets_dir = self.project_root / ".secrets"
        self.token_path = self.secrets_dir / "longbridge_oauth_token.json"

    def read_oauth_token(self) -> dict[str, Any] | None:
        raw = self._read_token_json()
        if not isinstance(raw, dict):
            return None
        return raw

    def save_oauth_token(self, data: dict[str, Any]) -> dict[str, Any]:
        existing = self.read_oauth_token() or {}
        now = datetime.now(timezone.utc).isoformat(timespec="seconds")
        payload = {
            "provider": "longbridge",
            "auth_type": "oauth2",
            "access_token": str(data.get("access_token", "")).strip(),
            "refresh_token": str(data.get("refresh_token", "")).strip(),
            "expires_at": str(data.get("expires_at", "")).strip(),
            "scope": str(data.get("scope", "quote")).strip() or "quote",
            "created_at": str(existing.get("created_at") or now),
            "updated_at": now,
            "note": str(data.get("note", "quote only")).strip() or "quote only",
        }
        self._write_token_json(payload)
        return self.get_oauth_token_status()

    def save_oauth_metadata(self, data: dict[str, Any]) -> dict[str, Any]:
        existing = self.read_oauth_token() or {}
        now = datetime.now(timezone.utc).isoformat(timespec="seconds")
        payload = {
            "provider": "longbridge",
            "auth_type": "oauth2",
            "access_token": str(existing.get("access_token", "")).strip(),
            "refresh_token": str(existing.get("refresh_token", "")).strip(),
            "expires_at": str(data.get("expires_at", existing.get("expires_at", ""))).strip(),
            "scope": str(data.get("scope", existing.get("scope", "quote"))).strip() or "quote",
            "created_at": str(existing.get("created_at") or data.get("created_at") or now),
            "updated_at": now,
            "note": str(data.get("note", existing.get("note", "quote only"))).strip() or "quote only",
            "sdk_managed": bool(data.get("sdk_managed", existing.get("sdk_managed", False))),
        }
        self._write_token_json(payload)
        return self.get_oauth_token_status()

    def clear_oauth_token(self) -> dict[str, Any]:
        if self.token_path.exists():
            self.token_path.unlink()
        return {
            "status": "missing",
            "token_file": "missing",
            "access_token": "missing",
            "refresh_token": "missing",
            "has_refresh_token": False,
            "expires_at": "",
            "updated_at": "",
            "masked_access_token": "",
            "token_path": str(self.token_path),
            "sdk_managed": False,
        }

    def get_oauth_token_status(self) -> dict[str, Any]:
        summary = {
            "provider": "longbridge",
            "auth_type": "oauth2",
            "token_file": "missing",
            "access_token": "missing",
            "refresh_token": "missing",
            "has_refresh_token": False,
            "expires_at": "",
            "updated_at": "",
            "masked_access_token": "",
            "status": "missing",
            "token_path": str(self.token_path),
            "note": "quote only",
            "scope": "quote",
            "sdk_managed": False,
        }

        if not self.token_path.exists():
            return summary

        raw = self._read_token_json()
        if not isinstance(raw, dict):
            summary["token_file"] = "configured"
            summary["status"] = "invalid_json"
            return summary

        access_token = str(raw.get("access_token", "")).strip()
        refresh_token = str(raw.get("refresh_token", "")).strip()
        expires_at = str(raw.get("expires_at", "")).strip()
        updated_at = str(raw.get("updated_at", "")).strip()

        summary.update(
            {
                "token_file": "configured",
                "access_token": "present" if access_token else "missing",
                "refresh_token": "present" if refresh_token else "missing",
                "has_refresh_token": bool(refresh_token),
                "expires_at": expires_at,
                "updated_at": updated_at,
                "masked_access_token": LocalSecretManager(self.project_root).mask_secret(access_token),
                "note": str(raw.get("note", "quote only")).strip() or "quote only",
                "scope": str(raw.get("scope", "quote")).strip() or "quote",
                "sdk_managed": bool(raw.get("sdk_managed", False)),
            }
        )

        if summary["sdk_managed"] and not access_token:
            summary["access_token"] = "sdk_managed"
            summary["refresh_token"] = "sdk_managed_or_unknown"
            summary["has_refresh_token"] = False
            summary["masked_access_token"] = ""
            summary["status"] = "sdk_managed_configured"
            return summary

        if not access_token:
            summary["status"] = "missing"
            return summary

        if not expires_at:
            summary["status"] = "unknown_expiry"
            return summary

        expires_at_dt = self._parse_datetime(expires_at)
        if expires_at_dt is None:
            summary["status"] = "unknown"
            return summary

        summary["status"] = "expired" if expires_at_dt <= datetime.now(timezone.utc) else "configured"
        return summary

    def _read_token_json(self) -> dict[str, Any] | None:
        if not self.token_path.exists():
            return None
        try:
            raw = json.loads(self.token_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return None
        if not isinstance(raw, dict):
            return None
        return raw

    def _write_token_json(self, payload: dict[str, Any]) -> None:
        self.secrets_dir.mkdir(parents=True, exist_ok=True)
        self.token_path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        try:
            os.chmod(self.token_path, 0o600)
        except OSError:
            pass

    def _parse_datetime(self, value: str) -> datetime | None:
        normalized = str(value).strip()
        if not normalized:
            return None
        if normalized.endswith("Z"):
            normalized = normalized[:-1] + "+00:00"
        try:
            parsed = datetime.fromisoformat(normalized)
        except ValueError:
            return None
        if parsed.tzinfo is None:
            return parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
