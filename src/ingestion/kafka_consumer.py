import json
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MockKafkaConsumer:
    """
    Simulation d'un Consumer Kafka (Couche A).
    En production, ceci utiliserait `confluent_kafka.Consumer`.
    Le but est de montrer comment le flux est ingéré, validé et passé à la Couche NLP.
    """
    
    def __init__(self, topic: str):
        self.topic = topic
        logger.info(f"KAFKA: Subscribed to topic '{self.topic}'")

    def validate_payload(self, payload: dict) -> bool:
        """S'assure que le message JSON respecte le schéma attendu."""
        required_keys = ['event_id', 'type', 'timestamp', 'metadata']
        for key in required_keys:
            if key not in payload:
                logger.error(f"KAFKA: Invalid payload. Missing key '{key}'")
                return False
        return True

    def consume_stream(self, nlp_parser_instance):
        """
        Simule l'écoute continue d'un flux d'événements.
        Dès qu'un message arrive, il est passé au NLP Parser.
        """
        logger.info("KAFKA: Listening for incoming events...")
        
        # Flux simulé (Normalement, boucle while True avec consumer.poll())
        simulated_events = [
            {
                "event_id": "uuid-1111",
                "type": "school_report",
                "timestamp": "2026-06-06T10:00:00Z",
                "metadata": {
                    "source": "École",
                    "text": "J. Dupont a frappé un élève hier dans la cour."
                }
            },
            {
                "event_id": "uuid-2222",
                "type": "police_report",
                "timestamp": "2026-06-07T14:30:00Z",
                "metadata": {
                    "source": "TAJ",
                    "text": "Plainte déposée contre Jean Dupont pour agression à l'arme blanche."
                }
            }
        ]
        
        results = []
        for event in simulated_events:
            logger.info(f"\n[+] KAFKA: Received event {event['event_id']}")
            
            if self.validate_payload(event):
                # Envoi à la couche B (Secrétaire / NLP)
                text = event['metadata'].get('text', '')
                source = event['metadata'].get('source', 'Unknown')
                
                parsed_data = nlp_parser_instance.parse_signal(text, source)
                results.append(parsed_data)
                
            time.sleep(1) # Simulation du temps de réseau
            
        return results

# Example Usage
if __name__ == "__main__":
    from nlp_parser import NLPParser
    
    consumer = MockKafkaConsumer(topic="raw_civic_signals")
    parser = NLPParser()
    
    output = consumer.consume_stream(parser)
    print("\n--- RÉSULTAT DU PIPELINE D'INGESTION ---")
    print(json.dumps(output, indent=2, ensure_ascii=False))
