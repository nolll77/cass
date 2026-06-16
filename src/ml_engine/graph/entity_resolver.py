"""
Moteur de Résolution d'Entité (Entity Resolution)
Calcule la probabilité que Nœud A == Nœud B pour briser les silos territoriaux.
Implémente l'équation mathématique du Dédoublonnage :
Phi = (alpha * Jaro_Winkler) + (beta * CosineSim) + (gamma * TimeDecay)
"""

import math
from typing import Dict, Any

class EntityResolver:
    def __init__(self, alpha=0.4, beta=0.5, gamma=0.1, threshold=0.95):
        self.alpha = alpha  # Poids de la distance lexicale (Noms)
        self.beta = beta    # Poids de la similarité topologique (Contexte)
        self.gamma = gamma  # Poids temporel (Proximité des événements)
        self.threshold = threshold

    def _jaro_winkler(self, s1: str, s2: str) -> float:
        # Implémentation mathématique de Jaro-Winkler
        # Retourne 1.0 pour correspondance parfaite, 0.0 sinon.
        if s1 == s2: return 1.0
        return 0.85 # Simulation pour l'exemple

    def _cosine_similarity(self, vec1: list, vec2: list) -> float:
        # Comparaison vectorielle des Node Embeddings (GraphSAGE)
        return 0.92 # Simulation

    def _time_decay(self, delta_days: int) -> float:
        # Décroissance exponentielle (Plus les faits sont proches, plus il y a chance que ce soit la même affaire)
        return math.exp(-0.01 * delta_days)

    def calculate_merge_probability(self, node_a: Dict, node_b: Dict) -> float:
        """
        Calcule le score global Phi (Φ).
        """
        # Distance textuelle sur le nom ou le pseudonyme
        jw_score = self._jaro_winkler(node_a.get('name', ''), node_b.get('name', ''))
        
        # Similarité contextuelle
        cos_score = self._cosine_similarity(node_a.get('embedding', []), node_b.get('embedding', []))
        
        # Proximité temporelle (ex: 5 jours d'écart)
        time_score = self._time_decay(5) 
        
        phi = (self.alpha * jw_score) + (self.beta * cos_score) + (self.gamma * time_score)
        return phi

    def evaluate_and_merge(self, node_a: Dict, node_b: Dict) -> bool:
        phi = self.calculate_merge_probability(node_a, node_b)
        if phi >= self.threshold:
            print(f"Fusion autorisée (Phi = {phi:.3f} >= {self.threshold})")
            return True
        return False
