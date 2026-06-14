def explain_time_contribution(events):
    """
    Module critique pour le CGIP : explicabilité temporelle.
    Calcule l'impact d'un délai entre deux événements sur le score GNN global.
    """
    contributions = []

    for i in range(len(events) - 1):
        delta = events[i+1]["time"] - events[i]["time"]

        contributions.append({
            "transition": (events[i]["type"], events[i+1]["type"]),
            "delay": delta,
            "impact": "high" if delta > 90 else "low"
        })

    return contributions
