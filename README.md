# 🌐 Integrated AI System: Network Reliability Simulator

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![NetworkX](https://img.shields.io/badge/NetworkX-Supported-green)
![Matplotlib](https://img.shields.io/badge/Matplotlib-UI-orange)

**Integrated AI System** adalah sebuah program simulasi berbasis *Artificial Intelligence* (AI) yang dirancang untuk mendeteksi, mendiagnosis, dan menangani gangguan (*node failure*) pada jaringan komputer secara dinamis. Program ini dilengkapi dengan antarmuka grafis (HMI) interaktif berbasis Matplotlib yang memvisualisasikan respons jaringan terhadap kerusakan secara *real-time*.

---

## 🚀 Fitur Utama

Sistem ini mengintegrasikan beberapa pendekatan Kecerdasan Buatan (AI) ke dalam satu kesatuan:

1. **Intelligent Search Algorithm (Pencarian Rute)**
   * Menggunakan algoritma **BFS (Breadth-First Search)** untuk mencari rute terpendek yang paling optimal dari titik awal ke tujuan.
   * Menggunakan modul `networkx.shortest_simple_paths` untuk mengkalkulasi dan mencari rute alternatif secara instan ketika rute utama terputus.

2. **Expert System (Sistem Pakar)**
   * Diotaki oleh metode **Forward Chaining**.
   * Memanfaatkan basis aturan logika *if-then* untuk mendiagnosis jenis gangguan jaringan secara otomatis berdasarkan gejala/fakta yang dikumpulkan dari node yang mati.

3. **Multi-Agent System (Sistem Multi-Agen)**
   Bekerja secara kolaboratif melalui dua agen utama:
   * 🕵️ **MonitoringAgent**: Bertugas melakukan observasi atau *ping* ke seluruh topologi jaringan, mendeteksi anomali, dan mengumpulkan fakta-fakta kerusakan.
   * 🛠️ **ResponseAgent**: Menerima hasil diagnosis dari *Expert System*, kemudian mengeksekusi tindakan perbaikan (mencari rute alternatif baru).

4. **Interactive HMI (Human-Machine Interface)**
   * **Topologi Dinamis**: Meng-generate topologi acak menggunakan model *Erdős–Rényi* dengan variasi 40 hingga 100 router setiap kali simulasi dijalankan.
   * **Interaksi Klik**: Pengguna dapat berinteraksi langsung dengan graf (memilih titik awal, titik tujuan, dan merusak router) hanya dengan klik mouse.

---

## 📂 Struktur Proyek

Berdasarkan arsitektur sistem, proyek ini dibagi menjadi beberapa modul utama:

* `main.py` : Berfungsi sebagai *entry point* dan pengatur UI/HMI (Matplotlib canvas, event listener klik mouse).
* `multi_agent.py` : Berisi logika untuk `MonitoringAgent` dan `ResponseAgent` agar dapat berkomunikasi.
* `search_agent.py` : Berisi implementasi algoritma pencarian rute (BFS & Alternative Path).
* `expert_system.py` : Berisi basis pengetahuan (knowledge base) dan logika *Forward Chaining* untuk diagnosis kerusakan.

---

## ⚙️ Persyaratan & Instalasi

Pastikan Anda telah menginstal **Python 3** di sistem Anda. Untuk menjalankan simulasi ini, Anda memerlukan dua library utama: `networkx` dan `matplotlib`.

1. Clone repositori ini ke komputer Anda:
   
```bash
   git clone https://github.com/xagafax/Ai_TE_09.git
   

```

2. Instal dependensi yang dibutuhkan:

```bash
   pip install networkx matplotlib
   

```

---

## 🎮 Panduan Penggunaan (Cara Interaksi UI)

Jalankan program utama melalui terminal:

```bash
cd Ai_TE_09

```

lalu

```bash
python main.py

```

Setelah jendela grafis terbuka, ikuti langkah-langkah interaksi berikut:

1. **Generate Jaringan**: Klik tombol **Acak Topologi Baru** pada UI untuk membuat bentuk graf jaringan yang baru (40-100 node).
2. **Set START**: Klik pada salah satu titik (node) sembarang untuk menjadikannya sebagai router asal.
3. **Set GOAL**: Klik pada titik (node) lain untuk menjadikannya sebagai router tujuan. Sistem akan otomatis menggambar garis rute terpendek.
4. **Simulasi Gangguan**: Klik tepat pada salah satu node yang dilewati oleh jalur rute aktif. Node tersebut akan disimulasikan sebagai router yang "mati/rusak".
5. **Auto-Recovery**: Perhatikan jendela terminal dan HMI. Agen akan mendiagnosis kerusakan dan sistem akan otomatis menggambar ulang jalur alternatif (menghindari node yang rusak).

### 🎨 Keterangan Warna Topologi

* 🔵 **Biru (START)** : Titik awal pengiriman paket.
* 🟢 **Hijau (GOAL)** : Titik tujuan akhir paket.
* 🔴 **Merah (FAIL)** : Router yang mengalami gangguan/kerusakan.
* ⚪ **Putih/Abu-abu** : Router normal yang tidak dilewati jalur.
* 🟡 **Jalur Kuning/Emas** : Rute jaringan aktif yang sedang digunakan.

---

## 📝 Catatan Khusus & Limitasi

* **Sifat Pencarian Rute Alternatif**: Fungsi `shortest_simple_paths` dari NetworkX akan men-generate (yield) jalur alternatif berdasarkan urutan dari yang jaraknya paling pendek ke yang paling panjang secara berurutan. Algoritma ini dirancang untuk mencari jalur pengganti terbaik secepat mungkin, bukan ditujukan secara eksplisit untuk mencari jalur terpanjang (worst-case route).
* **Penempatan Node**: Karena tata letak grafik menggunakan perhitungan posisi acak dari NetworkX, terkadang garis antar router akan terlihat bertumpuk. Anda bisa menekan tombol Acak Topologi Baru untuk mendapatkan tampilan yang lebih jelas.

---

## 👥 Kontributor

* **[xagafax (Muhammad Gazali)]
* **[payruzzz]
* **[prakososyuja (Prakoso Syujawanto)]

*Developed with Python, NetworkX, and Matplotlib for AI System Simulation.*
