def dpia_score(data_type, scale, automation, profiling):
    """
    Moteur de scoring DPIA (Data Protection Impact Assessment).
    Traduit les variables de traitement en score de risque (0-100)
    conforme aux guidelines RGPD.
    """
    score = 0
    if data_type == "SENSITIVE_DATA":
        score += 40
    if scale > 10000:
        score += 20
    if automation:
        score += 20
    if profiling:
        score += 20

    return min(score, 100)

def evaluate_risk(score):
    if score > 75: return "HIGH_RISK"
    if score > 40: return "MEDIUM_RISK"
    return "LOW_RISK"
