from dto.request_dto import BarangRequest
from repository.barang_repository import BarangRepository
from repository.jenis_repository import JenisRepository
from repository.satuan_repository import SatuanRepository
from repository.merek_repository import MerekRepository


class BarangService:
    def __init__(self, db_path: str = None):
        self.repo = BarangRepository(db_path) if db_path else BarangRepository()
        self.jenis_repo = JenisRepository(db_path) if db_path else JenisRepository()
        self.satuan_repo = SatuanRepository(db_path) if db_path else SatuanRepository()
        self.merek_repo = MerekRepository(db_path) if db_path else MerekRepository()

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id: int):
        return self.repo.get_by_id(id)

    def get_all_jenis(self):
        return self.jenis_repo.get_all()

    def get_all_satuan(self):
        return self.satuan_repo.get_all()

    def get_all_merek(self):
        return self.merek_repo.get_all()

    def create(self, idjenis: int, idsatuan: int, idmerek: int) -> tuple[bool, str, int]:
        request = BarangRequest(idjenis=idjenis, idsatuan=idsatuan, idmerek=idmerek)
        errors = request.validate()
        if errors:
            return False, "; ".join(errors), 0

        # Validasi foreign key exists
        if not self.jenis_repo.get_by_id(idjenis):
            return False, "Jenis tidak ditemukan", 0
        if not self.satuan_repo.get_by_id(idsatuan):
            return False, "Satuan tidak ditemukan", 0
        if not self.merek_repo.get_by_id(idmerek):
            return False, "Merek tidak ditemukan", 0

        new_id = self.repo.create(idjenis, idsatuan, idmerek)
        return True, "Barang berhasil ditambahkan", new_id

    def update(self, id: int, idjenis: int, idsatuan: int, idmerek: int) -> tuple[bool, str]:
        request = BarangRequest(idjenis=idjenis, idsatuan=idsatuan, idmerek=idmerek)
        errors = request.validate()
        if errors:
            return False, "; ".join(errors)

        if not self.jenis_repo.get_by_id(idjenis):
            return False, "Jenis tidak ditemukan"
        if not self.satuan_repo.get_by_id(idsatuan):
            return False, "Satuan tidak ditemukan"
        if not self.merek_repo.get_by_id(idmerek):
            return False, "Merek tidak ditemukan"

        result = self.repo.update(id, idjenis, idsatuan, idmerek)
        if result:
            return True, "Barang berhasil diupdate"
        return False, "Barang tidak ditemukan"

    def delete(self, id: int) -> tuple[bool, str]:
        result = self.repo.delete(id)
        if result:
            return True, "Barang berhasil dihapus"
        return False, "Barang tidak ditemukan"
