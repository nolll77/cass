FORBIDDEN = [
    "individual_prediction",
    "profiling",
    "automated_decision"
]

def validate_output(output):
    """
    Couche de sécurité RGPD.
    Vérifie qu'aucun output du système ne viole les invariants d'interdiction de décision automatisée.
    """
    for f in FORBIDDEN:
        if f in output:
            raise Exception(f"GDPR VIOLATION RISK: The system attempted an forbidden action -> {f}")
