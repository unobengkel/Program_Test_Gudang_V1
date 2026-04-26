import sqlite3
from config import DATABASE_PATH


def get_connection(db_path: str = DATABASE_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_database(db_path: str = DATABASE_PATH) -> None:
    conn = get_connection(db_path)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS satuan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL UNIQUE
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS jenis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL UNIQUE
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS merek (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL UNIQUE
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS barang (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            idjenis INTEGER NOT NULL,
            idsatuan INTEGER NOT NULL,
            idmerek INTEGER NOT NULL,
            FOREIGN KEY (idjenis) REFERENCES jenis(id) ON DELETE CASCADE,
            FOREIGN KEY (idsatuan) REFERENCES satuan(id) ON DELETE CASCADE,
            FOREIGN KEY (idmerek) REFERENCES merek(id) ON DELETE CASCADE
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS stok (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            idbarang INTEGER NOT NULL,
            jumlah INTEGER NOT NULL,
            datetime TEXT NOT NULL,
            FOREIGN KEY (idbarang) REFERENCES barang(id) ON DELETE CASCADE
        )
    """
    )

    conn.commit()
    conn.close()
