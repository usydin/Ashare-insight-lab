from datetime import datetime

from app_core.config_loader import load_settings
from app_core.path_utils import get_project_root


def main() -> None:
    settings = load_settings()
    project_root = get_project_root()
    current_time = datetime.now().isoformat(timespec="seconds")

    print(f"项目名称: {settings['project_name']}")
    print(f"英文名称: {settings['project_name_en']}")
    print(f"版本号: {settings['version']}")
    print(f"当前环境: {settings['environment']}")
    print(f"项目根目录: {project_root}")
    print(f"当前时间: {current_time}")
    print("提示: V0.1 dev skeleton is ready.")


if __name__ == "__main__":
    main()
