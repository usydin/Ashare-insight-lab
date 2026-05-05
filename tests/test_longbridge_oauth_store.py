from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

from app_core.security.longbridge_oauth_store import LongbridgeOAuthStore


def test_status_missing_when_token_file_absent(tmp_path: Path) -> None:
    store = LongbridgeOAuthStore(project_root=tmp_path)
    status = store.get_oauth_token_status()

    assert status["status"] == "missing"
    assert status["token_file"] == "missing"
    assert status["access_token"] == "missing"


def test_save_token_marks_status_configured(tmp_path: Path) -> None:
    store = LongbridgeOAuthStore(project_root=tmp_path)
    status = store.save_oauth_token(
        {
            "access_token": "oauth_demo",
            "refresh_token": "refresh_demo",
            "expires_at": (datetime.now(timezone.utc) + timedelta(days=1)).isoformat(timespec="seconds"),
        }
    )

    assert status["status"] == "configured"
    assert status["access_token"] == "present"
    assert status["has_refresh_token"] is True


def test_masked_status_does_not_leak_access_token(tmp_path: Path) -> None:
    store = LongbridgeOAuthStore(project_root=tmp_path)
    status = store.save_oauth_token(
        {
            "access_token": "oauth_demo",
            "expires_at": (datetime.now(timezone.utc) + timedelta(days=1)).isoformat(timespec="seconds"),
        }
    )

    assert status["masked_access_token"] == "****demo"
    assert "oauth_demo" not in json.dumps(status, ensure_ascii=False)


def test_refresh_flag_only(tmp_path: Path) -> None:
    store = LongbridgeOAuthStore(project_root=tmp_path)
    status = store.save_oauth_token(
        {
            "access_token": "oauth_demo",
            "refresh_token": "refresh_demo",
        }
    )

    assert status["has_refresh_token"] is True
    assert status["refresh_token"] == "present"
    assert "refresh_demo" not in json.dumps(status, ensure_ascii=False)


def test_expired_token_returns_expired_status(tmp_path: Path) -> None:
    store = LongbridgeOAuthStore(project_root=tmp_path)
    status = store.save_oauth_token(
        {
            "access_token": "oauth_demo",
            "expires_at": (datetime.now(timezone.utc) - timedelta(days=1)).isoformat(timespec="seconds"),
        }
    )

    assert status["status"] == "expired"


def test_invalid_json_returns_invalid_json_status(tmp_path: Path) -> None:
    store = LongbridgeOAuthStore(project_root=tmp_path)
    store.secrets_dir.mkdir(parents=True, exist_ok=True)
    store.token_path.write_text("{invalid-json", encoding="utf-8")

    status = store.get_oauth_token_status()

    assert status["status"] == "invalid_json"
    assert status["token_file"] == "configured"


def test_clear_removes_token_file(tmp_path: Path) -> None:
    store = LongbridgeOAuthStore(project_root=tmp_path)
    store.save_oauth_token({"access_token": "oauth_demo"})

    result = store.clear_oauth_token()

    assert result["status"] == "missing"
    assert not store.token_path.exists()


def test_save_metadata_marks_sdk_managed_without_leaking_token(tmp_path: Path) -> None:
    store = LongbridgeOAuthStore(project_root=tmp_path)
    status = store.save_oauth_metadata(
        {
            "scope": "quote",
            "sdk_managed": True,
            "note": "quote only; sdk managed",
        }
    )

    assert status["token_file"] == "configured"
    assert status["sdk_managed"] is True
    assert status["access_token"] == "missing"


def test_token_file_permissions_are_private(tmp_path: Path) -> None:
    store = LongbridgeOAuthStore(project_root=tmp_path)
    store.save_oauth_token({"access_token": "oauth_demo"})

    mode = store.token_path.stat().st_mode & 0o777
    assert mode == 0o600


def test_gitignore_covers_secret_directory() -> None:
    gitignore = Path("/Users/balwyn/Documents/trae_projects/ashare-insight-lab/.gitignore").read_text(encoding="utf-8")
    assert ".secrets/" in gitignore
