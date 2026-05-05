from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any

from app_core.path_utils import get_project_root
from app_core.security.token_expiry import analyze_token_expiry


SECRET_SPECS: dict[str, dict[str, Any]] = {
    "MARKETAUX_API_TOKEN": {
        "provider": "Marketaux",
        "display_name": "Marketaux 新闻 API",
        "note": "国际市场新闻",
        "supports_expiry_monitor": True,
    },
    "LONGBRIDGE_OAUTH_CLIENT_ID": {
        "provider": "Longbridge",
        "display_name": "Longbridge OAuth Client ID",
        "note": "OAuthBuilder 授权专用 Client ID，不等同于 App Key。",
        "supports_expiry_monitor": False,
    },
    "LONGBRIDGE_APP_KEY": {
        "provider": "Longbridge",
        "display_name": "Longbridge App Key",
        "note": "只读实时行情",
    },
    "LONGBRIDGE_APP_SECRET": {
        "provider": "Longbridge",
        "display_name": "Longbridge App Secret",
        "note": "只读实时行情",
    },
    "LONGBRIDGE_ACCESS_TOKEN": {
        "provider": "Longbridge",
        "display_name": "Longbridge Access Token",
        "note": "只读实时行情 / OAuth 兼容",
        "supports_expiry_monitor": True,
    },
    "LONGBRIDGE_REGION": {
        "provider": "Longbridge",
        "display_name": "Longbridge Region",
        "note": "区域配置",
    },
    "LONGBRIDGE_HTTP_URL": {
        "provider": "Longbridge",
        "display_name": "Longbridge HTTP URL",
        "note": "覆盖默认 API 地址 (可选)",
    },
    "LONGBRIDGE_QUOTE_WS_URL": {
        "provider": "Longbridge",
        "display_name": "Longbridge WS URL",
        "note": "覆盖默认行情 WebSocket 地址 (可选)",
    },
    "OPENAI_API_KEY": {
        "provider": "OpenAI",
        "display_name": "OpenAI API Key",
        "note": "后续 AI 研报与摘要",
        "supports_expiry_monitor": True,
    },
    "TUSHARE_TOKEN": {
        "provider": "Tushare",
        "display_name": "Tushare Pro Token",
        "note": "预留：A股历史/财务/基础数据",
        "supports_expiry_monitor": True,
    },
}


