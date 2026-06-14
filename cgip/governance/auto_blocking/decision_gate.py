class DecisionGate:
    """
    Le cœur du système préventif. Bloque l'exécution d'un modèle d'IA 
    si les contraintes RGPD / DPIA / Gouvernance sont violées.
    """
    def decide(self, risk_score, violations):

        if "PII_WITH_PROFILING" in violations:
            return "BLOCK"

        if risk_score >= 7:
            return "BLOCK"

        if risk_score >= 4:
            return "MODIFY"

        return "ALLOW"
