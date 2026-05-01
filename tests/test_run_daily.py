from __future__ import annotations

from pathlib import Path

import pandas as pd
from requests.exceptions import ProxyError

import app


class DummyLogger:
    def __init__(self) -> None:
        self.infos: list[str] = []
        self.warnings: list[str] = []
        self.exceptions: list[str] = []

    def info(self, message: str, *args: object) -> None:
        self.infos.append(message % args if args else message)

    def warning(self, message: str, *args: object) -> None:
        self.warnings.append(message % args if args else message)

    def exception(self, message: str, *args: object) -> None:
        self.exceptions.append(message % args if args else message)


def test_run_daily_continues_when_single_symbol_fetch_fails(monkeypatch, tmp_path: Path) -> None:
    logger = DummyLogger()
    fetch_timeouts: list[int] = []
    save_calls: list[tuple[pd.DataFrame, Path]] = []
    report_records: list[dict[str, object]] = []
    report_kwargs: dict[str, object] = {}

    def fake_fetch_stock_daily_history(
        symbol: str,
        timeout_seconds: int = 10,
    ) -> tuple[pd.DataFrame, pd.DataFrame]:
        fetch_timeouts.append(timeout_seconds)
        if symbol == "600519":
            raise ProxyError("proxy error")

        raw_dataframe = pd.DataFrame(
            {
                "日期": pd.date_range("2024-01-01", periods=25, freq="D"),
                "收盘": list(range(1, 26)),
            }
        )
        normalized_dataframe = pd.DataFrame(
            {
                "date": pd.date_range("2024-01-01", periods=25, freq="D"),
                "close": list(range(1, 26)),
            }
        )
        return raw_dataframe, normalized_dataframe

    def fake_save_dataframe_csv(
        dataframe: pd.DataFrame,
        relative_path: str | Path,
        *,
        index: bool = False,
    ) -> Path:
        del index
        output_path = tmp_path / Path(relative_path).name
        save_calls.append((dataframe.copy(), output_path))
        return output_path

    def fake_write_daily_report(
        records: list[dict[str, object]],
        *,
        report_date: str | None = None,
        generated_at: str | None = None,
        output_path: str | Path | None = None,
        stage_name: str = "V0.1.3 run-daily",
        processed_csv_path: str = "data/processed/daily_signals.csv",
        raw_data_dir: str = "data/raw",
        log_path: str = "logs/app.log",
    ) -> Path:
        del report_date, generated_at, output_path
        report_records.extend(records)
        report_kwargs.update(
            {
                "stage_name": stage_name,
                "processed_csv_path": processed_csv_path,
                "raw_data_dir": raw_data_dir,
                "log_path": log_path,
            }
        )
        return tmp_path / "daily_report.md"

    monkeypatch.setattr(app, "get_logger", lambda: logger)
    monkeypatch.setattr(
        app,
        "load_settings",
        lambda: {
            "network": {"request_timeout_seconds": 8},
            "storage": {
                "raw_dir": "data/raw",
                "processed_dir": "data/processed",
                "log_dir": "logs",
            },
        },
    )
    monkeypatch.setattr(
        app,
        "load_json",
        lambda _: {
            "watchlist": [
                {"code": "000001", "name": "平安银行", "market": "SZ", "industry": "银行", "enabled": True},
                {"code": "600519", "name": "贵州茅台", "market": "SH", "industry": "白酒", "enabled": True},
            ]
        },
    )
    monkeypatch.setattr(app, "ensure_directory", lambda _: None)
    monkeypatch.setattr(app, "fetch_stock_daily_history", fake_fetch_stock_daily_history)
    monkeypatch.setattr(app, "save_dataframe_csv", fake_save_dataframe_csv)
    monkeypatch.setattr(app, "write_daily_report", fake_write_daily_report)
    monkeypatch.setattr(app, "get_project_root", lambda: tmp_path)

    result = app.run_daily()

    processed_dataframe = save_calls[-1][0]
    success_row = processed_dataframe.loc[processed_dataframe["code"] == "000001"].iloc[0]
    failed_row = processed_dataframe.loc[processed_dataframe["code"] == "600519"].iloc[0]

    assert result == 0
    assert fetch_timeouts == [8, 8]
    assert len(processed_dataframe) == 2
    assert {"fetch_time", "raw_file_path", "latest_trade_date", "signal_level"}.issubset(
        set(processed_dataframe.columns)
    )
    assert success_row["latest_trade_date"] == "2024-01-25"
    assert success_row["signal_level"] == "positive"
    assert success_row["raw_file_path"] == "000001_daily_raw.csv"
    assert success_row["fetch_time"]
    assert failed_row["data_status"] == "fetch_failed"
    assert failed_row["error_message"] == "ProxyError: unable to connect to proxy"
    assert failed_row["signal_level"] == "unavailable"
    assert failed_row["raw_file_path"] == ""
    assert any(record["code"] == "600519" for record in report_records)
    assert report_kwargs == {
        "stage_name": "V0.1.3 run-daily",
        "processed_csv_path": "daily_signals.csv",
        "raw_data_dir": "data/raw",
        "log_path": "logs/app.log",
    }
    assert logger.exceptions == [
        "data collection failed for 600519 贵州茅台: ProxyError: unable to connect to proxy"
    ]
    assert any(
        "run-daily summary: success_count=1 failed_count=1 trend_up_count=1 trend_down_count=0 neutral_count=0"
        == message
        for message in logger.infos
    )
    assert any(
        "run-daily started app=AShare Insight Lab version=0.1.3 environment=development developer=pL enabled_symbols=2 request_timeout=8s"
        == message
        for message in logger.infos
    )


def test_run_daily_handles_keyboard_interrupt_gracefully(monkeypatch, capsys) -> None:
    logger = DummyLogger()
    fetch_timeouts: list[int] = []

    def fake_fetch_stock_daily_history(
        symbol: str,
        timeout_seconds: int = 10,
    ) -> tuple[pd.DataFrame, pd.DataFrame]:
        del symbol
        fetch_timeouts.append(timeout_seconds)
        raise KeyboardInterrupt

    monkeypatch.setattr(app, "get_logger", lambda: logger)
    monkeypatch.setattr(
        app,
        "load_settings",
        lambda: {
            "storage": {
                "raw_dir": "data/raw",
                "processed_dir": "data/processed",
                "log_dir": "logs",
            },
        },
    )
    monkeypatch.setattr(
        app,
        "load_json",
        lambda _: {
            "watchlist": [
                {"code": "000001", "name": "平安银行", "market": "SZ", "industry": "银行", "enabled": True},
            ]
        },
    )
    monkeypatch.setattr(app, "ensure_directory", lambda _: None)
    monkeypatch.setattr(app, "fetch_stock_daily_history", fake_fetch_stock_daily_history)
    monkeypatch.setattr(
        app,
        "save_dataframe_csv",
        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("should not save CSV after Ctrl+C")),
    )
    monkeypatch.setattr(
        app,
        "write_daily_report",
        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("should not write report after Ctrl+C")),
    )

    result = app.run_daily()
    captured = capsys.readouterr()

    assert result == 130
    assert fetch_timeouts == [10]
    assert "run-daily 已被用户中断" in captured.out
    assert logger.warnings == ["run-daily interrupted by user"]
