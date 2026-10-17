# Integrated AI System: Expert System, Search Algorithm & Multi-Agent

Program ini adalah simulasi sistem AI terpadu untuk deteksi, diagnosis, dan penanganan gangguan jaringan komputer secara interaktif menggunakan antarmuka grafis (HMI) berbasis Matplotlib.

## 🚀 Fitur Utama

1. **Search Algorithm (Pencarian Rute):**
   * **Rute Tercepat (Shortest Path):** Menggunakan algoritma *Breadth-First Search* (BFS) untuk menemukan jalur komunikasi secepat mungkin.
   * **Rute Terjauh (Longest Path/Alternatif):** Menggunakan `networkx.shortest_simple_paths` untuk mencari jalur alternatif terpanjang yang tersedia di jaringan.

2. **Expert System (Sistem Pakar):**
   * Menggunakan metode **Forward Chaining** berbasis aturan (*if-then*) untuk mendiagnosis jenis masalah jaringan secara otomatis berdasarkan fakta yang dikumpulkan oleh agen pemantau.

3. **Multi-Agent System:**
   * **`MonitoringAgent`**: Mengumpulkan status kesehatan dan fakta dari jaringan secara real-time.
   * **`ResponseAgent`**: Menganalisis hasil diagnosis sistem pakar dan mengeksekusi perencanaan ulang rute (*rerouting*) melalui mesin pencari.

4. **Interactive HMI Dashboard & Dynamic Topology:**
   * **Topologi Acak Organik (Erdős–Rényi):** Setiap kali tombol *"Acak Topologi Baru"* ditekan, sistem menghasilkan topologi jaringan acak baru secara instan dengan jumlah router bervariasi antara **40 hingga 100 router**.
   * **Interaksi Klik Langsung:** Pengguna dapat mengeklik node router pada kanvas untuk menentukan titik **START** (biru) dan **GOAL** (hijau).
   * **Simulasi Kerusakan Jaringan:** Mengeklik router yang sama saat aktif akan mematikan/memblokir node tersebut (`#e31a1c`), memicu agen AI untuk mencari ulang jalur alternatif secara dinamis.
   * **Kontrol GUI Modern:** Dilengkapi tombol grafis untuk beralih mode rute, mereset pilihan, dan mengacak topologi baru tanpa menggunakan *shortcut* keyboard.

---

## 📦 Prasyarat (Dependencies)

Pastikan pustaka Python berikut sudah terinstal di lingkungan Anda:
* Python 3.x
* `networkx`
* `matplotlib`

Anda dapat menginstalnya melalui pip jika belum memilikinya:
```bash
pip install networkx matplotlib

## 🛠️ Cara Menjalankan
Jalankan file `main.py` menggunakan Python 3:

```bash
python main.py
