import sys

import app


def test_main_version_outputs_version_info(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "--version"])

    result = app.main()
    captured = capsys.readouterr()

    assert result == 0
    assert "AShare Insight Lab 0.3.1 (Historical Query & Signal Change Summary)" in captured.out


def test_main_about_outputs_project_metadata(monkeypatch, capsys) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "about"])
    monkeypatch.setattr(
        app,
        "load_settings",
        lambda: {
            "environment": "development",
        },
    )

    result = app.main()
    captured = capsys.readouterr()

    assert result == 0
    assert "开发者: pL" in captured.out
    assert "维护者: pL" in captured.out
    assert "Copyright © 2026 @B‘lock10STUdio. All rights reserved." in captured.out
    assert "https://github.com/usydin/Ashare-insight-lab" in captured.out
    assert "仅用于研究和模拟盘验证，不构成实盘交易建议。" in captured.out


def test_main_check_data_source_invokes_doctor(monkeypatch) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "check-data-source"])
    monkeypatch.setattr(app, "run_data_source_doctor", lambda: 0)

    assert app.main() == 0


def test_main_doctor_invokes_doctor(monkeypatch) -> None:
    monkeypatch.setattr(sys, "argv", ["app.py", "doctor"])
    monkeypatch.setattr(app, "run_data_source_doctor", lambda: 0)

    assert app.main() == 0
