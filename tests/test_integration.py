"""
Integration test: Full CRUD flow across all entities
"""
import pytest
from service.jenis_service import JenisService
from service.satuan_service import SatuanService
from service.merek_service import MerekService
from service.barang_service import BarangService
from service.stok_service import StokService


class TestFullIntegration:
    def test_full_workflow(self, db_path):
        # 1. Create Jenis
        jenis_service = JenisService(db_path)
        j_success, _, id_jenis = jenis_service.create("Elektronik")
        assert j_success is True
        assert id_jenis > 0

        # 2. Create Satuan
        satuan_service = SatuanService(db_path)
        s_success, _, id_satuan = satuan_service.create("Unit")
        assert s_success is True
        assert id_satuan > 0

        # 3. Create Merek
        merek_service = MerekService(db_path)
        m_success, _, id_merek = merek_service.create("Samsung")
        assert m_success is True
        assert id_merek > 0

        # 4. Create Barang
        barang_service = BarangService(db_path)
        b_success, _, id_barang = barang_service.create(id_jenis, id_satuan, id_merek)
        assert b_success is True
        assert id_barang > 0

        # Verify barang with joins
        barang = barang_service.get_by_id(id_barang)
        assert barang is not None
        assert barang.nama_jenis == "Elektronik"
        assert barang.nama_satuan == "Unit"
        assert barang.nama_merek == "Samsung"

        # 5. Create Stok
        stok_service = StokService(db_path)
        st_success, _, id_stok = stok_service.create(id_barang, 100)
        assert st_success is True
        assert id_stok > 0

        # Verify stok
        stok = stok_service.get_by_id(id_stok)
        assert stok is not None
        assert stok.jumlah == 100

        # 6. Update Stok
        up_success, _ = stok_service.update(id_stok, id_barang, 200)
        assert up_success is True
        stok = stok_service.get_by_id(id_stok)
        assert stok.jumlah == 200

        # 7. Delete Stok
        d_success, _ = stok_service.delete(id_stok)
        assert d_success is True
        assert stok_service.get_by_id(id_stok) is None

        # 8. Delete Barang
        d_success, _ = barang_service.delete(id_barang)
        assert d_success is True
        assert barang_service.get_by_id(id_barang) is None

        # 9. Verify cascading should not delete reference tables
        assert jenis_service.get_by_id(id_jenis) is not None
        assert satuan_service.get_by_id(id_satuan) is not None
        assert merek_service.get_by_id(id_merek) is not None
