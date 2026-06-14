# 🗺️ ROADMAP & GITHUB ISSUES

Ce document retrace les objectifs et les prochaines tâches de développement pour la **Civic Graph Intelligence Platform (CGIP)**. Il sert de base de référence pour les *Issues* GitHub.

## 🗂️ Backlog (Tâches à Réaliser)

### 1. 🖥️ Interface Utilisateur (UI)
*   **Titre** : Connecter le Dashboard Streamlit au Pipeline de Simulation
*   **Description** : Actuellement, l'interface `ui/app.py` contient des données codées en dur (mock). L'objectif est de brancher cette interface sur les retours du `pipeline_router.py` pour afficher le vrai Graphe Neo4j, les calculs GNN et l'état du *Kill Switch* en temps réel.
*   **Labels** : `enhancement`, `ui`

### 2. 🐳 Infrastructure & Déploiement
*   **Titre** : Conteneuriser la Plateforme (Docker + Neo4j)
*   **Description** : Écrire un `Dockerfile` pour le backend/API/UI et un `docker-compose.yml` qui provisionne la stack complète incluant une instance de base de données graphe (Neo4j). L'objectif est que le projet soit exécutable par quiconque via un simple `docker-compose up`.
*   **Labels** : `infrastructure`, `devops`

### 3. 🧠 Machine Learning & Intelligence
*   **Titre** : Implémenter le réseau PyTorch Geometric (GNN)
*   **Description** : Remplacer le "stub" (la simulation textuelle) de la couche B par un véritable script `torch_geometric`. Créer un dataset synthétique, un modèle `GCNConv` minimal, et prouver l'inférence (Link Prediction).
*   **Labels** : `machine-learning`, `core`

### 4. ⚖️ Gouvernance et IA Constitutionnelle
*   **Titre** : Étendre le moteur de calcul DPIA (RGPD)
*   **Description** : Le moteur DPIA (`dpia_scoring.py`) actuel est très basique. Il faut y inclure un arbre de décision plus profond basé sur les articles du RGPD (catégorisation stricte des PII, pondération du risque de biais algorithmique) avant d'autoriser le passage dans le GNN.
*   **Labels** : `governance`, `compliance`

### 5. 🔬 Recherche & Épistémologie
*   **Titre** : Documenter la théorie causale mathématique (DoWhy)
*   **Description** : Rédiger un document technique (`epistemology.md` étendu) qui détaille l'équation mathématique liant le GNN et le DAG causal. Expliquer formellement pourquoi la "Causal Alignment Loss" (Couche BD) empêche l'IA de faire de la police prédictive statistique classique.
*   **Labels** : `documentation`, `research`
