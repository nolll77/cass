import datetime
from math import exp

"""
Moteur de Time Decay (Droit à l'oubli algorithmique).
Objectif : Réduire le poids d'un lien (edge) dans le graphe au fil du temps.
Un événement vieux de 10 ans sans récidive doit tendre vers zéro.
"""

class TimeDecayEngine:
    def __init__(self, half_life_years=5):
        # La durée de vie moyenne (demi-vie) d'un signalement non judiciaire
        self.half_life_days = half_life_years * 365

    def apply_time_decay(self, initial_confidence, event_timestamp, current_timestamp=None):
        """
        Applique une décroissance exponentielle au score de confiance.
        """
        if current_timestamp is None:
            current_timestamp = datetime.datetime.now()
            
        delta_days = (current_timestamp - event_timestamp).days
        if delta_days < 0:
            return initial_confidence
            
        # Décroissance exponentielle : C(t) = C0 * e^(-lambda * t)
        decay_factor = exp(- (0.693 / self.half_life_days) * delta_days)
        return initial_confidence * decay_factor
