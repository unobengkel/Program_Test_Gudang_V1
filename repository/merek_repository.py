from typing import Optional
from model.entity import Merek
from model.database import get_connection
from repository.base_repository import BaseRepository
from config import DATABASE_PATH


class MerekRepository(BaseRepository):
    def __init__(self, db_path: str = DATABASE_PATH):
        self.db_path = db_path

    def get_all(self) -> list[Merek]:
        conn = get_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, nama FROM merek ORDER BY id DESC")
        rows = cursor.fetchall()
        conn.close()
        return [Merek(id=row["id"], nama=row["nama"]) for row in rows]

    def get_by_id(self, id: int) -> Optional[Merek]:
        conn = get_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, nama FROM merek WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Merek(id=row["id"], nama=row["nama"])
        return None

    def create(self, nama: str) -> int:
        conn = get_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO merek (nama) VALUES (?)", (nama,))
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return new_id

    def update(self, id: int, nama: str) -> bool:
        conn = get_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE merek SET nama = ? WHERE id = ?", (nama, id))
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected > 0

    def delete(self, id: int) -> bool:
        conn = get_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM merek WHERE id = ?", (id,))
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected > 0
