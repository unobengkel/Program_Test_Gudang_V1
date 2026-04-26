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
├── ecosystem.config.js    # PM2 configuration
├── gudang.db              # Database SQLite (auto-generated)
│
├── model/                 # Entity & Database layer
├── dto/                   # Data Transfer Object
├── repository/            # Data Access Layer (5 modules)
├── service/               # Business Logic Layer (5 modules)
├── route/                 # HTTP Layer - Flask Blueprint (5 modules)
├── templates/             # HTML Templates (Jinja2 + Tailwind)
└── tests/                 # 50 Unit & Integration Tests
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

```bash
# Via environment variable
set PORT=8080 && python app.py   # Windows CMD
$env:PORT=8080; python app.py    # PowerShell
PORT=8080 python app.py          # Linux/Mac
```

### Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## 🏃‍♂️ Menjalankan dengan PM2

PM2 adalah process manager yang menjaga aplikasi tetap berjalan di background dan auto-restart jika crash.

### Install PM2

```bash
npm install -g pm2
```

### Start / Stop / Logs

```bash
# Start dengan ecosystem file
cd Program_Test_Gudang
pm2 start ecosystem.config.js

# Perintah dasar
pm2 status                 # Cek status
pm2 logs stok-gudang       # Lihat log realtime
pm2 stop stok-gudang       # Stop
pm2 restart stok-gudang    # Restart
pm2 delete stok-gudang     # Hapus dari PM2

# Auto-start saat reboot
pm2 save
pm2 startup
```

## 🌍 Menjalankan di Environment Terbatas

### Offline (Tanpa Internet)

```bash
# Di komputer ada internet: download packages
pip download -r requirements.txt -d offline_packages

# Copy folder offline_packages ke server
# Di server offline: install dari folder
pip install --no-index --find-links ./offline_packages -r requirements.txt
```

### Port Terbatas (Firewall)

```bash
set PORT=8080 && python app.py   # Ganti dengan port yang diizinkan
```

### Resource Terbatas (RAM Rendah)

```bash
# Install waitress (lebih ringan dari Flask dev server)
pip install waitress

# Jalankan
python -c "from waitress import serve; from app import app; serve(app, host='0.0.0.0', port=5000)"
```

### Tanpa Hak Admin

```bash
# Python user install
pip install --user -r requirements.txt

# PM2 lokal (tanpa -g global)
npm install pm2
npx pm2 start ecosystem.config.js
```

## 🧪 Menjalankan Test

```bash
# Semua test
python -m pytest tests/ -v

# Test spesifik
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
| PM2 | 5.x (optional) |

## 📄 Lisensi

MIT License

---

> Dibuat dengan ❤️ menggunakan Python Flask & Clean Architecture
