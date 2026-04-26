import pytest
from repository.barang_repository import BarangRepository
from repository.jenis_repository import JenisRepository
from repository.satuan_repository import SatuanRepository
from repository.merek_repository import MerekRepository


class TestBarangRepository:
    @pytest.fixture
    def setup_data(self, db_path):
        jenis_repo = JenisRepository(db_path)
        satuan_repo = SatuanRepository(db_path)
        merek_repo = MerekRepository(db_path)

        id_jenis = jenis_repo.create("Elektronik")
        id_satuan = satuan_repo.create("Unit")
        id_merek = merek_repo.create("Samsung")

        return db_path, id_jenis, id_satuan, id_merek

    def test_create_and_get_all(self, setup_data):
        db_path, id_jenis, id_satuan, id_merek = setup_data
        repo = BarangRepository(db_path)
        new_id = repo.create(id_jenis, id_satuan, id_merek)
        assert new_id > 0

        all_items = repo.get_all()
        assert len(all_items) == 1
        assert all_items[0].nama_jenis == "Elektronik"

    def test_get_by_id(self, setup_data):
        db_path, id_jenis, id_satuan, id_merek = setup_data
        repo = BarangRepository(db_path)
        new_id = repo.create(id_jenis, id_satuan, id_merek)
        item = repo.get_by_id(new_id)
        assert item is not None
        assert item.idjenis == id_jenis
        assert item.idsatuan == id_satuan
        assert item.idmerek == id_merek

    def test_update(self, setup_data):
        db_path, id_jenis, id_satuan, id_merek = setup_data

        # Create second set for update
        jenis_repo = JenisRepository(db_path)
        satuan_repo = SatuanRepository(db_path)
        merek_repo = MerekRepository(db_path)
        id_jenis2 = jenis_repo.create("Makanan")
        id_satuan2 = satuan_repo.create("Gram")
        id_merek2 = merek_repo.create("Indomie")

        repo = BarangRepository(db_path)
        new_id = repo.create(id_jenis, id_satuan, id_merek)
        result = repo.update(new_id, id_jenis2, id_satuan2, id_merek2)
        assert result is True

        updated = repo.get_by_id(new_id)
        assert updated.idjenis == id_jenis2

    def test_delete(self, setup_data):
        db_path, id_jenis, id_satuan, id_merek = setup_data
        repo = BarangRepository(db_path)
        new_id = repo.create(id_jenis, id_satuan, id_merek)
        result = repo.delete(new_id)
        assert result is True

        item = repo.get_by_id(new_id)
        assert item is None
