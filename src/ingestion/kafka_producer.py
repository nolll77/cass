import json
import time
import random
from datetime import datetime

# Fallback/Mock si la librairie 'confluent_kafka' n'est pas testée localement
try:
    from confluent_kafka import Producer
    HAS_KAFKA = True
except ImportError:
    HAS_KAFKA = False

class CGIPProducer:
    """
    Simule une institution (Ex: Commissariat de Paris, École primaire) 
    qui saisit un événement dans son système local. 
    L'événement est instantanément "poussé" dans le système nerveux Kafka.
    """
    def __init__(self, broker='localhost:9092', topic='cgip.events.raw'):
        self.topic = topic
        if HAS_KAFKA:
            self.producer = Producer({'bootstrap.servers': broker})
        else:
            self.producer = None # Mode Simulation Console

    def delivery_report(self, err, msg):
        if err is not None:
            print(f"[ERREUR] Échec de transmission: {err}")
        else:
            print(f"[PRODUCER] Événement expédié au topic {msg.topic()} [Partition: {msg.partition()}]")

    def publish_event(self, source_system: str, event_data: dict):
        """
        Format standardisé d'un événement entrant dans l'État.
        """
        payload = {
            "metadata": {
                "source": source_system,
                "timestamp": datetime.utcnow().isoformat(),
                "event_id": f"EVT-{random.randint(10000, 99999)}"
            },
            "payload": event_data
        }
        
        message_bytes = json.dumps(payload).encode('utf-8')
        
        if self.producer:
            self.producer.produce(self.topic, message_bytes, callback=self.delivery_report)
            self.producer.flush()
        else:
            print(f"\n[PRODUCER (MOCK)] 📡 Transmission depuis [{source_system}]...")
            print(f"Payload: {json.dumps(payload, indent=2)}")
            return payload

# ==========================================
# TEST RUNNER (Simulation Poussée d'un Événement)
# ==========================================
if __name__ == "__main__":
    producer = CGIPProducer()
    
    # Simulation : Un policier enregistre une plainte sur Cassiopée
    police_event = {
        "first_name": "Jean",
        "last_name": "Dupont",
        "date_of_birth": "1980-05-12",
        "event_type": "plainte_violences",
        "severity": 4,
        "location": "Paris 18e"
    }
    
    producer.publish_event("POLICE_CASSIOPEE_V2", police_event)
    time.sleep(1)
