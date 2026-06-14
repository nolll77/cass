"""
Moteur de Confiance (Privacy by Design).
Objectif : Attribuer un poids initial à un événement en fonction de sa provenance formelle.
Une condamnation pèse plus lourd qu'un signalement administratif.
"""

class ConfidenceEngine:
    def __init__(self):
        self.weights = {
            "OFFICIAL_JUDICIAL": 1.0,
            "ACTIVE_INVESTIGATION": 0.8,
            "ADMINISTRATIVE_ALERT": 0.4,
            "UNVERIFIED_RUMOR": 0.1
        }

    def evaluate_initial_confidence(self, event_type, source_agency):
        """
        Détermine le Confidence Score brut avant inférence GNN.
        """
        if event_type == "CONDAMNATION":
            return self.weights["OFFICIAL_JUDICIAL"]
        elif event_type == "PLAINTE":
            return self.weights["ACTIVE_INVESTIGATION"]
        elif source_agency == "EDUCATION":
            return self.weights["ADMINISTRATIVE_ALERT"]
        else:
            return self.weights["UNVERIFIED_RUMOR"]
