import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EntityResolver:
    """
    Couche d'Entity Resolution (Dédoublonnage Bayesien).
    Utilise la distance de Jaro-Winkler pour déterminer si deux identités (noms/prénoms)
    légèrement différentes correspondent à la même personne.
    """
    
    # Seuil de confiance légal pour fusionner deux identités sans identifiant unique
    MERGE_THRESHOLD = 0.85

    @staticmethod
    def calculate_similarity(name1: str, name2: str) -> float:
        """
        Calcule la similarité entre deux noms en utilisant Jaro-Winkler.
        Particulièrement efficace pour les fautes de frappe administratives ou les abréviations.
        """
        # Normalisation basique
        n1 = name1.lower().strip()
        n2 = name2.lower().strip()
        
        try:
            import jellyfish
            return jellyfish.jaro_winkler_similarity(n1, n2)
        except ImportError:
            import difflib
            return difflib.SequenceMatcher(None, n1, n2).ratio()

    @staticmethod
    def resolve_entities(incoming_entity: dict, db_entities: list) -> dict:
        """
        Prend une entité entrante (ex: issue d'un rapport d'école) et la compare aux entités
        existantes dans la base pour trouver un match.
        
        Args:
            incoming_entity (dict): {'name': 'J. Dupont', ...}
            db_entities (list): [{'id': 'uuid-1', 'name': 'Jean Dupont'}, ...]
            
        Returns:
            dict: Le résultat de la résolution (Match ou Création d'une nouvelle entité)
        """
        incoming_name = incoming_entity.get('name', '')
        best_match = None
        highest_score = 0.0
        
        for db_ent in db_entities:
            db_name = db_ent.get('name', '')
            score = EntityResolver.calculate_similarity(incoming_name, db_name)
            
            if score > highest_score:
                highest_score = score
                best_match = db_ent
                
        if highest_score >= EntityResolver.MERGE_THRESHOLD:
            logger.info(f"MATCH TROUVÉ : '{incoming_name}' fusionné avec '{best_match['name']}' (Score: {highest_score:.2f})")
            return {
                "action": "MERGE",
                "matched_id": best_match['id'],
                "confidence_score": highest_score
            }
        else:
            logger.info(f"AUCUN MATCH SUFFISANT : '{incoming_name}' sera créé comme nouvelle entité (Meilleur score: {highest_score:.2f})")
            return {
                "action": "CREATE_NEW",
                "matched_id": None,
                "confidence_score": 1.0
            }

# Example Usage
if __name__ == "__main__":
    db = [
        {"id": "123", "name": "Jean Dupont"},
        {"id": "456", "name": "Lyhanna M."}
    ]
    
    incoming = {"name": "J. Dupont"}
    result = EntityResolver.resolve_entities(incoming, db)
    print(result)
