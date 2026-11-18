# Scraping Indonesian Politic YouTube Comment Datasets

Dataset dan skrip pemrosesan untuk analisis komentar YouTube terkait diskursus politik Indonesia.

## 📁 Struktur Berkas

| Berkas | Format | Deskripsi |
|---|---|---|
| `komentar_prabowo.json` | JSON Lines | Data mentah hasil scraping komentar YouTube. |
| `komentar_raw.csv` | CSV | Data komentar dengan atribut `cid`, `text`, `timestamp`, `votes`, dan `reply`. |
| `komentar_clean.csv` | CSV | Data komentar bersih setelah filter spam (judi online/promosi), mention, URL, dan deduplikasi. |
| `komentar_utama.csv` | CSV | Komentar utama (non-reply) beserta username dan teks yang telah dibersihkan. |
| `komentar_utama.json` | JSON | Komentar utama dalam format JSON terstruktur. |
| `prep.py` | Python | Skrip untuk preprocessing data komentar, anonimasi, filter spam, dan pembersihan teks. |
| `clean.py` | Python | Skrip untuk memisahkan komentar utama serta merapikan format teks. |

## 🚀 Penggunaan

### Kebutuhan Sistem & Dependensi
Pastikan Python 3.x telah terinstal beserta paket `pandas`:
```bash
pip install pandas
```

### Menjalankan Pemrosesan
1. **Preprocessing & Filter Data (`prep.py`)**:
   ```bash
   python prep.py
   ```
   Akan membaca `komentar_prabowo.json` dan menghasilkan `komentar_raw.csv` serta `komentar_clean.csv`.

2. **Ekstraksi Komentar Utama (`clean.py`)**:
   ```bash
   python clean.py
   ```
   Akan memfilter komentar utama (bukan balasan/reply) dan menyimpannya ke `komentar_utama.csv` dan `komentar_utama.json`.
