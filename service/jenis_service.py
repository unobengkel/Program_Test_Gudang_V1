from dto.request_dto import NamaRequest
from repository.jenis_repository import JenisRepository


class JenisService:
    def __init__(self, db_path: str = None):
        self.repo = JenisRepository(db_path) if db_path else JenisRepository()

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id: int):
        return self.repo.get_by_id(id)

    def create(self, nama: str) -> tuple[bool, str, int]:
        request = NamaRequest(nama=nama)
        errors = request.validate()
        if errors:
            return False, "; ".join(errors), 0

        sanitized = request.sanitize()
        existing = self.repo.get_all()
        for item in existing:
            if item.nama.lower() == sanitized.lower():
                return False, "Nama jenis sudah ada", 0

        new_id = self.repo.create(sanitized)
        return True, "Jenis berhasil ditambahkan", new_id

    def update(self, id: int, nama: str) -> tuple[bool, str]:
        request = NamaRequest(nama=nama)
        errors = request.validate()
        if errors:
            return False, "; ".join(errors)

        sanitized = request.sanitize()
        existing = self.repo.get_all()
        for item in existing:
            if item.id != id and item.nama.lower() == sanitized.lower():
                return False, "Nama jenis sudah ada"

        result = self.repo.update(id, sanitized)
        if result:
            return True, "Jenis berhasil diupdate"
        return False, "Jenis tidak ditemukan"

    def delete(self, id: int) -> tuple[bool, str]:
        result = self.repo.delete(id)
        if result:
            return True, "Jenis berhasil dihapus"
        return False, "Jenis tidak ditemukan"
