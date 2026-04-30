from pathlib import Path


def get_project_root() -> Path:
    """Return the project root based on the current file location."""
    return Path(__file__).resolve().parent.parent
