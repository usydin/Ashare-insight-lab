from __future__ import annotations

import json
from pathlib import Path

from app_core.security.local_secret_manager import LocalSecretManager


def test_env_missing_does_not_crash(tmp_path: Path, monkeypatch) -> None:
    # 确保环境变量缺失，避免 fallback 到真实环境
    monkeypatch.delenv("MARKETAUX_API_TOKEN", raising=False)
    
    manager = LocalSecretManager(project_root=tmp_path)
    statuses = manager.get_secret_statuses()

    assert statuses
    marketaux = next(item for item in statuses if item["key"] == "MARKETAUX_API_TOKEN")
    assert marketaux["status"] == "missing"
    assert marketaux["source"] == "missing"


def test_reads_present_and_missing_statuses(tmp_path: Path) -> None:
    (tmp_path / ".env").write_text("MARKETAUX_API_TOKEN=demo-secret-1234\nOPENAI_API_KEY=\n", encoding="utf-8")
    manager = LocalSecretManager(project_root=tmp_path)

    statuses = manager.get_secret_statuses()
    marketaux = next(item for item in statuses if item["key"] == "MARKETAUX_API_TOKEN")
    openai = next(item for item in statuses if item["key"] == "OPENAI_API_KEY")

    assert marketaux["status"] == "configured"
    assert marketaux["source"] == ".env"
    assert openai["status"] == "empty"


def test_masked_never_leaks_full_token(tmp_path: Path) -> None:
    manager = LocalSecretManager(project_root=tmp_path)

    assert manager.mask_secret("") == ""
    assert manager.mask_secret("abcd") == "****"
    assert manager.mask_secret("abcdefgh") == "****efgh"


def test_set_secret_creates_and_updates_env(tmp_path: Path) -> None:
    manager = LocalSecretManager(project_root=tmp_path)

    result = manager.set_secret("MARKETAUX_API_TOKEN", "demo-secret-1234")

    env_content = (tmp_path / ".env").read_text(encoding="utf-8")
    assert "MARKETAUX_API_TOKEN=demo-secret-1234" in env_content
    assert result["status"] == "configured"
    assert result["masked"] == "****1234"


def test_clear_secret_only_affects_target_key(tmp_path: Path) -> None:
    env_path = tmp_path / ".env"
    env_path.write_text(
        "MARKETAUX_API_TOKEN=demo-secret-1234\nOPENAI_API_KEY=openai-secret-5678\n",
        encoding="utf-8",
    )
    manager = LocalSecretManager(project_root=tmp_path)

    result = manager.clear_secret("MARKETAUX_API_TOKEN")
    env_content = env_path.read_text(encoding="utf-8")

    assert "MARKETAUX_API_TOKEN=\n" in env_content
    assert "OPENAI_API_KEY=openai-secret-5678" in env_content
    assert result["status"] == "empty"


def test_metadata_does_not_store_real_token(tmp_path: Path) -> None:
    manager = LocalSecretManager(project_root=tmp_path)
    manager.set_secret("MARKETAUX_API_TOKEN", "demo-secret-1234")

    metadata = json.loads((tmp_path / ".secrets" / "token_metadata.json").read_text(encoding="utf-8"))
    marketaux = metadata["MARKETAUX_API_TOKEN"]

    assert marketaux["masked"] == "****1234"
    assert "demo-secret-1234" not in json.dumps(metadata, ensure_ascii=False)


def test_gitignore_covers_env_and_secrets() -> None:
    gitignore = Path("/Users/balwyn/Documents/trae_projects/ashare-insight-lab/.gitignore").read_text(encoding="utf-8")
    assert ".env" in gitignore
    assert ".secrets/" in gitignore


def test_record_secret_usage_updates_metadata(tmp_path: Path) -> None:
    manager = LocalSecretManager(project_root=tmp_path)
    manager.set_secret("MARKETAUX_API_TOKEN", "demo-secret-1234")
    manager.record_secret_usage("MARKETAUX_API_TOKEN", "marketaux-status")

    metadata = json.loads((tmp_path / ".secrets" / "token_metadata.json").read_text(encoding="utf-8"))
    assert metadata["MARKETAUX_API_TOKEN"]["last_used_for"] == "marketaux-status"


def test_load_local_env_to_process_env(tmp_path: Path, monkeypatch) -> None:
    # 准备测试数据
    (tmp_path / ".env").write_text(
        "MARKETAUX_API_TOKEN=demo-token-1234\n"
        "LONGBRIDGE_APP_KEY=key-5678\n"
        "LONGBRIDGE_OAUTH_CLIENT_ID=cli-1234\n"
        "OPENAI_API_KEY=\n",  # 空值
        encoding="utf-8"
    )
    
    # 确保环境变量初始为空
    monkeypatch.delenv("MARKETAUX_API_TOKEN", raising=False)
    monkeypatch.delenv("LONGBRIDGE_APP_KEY", raising=False)
    monkeypatch.delenv("LONGBRIDGE_OAUTH_CLIENT_ID", raising=False)
    monkeypatch.setenv("EXISTING_TOKEN", "already-set")
    
    # 执行加载
    summary = LocalSecretManager.load_local_env_to_process_env(project_root=tmp_path)
    
    # 验证 os.environ
    import os
    assert os.environ["MARKETAUX_API_TOKEN"] == "demo-token-1234"
    assert os.environ["LONGBRIDGE_APP_KEY"] == "key-5678"
    assert os.environ["LONGBRIDGE_OAUTH_CLIENT_ID"] == "cli-1234"
    assert "OPENAI_API_KEY" not in os.environ
    
    # 验证摘要内容
    assert "MARKETAUX_API_TOKEN" in summary["loaded_keys"]
    assert "LONGBRIDGE_APP_KEY" in summary["loaded_keys"]
    assert "LONGBRIDGE_OAUTH_CLIENT_ID" in summary["loaded_keys"]
    assert "OPENAI_API_KEY" in summary["empty_keys"]
    assert "demo-token-1234" not in str(summary)
    
    # 验证 override=False (默认)
    (tmp_path / ".env").write_text("MARKETAUX_API_TOKEN=new-token\n", encoding="utf-8")
    summary2 = LocalSecretManager.load_local_env_to_process_env(project_root=tmp_path)
    assert os.environ["MARKETAUX_API_TOKEN"] == "demo-token-1234"  # 未改变
    assert "MARKETAUX_API_TOKEN" in summary2["skipped_existing_keys"]
    
    # 验证 override=True
    summary3 = LocalSecretManager.load_local_env_to_process_env(project_root=tmp_path, override=True)
    assert os.environ["MARKETAUX_API_TOKEN"] == "new-token"
    assert "MARKETAUX_API_TOKEN" in summary3["loaded_keys"]
