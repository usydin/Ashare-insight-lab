from app_core.config_loader import load_json, load_settings


def test_load_settings_reads_required_fields() -> None:
    settings = load_settings()

    assert settings["project_name"] == "A股智研台"
    assert settings["project_name_en"] == "AShare Insight Lab"
    assert settings["environment"] == "development"
    assert settings["network"]["request_timeout_seconds"] == 10


def test_load_watchlist_reads_entries() -> None:
    watchlist = load_json("config/watchlist.json")

    assert "watchlist" in watchlist
    assert len(watchlist["watchlist"]) >= 1
    assert any(item["enabled"] for item in watchlist["watchlist"])
