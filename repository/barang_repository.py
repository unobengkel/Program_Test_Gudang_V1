from typing import Optional
from model.entity import Barang
from model.database import get_connection
from repository.base_repository import BaseRepository
from config import DATABASE_PATH


class BarangRepository(BaseRepository):
    def __init__(self, db_path: str = DATABASE_PATH):
        self.db_path = db_path

    def get_all(self) -> list[Barang]:
        conn = get_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT b.id, b.idjenis, b.idsatuan, b.idmerek,
                   j.nama as nama_jenis, s.nama as nama_satuan, m.nama as nama_merek
            FROM barang b
            LEFT JOIN jenis j ON b.idjenis = j.id
            LEFT JOIN satuan s ON b.idsatuan = s.id
            LEFT JOIN merek m ON b.idmerek = m.id
            ORDER BY b.id DESC
            """
        )
        rows = cursor.fetchall()
        conn.close()
        return [
            Barang(
                id=row["id"],
                idjenis=row["idjenis"],
                idsatuan=row["idsatuan"],
                idmerek=row["idmerek"],
                nama_jenis=row["nama_jenis"],
                nama_satuan=row["nama_satuan"],
                nama_merek=row["nama_merek"],
            )
            for row in rows
        ]

    def get_by_id(self, id: int) -> Optional[Barang]:
        conn = get_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT b.id, b.idjenis, b.idsatuan, b.idmerek,
                   j.nama as nama_jenis, s.nama as nama_satuan, m.nama as nama_merek
            FROM barang b
            LEFT JOIN jenis j ON b.idjenis = j.id
            LEFT JOIN satuan s ON b.idsatuan = s.id
            LEFT JOIN merek m ON b.idmerek = m.id
            WHERE b.id = ?
            """,
            (id,),
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            return Barang(
                id=row["id"],
                idjenis=row["idjenis"],
                idsatuan=row["idsatuan"],
                idmerek=row["idmerek"],
                nama_jenis=row["nama_jenis"],
                nama_satuan=row["nama_satuan"],
                nama_merek=row["nama_merek"],
            )
        return None

    def create(self, idjenis: int, idsatuan: int, idmerek: int) -> int:
        conn = get_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO barang (idjenis, idsatuan, idmerek) VALUES (?, ?, ?)",
            (idjenis, idsatuan, idmerek),
        )
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return new_id

    def update(self, id: int, idjenis: int, idsatuan: int, idmerek: int) -> bool:
        conn = get_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE barang SET idjenis = ?, idsatuan = ?, idmerek = ? WHERE id = ?",
            (idjenis, idsatuan, idmerek, id),
        )
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected > 0

    def delete(self, id: int) -> bool:
        conn = get_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM barang WHERE id = ?", (id,))
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected > 0
