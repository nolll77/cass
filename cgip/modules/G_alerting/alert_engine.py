def evaluate_alert(event):
    """
    Alerting Engine (Hybride ML + Règles).
    Examine les événements en temps réel et remonte les signaux aux analystes.
    """
    if event.get("risk_score", 0) > 80:
        return "CRITICAL_ALERT"

    if event.get("pattern") == "repeat_offender":
        return "ESCALATION"

    return "OK"
