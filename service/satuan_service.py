from dto.request_dto import NamaRequest
from repository.satuan_repository import SatuanRepository


class SatuanService:
    def __init__(self, db_path: str = None):
        self.repo = SatuanRepository(db_path) if db_path else SatuanRepository()

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
                return False, "Nama satuan sudah ada", 0

        new_id = self.repo.create(sanitized)
        return True, "Satuan berhasil ditambahkan", new_id

    def update(self, id: int, nama: str) -> tuple[bool, str]:
        request = NamaRequest(nama=nama)
        errors = request.validate()
        if errors:
            return False, "; ".join(errors)

        sanitized = request.sanitize()
        existing = self.repo.get_all()
        for item in existing:
            if item.id != id and item.nama.lower() == sanitized.lower():
                return False, "Nama satuan sudah ada"

        result = self.repo.update(id, sanitized)
        if result:
            return True, "Satuan berhasil diupdate"
        return False, "Satuan tidak ditemukan"

    def delete(self, id: int) -> tuple[bool, str]:
        result = self.repo.delete(id)
        if result:
            return True, "Satuan berhasil dihapus"
        return False, "Satuan tidak ditemukan"
