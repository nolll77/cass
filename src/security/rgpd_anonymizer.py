import hashlib
import hmac
import os
import uuid

class RGPDAnonymizer:
    """
    Le Sas Cryptographique de la CGIP.
    Transforme les PII (Personally Identifiable Information) en Hash irréversibles
    avant de les injecter dans le Data Lake, le ML ou le Graphe.
    """
    def __init__(self, secret_key: str = None):
        # En production, cette clé est gérée par un KMS (Key Management Service) type SecNumCloud
        self.secret_key = secret_key.encode('utf-8') if secret_key else os.getenv("CGIP_KMS_SECRET", "default_dev_secret").encode('utf-8')

    def anonymize_identity(self, first_name: str, last_name: str, date_of_birth: str) -> dict:
        """
        Hache l'identité civile.
        """
        # Normalisation pour éviter les erreurs de casse/espaces (Entity Resolution brute)
        normalized_str = f"{first_name.strip().upper()}|{last_name.strip().upper()}|{date_of_birth.strip()}"
        
        # Hashing HMAC-SHA256 (Résiste aux attaques par dictionnaire si la clé est forte)
        identity_hash = hmac.new(self.secret_key, normalized_str.encode('utf-8'), hashlib.sha256).hexdigest()
        
        return {
            "pseudo_id": f"P-{identity_hash[:16]}", # Troncature pour l'affichage Neo4j
            "full_hash": identity_hash,
            "is_anonymized": True
        }

    def process_raw_event(self, raw_event: dict) -> dict:
        """
        Désinfecte un événement entrant de toute donnée personnelle.
        """
        clean_event = raw_event.copy()
        
        if "first_name" in clean_event and "last_name" in clean_event:
            anon = self.anonymize_identity(clean_event["first_name"], clean_event["last_name"], clean_event.get("date_of_birth", "1900-01-01"))
            clean_event["person_id"] = anon["pseudo_id"]
            
            # Suppression des PII
            del clean_event["first_name"]
            del clean_event["last_name"]
            if "date_of_birth" in clean_event:
                del clean_event["date_of_birth"]
                
        return clean_event

# Mock Test
if __name__ == "__main__":
    anonymizer = RGPDAnonymizer("secret_etat_123")
    raw_data = {"first_name": "Jean", "last_name": "Dupont", "date_of_birth": "1980-05-12", "event_type": "signalement", "severity": 2}
    print("RAW:", raw_data)
    print("ANON:", anonymizer.process_raw_event(raw_data))
