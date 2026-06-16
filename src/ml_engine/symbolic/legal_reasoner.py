"""
Moteur IA Neuro-Symbolique (Compliance Légale)
Vérifie les déductions probabilistes du GNN contre la logique formelle du Code Pénal.
Empêche l'IA de signaler une 'escalade' si les faits ne qualifient aucune infraction légale.
"""

from typing import List, Dict

class LegalReasoner:
    def __init__(self):
        # Ontologie simplifiée du Code Pénal (Graphe de Connaissances formel)
        self.penal_ontology = {
            "MENACE": {"severity": 2, "requires_target": True, "article": "222-17"},
            "VIOLENCE_VOLONTAIRE": {"severity": 4, "requires_target": True, "article": "222-11"},
            "VANDALISME": {"severity": 1, "requires_target": False, "article": "322-1"}
        }

    def validate_ml_alert(self, graph_sub_network: Dict, ml_score: float) -> bool:
        """
        Le GNN (Neuro) pousse un ml_score de 0.9.
        Le Legal Reasoner (Symbolique) vérifie si le graphe contient des éléments
        qualifiables pénalement avant d'alerter le Magistrat.
        """
        has_legal_basis = False
        
        for event in graph_sub_network.get("events", []):
            event_type = event.get("type")
            if event_type in self.penal_ontology:
                rules = self.penal_ontology[event_type]
                
                # Vérification logique stricte
                if rules["requires_target"] and not event.get("has_target"):
                    continue # Non qualifiable
                
                has_legal_basis = True
                break
                
        if not has_legal_basis:
            print("REJET SYMBOLIQUE : L'IA a trouvé un pattern, mais aucune base légale n'est qualifiable.")
            return False
            
        print("VALIDATION NEURO-SYMBOLIQUE : Alerte légalement fondée.")
        return True
