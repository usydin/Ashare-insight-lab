from __future__ import annotations

import sqlite3
from pathlib import Path
from datetime import datetime
from typing import Any
import json

from app_core.path_utils import get_project_root


def get_default_database_path() -> Path:
    """返回默认 SQLite 数据库路径"""
    return get_project_root() / "data" / "history" / "ashare_insight_lab.sqlite3"


def ensure_database(database_path: str | Path | None = None) -> Path:
    """确保数据库及其表结构存在"""
    path = Path(database_path) if database_path else get_default_database_path()
    path.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(path) as conn:
        initialize_schema(conn)

    return path


def initialize_schema(conn: sqlite3.Connection) -> None:
    """初始化数据库表结构"""
    cursor = conn.cursor()

    # 1. 运行历史表
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS daily_runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_date TEXT NOT NULL,
            started_at TEXT,
            finished_at TEXT,
            app_version TEXT,
            stage TEXT,
            status TEXT,
            index_count INTEGER,
            sector_count INTEGER,
            stock_count INTEGER,
            report_path TEXT,
            processed_csv_path TEXT,
            log_path TEXT,
            created_at TEXT DEFAULT (datetime('now', 'localtime'))
        )
    """)

    # 2. 指数信号历史表
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS index_signals_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id INTEGER,
            fetch_time TEXT,
            symbol TEXT,
            name TEXT,
            category TEXT,
            date TEXT,
            close REAL,
            ma5 REAL,
            ma20 REAL,
            signal TEXT,
            signal_level TEXT,
            data_status TEXT,
            error_message TEXT,
            created_at TEXT DEFAULT (datetime('now', 'localtime')),
            FOREIGN KEY (run_id) REFERENCES daily_runs (id)
        )
    """)

    # 3. 行业/板块信号历史表
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sector_signals_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id INTEGER,
            fetch_time TEXT,
            symbol TEXT,
            name TEXT,
            board_type TEXT,
            category TEXT,
            priority TEXT,
            observe_reason TEXT,
            risk_note TEXT,
            date TEXT,
            close REAL,
            ma5 REAL,
            ma20 REAL,
            signal TEXT,
            signal_level TEXT,
            data_status TEXT,
            error_message TEXT,
            created_at TEXT DEFAULT (datetime('now', 'localtime')),
            FOREIGN KEY (run_id) REFERENCES daily_runs (id)
        )
    """)

    # 4. 个股信号历史表
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock_signals_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id INTEGER,
            fetch_time TEXT,
            date TEXT,
            code TEXT,
            name TEXT,
            market TEXT,
            industry TEXT,
            sector TEXT,
            board TEXT,
            tags TEXT,
            priority TEXT,
            position_status TEXT,
            observe_reason TEXT,
            risk_note TEXT,
            data_source TEXT,
            close REAL,
            ma5 REAL,
            ma20 REAL,
            signal TEXT,
            signal_level TEXT,
            data_status TEXT,
            error_message TEXT,
            raw_file_path TEXT,
            created_at TEXT DEFAULT (datetime('now', 'localtime')),
            FOREIGN KEY (run_id) REFERENCES daily_runs (id)
        )
    """)

    # 基础索引
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_index_symbol_date ON index_signals_history(symbol, date)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_sector_symbol_date ON sector_signals_history(symbol, date)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_stock_code_date ON stock_signals_history(code, date)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_runs_date ON daily_runs(run_date)")

    conn.commit()


