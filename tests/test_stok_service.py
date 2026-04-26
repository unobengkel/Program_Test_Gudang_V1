import pytest
from service.stok_service import StokService
from repository.jenis_repository import JenisRepository
from repository.satuan_repository import SatuanRepository
from repository.merek_repository import MerekRepository
from repository.barang_repository import BarangRepository


class TestStokService:
    @pytest.fixture
    def setup_data(self, db_path):
        jenis_repo = JenisRepository(db_path)
        satuan_repo = SatuanRepository(db_path)
        merek_repo = MerekRepository(db_path)
        barang_repo = BarangRepository(db_path)

        id_jenis = jenis_repo.create("Elektronik")
        id_satuan = satuan_repo.create("Unit")
        id_merek = merek_repo.create("Samsung")
        id_barang = barang_repo.create(id_jenis, id_satuan, id_merek)

        return db_path, id_barang

    def test_create_success(self, setup_data):
        db_path, id_barang = setup_data
        service = StokService(db_path)
        success, message, new_id = service.create(id_barang, 100)
        assert success is True
        assert new_id > 0

    def test_create_invalid_jumlah(self, db_path):
        service = StokService(db_path)
        success, message, _ = service.create(1, 0)
        assert success is False
        assert "lebih dari 0" in message

    def test_create_barang_not_found(self, db_path):
        service = StokService(db_path)
        success, message, _ = service.create(999, 100)
        assert success is False
        assert "tidak ditemukan" in message

    def test_update_success(self, setup_data):
        db_path, id_barang = setup_data
        service = StokService(db_path)
        _, _, new_id = service.create(id_barang, 50)
        success, message = service.update(new_id, id_barang, 75)
        assert success is True

    def test_delete_success(self, setup_data):
        db_path, id_barang = setup_data
        service = StokService(db_path)
        _, _, new_id = service.create(id_barang, 30)
        success, message = service.delete(new_id)
        assert success is True
