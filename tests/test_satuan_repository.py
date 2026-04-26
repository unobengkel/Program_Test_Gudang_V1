import pytest
from repository.satuan_repository import SatuanRepository
from model.entity import Satuan


class TestSatuanRepository:
    def test_create_and_get_all(self, db_path):
        repo = SatuanRepository(db_path)
        new_id = repo.create("Kilogram")
        assert new_id > 0

        all_items = repo.get_all()
        assert len(all_items) == 1
        assert all_items[0].nama == "Kilogram"

    def test_get_by_id(self, db_path):
        repo = SatuanRepository(db_path)
        new_id = repo.create("Liter")
        item = repo.get_by_id(new_id)
        assert item is not None
        assert item.nama == "Liter"
        assert item.id == new_id

    def test_get_by_id_not_found(self, db_path):
        repo = SatuanRepository(db_path)
        item = repo.get_by_id(999)
        assert item is None

    def test_update(self, db_path):
        repo = SatuanRepository(db_path)
        new_id = repo.create("Meter")
        result = repo.update(new_id, "Centimeter")
        assert result is True

        updated = repo.get_by_id(new_id)
        assert updated.nama == "Centimeter"

    def test_update_not_found(self, db_path):
        repo = SatuanRepository(db_path)
        result = repo.update(999, "Test")
        assert result is False

    def test_delete(self, db_path):
        repo = SatuanRepository(db_path)
        new_id = repo.create("Gram")
        result = repo.delete(new_id)
        assert result is True

        item = repo.get_by_id(new_id)
        assert item is None

    def test_delete_not_found(self, db_path):
        repo = SatuanRepository(db_path)
        result = repo.delete(999)
        assert result is False
