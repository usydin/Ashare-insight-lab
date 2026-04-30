from pathlib import Path

import pandas as pd

from app_core.path_utils import get_project_root


def ensure_directory(relative_dir: str | Path) -> Path:
    """Create a project-relative directory if it does not exist."""
    directory = Path(relative_dir)
    if not directory.is_absolute():
        directory = get_project_root() / directory
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def save_dataframe_csv(
    dataframe: pd.DataFrame,
    relative_path: str | Path,
    *,
    index: bool = False,
) -> Path:
    """Save a DataFrame to a project-relative CSV file."""
    file_path = Path(relative_path)
    if not file_path.is_absolute():
        file_path = get_project_root() / file_path
    file_path.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(file_path, index=index, encoding="utf-8-sig")
    return file_path


def write_text_file(content: str, relative_path: str | Path) -> Path:
    """Write UTF-8 text to a project-relative file."""
    file_path = Path(relative_path)
    if not file_path.is_absolute():
        file_path = get_project_root() / file_path
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding="utf-8")
    return file_path
