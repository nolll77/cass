def compute_risk(graph):
    """
    Score de risque systémique (et non individuel).
    Analyse les métriques du graphe pour détecter les défaillances de processus.
    """
    return {
        "delay_risk": graph.avg_delay() * 0.7,
        "fragmentation": graph.missing_edges_ratio(),
        "load_imbalance": graph.load_variance()
    }
