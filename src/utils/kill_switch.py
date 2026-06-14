import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DPIABlockError(Exception):
    """Exception levée lorsque le système tente une opération interdite par le RGPD ou la CNIL."""
    pass

class KillSwitch:
    """
    Garde-fou juridique de la Zone Rouge.
    Intercepte les requêtes Python et lève une erreur si le système tente de profiler individuellement.
    """
    
    # Seuil légal : à partir de quel score considère-t-on que l'algorithme "juge" ?
    MAX_ALLOWED_AUTOMATED_SCORE = 0.85 

    @staticmethod
    def verify_action(action_type: str, context: dict):
        """
        Vérifie si une action algorithmique est légale avant de l'exécuter.
        
        Args:
            action_type (str): Le type d'action (ex: 'generate_alert', 'automated_sanction')
            context (dict): Les métadonnées de l'action (ex: {'score': 0.88, 'target': 'person_id'})
        """
        logger.info(f"KILL-SWITCH: Checking action '{action_type}'...")
        
        if action_type == "automated_sanction":
            raise DPIABlockError("VIOLATION DE LA ZONE ROUGE : La machine ne peut pas prendre de décision punitive ou privative de liberté sans humain dans la boucle.")
        
        if action_type == "generate_alert":
            score = context.get('score', 0.0)
            if score > KillSwitch.MAX_ALLOWED_AUTOMATED_SCORE:
                # Le système a le droit d'alerter, mais il doit flagger explicitement que c'est une recommandation
                logger.warning(f"KILL-SWITCH TRIGGERED: Score {score} dépasse la limite d'alerte silencieuse. Transmission obligatoire en Zone Rouge (Magistrat).")
                context['status'] = "REVUE_HUMAINE_RECOMMANDEE"
                return context
        
        return True

# Example Usage
if __name__ == "__main__":
    try:
        KillSwitch.verify_action("automated_sanction", {"target": "user_123"})
    except DPIABlockError as e:
        print(f"Blocage réussi : {e}")
