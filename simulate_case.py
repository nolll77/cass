import json
import logging
from src.ingestion.kafka_consumer import MockKafkaConsumer
from src.ingestion.nlp_parser import NLPParser
from src.entity_resolution.deduplication import EntityResolver
from src.utils.kill_switch import KillSwitch, DPIABlockError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_simulation():
    print("="*50)
    print("CGIP: CIVIC GRAPH INTELLIGENCE PLATFORM - END TO END SIMULATION")
    print("="*50)

    # 1. Initialiser les modules
    logger.info("Démarrage des services...")
    kafka_stream = MockKafkaConsumer(topic="raw_civic_signals")
    nlp_engine = NLPParser()
    
    # Base de données Graph (MOCK)
    # Contient déjà un dossier pour "Jean Dupont"
    graph_db = [
        {"id": "uuid-9999", "name": "Jean Dupont", "privacy_tier": "Standard"}
    ]
    
    print("\n--- PHASE 1: INGESTION KAFKA & NLP (ZONE VERTE) ---")
    # 2. Ingestion & NLP
    parsed_events = kafka_stream.consume_stream(nlp_engine)
    
    print("\n--- PHASE 2: ENTITY RESOLUTION (DÉDOUBLONNAGE) ---")
    # 3. Entity Resolution
    for event in parsed_events:
        persons = event.get('extracted_nodes', {}).get('persons', [])
        for person in persons:
            incoming_name = person['raw_name']
            
            resolution = EntityResolver.resolve_entities({"name": incoming_name}, graph_db)
            
            if resolution['action'] == 'MERGE':
                print(f"✅ Graphe mis à jour : Lien établi entre le nouvel événement et l'ID existant {resolution['matched_id']}")
            else:
                print(f"🆕 Création d'un nouveau nœud Personne dans le Graphe pour : {incoming_name}")
                
    print("\n--- PHASE 3: SCORING & GOUVERNANCE (ZONE ROUGE) ---")
    # 4. Kill Switch (DPIA)
    # Simulons que le modèle XGBoost ait calculé un score de risque très élevé après ces deux événements
    ml_risk_score = 0.88
    
    try:
        # L'IA tente de générer l'alerte
        decision = KillSwitch.verify_action("generate_alert", {"score": ml_risk_score, "target": "uuid-9999"})
        print(f"⚖️ DÉCISION DU SYSTÈME : {decision['status']} (L'IA s'est arrêtée avant de juger, conformément au RGPD).")
        
        # Testons le blocage absolu
        print("\n[!] L'IA tente d'ordonner une sanction automatique...")
        KillSwitch.verify_action("automated_sanction", {"target": "uuid-9999"})
        
    except DPIABlockError as e:
        print(f"🛑 KILL-SWITCH ACTIVÉ : {e}")

if __name__ == "__main__":
    run_simulation()
