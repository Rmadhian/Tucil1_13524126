# Tugas Kecil 1 IF2211 Strategi Algoritma
## Penyelesaian Permainan Queens Linkedin

### a. Penjelasan Singkat Program
Program ini adalah implementasi algoritma **Brute Force** untuk menyelesaikan variasi masalah N-Queens pada papan berwarna berukuran N x N. 

Berbeda dengan masalah N-Queens standar, program ini mencari konfigurasi penempatan N ratu dengan aturan constraints sebagai berikut:
1.  **Satu per Baris & Kolom:** Setiap baris dan setiap kolom hanya boleh diisi oleh tepat satu item.
2.  **Kendala Warna (Region):** Tidak ada dua item yang boleh menempati petak dengan warna (region) yang sama. Warna petak didefinisikan dalam file input.
3.  **Kendala Diagonal:** Dua item yang berada pada baris yang bersebelahan tidak boleh berada pada satu garis diagonal yang sama.

Program bekerja dengan membangkitkan permutasi posisi kolom untuk setiap baris, lalu memvalidasi apakah konfigurasi tersebut memenuhi seluruh kendala di atas. Program juga menampilkan visualisasi pencarian solusi secara *live* di terminal serta mencatat waktu eksekusi dan jumlah kasus yang ditinjau.

### b. Requirements Program
Program ini ditulis menggunakan bahasa pemrograman **Python 3**.
Program menggunakan modul bawaan Python:
* `os`: Untuk operasi sistem (membersihkan layar, manajemen path file).
* `sys`: Untuk interaksi sistem.
* `time`: Untuk menghitung durasi eksekusi dan jeda visualisasi.

**Prasyarat:**
* Pastikan **Python 3.x** sudah terinstal di komputer Anda dan dapat dijalankan melalui terminal/command prompt.

### c. Cara Kompilasi
Program ini berbasis *interpreted language* (Python), sehingga **tidak memerlukan proses kompilasi**. Anda dapat langsung menjalankan *source code* yang tersedia.

### d. Cara Menjalankan dan Menggunakan Program

#### 1. Struktur Folder
Pastikan struktur folder proyek Anda terlihat seperti berikut agar *script* berjalan lancar:

```text
Tucil1_13524126/
├── bin/
│   ├── run.bat      (Script eksekusi untuk Windows)
│   └── run.sh       (Script eksekusi untuk Linux/Mac)
├── src/
│   └── Queens.py    (Source code utama)
├── test/
│   ├── tc1.txt      (Contoh file input)
│   └── ...
└── README.md
```

#### 2. Menjalankan Program
Anda dapat menjalankan program dengan dua cara:

**Cara A: Melalui Script Helper (Direkomendasikan)**
1.  Buka terminal dan masuk ke folder `bin`.
2.  **Untuk Windows:**
    Jalankan perintah:
    ```cmd
    run.bat
    ```
    Atau klik ganda file `run.bat` dari File Explorer.
3.  **Untuk Linux / macOS:**
    Berikan izin eksekusi (hanya pertama kali), lalu jalankan:
    ```bash
    chmod +x run.sh
    ./run.sh
    ```

**Cara B: Menjalankan Langsung dengan Python**
1.  Buka terminal dan arahkan ke folder utama proyek (`Tucil1_13524126`).
2.  Jalankan perintah berikut:
    ```bash
    python src/Queens.py
    ```
    *(Catatan: Jika perintah `python` tidak dikenali, coba gunakan `python3`)*

#### 3. Cara Penggunaan
1.  Setelah program berjalan, Anda akan diminta memasukkan **nama file input**.
    * Pastikan file input sudah berada di dalam folder `test`.
    * Masukkan nama file lengkap beserta ekstensinya (contoh: `tc1.txt`).
2.  Program akan menampilkan proses pencarian solusi.
3.  Setelah selesai, program akan menampilkan:
    * Status solusi (Ditemukan/Tidak).
    * Konfigurasi papan akhir (posisi ratu ditandai dengan `#`).
    * Waktu pencarian.
    * Banyak kasus yang ditinjau.
4.  Anda akan ditanya apakah ingin **menyimpan solusi**.
    * Ketik `y` untuk menyimpan, lalu masukkan nama file output (misal: `solusi_tc1.txt`).
    * File output akan disimpan secara otomatis di folder `test`.

### e. Identitas Pembuat
* **NAMA:** Ramadhian Nabil Firdaus Gumay
* **NIM:** 13524126
