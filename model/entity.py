from dataclasses import dataclass


@dataclass
class Satuan:
    id: int
    nama: str


@dataclass
class Jenis:
    id: int
    nama: str


@dataclass
class Merek:
    id: int
    nama: str


@dataclass
class Barang:
    id: int
    idjenis: int
    idsatuan: int
    idmerek: int
    nama_jenis: str = ""
    nama_satuan: str = ""
    nama_merek: str = ""


@dataclass
class Stok:
    id: int
    idbarang: int
    jumlah: int
    datetime: str
    nama_barang: str = ""
