# 🎥 StreamFlow - Panduan Deployment Streamlit.io

## URL Target
Setelah deployment berhasil, aplikasi akan tersedia di:
```
https://[app-name]-[random-string].streamlit.app/
```

Contoh URL yang akan didapat:
- `https://streamflow-kgui32aj2l6kw5nc9tuenv.streamlit.app/`
- `https://streamflow-demo-abc123def456.streamlit.app/`
- `https://live-streaming-xyz789.streamlit.app/`

## Langkah-langkah Deployment

### 1. Persiapan Repository GitHub

**Buat repository baru:**
- Nama: `streamflow-demo` atau `live-streaming-platform`
- Visibility: Public
- Jangan include README atau .gitignore

**Upload file-file berikut:**
```
streamflow-demo/
├── streamlit_app.py          # File utama aplikasi
├── requirements.txt          # Dependencies (hanya: streamlit)
├── README.md                 # Dokumentasi
└── .streamlit/
    └── config.toml          # Konfigurasi Streamlit
```

### 2. Deploy ke Streamlit.io

1. **Buka Streamlit.io**
   - Pergi ke: https://share.streamlit.io/
   - Login dengan GitHub account

2. **Create New App**
   - Klik "New app"
   - Connect ke GitHub repository
   - Pilih repository: `streamflow-demo`

3. **Konfigurasi Deployment**
   ```
   Repository: username/streamflow-demo
   Branch: main
   Main file path: streamlit_app.py
   App URL: streamflow-demo (akan menjadi prefix)
   ```

4. **Deploy**
   - Klik "Deploy!"
   - Tunggu proses deployment (2-5 menit)

### 3. Verifikasi Deployment

**URL yang akan didapat:**
```
https://streamflow-demo-[random].streamlit.app/
```

**Test aplikasi:**
1. Buka URL yang diberikan
2. Login dengan: `admin` / `admin123`
3. Check semua fitur berfungsi

### 4. Troubleshooting

**Jika ada error health check:**
1. Pastikan file `config.toml` ada di folder `.streamlit/`
2. Check `requirements.txt` hanya berisi `streamlit`
3. Pastikan tidak ada file `pyproject.toml` atau `uv.lock`
4. Redeploy dengan repository yang bersih

**Jika subdomain tidak sesuai:**
1. Nama repository akan menjadi prefix URL
2. Untuk custom prefix, ubah nama repository
3. Contoh: `live-streaming` → `https://live-streaming-xyz.streamlit.app`

## File Deployment

### streamlit_app.py
Aplikasi utama dengan fitur:
- Authentication system
- Dashboard monitoring
- Video management
- Live streaming setup
- User settings

### requirements.txt
```
streamlit
```

### .streamlit/config.toml
```
[server]
headless = true
enableCORS = false
enableXsrfProtection = false

[browser]
gatherUsageStats = false

[theme]
primaryColor = "#0055FF"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
```

### README.md
Dokumentasi untuk pengunjung repository

## Demo Account
- **Username**: `admin`
- **Password**: `admin123`

## Fitur yang Tersedia
- ✅ Login/Register system
- ✅ Dashboard dengan metrics
- ✅ Upload video (demo mode)
- ✅ Konfigurasi live streaming multi-platform
- ✅ User management dan settings

## Catatan Deployment
- Deployment gratis di Streamlit.io
- URL dengan subdomain `.streamlit.app`
- Data menggunakan session state (tidak persistent)
- Cocok untuk demo dan prototype
- Restart otomatis saat file diupdate

## Contoh URL Sukses
Setelah deployment berhasil, Anda akan mendapat URL seperti:
```
https://kgui32aj2l6kw5nc9tuenv.streamlit.app/
```
URL ini akan aktif dan dapat diakses oleh siapa saja.