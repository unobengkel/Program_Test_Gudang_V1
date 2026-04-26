from datetime import datetime
from dto.request_dto import StokRequest
from repository.stok_repository import StokRepository
from repository.barang_repository import BarangRepository


class StokService:
    def __init__(self, db_path: str = None):
        self.repo = StokRepository(db_path) if db_path else StokRepository()
        self.barang_repo = BarangRepository(db_path) if db_path else BarangRepository()

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id: int):
        return self.repo.get_by_id(id)

    def get_all_barang(self):
        return self.barang_repo.get_all()

    def create(self, idbarang: int, jumlah: int) -> tuple[bool, str, int]:
        request = StokRequest(idbarang=idbarang, jumlah=jumlah)
        errors = request.validate()
        if errors:
            return False, "; ".join(errors), 0

        if not self.barang_repo.get_by_id(idbarang):
            return False, "Barang tidak ditemukan", 0

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_id = self.repo.create(idbarang, jumlah, now)
        return True, "Stok berhasil ditambahkan", new_id

    def update(self, id: int, idbarang: int, jumlah: int) -> tuple[bool, str]:
        request = StokRequest(idbarang=idbarang, jumlah=jumlah)
        errors = request.validate()
        if errors:
            return False, "; ".join(errors)

        if not self.barang_repo.get_by_id(idbarang):
            return False, "Barang tidak ditemukan"

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = self.repo.update(id, idbarang, jumlah, now)
        if result:
            return True, "Stok berhasil diupdate"
        return False, "Stok tidak ditemukan"

    def delete(self, id: int) -> tuple[bool, str]:
        result = self.repo.delete(id)
        if result:
            return True, "Stok berhasil dihapus"
        return False, "Stok tidak ditemukan"
