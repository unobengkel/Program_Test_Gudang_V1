import pytest
from repository.stok_repository import StokRepository
from repository.barang_repository import BarangRepository
from repository.jenis_repository import JenisRepository
from repository.satuan_repository import SatuanRepository
from repository.merek_repository import MerekRepository


class TestStokRepository:
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

    def test_create_and_get_all(self, setup_data):
        db_path, id_barang = setup_data
        repo = StokRepository(db_path)
        new_id = repo.create(id_barang, 100, "2024-01-01 10:00:00")
        assert new_id > 0

        all_items = repo.get_all()
        assert len(all_items) == 1
        assert all_items[0].jumlah == 100

    def test_get_by_id(self, setup_data):
        db_path, id_barang = setup_data
        repo = StokRepository(db_path)
        new_id = repo.create(id_barang, 50, "2024-01-01 10:00:00")
        item = repo.get_by_id(new_id)
        assert item is not None
        assert item.jumlah == 50
        assert item.idbarang == id_barang

    def test_update(self, setup_data):
        db_path, id_barang = setup_data
        repo = StokRepository(db_path)
        new_id = repo.create(id_barang, 100, "2024-01-01 10:00:00")
        result = repo.update(new_id, id_barang, 200, "2024-02-01 10:00:00")
        assert result is True

        updated = repo.get_by_id(new_id)
        assert updated.jumlah == 200

    def test_delete(self, setup_data):
        db_path, id_barang = setup_data
        repo = StokRepository(db_path)
        new_id = repo.create(id_barang, 75, "2024-01-01 10:00:00")
        result = repo.delete(new_id)
        assert result is True

        item = repo.get_by_id(new_id)
        assert item is None
