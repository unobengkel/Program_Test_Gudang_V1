from typing import Optional
from model.entity import Stok
from model.database import get_connection
from repository.base_repository import BaseRepository
from config import DATABASE_PATH


class StokRepository(BaseRepository):
    def __init__(self, db_path: str = DATABASE_PATH):
        self.db_path = db_path

    def get_all(self) -> list[Stok]:
        conn = get_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT s.id, s.idbarang, s.jumlah, s.datetime,
                   COALESCE(
                       (SELECT j.nama || ' - ' || m.nama || ' (' || sat.nama || ')'
                        FROM barang b
                        LEFT JOIN jenis j ON b.idjenis = j.id
                        LEFT JOIN merek m ON b.idmerek = m.id
                        LEFT JOIN satuan sat ON b.idsatuan = sat.id
                        WHERE b.id = s.idbarang),
                       'Unknown'
                   ) as nama_barang
            FROM stok s
            ORDER BY s.id DESC
            """
        )
        rows = cursor.fetchall()
        conn.close()
        return [
            Stok(
                id=row["id"],
                idbarang=row["idbarang"],
                jumlah=row["jumlah"],
                datetime=row["datetime"],
                nama_barang=row["nama_barang"],
            )
            for row in rows
        ]

    def get_by_id(self, id: int) -> Optional[Stok]:
        conn = get_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT s.id, s.idbarang, s.jumlah, s.datetime,
                   COALESCE(
                       (SELECT j.nama || ' - ' || m.nama || ' (' || sat.nama || ')'
                        FROM barang b
                        LEFT JOIN jenis j ON b.idjenis = j.id
                        LEFT JOIN merek m ON b.idmerek = m.id
                        LEFT JOIN satuan sat ON b.idsatuan = sat.id
                        WHERE b.id = s.idbarang),
                       'Unknown'
                   ) as nama_barang
            FROM stok s
            WHERE s.id = ?
            """,
            (id,),
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            return Stok(
                id=row["id"],
                idbarang=row["idbarang"],
                jumlah=row["jumlah"],
                datetime=row["datetime"],
                nama_barang=row["nama_barang"],
            )
        return None

    def create(self, idbarang: int, jumlah: int, datetime: str) -> int:
        conn = get_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO stok (idbarang, jumlah, datetime) VALUES (?, ?, ?)",
            (idbarang, jumlah, datetime),
        )
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return new_id

    def update(self, id: int, idbarang: int, jumlah: int, datetime: str) -> bool:
        conn = get_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE stok SET idbarang = ?, jumlah = ?, datetime = ? WHERE id = ?",
            (idbarang, jumlah, datetime, id),
        )
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected > 0

    def delete(self, id: int) -> bool:
        conn = get_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM stok WHERE id = ?", (id,))
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected > 0
