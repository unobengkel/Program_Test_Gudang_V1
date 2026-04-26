from dataclasses import dataclass, field
from typing import Optional


@dataclass
class NamaRequest:
    nama: str

    def validate(self) -> list[str]:
        errors: list[str] = []
        if not self.nama or not self.nama.strip():
            errors.append("Nama tidak boleh kosong")
        elif len(self.nama.strip()) > 100:
            errors.append("Nama maksimal 100 karakter")
        return errors

    def sanitize(self) -> str:
        return self.nama.strip()


@dataclass
class BarangRequest:
    idjenis: int
    idsatuan: int
    idmerek: int

    def validate(self) -> list[str]:
        errors: list[str] = []
        if self.idjenis <= 0:
            errors.append("Jenis harus dipilih")
        if self.idsatuan <= 0:
            errors.append("Satuan harus dipilih")
        if self.idmerek <= 0:
            errors.append("Merek harus dipilih")
        return errors


@dataclass
class StokRequest:
    idbarang: int
    jumlah: int

    def validate(self) -> list[str]:
        errors: list[str] = []
        if self.idbarang <= 0:
            errors.append("Barang harus dipilih")
        if self.jumlah <= 0:
            errors.append("Jumlah harus lebih dari 0")
        return errors
