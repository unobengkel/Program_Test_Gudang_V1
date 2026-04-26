import pytest
from service.merek_service import MerekService


class TestMerekService:
    def test_create_success(self, db_path):
        service = MerekService(db_path)
        success, message, new_id = service.create("Samsung")
        assert success is True
        assert new_id > 0

    def test_create_duplicate(self, db_path):
        service = MerekService(db_path)
        service.create("Samsung")
        success, message, _ = service.create("Samsung")
        assert success is False
        assert "sudah ada" in message

    def test_update_success(self, db_path):
        service = MerekService(db_path)
        _, _, new_id = service.create("LG")
        success, message = service.update(new_id, "LG Electronics")
        assert success is True

    def test_delete_success(self, db_path):
        service = MerekService(db_path)
        _, _, new_id = service.create("Sharp")
        success, message = service.delete(new_id)
        assert success is True
