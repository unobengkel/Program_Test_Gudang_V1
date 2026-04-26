import pytest
from repository.merek_repository import MerekRepository


class TestMerekRepository:
    def test_create_and_get_all(self, db_path):
        repo = MerekRepository(db_path)
        new_id = repo.create("Samsung")
        assert new_id > 0

        all_items = repo.get_all()
        assert len(all_items) == 1
        assert all_items[0].nama == "Samsung"

    def test_get_by_id(self, db_path):
        repo = MerekRepository(db_path)
        new_id = repo.create("LG")
        item = repo.get_by_id(new_id)
        assert item is not None
        assert item.nama == "LG"

    def test_update(self, db_path):
        repo = MerekRepository(db_path)
        new_id = repo.create("Sharp")
        result = repo.update(new_id, "Sharp Electronics")
        assert result is True

        updated = repo.get_by_id(new_id)
        assert updated.nama == "Sharp Electronics"

    def test_delete(self, db_path):
        repo = MerekRepository(db_path)
        new_id = repo.create("Polytron")
        result = repo.delete(new_id)
        assert result is True

        item = repo.get_by_id(new_id)
        assert item is None
