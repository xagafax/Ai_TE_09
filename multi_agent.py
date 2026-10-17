import threading
import time
import random
from queue import Queue

class MonitoringAgent(threading.Thread):
    """Agen 1: Berjalan non-stop di background, memantau jaringan secara dinamis."""
    def __init__(self, name, alert_queue):
        super().__init__(daemon=True)
        self.name = name
        self.alert_queue = alert_queue

    def run(self):
        print(f"[{self.name}] Memulai pemantauan jaringan 24/7...")
        while True:
            time.sleep(4)  # Simulasi siklus pengecekan setiap 4 detik
            
            # Simulasi AI membaca kondisi lapangan yang bisa berubah-ubah
            # Secara acak menentukan apakah terjadi masalah atau tidak
            is_cable_cut = random.choice([True, False, False]) # 33% kemungkinan kabel putus
            
            facts = {
                "ping_high": is_cable_cut, 
                "packet_loss": is_cable_cut,
                "cable_disconnected": is_cable_cut,
                "server_down": False,
                "power_ok": True
            }

            if is_cable_cut:
                print(f"\n[{self.name}] ⚠️ ANOMALI TERDETEKSI! Mengirim data ke Response Agent.")
                # Kirim fakta ke antrean (Queue) agar dibaca oleh Response Agent
                self.alert_queue.put(facts)
            else:
                print(f"[{self.name}] Jaringan aman terkendali.")


class ResponseAgent(threading.Thread):
    """Agen 2: Standby menunggu laporan, lalu mendiagnosis dan bertindak."""
    def __init__(self, name, expert_system, search_engine, alert_queue, start_node, goal_node):
        super().__init__(daemon=True)
        self.name = name
        self.expert_system = expert_system
        self.search_engine = search_engine
        self.alert_queue = alert_queue
        self.start_node = start_node
        self.goal_node = goal_node

    def run(self):
        print(f"[{self.name}] Standby menunggu instruksi...")
        while True:
            # Program akan tertahan di sini (blocking) sampai ada pesan di antrean
            facts = self.alert_queue.get()
            print(f"[{self.name}] Menerima insiden baru. Memulai analisis...")

            # 1. Analisis masalah dengan Expert System
            diagnosis = self.expert_system.diagnose(facts)
            print(f"[{self.name}] 🧠 Hasil Diagnosis AI: '{diagnosis}'")

            # 2. Ambil tindakan berdasarkan hasil diagnosis
            if "Terputus" in diagnosis or "Padat" in diagnosis:
                print(f"[{self.name}] 🗺️ Mencari rute cadangan cerdas...")
                # Jika Anda sudah mengupdate search_engine ke Dijkstra, gunakan itu. 
                # Jika masih BFS, method find_shortest_path tetap berlaku.
                path = self.search_engine.find_shortest_path(self.start_node, self.goal_node)
                
                if path:
                    print(f"[{self.name}] ✅ Rute dialihkan: {' -> '.join(path)}\n")
                else:
                    print(f"[{self.name}] ❌ Jaringan terisolasi total!\n")
            else:
                print(f"[{self.name}] Tidak perlu pengalihan rute. Sistem di-restart...\n")

            # Beri tahu antrean bahwa tugas ini sudah selesai
            self.alert_queue.task_done()