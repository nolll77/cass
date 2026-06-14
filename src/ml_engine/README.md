# Module Machine Learning & Scoring de Risque

Le pipeline ML XGBoost et son Rule Engine Légal structurent le cœur analytique de la plateforme (Script : `risk_scorer.py`).

## Architecture

1. **Extraction des Features (`extract_features`)** : Le pipeline extrait les variables statistiques traditionnelles (nombre d'événements, gravité) issues de la base relationnelle PostgreSQL, et intègre de manière prépondérante les features topologiques (centralité, proximité) issues du Graphe Neo4j.
2. **Le Modèle XGBoost** : La profondeur de l'arbre est volontairement bridée (`max_depth=4`). Cette limitation structurelle empêche le modèle d'apprendre des corrélations opaques ("Boîte Noire") qui rendraient l'explicabilité impossible lors d'un audit ou au tribunal.
3. **Le Bouclier Légal (`apply_constraints`)** : C'est la traduction algorithmique du socle juridique. Même face à un risque probabiliste estimé à 99% par l'IA, le moteur de règles intervient : si l'individu n'a qu'un seul événement à son actif, le code applique un malus sévère (multiplication du score par 0.70). Dans l'architecture CGIP, le Droit prévaut systématiquement sur la Statistique.
4. **L'Explicabilité (`explain_model`)** : Conçu pour répondre aux exigences de l'AI Act européen. Le script génère en clair les facteurs ayant conduit au score afin de garantir une transparence totale au magistrat (ex: "Accélération temporelle critique de 1.5x").

À l'issue de la compilation, le pipeline génère un objet JSON standardisé :

```json
{
  "person_id": "P001",
  "pipeline_status": "SUCCESS",
  "raw_score_ml": 0.94,
  "final_score_legal": 0.94,
  "alert_level": "CRITICAL_REVIEW_REQUIRED",
  "explanation": {
    "top_factors": [
      "Proximité graphe très élevée (0.85)",
      "Accélération temporelle critique (1.5x)",
      "Convergence 3 institutions"
    ],
    "confidence": 0.88,
    "model_version": "v1.0"
  }
}
```

Le Cœur analytique de la machine est en place. L'étape suivante consiste en l'intégration de jeux de données massifs (Dataset) afin d'éprouver et d'entraîner l'architecture.


---

## Le Modèle GNN (Graph Neural Network)

Le cerveau profond de la CGIP est en place avec le modèle GNN (Script : `gnn_model.py`).

### 1. Les Mathématiques pures
Les équations formelles du *Message Passing* (Agrégation + Mise à jour de la matrice de poids) qui propulsent l'algorithme GraphSAGE ont été modélisées. L'objectif est de rendre auditable la manière dont le modèle mathématique "absorbe" le risque d'un individu via son entourage (à K=2, c'est-à-dire l'ami de l'ami).

### 2. Le Code PyTorch (`gnn_model.py`)
L'architecture du réseau de neurones a été codée en PyTorch Geometric. Le GNN traverse deux couches convolutives (`SAGEConv`). La méthode `get_social_signature(node_id)` prend le sous-graphe d'un suspect (ex: P001) et écrase la topologie sociale de Neo4j en un Vecteur Dense Incompréhensible de dimension `[1, 128]`.

### 3. L'Encapsulation
L'encapsulation est parfaite : La "Boîte Noire" du Deep Learning est isolée ici. Ce script PyTorch ne prend **aucune** décision juridique. Il se contente de générer cette "ADN sociale" (les 128 nombres) qui sera ensuite envoyée à notre script XGBoost (`risk_scorer.py`), seul habilité à formuler la probabilité, elle-même verrouillée par notre Bouclier Légal RGPD.


### Module d'Audit (Bias Monitor & Kill Switch)
Le script `bias_monitor.py` surveille en continu les sorties du modèle (GNN/XGBoost). Conformément à l'AI Act européen, s'il détecte une dérive statistique (une variance > 20% sur la géographie ou la démographie de l'individu), il déclenche un **Hard Limit (Kill Switch)**. Le modèle est déconnecté et ne renvoie plus que l'alerte `AUDIT_REQUIRED` aux enquêteurs, forçant l'intervention d'un Data Scientist humain.
