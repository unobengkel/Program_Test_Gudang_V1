import pytest
from repository.jenis_repository import JenisRepository


class TestJenisRepository:
    def test_create_and_get_all(self, db_path):
        repo = JenisRepository(db_path)
        new_id = repo.create("Elektronik")
        assert new_id > 0

        all_items = repo.get_all()
        assert len(all_items) == 1
        assert all_items[0].nama == "Elektronik"

    def test_get_by_id(self, db_path):
        repo = JenisRepository(db_path)
        new_id = repo.create("Makanan")
        item = repo.get_by_id(new_id)
        assert item is not None
        assert item.nama == "Makanan"

    def test_get_by_id_not_found(self, db_path):
        repo = JenisRepository(db_path)
        item = repo.get_by_id(999)
        assert item is None

    def test_update(self, db_path):
        repo = JenisRepository(db_path)
        new_id = repo.create("Minuman")
        result = repo.update(new_id, "Minuman Ringan")
        assert result is True

        updated = repo.get_by_id(new_id)
        assert updated.nama == "Minuman Ringan"

    def test_delete(self, db_path):
        repo = JenisRepository(db_path)
        new_id = repo.create("Alat Tulis")
        result = repo.delete(new_id)
        assert result is True

        item = repo.get_by_id(new_id)
        assert item is None
