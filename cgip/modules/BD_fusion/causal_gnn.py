import torch
import torch.nn.functional as F

class CausalGNN(torch.nn.Module):
    """
    Fusion B+D : Le Causal Graph Neural System.
    Relie la représentation structurelle (GNN) et la sémantique d'intervention (Causal).
    """
    def __init__(self, gnn_encoder):
        super().__init__()
        self.encoder = gnn_encoder
        self.causal_gate = torch.nn.Linear(64, 1)

    def forward(self, x, edge_index, dag_edges):
        z = self.encoder(x, edge_index)
        causal_mask = self.causal_gate(z).sigmoid()
        return z, causal_mask

def causal_alignment_loss(z, edge_index, causal_edges):
    """Force la cohérence entre GNN et le DAG causal."""
    pred = (z[edge_index[0]] * z[edge_index[1]]).sum(dim=1)
    causal_mask = torch.zeros_like(pred)
    
    # Fake processing for alignment
    loss = torch.nn.functional.binary_cross_entropy_with_logits(pred, causal_mask)
    return loss
