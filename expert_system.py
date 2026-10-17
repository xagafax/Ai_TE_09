class NetworkExpertSystem:
    """Diagnosis masalah berdasarkan kondisi/gejala menggunakan Rule-Based Expert System"""
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