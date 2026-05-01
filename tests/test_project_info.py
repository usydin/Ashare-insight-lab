from app_core import project_info


def test_project_info_has_required_core_fields() -> None:
    assert project_info.APP_NAME_CN == "A股智研台"
    assert project_info.APP_NAME_EN == "AShare Insight Lab"
    assert project_info.VERSION == "0.1.2"
    assert project_info.DEVELOPER == "pL"
    assert project_info.MAINTAINER == "pL"
    assert project_info.COPYRIGHT_OWNER == "@B‘lock10STUdio"
    assert "Copyright © 2026" in project_info.COPYRIGHT_TEXT
    assert project_info.REPOSITORY_URL == "https://github.com/usydin/Ashare-insight-lab"
    assert "研究和模拟盘验证" in project_info.SAFETY_NOTICE
