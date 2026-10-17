import os
from collections import deque
import matplotlib.pyplot as plt
import networkx as nx

# ==========================================
# 1. SEARCH ALGORITHM (Breadth-First Search)
# ==========================================
class NetworkSearch:
    def __init__(self, graph):
        self.graph = graph

    def find_shortest_path(self, start, goal):
        queue = deque([[start]])
        visited = set([start])

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node == goal:
                return path

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
        return None

# ==========================================
# 2. EXPERT SYSTEM (Forward Chaining)
# ==========================================
class NetworkExpertSystem:
    def diagnose(self, facts):
        rules = [
            {
                "conditions": {"ping_high": True, "packet_loss": True},
                "diagnosis": "Jalur Jaringan Padat / Congestion"
            },
            {
                "conditions": {"server_down": True, "power_ok": True},
                "diagnosis": "Layanan Server Mati (Service Crash)"
            },
            {
                "conditions": {"ping_high": False, "packet_loss": True, "cable_disconnected": True},
                "diagnosis": "Kabel Utama Terputus"
            }
        ]

        for rule in rules:
            match = True
            for key, value in rule["conditions"].items():
                if facts.get(key) != value:
                    match = False
                    break
            if match:
                return rule["diagnosis"]
        
        return "Kondisi Normal / Tidak Terdeteksi Masalah Khusus"

# ==========================================
# 3. MULTI-AGENT SYSTEM
# ==========================================
class MonitoringAgent:
    def __init__(self, name):
        self.name = name

    def collect_network_status(self):
        print(f"[{self.name}] Memeriksa status jaringan...")
        return {
            "ping_high": False,
            "packet_loss": True,
            "cable_disconnected": True,
            "server_down": False,
            "power_ok": True
        }

class ResponseAgent:
    def __init__(self, name, expert_system, search_engine):
        self.name = name
        self.expert_system = expert_system
        self.search_engine = search_engine

    def process_incident(self, facts, start_node, goal_node):
        print(f"[{self.name}] Menerima data dari Monitoring Agent.")
        diagnosis = self.expert_system.diagnose(facts)
        print(f"[{self.name}] Hasil Diagnosis Expert System: '{diagnosis}'")

        path = None
        if "Terputus" in diagnosis or "Padat" in diagnosis:
            print(f"[{self.name}] Memulai Search Algorithm untuk mencari jalur cadangan...")
            path = self.search_engine.find_shortest_path(start_node, goal_node)
            if path:
                print(f"[{self.name}] Jalur cadangan ditemukan: {' -> '.join(path)}")
            else:
                print(f"[{self.name}] Tidak ada jalur cadangan yang tersedia.")
        else:
            print(f"[{self.name}] Tidak perlu pengalihan rute. Melakukan restart layanan...")

        return diagnosis, path

# ==========================================
# VISUALISASI GRAF JARINGAN
# ==========================================
def visualize_network(topology, path_found=None):
    G = nx.DiGraph()
    for node, neighbors in topology.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(9, 6))

    node_colors = ['#1f78b4' for node in G.nodes()]
    edge_colors = ['gray' for edge in G.edges()]

    if path_found:
        path_edges = list(zip(path_found[:-1], path_found[1:]))
        edge_colors = ['#e31a1c' if edge in path_edges else 'gray' for edge in G.edges()]
        node_colors = ['#2ca02c' if node in path_found else '#1f78b4' for node in G.nodes()]

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2000)
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2.5, arrowstyle='->', arrowsize=20)
    nx.draw_networkx_labels(G, pos, font_color='white', font_weight='bold')

    plt.title("Visualisasi Topologi Jaringan & Rute Cadangan (BFS)", fontsize=14)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    network_topology = {
        "Router_A": ["Router_B", "Router_C"],
        "Router_B": ["Router_A", "Router_D"],
        "Router_C": ["Router_A", "Router_D", "Router_E"],
        "Router_D": ["Router_B", "Router_C", "Server_Goal"],
        "Router_E": ["Router_C", "Server_Goal"],
        "Server_Goal": []
    }

    search_engine = NetworkSearch(network_topology)
    expert_system = NetworkExpertSystem()

    monitor_agent = MonitoringAgent("Agent-Monitor-01")
    response_agent = ResponseAgent("Agent-Response-01", expert_system, search_engine)

    print("=== SIMULASI SISTEM AI TERPADU ===")
    network_facts = monitor_agent.collect_network_status()
    response_agent.process_incident(
        facts=network_facts, 
        start_node="Router_A", 
        goal_node="Server_Goal"
    )

if __name__ == "__main__":
    main()