def insert_run_daily_snapshot(
    run_metadata: dict[str, Any],
    index_records: list[dict[str, Any]],
    sector_records: list[dict[str, Any]],
    watchlist_records: list[dict[str, Any]],
    database_path: str | Path | None = None,
) -> dict[str, Any]:
    """写入一次 run-daily 的完整快照"""
    path = Path(database_path) if database_path else get_default_database_path()
    ensure_database(path)

    with sqlite3.connect(path) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # 插入 daily_runs
        cursor.execute("""
            INSERT INTO daily_runs (
                run_date, started_at, finished_at, app_version, stage, status,
                index_count, sector_count, stock_count, report_path,
                processed_csv_path, log_path
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            run_metadata.get("run_date"),
            run_metadata.get("started_at"),
            run_metadata.get("finished_at"),
            run_metadata.get("app_version"),
            run_metadata.get("stage"),
            run_metadata.get("status"),
            run_metadata.get("index_count"),
            run_metadata.get("sector_count"),
            run_metadata.get("stock_count"),
            run_metadata.get("report_path"),
            run_metadata.get("processed_csv_path"),
            run_metadata.get("log_path"),
        ))
        run_id = cursor.lastrowid

        # 插入指数
        for rec in index_records:
            cursor.execute("""
                INSERT INTO index_signals_history (
                    run_id, fetch_time, symbol, name, category, date,
                    close, ma5, ma20, signal, signal_level, data_status, error_message
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                run_id, rec.get("fetch_time"), rec.get("symbol"), rec.get("name"),
                rec.get("category"), rec.get("date"), rec.get("close"),
                rec.get("ma5"), rec.get("ma20"), rec.get("signal"),
                rec.get("signal_level"), rec.get("data_status"), rec.get("error_message")
            ))

        # 插入板块
        for rec in sector_records:
            cursor.execute("""
                INSERT INTO sector_signals_history (
                    run_id, fetch_time, symbol, name, board_type, category,
                    priority, observe_reason, risk_note, date, close,
                    ma5, ma20, signal, signal_level, data_status, error_message
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                run_id, rec.get("fetch_time"), rec.get("symbol"), rec.get("name"),
                rec.get("board_type"), rec.get("category"), rec.get("priority"),
                rec.get("observe_reason"), rec.get("risk_note"), rec.get("date"),
                rec.get("close"), rec.get("ma5"), rec.get("ma20"), rec.get("signal"),
                rec.get("signal_level"), rec.get("data_status"), rec.get("error_message")
            ))

        # 插入自选股
        for rec in watchlist_records:
            # 处理 tags (可能是 list)
            tags = rec.get("tags", "")
            if isinstance(tags, list):
                tags = ",".join(tags)

            cursor.execute("""
                INSERT INTO stock_signals_history (
                    run_id, fetch_time, date, code, name, market, industry,
                    sector, board, tags, priority, position_status,
                    observe_reason, risk_note, data_source, close,
                    ma5, ma20, signal, signal_level, data_status,
                    error_message, raw_file_path
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                run_id, rec.get("fetch_time"), rec.get("date"), rec.get("code"),
                rec.get("name"), rec.get("market"), rec.get("industry"),
                rec.get("sector"), rec.get("board"), tags, rec.get("priority"),
                rec.get("position_status"), rec.get("observe_reason"),
                rec.get("risk_note"), rec.get("data_source"), rec.get("close"),
                rec.get("ma5"), rec.get("ma20"), rec.get("signal"),
                rec.get("signal_level"), rec.get("data_status"),
                rec.get("error_message"), rec.get("raw_file_path")
            ))

        conn.commit()

        return {
            "database_path": str(path),
            "run_id": run_id,
            "index_count": len(index_records),
            "sector_count": len(sector_records),
            "stock_count": len(watchlist_records)
        }


def get_latest_runs(limit: int = 10, database_path: str | Path | None = None) -> list[dict[str, Any]]:
    """读取最近运行记录"""
    path = Path(database_path) if database_path else get_default_database_path()
    if not path.exists():
        return []

    with sqlite3.connect(path) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM daily_runs ORDER BY id DESC LIMIT ?", (limit,))
        return [dict(row) for row in cursor.fetchall()]


def get_signal_history(
    asset_type: str,
    symbol: str,
    limit: int = 30,
    database_path: str | Path | None = None
) -> list[dict[str, Any]]:
    """读取某个指数/板块/个股历史信号"""
    path = Path(database_path) if database_path else get_default_database_path()
    if not path.exists():
        return []

    table_map = {
        "index": ("index_signals_history", "symbol"),
        "sector": ("sector_signals_history", "symbol"),
        "stock": ("stock_signals_history", "code"),
    }

    if asset_type not in table_map:
        raise ValueError(f"不支持的资产类型: {asset_type}")

    table_name, col_name = table_map[asset_type]

    with sqlite3.connect(path) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        query = f"SELECT * FROM {table_name} WHERE {col_name} = ? ORDER BY date DESC LIMIT ?"
        cursor.execute(query, (symbol, limit))
        return [dict(row) for row in cursor.fetchall()]
