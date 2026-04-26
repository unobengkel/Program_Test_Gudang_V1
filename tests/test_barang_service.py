import pytest
from service.barang_service import BarangService
from repository.jenis_repository import JenisRepository
from repository.satuan_repository import SatuanRepository
from repository.merek_repository import MerekRepository


class TestBarangService:
    @pytest.fixture
    def setup_data(self, db_path):
        jenis_repo = JenisRepository(db_path)
        satuan_repo = SatuanRepository(db_path)
        merek_repo = MerekRepository(db_path)

        id_jenis = jenis_repo.create("Elektronik")
        id_satuan = satuan_repo.create("Unit")
        id_merek = merek_repo.create("Samsung")

        return db_path, id_jenis, id_satuan, id_merek

    def test_create_success(self, setup_data):
        db_path, id_jenis, id_satuan, id_merek = setup_data
        service = BarangService(db_path)
        success, message, new_id = service.create(id_jenis, id_satuan, id_merek)
        assert success is True
        assert new_id > 0

    def test_create_invalid_jenis(self, db_path):
        service = BarangService(db_path)
        success, message, _ = service.create(0, 1, 1)
        assert success is False
        assert "dipilih" in message

    def test_create_jenis_not_found(self, db_path):
        satuan_repo = SatuanRepository(db_path)
        merek_repo = MerekRepository(db_path)
        id_satuan = satuan_repo.create("Unit")
        id_merek = merek_repo.create("Samsung")

        service = BarangService(db_path)
        success, message, _ = service.create(999, id_satuan, id_merek)
        assert success is False
        assert "tidak ditemukan" in message

    def test_get_all_jenis_satuan_merek(self, db_path):
        service = BarangService(db_path)
        jenis_list = service.get_all_jenis()
        satuan_list = service.get_all_satuan()
        merek_list = service.get_all_merek()
        assert len(jenis_list) == 0
        assert len(satuan_list) == 0
        assert len(merek_list) == 0
