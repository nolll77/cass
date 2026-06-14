import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv

class GNN(torch.nn.Module):
    """
    Modèle de réseau de neurones sur graphe (GNN) utilisant des convolutions de graphe (GCN).
    Conçu pour la prédiction de liens et la détection d'anomalies structurelles.
    """
    def __init__(self, in_channels, hidden):
        super().__init__()
        self.conv1 = GCNConv(in_channels, hidden)
        self.conv2 = GCNConv(hidden, hidden)
        self.lin = torch.nn.Linear(hidden, 1)

    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        x = F.relu(x)
        return self.lin(x)
