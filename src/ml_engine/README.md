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
