import json
from pathlib import Path
from typing import Any

from app_core.path_utils import get_project_root


def load_settings() -> dict[str, Any]:
    """Load project settings from config/settings.json."""
    settings_path = get_project_root() / "config" / "settings.json"
    with settings_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_json(relative_path: str) -> dict[str, Any]:
    """Load a JSON file using a project-relative path."""
    file_path = get_project_root() / Path(relative_path)
    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)
