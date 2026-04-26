# 📦 Aplikasi Stok Gudang

Aplikasi web sederhana untuk mengelola stok gudang berbasis **Python Flask + SQLite + Tailwind CSS** dengan arsitektur **Clean Architecture**.

## ✨ Fitur

- **Manajemen Data Master**: CRUD untuk Jenis, Satuan, Merek
- **Manajemen Barang**: Kombinasi Jenis + Satuan + Merek
- **Manajemen Stok**: Pencatatan stok barang dengan timestamp otomatis
- **Validasi Data**: Cegah duplikasi nama, validasi input kosong
- **Notifikasi Flash**: Feedback sukses/gagal pada setiap aksi
- **UI Responsif**: Tailwind CSS, mobile-friendly
- **Clean Architecture**: Model, DTO, Repository, Service, Route
- **Unit Test & Integration Test**: 50 test dengan pytest

## 🖼️ Tampilan Aplikasi

| Halaman | Deskripsi |
|---------|-----------|
| 🏠 **Beranda** | Menu navigasi ke semua modul |
| 📋 **Jenis** | CRUD data jenis barang |
| ⚖️ **Satuan** | CRUD data satuan barang |
| 🏷️ **Merek** | CRUD data merek barang |
| 📦 **Barang** | CRUD data barang (dropdown relasi) |
| 📊 **Stok** | CRUD data stok gudang |

## 🏗️ Arsitektur

```
Program_Test_Gudang/
│
├── app.py                 # Entry point Flask
├── config.py              # Konfigurasi database
├── requirements.txt       # Dependencies
├── gudang.db              # Database SQLite (auto-generated)
│
├── model/                 # Entity & Database layer
│   ├── entity.py          # Dataclass: Satuan, Jenis, Merek, Barang, Stok
│   └── database.py        # Koneksi SQLite, inisialisasi tabel
│
├── dto/                   # Data Transfer Object
│   └── request_dto.py     # Validasi input (NamaRequest, BarangRequest, StokRequest)
│
├── repository/            # Data Access Layer
│   ├── base_repository.py # Abstract base class
│   ├── satuan_repository.py
│   ├── jenis_repository.py
│   ├── merek_repository.py
│   ├── barang_repository.py
│   └── stok_repository.py
│
├── service/               # Business Logic Layer
│   ├── satuan_service.py
│   ├── jenis_service.py
│   ├── merek_service.py
│   ├── barang_service.py
│   └── stok_service.py
│
├── route/                 # HTTP Layer (Flask Blueprint)
│   ├── satuan_bp.py
│   ├── jenis_bp.py
│   ├── merek_bp.py
│   ├── barang_bp.py
│   └── stok_bp.py
│
├── templates/             # HTML Templates (Jinja2 + Tailwind)
│   ├── base.html
│   ├── home.html
│   ├── satuan/index.html
│   ├── jenis/index.html
│   ├── merek/index.html
│   ├── barang/index.html
│   └── stok/index.html
│
└── tests/                 # Unit & Integration Tests
    ├── conftest.py
    ├── test_satuan_repository.py
    ├── test_jenis_repository.py
    ├── test_merek_repository.py
    ├── test_barang_repository.py
    ├── test_stok_repository.py
    ├── test_satuan_service.py
    ├── test_jenis_service.py
    ├── test_merek_service.py
    ├── test_barang_service.py
    ├── test_stok_service.py
    └── test_integration.py
```

## 🗄️ Database Schema

| Tabel | Kolom |
|-------|-------|
| **satuan** | `id` (PK, AUTOINCREMENT), `nama` (UNIQUE) |
| **jenis** | `id` (PK, AUTOINCREMENT), `nama` (UNIQUE) |
| **merek** | `id` (PK, AUTOINCREMENT), `nama` (UNIQUE) |
| **barang** | `id` (PK, AUTOINCREMENT), `idjenis` (FK→jenis), `idsatuan` (FK→satuan), `idmerek` (FK→merek) |
| **stok** | `id` (PK, AUTOINCREMENT), `idbarang` (FK→barang), `jumlah`, `datetime` |

## 🚀 Cara Setup & Menjalankan

### Prasyarat

- Python 3.8+
- pip

### Langkah

```bash
# 1. Clone repository
git clone https://github.com/username/program-stok-gudang.git
cd program-stok-gudang

# 2. Install dependencies
pip install -r requirements.txt

# 3. Jalankan aplikasi
python app.py

# 4. Buka browser
# http://127.0.0.1:5000
```

### Mengubah Port

#### Metode 1: Ubah file `app.py`

```python
app.run(debug=True, host="0.0.0.0", port=8080)
```

#### Metode 2: Environment variable

```bash
# Windows CMD
set PORT=8080 && python app.py

# PowerShell
$env:PORT=8080; python app.py
```

## 🧪 Menjalankan Test

```bash
# Jalankan semua test (50 test)
python -m pytest tests/ -v

# Jalankan test spesifik
python -m pytest tests/test_satuan_repository.py -v
python -m pytest tests/test_integration.py -v
```

### Hasil Test

```
============================= 50 passed in 4.17s ==============================
```

- ✅ **22** Repository Unit Tests (CRUD all entities)
- ✅ **23** Service Unit Tests (business logic validation)
- ✅ **1** Integration Test (full workflow: create → read → update → delete)

## 💻 Teknologi

| Tech | Versi |
|------|-------|
| Python | 3.13 |
| Flask | 3.0 |
| Jinja2 | 3.1 |
| SQLite | 3.x |
| Tailwind CSS | CDN |
| Pytest | 9.0 |

## 📄 Lisensi

MIT License

---

> Dibuat dengan ❤️ menggunakan Python Flask & Clean Architecture
