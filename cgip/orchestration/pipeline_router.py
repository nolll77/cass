from orchestration.feature_flags import FEATURES
from core.graph.graph_model import Graph

def run_pipeline(data):
    """
    Routeur central de la plateforme CGIP. 
    Construit le graphe de base et empile les couches de complexité 
    (GNN, Temporal, Causal, Self-Evolving) uniquement si elles sont activées.
    Le module de Gouvernance (E) reste invariant.
    """
    graph = Graph()
    
    if FEATURES["A_basic_graph"]:
        graph.add_node(data.get("entity_a", "A"))
        graph.add_node(data.get("entity_b", "B"))
        graph.add_edge(data.get("entity_a", "A"), data.get("entity_b", "B"), "related")

    if FEATURES["B_gnn"]:
        # graph = run_gnn(graph)
        pass

    if FEATURES["C_temporal"]:
        # graph = add_time_edges(graph)
        pass

    if FEATURES["D_causal"]:
        # graph = causal_inference(graph)
        pass

    if FEATURES["E_governance"]:
        # dpia_check(graph)
        pass

    if FEATURES["F_self_evolving"]:
        # graph = run_agents(graph)
        pass

    return graph
