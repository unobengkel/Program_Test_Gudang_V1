import pytest
from service.satuan_service import SatuanService


class TestSatuanService:
    def test_create_success(self, db_path):
        service = SatuanService(db_path)
        success, message, new_id = service.create("Kilogram")
        assert success is True
        assert new_id > 0

    def test_create_empty_name(self, db_path):
        service = SatuanService(db_path)
        success, message, new_id = service.create("")
        assert success is False
        assert "kosong" in message.lower()
        assert new_id == 0

    def test_create_duplicate(self, db_path):
        service = SatuanService(db_path)
        service.create("Kilogram")
        success, message, _ = service.create("Kilogram")
        assert success is False
        assert "sudah ada" in message

    def test_update_success(self, db_path):
        service = SatuanService(db_path)
        _, _, new_id = service.create("Meter")
        success, message = service.update(new_id, "Centimeter")
        assert success is True

    def test_update_not_found(self, db_path):
        service = SatuanService(db_path)
        success, message = service.update(999, "Test")
        assert success is False
        assert "tidak ditemukan" in message

    def test_delete_success(self, db_path):
        service = SatuanService(db_path)
        _, _, new_id = service.create("Gram")
        success, message = service.delete(new_id)
        assert success is True

    def test_delete_not_found(self, db_path):
        service = SatuanService(db_path)
        success, message = service.delete(999)
        assert success is False
        assert "tidak ditemukan" in message

    def test_get_all(self, db_path):
        service = SatuanService(db_path)
        service.create("Liter")
        service.create("Mililiter")
        data = service.get_all()
        assert len(data) == 2
