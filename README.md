# Integrated AI System

## Deskripsi
Program simulasi AI untuk mendeteksi, mendiagnosis, dan menangani gangguan jaringan komputer melalui antarmuka grafis (HMI) berbasis Matplotlib.

## Fitur Utama

1. **Search Algorithm:** Menggunakan BFS untuk mencari rute terpendek dan `networkx.shortest_simple_paths` untuk mencari rute alternatif.
2. **Expert System:** Menggunakan metode *Forward Chaining* berbasis aturan *if-then* untuk mendiagnosis gangguan jaringan.
3. **Multi-Agent System:**
   - `MonitoringAgent`: Memantau kondisi jaringan dan mengumpulkan fakta gangguan.
   - `ResponseAgent`: Menganalisis diagnosis dan mencari rute alternatif.
4. **Interactive HMI:** Menampilkan topologi acak Erdős–Rényi dengan 40–100 router, pemilihan START/GOAL, simulasi kerusakan router, dan pencarian ulang rute secara dinamis.

## Teknologi
- Python 3
- NetworkX
- Matplotlib

## Instalasi

Instal dependencies dengan perintah:

```bash
pip install networkx matplotlib
```

## Cara Menjalankan

Jalankan program melalui terminal pada direktori proyek:

```bash
python main.py
```

## Panduan Penggunaan

1. Klik **Acak Topologi Baru** untuk membuat jaringan.
2. Klik node untuk menentukan **START** dan **GOAL**.
3. Pilih mode pencarian rute.
4. Klik kembali node aktif untuk menyimulasikan gangguan router.
5. Amati hasil diagnosis dan perubahan rute pada HMI.

## Keterangan Warna

- 🔵 Biru: START
- 🟢 Hijau: GOAL
- 🔴 Merah: Router mengalami gangguan

## Catatan
`shortest_simple_paths` menghasilkan jalur alternatif berdasarkan urutan dari yang terpendek. Algoritma ini tidak secara langsung mencari jalur terpanjang.
<img width="1626" height="963" alt="image" src="https://github.com/user-attachments/assets/c2419ee0-e6f8-4b51-bddd-57320143867c" />

---

**Developed with Python, NetworkX, and Matplotlib.**
