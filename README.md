# 🏛️ Civic Graph Intelligence Platform (CGIP)

> **"Briser les silos institutionnels par l'intelligence sur graphes, sous contrainte constitutionnelle."**

![Status](https://img.shields.io/badge/Status-Proof_of_Concept-blue.svg)
![Architecture](https://img.shields.io/badge/Architecture-Palantir--Like_Clone-orange.svg)
![Governance](https://img.shields.io/badge/Compliance-By--Design-brightgreen.svg)

## 📖 Vision Fondatrice

Le projet **Cass / CGIP** naît d'un diagnostic d'échec systémique au sein des institutions étatiques (Police, Justice, Éducation, Services Sociaux). L'incapacité à croiser des signaux faibles isolés (une procédure classée ici, une alerte scolaire là) mène régulièrement à des tragédies évitables. 

Les systèmes d'information actuels sont des **silos tabulaires**. La CGIP propose un changement de paradigme fondamental : **passer d'un stockage en silos à une représentation en graphes temporels**, pilotée par l'Intelligence Artificielle, mais rigoureusement bridée par un moteur de conformité juridique codé en dur (*Compliance as Code*).

Ce projet n'est pas un outil de "police prédictive" ou de "profilage individuel" (strictement encadrés par le RGPD). C'est un **auditeur de structure institutionnelle** qui relie les angles morts.

---

## 🏗️ Architecture Multi-Couches (A-H)

L'architecture est construite de manière incrémentale, chaque couche ajoutant une dimension épistémologique ou légale au traitement de l'information :

*   **Couche A (Core Graph)** : La vérité immuable. Ingestion des événements fragmentés dans un graphe de connaissances (Neo4j-ready).
*   **Couche B (Graph Neural Networks - GNN)** : Inférence structurelle. Utilisation de *PyTorch Geometric* pour calculer des embeddings spatiaux et prédire les liens manquants (Link Prediction) entre des dossiers apparemment distincts.
*   **Couche D (Causal Engine)** : La validation scientifique. Utilisation de graphes acycliques dirigés (DAG / DoWhy) pour distinguer les simples corrélations statistiques des véritables liens de causalité.
*   **Couche BD (Causal GNN)** : Fusion. Une *Loss Function* qui force mathématiquement le réseau de neurones à respecter les règles de précédence temporelle et de causalité.
*   **Couche E (GDPR / DPIA Engine)** : L'audit légal en temps réel. Un moteur qui calcule dynamiquement le *Data Protection Impact Assessment* (DPIA) de chaque sous-graphe avant même l'inférence.
*   **Couche F (Auto-Blocking / Kill Switch)** : L'enforcement. Si le score DPIA indique un risque de profilage illégal ou de biais discriminatoire, le "Kill Switch" stoppe le pipeline mathématique instantanément.
*   **Couche G & H (Alerting & Case Management)** : L'interface humaine. Quand le système détecte une faille systémique (ex: un individu lié à 3 entités différentes sans que les institutions ne se parlent), il déclenche une escalade et ouvre un espace d'investigation (Workspace) auditable.

---

## 🚀 Preuve de Conception (Simulation End-to-End)

Le dépôt inclut une simulation exécutable démontrant le fonctionnement global du système face au "Fractionnement Institutionnel".

### Scénario simulé :
1. **2020** : Éducation Nationale -> Signalement scolaire d'une élève ("Alice") avec un individu ("Bob").
2. **2022** : Police Nationale -> Plainte classée sans suite avec des identités partiellement renseignées ("A.", "Robert").
3. **2024** : Services Sociaux -> Alerte sur des comportements à risque.

*Sans la CGIP, ces 3 événements n'auraient jamais été liés.*

### Exécuter la simulation locale :

```bash
python cgip/simulate_case.py
```

**Comportement attendu :**
Le script va ingérer les 3 événements, le moteur RGPD va autoriser le traitement sous surveillance (Score: 60/100), le GNN va reconnaître la similarité topologique des individus (Bob = Robert) à 92%, et le module de *Case Management* va ouvrir le dossier `CASE_2024_001` avec une `CRITICAL_ALERT` pour forcer la coordination inter-services.

---

## 📂 Structure du Répertoire (Feature Flags Design)

```text
cgip/
├── core/                   # Moteur de graphe immuable
│   └── graph/graph_model.py
├── modules/                # Architecture par plugins (Feature Flags)
│   ├── B_gnn/              # Intelligence structurelle (PyG)
│   ├── BD_fusion/          # Causal GNN constraint
│   ├── E_gdpr_engine/      # Compliance-as-code
│   ├── F_autoblocking/     # Hardware/Software Kill Switch
│   ├── G_alerting/         # Rules + ML hybrid escalation
│   └── H_case_management/  # Foundry-like Workspace
├── orchestration/          # Router central & DAG
│   └── pipeline_router.py
├── ui/                     # Interface Streamlit ("Palantir-like")
│   └── app.py
└── simulate_case.py        # Le point d'entrée démonstratif
```

---

## 🔒 Éthique et Gouvernance (Le Pacte Faustien Résolu)

Dans les architectures classiques, la sécurité et la conformité légale (RGPD) sont testées *après* que l'IA a ingéré les données. 
Dans la CGIP, la **Compliance est déplacée avant la computation**.
La Couche E et la Couche F constituent un pare-feu infranchissable. C'est l'essence même d'une IA Constitutionnelle : la machine n'a pas le droit de violer la loi, car son architecture logicielle (via le `KillSwitch`) ne lui permet pas de compiler une inférence risquée.

---

## 🛠️ Prochaines Étapes Techniques (Production-Grade)

Pour passer ce PoC à l'échelle industrielle (Enterprise Stack), l'architecture est conçue pour basculer sur :
1. **Streaming Data** : Cluster Kafka (Strimzi) pour l'ingestion temps réel.
2. **Distributed Graph** : Neo4j Cluster (HA Mode) ou TigerGraph.
3. **MLOps** : MLflow pour le registre de modèles GNN.
4. **Orchestration** : Déploiement Kubernetes natif avec Prometheus/Grafana pour l'observabilité du scoring de risque en temps réel.
