import logging
import hashlib

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NLPParser:
    """
    Couche B (Secrétaire) : Analyse le texte brut et extrait les entités
    pour les structurer au format Graphe (Nœuds et Arêtes).
    """

    def __init__(self):
        # Pour le prototype, on utilise le modèle Spacy français léger.
        try:
            import spacy
            self.nlp = spacy.load("fr_core_news_sm")
        except Exception:
            logger.warning("Spacy non disponible. Utilisation du fallback NLP basique (Regex).")
            self.nlp = None

    @staticmethod
    def hash_identity(name: str) -> str:
        """Hache une identité pour respecter le RGPD (Privacy by Design)."""
        # Dans un vrai système, un 'sel' secret serait ajouté
        return hashlib.sha256(name.lower().strip().encode('utf-8')).hexdigest()

    def parse_signal(self, text: str, source: str) -> dict:
        """
        Ingère un texte brut (ex: rapport scolaire) et retourne les entités reconnues.
        """
        logger.info(f"NLP: Parsing signal from {source}...")
        
        if not self.nlp:
            logger.warning("NLP Model not loaded. Using regex fallback.")
            
        doc = None
        if self.nlp:
            doc = self.nlp(text)
        
        persons = []
        locations = []
        organizations = []
        
        # 1. Named Entity Recognition (NER)
        if self.nlp:
            for ent in doc.ents:
                if ent.label_ == "PER":
                    persons.append({
                        "raw_name": ent.text,
                        "hashed_id": self.hash_identity(ent.text)
                    })
                elif ent.label_ == "LOC":
                    locations.append(ent.text)
                elif ent.label_ == "ORG":
                    organizations.append(ent.text)
        else:
            # Fallback regex basique
            import re
            names = re.findall(r'[A-Z]\.\s[A-Z][a-z]+|[A-Z][a-z]+\s[A-Z][a-z]+', text)
            for n in names:
                persons.append({
                    "raw_name": n,
                    "hashed_id": self.hash_identity(n)
                })
            if "Collège" in text or "École" in text:
                organizations.append("École/Collège")
                
        # 2. Heuristique basique pour détecter la sévérité (À remplacer par un modèle de classification de texte)
        severity = 2 # Défaut
        danger_keywords = ['violent', 'frappé', 'arme', 'blessé', 'viol', 'agression']
        if any(keyword in text.lower() for keyword in danger_keywords):
            severity = 8
            
        return {
            "source": source,
            "original_text_length": len(text),
            "extracted_nodes": {
                "persons": persons,
                "contexts": locations + organizations,
                "event": {
                    "type": "AdminSignal" if source in ["École", "Hôpital", "Social"] else "OfficialEvent",
                    "estimated_severity": severity
                }
            }
        }

# Example Usage
if __name__ == "__main__":
    parser = NLPParser()
    report = "Hier, le petit J. Dupont a violemment frappé un camarade dans la cour du Collège Rousseau."
    result = parser.parse_signal(report, source="École")
    import json
    print(json.dumps(result, indent=2, ensure_ascii=False))
