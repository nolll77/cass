import json
import time

# Simulation des modules CGIP déjà codés
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'security'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'ml_engine'))

# Import des modules d'architecture
try:
    from rgpd_anonymizer import RGPDAnonymizer
    from risk_scorer import RiskScorer
except ImportError:
    pass

class CGIPConsumer:
    """
    Le Chef d'Orchestre Temps Réel.
    Il écoute le topic Kafka 'cgip.events.raw', nettoie la donnée, 
    met à jour les bases de données (SQL/Graph) et déclenche l'IA (XGBoost).
    """
    def __init__(self, topic='cgip.events.raw'):
        self.topic = topic
        # Initialisation des sous-systèmes
        self.anonymizer = RGPDAnonymizer("CGIP_PROD_SECRET_KEY")
        self.scorer = RiskScorer()

    def process_message(self, raw_message: str):
        """
        La chaîne d'orchestration stricte.
        """
        print("\n[CONSUMER] 📥 Nouveau message intercepté sur la file Kafka.")
        
        try:
            event = json.loads(raw_message) if isinstance(raw_message, str) else raw_message
            payload = event["payload"]
            
            # 1. ÉTAPE JURIDIQUE : Le Sas Cryptographique
            print("  ├── 🛡️ [ETAPE 1] Anonymisation RGPD (Hashing)")
            clean_payload = self.anonymizer.process_raw_event(payload)
            pseudo_id = clean_payload["person_id"]
            print(f"  │   Identité convertie en: {pseudo_id}")
            
            # 2. ÉTAPE SYSTEM OF RECORD : Commit SQL
            print("  ├── 💾 [ETAPE 2] Écriture PostgreSQL (System of Record)")
            # Simule l'INSERT INTO events...
            
            # 3. ÉTAPE CONTEXTE : Mise à jour du Graphe
            print("  ├── 🕸️ [ETAPE 3] Mise à jour Neo4j (Création Nœud/Arête)")
            # Simule l'exécution Cypher : MERGE (p:Person)-[:INVOLVED]->(e:Event)
            
            # 4. ÉTAPE ANALYTIQUE : Déclenchement du ML
            print("  └── 🧠 [ETAPE 4] Réveil du Modèle ML (XGBoost + Rule Engine)")
            alert_json = self.scorer.compute_risk_score(pseudo_id)
            
            # Résultat
            if alert_json["alert_level"] == "CRITICAL_REVIEW_REQUIRED":
                print(f"\n🚨 [ALERTE ROUGE] Score critique détecté ({alert_json['final_score_legal']}). Transfert immédiat au Magistrat de permanence.")
            else:
                print(f"\n✅ [INFO] Événement digéré. Score actuel: {alert_json['final_score_legal']}. Pas d'action.")
                
        except Exception as e:
            print(f"[ERREUR CONSUMER] Impossible de traiter le message : {e}")

# ==========================================
# TEST RUNNER (Simulation de la boucle)
# ==========================================
if __name__ == "__main__":
    print("--- DÉMARRAGE DU DAEMON KAFKA CONSUMER ---")
    consumer = CGIPConsumer()
    
    # On simule un message entrant (celui que le Producer vient d'envoyer)
    mock_incoming_message = {
        "metadata": {
            "source": "POLICE_CASSIOPEE_V2",
            "timestamp": "2026-06-14T20:00:00",
            "event_id": "EVT-84729"
        },
        "payload": {
            "first_name": "Jean",
            "last_name": "Dupont",
            "date_of_birth": "1980-05-12",
            "event_type": "plainte_violences",
            "severity": 4,
            "location": "Paris 18e"
        }
    }
    
    time.sleep(1) # Simule l'attente réseau
    consumer.process_message(mock_incoming_message)
