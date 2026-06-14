import torch
from torch_geometric.data import Data

def build_graph():
    """
    Construit un dataset Graphe (PyG format) synthétique pour l'entraînement.
    Les 'features' représentent la densité temporelle et le degré des noeuds.
    """
    x = torch.tensor([
        [1.0, 0.0],
        [0.9, 0.1],
        [0.2, 0.8],
        [0.3, 0.7],
        [0.5, 0.5]
    ], dtype=torch.float)

    edge_index = torch.tensor([
        [0, 1, 2, 3, 1],
        [1, 2, 3, 4, 4]
    ], dtype=torch.long)

    edge_label = torch.tensor([1, 1, 0, 1, 0], dtype=torch.float)
    return Data(x=x, edge_index=edge_index, y=edge_label)