class LocalSecretManager:
    """本地 .env / .secrets Secret 管理器。"""

    def __init__(self, project_root: Path | None = None) -> None:
        self.project_root = project_root or get_project_root()
        self.env_path = self.project_root / ".env"
        self.secrets_dir = self.project_root / ".secrets"
        self.metadata_path = self.secrets_dir / "token_metadata.json"

    @staticmethod
    def load_local_env_to_process_env(
        project_root: Path | None = None, override: bool = False
    ) -> dict[str, Any]:
        """将本地 .env 中的已知 Key 加载到 os.environ。"""
        root = project_root or get_project_root()
        env_path = root / ".env"
        
        summary = {
            "source_path": str(env_path),
            "missing_file": not env_path.exists(),
            "loaded_keys": [],
            "skipped_existing_keys": [],
            "empty_keys": [],
        }

        if not env_path.exists():
            return summary

        # 借用内部读取逻辑
        temp_manager = LocalSecretManager(project_root=root)
        env_values = temp_manager._read_env_file()

        known_keys = list(SECRET_SPECS.keys())

        for key in known_keys:
            if key not in env_values:
                continue
            
            value = env_values[key]
            if not value:
                summary["empty_keys"].append(key)
                continue

            if key in os.environ and not override:
                summary["skipped_existing_keys"].append(key)
                continue

            os.environ[key] = value
            summary["loaded_keys"].append(key)

        return summary

    def get_secret_statuses(self) -> list[dict[str, Any]]:
        env_values = self._read_env_file()
        metadata = self._read_metadata()
        checked_at = datetime.now().isoformat(timespec="seconds")
        results: list[dict[str, Any]] = []

        for key, spec in SECRET_SPECS.items():
            env_file_has_key = key in env_values
            env_file_value = env_values.get(key, "")
            process_value = os.getenv(key, "")

            if env_file_has_key:
                source = ".env"
                raw_value = env_file_value
            elif process_value:
                source = "environment"
                raw_value = process_value
            else:
                source = "missing"
                raw_value = ""

            if source == "missing":
                status = "missing"
            elif str(raw_value).strip() == "":
                status = "empty"
            else:
                status = "configured"

            masked = self.mask_secret(raw_value)
            existing_metadata = metadata.get(key, {})
            updated_at = str(existing_metadata.get("updated_at", ""))

            item = {
                "key": key,
                "provider": spec["provider"],
                "display_name": spec["display_name"],
                "status": status,
                "source": source,
                "masked": masked,
                "length": len(str(raw_value)) if raw_value else 0,
                "updated_at": updated_at,
                "last_checked_at": checked_at,
                "note": str(existing_metadata.get("note") or spec["note"]),
                "supports_expiry_monitor": bool(spec.get("supports_expiry_monitor", False)),
            }
            if item["supports_expiry_monitor"]:
                item.update(self._build_expiry_fields(raw_value))
            results.append(item)

            metadata[key] = {
                **existing_metadata,
                "created_at": str(existing_metadata.get("created_at", "")),
                "updated_at": updated_at,
                "last_checked_at": checked_at,
                "last_used_for": str(existing_metadata.get("last_used_for", "")),
                "note": item["note"],
                "masked": masked,
                "status": status,
            }

        self._write_metadata(metadata)
        return results

    def get_token_expiry_statuses(self) -> list[dict[str, Any]]:
        statuses = self.get_secret_statuses()
        return [item for item in statuses if bool(item.get("supports_expiry_monitor"))]

    def set_secret(self, key: str, value: str, note: str | None = None) -> dict[str, Any]:
        normalized_key = self._validate_key(key)
        normalized_value = str(value).strip()
        env_values = self._read_env_file()
        env_values[normalized_key] = normalized_value
        self._write_env_file(env_values)

        metadata = self._read_metadata()
        now = datetime.now().isoformat(timespec="seconds")
        existing = metadata.get(normalized_key, {})
        metadata[normalized_key] = {
            "created_at": str(existing.get("created_at") or now),
            "updated_at": now,
            "last_checked_at": str(existing.get("last_checked_at", "")),
            "last_used_for": str(existing.get("last_used_for", "")),
            "note": note or SECRET_SPECS[normalized_key]["note"],
            "masked": self.mask_secret(normalized_value),
            "status": "configured" if normalized_value else "empty",
        }
        self._write_metadata(metadata)
        return self.get_secret_status(normalized_key)

    def clear_secret(self, key: str) -> dict[str, Any]:
        normalized_key = self._validate_key(key)
        env_values = self._read_env_file()
        env_values[normalized_key] = ""
        self._write_env_file(env_values)

        metadata = self._read_metadata()
        now = datetime.now().isoformat(timespec="seconds")
        existing = metadata.get(normalized_key, {})
        metadata[normalized_key] = {
            "created_at": str(existing.get("created_at") or now),
            "updated_at": now,
            "last_checked_at": str(existing.get("last_checked_at", "")),
            "last_used_for": str(existing.get("last_used_for", "")),
            "note": str(existing.get("note") or SECRET_SPECS[normalized_key]["note"]),
            "masked": "",
            "status": "empty",
        }
        self._write_metadata(metadata)
        return self.get_secret_status(normalized_key)

    def get_secret_status(self, key: str) -> dict[str, Any]:
        normalized_key = self._validate_key(key)
        statuses = self.get_secret_statuses()
        for item in statuses:
            if item["key"] == normalized_key:
                return item
        raise KeyError(normalized_key)

    def record_secret_usage(self, key: str, purpose: str) -> None:
        normalized_key = self._validate_key(key)
        metadata = self._read_metadata()
        existing = metadata.get(normalized_key, {})
        metadata[normalized_key] = {
            "created_at": str(existing.get("created_at", "")),
            "updated_at": str(existing.get("updated_at", "")),
            "last_checked_at": str(existing.get("last_checked_at", "")),
            "last_used_for": purpose,
            "note": str(existing.get("note") or SECRET_SPECS[normalized_key]["note"]),
            "masked": str(existing.get("masked", "")),
            "status": str(existing.get("status", "missing")),
        }
        self._write_metadata(metadata)

    def mask_secret(self, value: str) -> str:
        normalized = str(value or "").strip()
        if not normalized:
            return ""
        if len(normalized) <= 4:
            return "****"
        return f"****{normalized[-4:]}"

    def _build_expiry_fields(self, raw_value: str) -> dict[str, Any]:
        expiry = analyze_token_expiry(str(raw_value or ""))
        return {
            "expires_at_utc": expiry["expires_at_utc"],
            "issued_at_utc": expiry["issued_at_utc"],
            "not_before_utc": expiry["not_before_utc"],
            "days_remaining": expiry["days_remaining"],
            "seconds_remaining": expiry["seconds_remaining"],
            "expiry_status": expiry["status"],
            "expiry_message": expiry["message"],
            "manual_expires_at": expiry["manual_expires_at"],
        }

    def _validate_key(self, key: str) -> str:
        normalized_key = str(key).strip()
        if normalized_key not in SECRET_SPECS:
            raise ValueError(f"不支持的 key: {normalized_key}")
        return normalized_key

    def _read_env_file(self) -> dict[str, str]:
        if not self.env_path.exists():
            return {}

        values: dict[str, str] = {}
        for raw_line in self.env_path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            parsed_value = value.strip()
            if len(parsed_value) >= 2 and parsed_value[0] == parsed_value[-1] and parsed_value[0] in {"'", '"'}:
                parsed_value = parsed_value[1:-1]
            values[key.strip()] = parsed_value
        return values

    def _write_env_file(self, env_values: dict[str, str]) -> None:
        ordered_keys = list(env_values.keys())
        lines = [f"{key}={env_values[key]}" for key in ordered_keys]
        self.env_path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
        os.chmod(self.env_path, 0o600)

    def _read_metadata(self) -> dict[str, dict[str, Any]]:
        if not self.metadata_path.exists():
            return {}
        try:
            raw = json.loads(self.metadata_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
        if not isinstance(raw, dict):
            return {}
        return {str(key): value for key, value in raw.items() if isinstance(value, dict)}

    def _write_metadata(self, metadata: dict[str, dict[str, Any]]) -> None:
        self.secrets_dir.mkdir(parents=True, exist_ok=True)
        self.metadata_path.write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        try:
            os.chmod(self.metadata_path, 0o600)
        except OSError:
            pass
