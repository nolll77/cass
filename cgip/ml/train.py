import torch
from model import GNN
from dataset import build_graph

def train():
    """
    Boucle d'entraînement du modèle GNN.
    Optimise la prédiction de relations cachées ou de liens manquants.
    """
    data = build_graph()
    model = GNN(in_channels=2, hidden=8)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    loss_fn = torch.nn.BCEWithLogitsLoss()

    for epoch in range(50):
        optimizer.zero_grad()
        out = model(data.x, data.edge_index).squeeze()
        loss = loss_fn(out, data.y)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch} loss={loss.item()}")

    torch.save(model.state_dict(), "gnn.pt")

if __name__ == "__main__":
    train()
