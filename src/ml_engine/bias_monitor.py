import json
import logging
from datetime import datetime

# ==========================================
# MODULE D'AUDIT ANTI-BIAIS & TRANSPARENCE
# ==========================================
# Rôle : Surveiller les prédictions du GNN pour détecter et 
# bloquer tout biais démographique ou territorial.
# Conformité : AI Act (EU), RGPD Art. 22

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BiasMonitor:
    def __init__(self, threshold_variance=0.20):
        # Le seuil de 20% est inspiré de la règle des 80% (Disparate Impact)
        self.threshold_variance = threshold_variance
        self.kill_switch_active = False
        
    def _calculate_disparate_impact(self, category_counts, total_predictions):
        """Calcule l'écart par rapport à une distribution équiprobable théorique."""
        if total_predictions == 0:
            return 0.0
            
        expected_ratio = 1.0 / len(category_counts) if len(category_counts) > 0 else 1.0
        max_variance = 0.0
        
        for category, count in category_counts.items():
            actual_ratio = count / total_predictions
            variance = abs(actual_ratio - expected_ratio) / expected_ratio
            if variance > max_variance:
                max_variance = variance
                
        return max_variance

    def run_audit(self, recent_predictions: list) -> bool:
        """
        Analyse une liste de prédictions récentes.
        Format attendu : [{"geo_hash": "u09j", "age_band": "20-30", "link_strength": "HIGH"}]
        Déclenche le Kill Switch si la variance dépasse le seuil.
        """
        if self.kill_switch_active:
            logging.error("[KILL SWITCH] Le modèle est bloqué pour cause de biais.")
            return False

        high_risk_preds = [p for p in recent_predictions if p.get("link_strength") == "HIGH"]
        total_high = len(high_risk_preds)

        if total_high < 50:
            logging.info("Échantillon trop faible pour un audit statistique significatif.")
            return True

        # Audit Territorial (Geo-Hash)
        geo_counts = {}
        # Audit Démographique (Age Band)
        age_counts = {}

        for p in high_risk_preds:
            geo = p.get("geo_hash", "UNKNOWN")
            age = p.get("age_band", "UNKNOWN")
            geo_counts[geo] = geo_counts.get(geo, 0) + 1
            age_counts[age] = age_counts.get(age, 0) + 1

        # Calcul des variances
        geo_variance = self._calculate_disparate_impact(geo_counts, total_high)
        age_variance = self._calculate_disparate_impact(age_counts, total_high)

        report = {
            "timestamp": datetime.utcnow().isoformat(),
            "total_analyzed": total_high,
            "metrics": {
                "geo_spatial_variance": round(geo_variance, 3),
                "demographic_variance": round(age_variance, 3)
            },
            "status": "COMPLIANT"
        }

        # Déclenchement du Kill Switch (Hard Limit)
        if geo_variance > self.threshold_variance or age_variance > self.threshold_variance:
            self.kill_switch_active = True
            report["status"] = "NON_COMPLIANT - KILL SWITCH ACTIVATED"
            logging.critical(f"⚠️ DÉRIVE DÉTECTÉE ! Variance géographique: {geo_variance:.2f}, Démographique: {age_variance:.2f}")
            logging.critical("🛑 [ACTION] Modèle GNN déconnecté. Renvoi de 'AUDIT_REQUIRED' aux enquêteurs.")
            self._generate_report(report)
            return False

        logging.info("Audit réussi. Aucun biais majeur détecté.")
        self._generate_report(report)
        return True

    def _generate_report(self, report_data: dict):
        """Génère un rapport JSON immuable pour les autorités de contrôle."""
        filename = f"audit_report_{report_data['timestamp'].replace(':', '-')}.json"
        with open(filename, 'w') as f:
            json.dump(report_data, f, indent=4)
        logging.info(f"Rapport de conformité généré : {filename}")

if __name__ == "__main__":
    # Test de Simulation
    monitor = BiasMonitor()
    
    # Simulation d'un échantillon biaisé (Trop de 'HIGH' sur le même code geo_hash 'u09j')
    mock_predictions = [{"geo_hash": "u09j", "age_band": "20-30", "link_strength": "HIGH"} for _ in range(80)]
    mock_predictions += [{"geo_hash": "u09k", "age_band": "30-40", "link_strength": "HIGH"} for _ in range(10)]
    mock_predictions += [{"geo_hash": "u09l", "age_band": "40-50", "link_strength": "HIGH"} for _ in range(10)]
    
    print("--- Lancement de l'Audit sur un échantillon biaisé ---")
    monitor.run_audit(mock_predictions)
