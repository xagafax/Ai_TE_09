class NetworkExpertSystem:
    """
    Sistem Pakar berbasis Aturan (Rule-Based Expert System) 
    menggunakan Forward Chaining dengan Confidence Scoring.
    """
    def __init__(self):
        # KNOWLEDGE BASE (Basis Pengetahuan AI)
        # Berisi aturan-aturan yang diajarkan oleh "Pakar Jaringan"
        self.knowledge_base = [
            {
                "rule_id": "ERR-001",
                "diagnosis": "Jalur Jaringan Padat (Congestion)",
                "symptoms": ["ping_high", "packet_loss"],
                "recommended_action": "REROUTE"
            },
            {
                "rule_id": "ERR-002",
                "diagnosis": "Kabel Utama Terputus (Link Down)",
                "symptoms": ["cable_disconnected", "packet_loss", "ping_high"],
                "recommended_action": "REROUTE"
            },
            {
                "rule_id": "ERR-003",
                "diagnosis": "Layanan Server Mati (Service Crash)",
                "symptoms": ["server_down", "power_ok"],
                "recommended_action": "RESTART_SERVICE"
            },
            {
                "rule_id": "ERR-004",
                "diagnosis": "Pemadaman Listrik (Blackout)",
                "symptoms": ["server_down"], # power_ok bernilai False
                "recommended_action": "ACTIVATE_UPS"
            }
        ]

    def diagnose(self, facts):
        """
        INFERENCE ENGINE (Mesin Penalar)
        Mencocokkan fakta dari lapangan dengan Knowledge Base 
        dan menghitung persentase keyakinan (Confidence Score).
        """
        # Ekstrak gejala (symptoms) yang bernilai True dari lapangan
        active_symptoms = [key for key, value in facts.items() if value is True]
        
        # Jika tidak ada gejala buruk dan listrik menyala, berarti aman
        if not active_symptoms or (len(active_symptoms) == 1 and "power_ok" in active_symptoms):
            return {
                "diagnosis": "Jaringan Normal",
                "confidence": 100.0,
                "action": "NONE"
            }

        best_match = None
        highest_confidence = 0.0

        # Evaluasi setiap aturan di Knowledge Base
        for rule in self.knowledge_base:
            rule_symptoms = rule["symptoms"]
            
            # Hitung berapa banyak gejala di lapangan yang cocok dengan aturan ini
            match_count = sum(1 for symptom in rule_symptoms if symptom in active_symptoms)
            
            # Hitung persentase kecocokan (Confidence Score)
            if len(rule_symptoms) > 0:
                confidence = (match_count / len(rule_symptoms)) * 100
            else:
                confidence = 0.0

            # Validasi khusus untuk mengecualikan rule "Pemadaman Listrik" jika power_ok = True
            if rule["rule_id"] == "ERR-004" and "power_ok" in active_symptoms:
                confidence = 0.0

            # Selalu simpan diagnosis dengan tingkat keyakinan paling tinggi
            if confidence > highest_confidence:
                highest_confidence = confidence
                best_match = rule

        # Return hasil analisis
        if best_match and highest_confidence >= 50.0: # Ambang batas toleransi AI (Threshold)
            return {
                "diagnosis": best_match["diagnosis"],
                "confidence": round(highest_confidence, 2),
                "action": best_match["recommended_action"]
            }
        
        return {
            "diagnosis": "Anomali Tidak Dikenali (Unclassified Error)",
            "confidence": 0.0,
            "action": "MANUAL_CHECK"
        }