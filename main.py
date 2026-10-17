import math
import random
from collections import deque
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import networkx as nx

# ==========================================
# 1. SEARCH ALGORITHM (Tercepat & Terjauh)
# ==========================================
class NetworkSearch:
    def __init__(self, graph):
        self.graph = graph

    def update_graph(self, new_graph):
        self.graph = new_graph

    def find_shortest_path(self, start, goal, blocked_nodes):
        if not start or not goal or start in blocked_nodes or goal in blocked_nodes:
            return None

        queue = deque([[start]])
        visited = set([start])

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node == goal:
                return path

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited and neighbor not in blocked_nodes:
                    visited.add(neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
        return None

    def find_longest_path(self, start, goal, blocked_nodes):
        if not start or not goal or start in blocked_nodes or goal in blocked_nodes:
            return None

        try:
            G_temp = nx.Graph(self.graph)
            
            for node in blocked_nodes:
                if node in G_temp:
                    G_temp.remove_node(node)
            
            if start not in G_temp or goal not in G_temp:
                return None

            generator = nx.shortest_simple_paths(G_temp, source=start, target=goal)
            
            paths = []
            for path in generator:
                paths.append(path)
                if len(paths) >= 8:
                    break
            
            if not paths:
                return None
            
            return paths[-1] if len(paths) > 1 else paths[0]
            
        except Exception as e:
            print(f"[ERROR] Gagal mencari rute terjauh: {e}")
            return None

# ==========================================
# 2. EXPERT SYSTEM
# ==========================================
class NetworkExpertSystem:
    def diagnose(self, facts):
        rules = [
            {"conditions": {"ping_high": True, "packet_loss": True}, "diagnosis": "Jalur Jaringan Padat / Congestion"},
            {"conditions": {"server_down": True, "power_ok": True}, "diagnosis": "Layanan Server Mati (Service Crash)"},
            {"conditions": {"ping_high": False, "packet_loss": True, "cable_disconnected": True}, "diagnosis": "Kabel Utama Terputus"}
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

    def collect_network_status(self, is_node_down):
        if is_node_down:
            return {"ping_high": False, "packet_loss": True, "cable_disconnected": True, "server_down": False, "power_ok": True}
        else:
            return {"ping_high": False, "packet_loss": False, "cable_disconnected": False, "server_down": False, "power_ok": True}

class ResponseAgent:
    def __init__(self, name, expert_system, search_engine):
        self.name = name
        self.expert_system = expert_system
        self.search_engine = search_engine

    def process_incident(self, facts, start_node, goal_node, blocked_nodes, mode="shortest"):
        diagnosis = self.expert_system.diagnose(facts)
        
        if mode == "longest":
            mode_label = "RUTE TERJAUH (Alternatif)"
        else:
            mode_label = "RUTE TERCEPAT"

        if not start_node or not goal_node:
            return diagnosis, [], mode_label

        if mode == "longest":
            path = self.search_engine.find_longest_path(start_node, goal_node, blocked_nodes)
        else:
            path = self.search_engine.find_shortest_path(start_node, goal_node, blocked_nodes)
        
        return diagnosis, path, mode_label


# ==========================================
# 4. TOPOLOGY GENERATOR (JUMLAH ROUTER ACAK 40 s.d. 100)
# ==========================================
def generate_random_topology():
    num_routers = random.randint(40, 100)
    p = max(0.05, min(0.25, 4.0 / num_routers))
    
    while True:
        G_rand = nx.erdos_renyi_graph(num_routers, p)
        if nx.is_connected(G_rand) and num_routers > 1:
            break
            
    topology = {}
    for u in G_rand.nodes():
        name = f"R_{u}"
        topology[name] = [f"R_{v}" for v in G_rand.neighbors(u)]
        
    return topology, num_routers


# ==========================================
# 5. INTERACTIVE DASHBOARD
# ==========================================
if __name__ == "__main__":
    print("\n" + "="*50)
    print(" 🤖 AI NETWORK SEARCH AGENT - CLEAN UI DASHBOARD 🤖")
    print("="*50)
    print("[INFO] Membuka jendela dasbor interaktif...")

    network_topology, current_num_routers = generate_random_topology()
    app_state = {
        "start_node": None,
        "goal_node": None,
        "mode": "shortest"
    }
    blocked_nodes = set()

    search_engine = NetworkSearch(network_topology)
    expert_system = NetworkExpertSystem()
    monitor_agent = MonitoringAgent("Agent-Monitor-01")
    response_agent = ResponseAgent("Agent-Response-01", expert_system, search_engine)

    G = nx.DiGraph()
    for node, neighbors in network_topology.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.random_layout(G)
    
    fig, ax = plt.subplots(figsize=(14, 9)) 
    plt.subplots_adjust(bottom=0.22, top=0.82)

    # Membuat objek teks status sekali saja di awal agar tidak menumpuk
    status_box = fig.text(
        0.5, 0.89, "", ha='center', va='center', fontsize=9.5, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#f0f4f8', edgecolor='#b0c4de', linewidth=1.5)
    )

    def rebuild_topology_and_refresh():
        global network_topology, current_num_routers, G, pos
        network_topology, current_num_routers = generate_random_topology()
        search_engine.update_graph(network_topology)
        
        G.clear()
        for node, neighbors in network_topology.items():
            for neighbor in neighbors:
                G.add_edge(node, neighbor)
                
        pos.clear()
        pos.update(nx.random_layout(G))
        
        app_state["start_node"] = None
        app_state["goal_node"] = None
        blocked_nodes.clear()
        app_state["mode"] = "shortest"

    def draw_dashboard():
        ax.clear()
        
        is_node_down = len(blocked_nodes) > 0
        facts = monitor_agent.collect_network_status(is_node_down)
        diagnosis, current_path, mode_label = response_agent.process_incident(
            facts, app_state["start_node"], app_state["goal_node"], blocked_nodes, mode=app_state["mode"]
        )

        node_colors = []
        node_sizes = []
        for node in G.nodes():
            if node in blocked_nodes:
                node_colors.append('#e31a1c')
                node_sizes.append(300)
            elif node == app_state["start_node"]:
                node_colors.append('#1f77b4')
                node_sizes.append(1100)
            elif node == app_state["goal_node"]:
                node_colors.append('#2ca02c')
                node_sizes.append(1100)
            else:
                node_colors.append('#aec7e8')
                node_sizes.append(250)

        edge_colors = []
        edge_widths = []
        path_edges = []
        if current_path:
            path_edges = list(zip(current_path[:-1], current_path[1:]))
            
        for edge in G.edges():
            if edge in path_edges or (edge[1], edge[0]) in path_edges:
                edge_colors.append('#ff4500')
                edge_widths.append(4.5)
            else:
                edge_colors.append('#b0b0b0')
                edge_widths.append(0.8)

        nx.draw_networkx_nodes(G, pos, ax=ax, node_color=node_colors, node_size=node_sizes)
        nx.draw_networkx_edges(G, pos, ax=ax, edge_color=edge_colors, 
                               width=edge_widths, 
                               arrowstyle='->', arrowsize=6)
        
        font_sz = 6 if current_num_routers > 70 else 7
        nx.draw_networkx_labels(G, pos, ax=ax, font_color='black', font_size=font_sz, font_weight='bold')

        ax.set_title(f"AI SEARCH AGENT - RANDOM TOPOLOGY ({current_num_routers} ROUTERS ACTIVE)", fontsize=12, fontweight='bold', pad=10)

        start_text = app_state["start_node"] if app_state["start_node"] else "Belum Dipilih (Klik Router)"
        goal_text = app_state["goal_node"] if app_state["goal_node"] else "Belum Dipilih (Klik Router)"
        
        panel_text = f"🔵 START: {start_text}   |   🟢 GOAL: {goal_text}   |   ⚙️ MODE: {mode_label}   |   🌐 TOTAL ROUTER: {current_num_routers}\n"
        if current_path:
            panel_text += f"📍 JALUR AKTIF: {' -> '.join(current_path)}"
        elif app_state["start_node"] and app_state["goal_node"]:
            panel_text += "❌ STATUS: JARINGAN TERISOLASI (TIDAK ADA JALUR YANG TERSEDIA!)"
        else:
            panel_text += "👉 PANDUAN: Klik 1 router untuk START, lalu klik 1 router lain untuk GOAL."

        # Memperbarui teks pada objek status_box yang sama tanpa membuat tumpukan baru
        status_box.set_text(panel_text)

        ax.axis('off')
        fig.canvas.draw_idle()

    def on_click(event):
        if event.inaxes != ax: return
        if event.xdata is None or event.ydata is None: return

        closest_node = None
        min_dist = float('inf')
        
        for node, (x, y) in pos.items():
            dist = math.sqrt((event.xdata - x)**2 + (event.ydata - y)**2)
            if dist < min_dist:
                min_dist = dist
                closest_node = node
                
        if min_dist < 0.07 and closest_node:
            if app_state["start_node"] is None:
                app_state["start_node"] = closest_node
                print(f"\n[USER ACTION] 🔵 Titik AWAL (START) dipilih: {closest_node}")
            elif app_state["goal_node"] is None and closest_node != app_state["start_node"]:
                app_state["goal_node"] = closest_node
                print(f"\n[USER ACTION] 🟢 Titik TUJUAN (GOAL) dipilih: {closest_node}")
                print(f"[AI] Menghitung rute {app_state['mode']} dari {app_state['start_node']} ke {app_state['goal_node']}...")
            else:
                if closest_node in [app_state["start_node"], app_state["goal_node"]]:
                    print(f"\n[SYSTEM] Titik {closest_node} adalah Start/Goal aktif!")
                    return
                    
                if closest_node in blocked_nodes:
                    blocked_nodes.remove(closest_node)
                    print(f"\n[USER ACTION] 🔧 Router {closest_node} DIPERBAIKI.")
                else:
                    blocked_nodes.add(closest_node)
                    print(f"\n[USER ACTION] 💥 Router {closest_node} DIMATIKAN! AI mencari ulang rute...")
            
            draw_dashboard()

    ax_btn_short = plt.axes([0.10, 0.04, 0.18, 0.07])
    ax_btn_long  = plt.axes([0.30, 0.04, 0.18, 0.07])
    ax_btn_reset = plt.axes([0.50, 0.04, 0.18, 0.07])
    ax_btn_new   = plt.axes([0.70, 0.04, 0.20, 0.07])

    btn_shortest = Button(ax_btn_short, 'Rute Tercepat', color='#e0f3f8', hovercolor='#9ecae1')
    btn_longest  = Button(ax_btn_long, 'Rute Terjauh', color='#fee0d2', hovercolor='#fc9272')
    btn_reset    = Button(ax_btn_reset, 'Reset Pilihan', color='#e5f5e0', hovercolor='#a1d99b')
    btn_new_topo = Button(ax_btn_new, 'Acak Topologi Baru', color='#ffffcc', hovercolor='#ffe680')

    def trigger_shortest(event):
        app_state["mode"] = "shortest"
        print("\n[GUI COMMAND] ⚡ Mode diubah ke Rute Tercepat!")
        draw_dashboard()

    def trigger_longest(event):
        app_state["mode"] = "longest"
        print("\n[GUI COMMAND] 🔄 Mode diubah ke Rute Terjauh!")
        draw_dashboard()

    def trigger_reset(event):
        app_state["start_node"] = None
        app_state["goal_node"] = None
        blocked_nodes.clear()
        app_state["mode"] = "shortest"
        print("\n[GUI COMMAND] 🔄 Pilihan di-reset! Pilih ulang Start & Goal.")
        draw_dashboard()

    def trigger_new_topology(event):
        rebuild_topology_and_refresh()
        print(f"\n[GUI COMMAND] 🌐 Topologi baru berhasil di-generate! Total router saat ini: {current_num_routers}")
        draw_dashboard()

    btn_shortest.on_clicked(trigger_shortest)
    btn_longest.on_clicked(trigger_longest)
    btn_reset.on_clicked(trigger_reset)
    btn_new_topo.on_clicked(trigger_new_topology)

    fig.canvas.mpl_connect('button_press_event', on_click)
    
    print("\n[INFO] Jendela visualisasi berhasil dibuka.")
    print("Petunjuk Interaksi:")
    print(" 1. Klik router pertama (START) & router kedua (GOAL).")
    print(" 2. Panel informasi status sekarang bersih dan bebas dari penumpukan teks.")
    draw_dashboard()
    plt.show()