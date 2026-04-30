import logging
from pathlib import Path

from app_core.path_utils import get_project_root


LOGGER_NAME = "ashare_insight_lab"


def get_logger(log_file_path: str | Path = "logs/app.log") -> logging.Logger:
    """Return a configured project logger."""
    logger = logging.getLogger(LOGGER_NAME)
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    file_path = get_project_root() / Path(log_file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(file_path, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.propagate = False
    return logger
