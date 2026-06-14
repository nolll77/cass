class AccessControl:
    """
    Implémentation RBAC (Role-Based Access Control).
    Définit qui a le droit de voir quoi. Séparation du pouvoir Algorithmique vs Judiciaire.
    """

    ROLES = {
        "DATA_SCIENTIST": {
            "can_view_pii": False,
            "can_train_models": True,
            "can_trigger_arrest": False
        },
        "WORKER_SOCIAL": {
            "can_view_pii": True, # Sur son secteur uniquement (filtré en amont)
            "can_train_models": False,
            "can_trigger_arrest": False
        },
        "MAGISTRAT": {
            "can_view_pii": True, # A la clé cryptographique globale
            "can_train_models": False,
            "can_trigger_arrest": True # Le seul humain autorisé à valider l'IA
        }
    }

    @staticmethod
    def authorize_action(user_role: str, action: str) -> bool:
        if user_role not in AccessControl.ROLES:
            return False
            
        permissions = AccessControl.ROLES[user_role]
        return permissions.get(action, False)

    @staticmethod
    def get_viewable_data(user_role: str, raw_data: dict, anonymizer) -> dict:
        """
        Renvoie la donnée hachée ou en clair selon les droits du rôle.
        """
        if AccessControl.authorize_action(user_role, "can_view_pii"):
            return raw_data # Le Magistrat voit "Jean Dupont"
        else:
            return anonymizer.process_raw_event(raw_data) # Le Data Scientist voit "P-8f4c2..."

# Mock Test
if __name__ == "__main__":
    from rgpd_anonymizer import RGPDAnonymizer
    
    anon = RGPDAnonymizer("secret")
    data = {"first_name": "Lyhanna", "last_name": "Smith", "event_type": "signalement_social"}
    
    print("Vue Data Scientist :", AccessControl.get_viewable_data("DATA_SCIENTIST", data, anon))
    print("Vue Magistrat      :", AccessControl.get_viewable_data("MAGISTRAT", data, anon))
