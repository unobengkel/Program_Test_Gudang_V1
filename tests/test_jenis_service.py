import pytest
from service.jenis_service import JenisService


class TestJenisService:
    def test_create_success(self, db_path):
        service = JenisService(db_path)
        success, message, new_id = service.create("Elektronik")
        assert success is True
        assert new_id > 0

    def test_create_duplicate(self, db_path):
        service = JenisService(db_path)
        service.create("Elektronik")
        success, message, _ = service.create("Elektronik")
        assert success is False
        assert "sudah ada" in message

    def test_update_success(self, db_path):
        service = JenisService(db_path)
        _, _, new_id = service.create("Makanan")
        success, message = service.update(new_id, "Makanan Ringan")
        assert success is True

    def test_delete_success(self, db_path):
        service = JenisService(db_path)
        _, _, new_id = service.create("Alat Tulis")
        success, message = service.delete(new_id)
        assert success is True
