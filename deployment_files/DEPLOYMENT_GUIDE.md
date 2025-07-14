# StreamFlow Deployment Guide untuk Streamlit.io

## File yang Diperlukan untuk Deployment

```
streamflow-demo/
├── streamlit_app.py          # Aplikasi utama
├── requirements.txt          # Dependencies
├── README.md                 # Dokumentasi
├── .streamlit/
│   └── config.toml          # Konfigurasi Streamlit
└── test_app.py              # File test (opsional)
```

## Langkah-langkah Deployment

### 1. Buat Repository GitHub Baru
- Buka GitHub.com
- Klik "New Repository"
- Nama: `streamflow-demo`
- Public repository
- Jangan centang "Add README"

### 2. Upload File
Upload semua file dari folder `deployment_files/`:
- `streamlit_app.py`
- `requirements.txt`
- `README.md`
- `.streamlit/config.toml`

### 3. Deploy ke Streamlit.io
- Buka https://share.streamlit.io/
- Klik "New app"
- Connect GitHub account
- Pilih repository: `streamflow-demo`
- Main file path: `streamlit_app.py`
- Klik "Deploy!"

## Troubleshooting Health Check Error

Jika mendapat error "connection refused" pada port 8501:

1. **Pastikan config.toml ada** di folder `.streamlit/`
2. **Cek requirements.txt** hanya berisi dependencies minimal
3. **Test lokal** dengan `streamlit run streamlit_app.py`
4. **Redeploy** setelah semua file terupload

## URL Aplikasi

Setelah deployment berhasil, aplikasi akan tersedia di:
```
https://[app-name]-[random-string].streamlit.app
```

Contoh:
```
https://streamflow-demo-abc123.streamlit.app
```

## Demo Login

- **Username**: `admin`
- **Password**: `admin123`

## Fitur yang Tersedia

- ✅ Sistem autentikasi
- ✅ Dashboard monitoring
- ✅ Upload video (demo mode)
- ✅ Konfigurasi streaming multi-platform
- ✅ Pengaturan akun

## Catatan Penting

- Aplikasi menggunakan session state storage
- Data tidak persisten antar session
- Cocok untuk demo dan prototype
- Untuk production, gunakan database eksternal