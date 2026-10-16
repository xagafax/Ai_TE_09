from search_agent import NetworkSearch
from expert_system import NetworkExpertSystem
from multi_agent import MonitoringAgent, ResponseAgent

def main():
    # Topologi Jaringan (Peta Graph untuk Search Algorithm)
    network_topology = {
        "Router_A": ["Router_B", "Router_C"],
        "Router_B": ["Router_A", "Router_D"],
        "Router_C": ["Router_A", "Router_D", "Router_E"],
        "Router_D": ["Router_B", "Router_C", "Server_Goal"],
        "Router_E": ["Router_C", "Server_Goal"],
        "Server_Goal": []
    }

    # Inisialisasi Komponen AI
    search_engine = NetworkSearch(network_topology)
    expert_system = NetworkExpertSystem()

    # Inisialisasi Agen Multi-Agent
    monitor_agent = MonitoringAgent(name="Agent-Monitor-01")
    response_agent = ResponseAgent(
        name="Agent-Response-01", 
        expert_system=expert_system, 
        search_engine=search_engine
    )

    # Jalankan Simulasi
    print("=== SIMULASI SISTEM AI TERPADU ===")
    network_facts = monitor_agent.collect_network_status()
    response_agent.process_incident(
        facts=network_facts, 
        start_node="Router_A", 
        goal_node="Server_Goal"
    )

if __name__ == "__main__":
    main()
