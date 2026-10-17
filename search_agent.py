import threading
import time
import random
import heapq
from queue import Queue

# ==========================================
# 1. SMART SEARCH ALGORITHM (Dijkstra)
# ==========================================
class AdvancedNetworkSearch:
    def __init__(self, graph):
        self.graph = graph  # Graf sekarang menggunakan bobot (latency/ping)

    def find_best_route(self, start, goal):
        """
        Mencari rute paling optimal berdasarkan latency terendah (Dijkstra).
        """
        # Priority queue menyimpan (total_cost, current_node, path)
        queue = [(0, start, [start])]
        visited = set()

        while queue:
            # Selalu mengambil rute dengan cost (latency) paling kecil
            (cost, current_node, path) = heapq.heappop(queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node == goal:
                return path, cost

            for neighbor, weight in self.graph.get(current_node, {}).items():
                if neighbor not in visited:
                    # AI menghindari node yang mati (weight = infinity/sangat besar)
                    if weight < 9999: 
                        heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))
                        
        return None, float('inf')

# ==========================================
# 2. AUTONOMOUS MULTI-AGENT SYSTEM
# ==========================================
class AdvancedMonitoringAgent(threading.Thread):
    def __init__(self, name, network_state, alert_queue):
        super().__init__(daemon=True) # Daemon agar thread mati saat program utama selesai
        self.name = name
        self.network_state = network_state
        self.alert_queue = alert_queue

    def run(self):
        """Berjalan terus-menerus di latar belakang."""
        print(f"[{self.name}] Memulai pemantauan real-time...")
        while True:
            # Simulasi AI mendeteksi perubahan kondisi lapangan secara dinamis
            time.sleep(3) # Mengecek setiap 3 detik
            
            # Simulasi masalah: Tiba-tiba ping Router_B melonjak drastis
            is_anomaly = random.choice([True, False])
            if is_anomaly:
                print(f"\n[{self.name}] ⚠️ ANOMALI TERDETEKSI! Ping Router_B melonjak (5000ms). Mengirim sinyal ke Response Agent!")
                # Mengubah state jaringan secara real-time
                self.network_state["Router_B"]["Router_D"] = 5000 
                # Mengirim pesan darurat ke agen respons
                self.alert_queue.put({"incident": "High Latency", "node": "Router_B"})
            else:
                # Kondisi normal, pulihkan jaringan
                self.network_state["Router_B"]["Router_D"] = 15
                print(f"[{self.name}] Jaringan stabil...")

class AdvancedResponseAgent(threading.Thread):
    def __init__(self, name, search_engine, alert_queue):
        super().__init__(daemon=True)
        self.name = name
        self.search_engine = search_engine
        self.alert_queue = alert_queue

    def run(self):
        """Tertidur menunggu pesan dari queue, bangun jika ada masalah."""
        print(f"[{self.name}] Standby menunggu laporan insiden...")
        while True:
            # Thread berhenti di sini (blocking) sampai ada pesan masuk ke queue
            alert = self.alert_queue.get()
            print(f"[{self.name}] Menerima alert '{alert['incident']}' pada {alert['node']}.")
            
            print(f"[{self.name}] Menghitung ulang rute AI secara dinamis...")
            best_path, total_ping = self.search_engine.find_best_route("Router_A", "Server_Goal")
            
            if best_path:
                print(f"[{self.name}] ✅ Rute Cerdas Ditemukan: {' -> '.join(best_path)} (Total Ping: {total_ping}ms)\n")
            else:
                print(f"[{self.name}] ❌ Jaringan terisolasi total!\n")
            
            self.alert_queue.task_done()

# ==========================================
# MAIN EXECUTION (Uji Coba Langsung)
# ==========================================
if __name__ == "__main__":
    # Topologi dengan bobot (Ping dalam satuan ms)
    # Rute A->B->D normalnya sangat cepat (10 + 15 = 25ms)
    # Rute A->C->E->D memutar dan lebih lambat (20 + 30 + 10 = 60ms)
    dynamic_topology = {
        "Router_A": {"Router_B": 10, "Router_C": 20},
        "Router_B": {"Router_A": 10, "Router_D": 15},
        "Router_C": {"Router_A": 20, "Router_D": 50, "Router_E": 30},
        "Router_D": {"Router_B": 15, "Router_C": 50, "Server_Goal": 5},
        "Router_E": {"Router_C": 30, "Server_Goal": 25},
        "Server_Goal": {}
    }

    ai_search = AdvancedNetworkSearch(dynamic_topology)
    communication_channel = Queue() # Jalur komunikasi antar agen

    monitor = AdvancedMonitoringAgent("Agent-Monitor-02", dynamic_topology, communication_channel)
    responder = AdvancedResponseAgent("Agent-Response-02", ai_search, communication_channel)

    print("=== MENGHIDUPKAN SISTEM AI OTONOM ===")
    responder.start()
    monitor.start()

    # Membiarkan sistem simulasi berjalan selama 15 detik
    try:
        time.sleep(15)
        print("\n=== SIMULASI SELESAI ===")
    except KeyboardInterrupt:
        print("\nDimatikan paksa.")