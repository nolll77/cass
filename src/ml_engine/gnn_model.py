import torch
import torch.nn.functional as F
# Importation de PyTorch Geometric (Mock/Fallback si non installé, pour prototypage)
try:
    from torch_geometric.nn import SAGEConv
except ImportError:
    # Fallback formel pour illustrer l'architecture si torch_geometric manque
    class SAGEConv(torch.nn.Module):
        def __init__(self, in_channels, out_channels):
            super().__init__()
            self.lin = torch.nn.Linear(in_channels * 2, out_channels)
        def forward(self, x, edge_index):
            # Simulation de Message Passing (Moyenne très basique)
            # En réalité, SAGEConv agrège les voisins de manière complexe
            return self.lin(torch.cat([x, x], dim=-1))

class SocialGraphSAGE(torch.nn.Module):
    """
    Architecture GraphSAGE (Sample and Aggregate) pour la CGIP.
    Objectif : Compresser le contexte social (Graphe Neo4j) d'un suspect en un vecteur Dense [1, 128].
    Aucune décision n'est prise ici. Le modèle crache uniquement une "signature".
    """
    def __init__(self, in_channels: int, hidden_channels: int, out_channels: int = 128):
        super(SocialGraphSAGE, self).__init__()
        
        # Couche 1 : K=1 (Agrégation des voisins directs : complices, amis proches)
        self.conv1 = SAGEConv(in_channels, hidden_channels)
        
        # Couche 2 : K=2 (Agrégation des voisins de voisins : réseau étendu)
        self.conv2 = SAGEConv(hidden_channels, out_channels)

    def forward(self, x, edge_index):
        """
        Passage Vorace (Forward Pass).
        x: Matrice des features initiales (ex: Age, Sexe, Nbr Délits SQL).
        edge_index: Tenseur de connectivité [2, num_edges] issu de Neo4j.
        """
        # Passage de Message Couche 1
        h1 = self.conv1(x, edge_index)
        h1 = F.relu(h1)          # Activation non-linéaire
        h1 = F.dropout(h1, p=0.5, training=self.training) # Régularisation anti-overfitting
        
        # Passage de Message Couche 2
        h2 = self.conv2(h1, edge_index)
        
        # Le tenseur final h2 est de dimension [N, 128]
        # Il représente l'embedding vectoriel (la signature de risque).
        return h2

    def get_social_signature(self, node_id: int, x, edge_index) -> torch.Tensor:
        """
        Extraction chirurgicale du vecteur d'un suspect précis.
        Ce vecteur [1, 128] sera directement injecté dans XGBoost.
        """
        embeddings = self.forward(x, edge_index)
        return embeddings[node_id]

# ==========================================
# TEST RUNNER (Simulation Mathématique)
# ==========================================
if __name__ == "__main__":
    print("--- COMPILATION DU GRAPH NEURAL NETWORK (GraphSAGE) ---")
    
    # Paramètres simulés
    num_nodes = 5         # 5 Personnes
    num_node_features = 3 # 3 Variables SQL de base (Ex: Age_normalisé, Sexe_enc, Gravité_moyenne)
    embedding_dim = 128   # La dimension ciblée par la doctrine
    
    # 1. Génération de Features factices (Les nœuds Neo4j)
    x_fake = torch.randn((num_nodes, num_node_features))
    
    # 2. Génération de Connexions factices (Les arêtes Neo4j)
    # [Person 0 <-> Person 1], [Person 1 <-> Person 2] etc.
    edge_index_fake = torch.tensor(
        [[0, 1, 1, 2, 2, 3, 3, 4],
         [1, 0, 2, 1, 3, 2, 4, 3]], dtype=torch.long)
    
    # 3. Instanciation du Modèle GNN
    # Entrée=3, Couche Cachée=64, Sortie=128
    model = SocialGraphSAGE(in_channels=num_node_features, hidden_channels=64, out_channels=embedding_dim)
    
    # 4. Simulation : On demande l'ADN social du Suspect 'P001' (Index 0)
    signature_P001 = model.get_social_signature(0, x_fake, edge_index_fake)
    
    print(f"\n> Suspect: P001 (Index 0)")
    print(f"> Dimension Tensor: {signature_P001.shape}")
    print(f"> Signature extraite (Extrait): {signature_P001[:5].detach().numpy()} ...")
    print("\n[SUCCESS] Le Modèle GNN génère un vecteur compatible avec XGBoost.")
