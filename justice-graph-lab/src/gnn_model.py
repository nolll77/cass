import torch
import torch.nn.functional as F
from torch_geometric.nn import SAGEConv, GATConv

class EventGNN(torch.nn.Module):
    """
    Graph Neural Network pour la classification de noeuds (Event).
    Objectif : Prédire si un événement fait partie d'une trajectoire multi-étapes structurée (Link Prediction / Node Classification).
    """
    def __init__(self, in_channels):
        super().__init__()
        self.conv1 = SAGEConv(in_channels, 32)
        self.conv2 = GATConv(32, 16, heads=2, concat=True)
        self.lin = torch.nn.Linear(32, 2)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        
        # Convolution spatiale
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        
        # Attention spatiale temporelle (GAT)
        x = self.conv2(x, edge_index)
        x = F.relu(x)
        
        # Classification (Isolé vs Motif)
        x = self.lin(x)
        return x
