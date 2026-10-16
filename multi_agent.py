class MonitoringAgent:
    """Agen 1: Bertugas mengumpulkan status/fakta dari lingkungan jaringan"""
    def __init__(self, name):
        self.name = name

    def collect_network_status(self):
        print(f"[{self.name}] Memeriksa status jaringan...")
        # Simulasi fakta/gejala yang ditemukan di lapangan
        facts = {
            "ping_high": False,
            "packet_loss": True,
            "cable_disconnected": True,
            "server_down": False,
            "power_ok": True
        }
        return facts


class ResponseAgent:
    """Agen 2: Menerima hasil diagnosis dan mengeksekusi aksi perbaikan"""
    def __init__(self, name, expert_system, search_engine):
        self.name = name
        self.expert_system = expert_system
        self.search_engine = search_engine

    def process_incident(self, facts, start_node, goal_node):
        print(f"[{self.name}] Menerima data dari Monitoring Agent.")
        
        # Mendiagnosis menggunakan Expert System
        diagnosis = self.expert_system.diagnose(facts)
        print(f"[{self.name}] Hasil Diagnosis Expert System: '{diagnosis}'")

        # Jika diagnosis membutuhkan pengalihan rute
        if "Terputus" in diagnosis or "Padat" in diagnosis:
            print(f"[{self.name}] Memulai Search Algorithm untuk mencari jalur cadangan...")
            path = self.search_engine.find_shortest_path(start_node, goal_node)
            if path:
                print(f"[{self.name}] Jalur cadangan ditemukan: {' -> '.join(path)}")
            else:
                print(f"[{self.name}] Tidak ada jalur cadangan yang tersedia.")
        else:
            print(f"[{self.name}] Tidak perlu pengalihan rute. Melakukan restart layanan...")
