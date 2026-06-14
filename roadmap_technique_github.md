# Roadmap d'Implémentation Technique (Projet `justice-knowledge-system`)

Ce document détaille la déclinaison du Tome III en un Proof of Concept (PoC) informatique réaliste. Il s'agit du pilier "Code" du triptyque (Livre, Code, Science). L'objectif est de construire un **Laboratoire open-source de modélisation des défaillances informationnelles**.

## La Méthodologie O-M-D-E-V-A
1. **Observation :** Collecter sans interpréter.
2. **Modélisation :** Transformer le réel en modèle (Événements, Acteurs).
3. **Données :** Créer un format exploitable.
4. **Expérimentation :** Tester en SQL et Neo4j sans IA.
5. **Validation :** Le modèle décrit-il ce qui s'est passé ?
6. **Automatisation :** LLM, Machine Learning, GNN (seulement à la fin).

## L'Architecture en 15 Couches (De la Réalité à l'IA)

- **Couche 0 — Épistémologie :** Définir ce qu'on observe (faits vs récits).
- **Couche 1 — Sources :** Le corpus documentaire brut (`/data/raw/`).
- **Couche 2 — Extraction des faits :** NLP/LLM pour extraire les événements sans interprétation.
- **Couche 3 — Ontologie :** Le vocabulaire du système (Alias : procureur = parquet).
- **Couche 4 — Résolution d'entités :** Fusionner les identités multiples (J. Dupont = Jean Dupont).
- **Couche 5 — Chronologie :** L'ordonnancement temporel des événements (`build_timeline.py`).
- **Couche 6 — Acteurs :** Personnes, institutions, juridictions.
- **Couche 7 — Flux d'information :** Où l'information circule et où elle s'arrête (goulots).
- **Couche 8 — Base SQL :** Requêtes relationnelles (PostgreSQL).
- **Couche 9 — Base Graphe :** Modélisation Neo4j (`Person -> FILED -> Complaint`).
- **Couche 10 — Métriques :** Mesure scientifique des délais et des ruptures.
- **Couche 11 — Hypothèses :** Tests scientifiques (ex: Les délais sont le principal facteur).
- **Couche 12 — IA & Machine Learning :** Détection d'anomalies, priorisation.
- **Couche 13 — Auditabilité :** Traçabilité totale (de la prédiction à la source originale).
- **Couche 14 — Gouvernance :** Qui valide, qui corrige, qui a accès ?
- **Couche 15 — Reproductibilité :** Conteneurisation Docker, Open Source.

*Note : 80% de la valeur intellectuelle et de l'analyse systémique apparaît dès la Couche 8, avant même l'introduction de l'Intelligence Artificielle.*
