# Justice Graph Lab (Open Stack Intelligence Platform)

## 🎯 Objectif
**Un laboratoire open-source de modélisation des défaillances informationnelles.**
L'objectif n'est plus d'enquêter sur une affaire spécifique ("Qui est responsable ?"), mais d'étudier la mécanique des angles morts ("Pourquoi le système ne voit-il pas ce qu'il devrait voir ?"). 
Ce projet implémente un pipeline complet (Ingestion -> Graph DB -> PyTorch Geometric) pour relier des informations fragmentées et détecter des motifs d'accélération dans les trajectoires institutionnelles.

⚠️ Ce projet est :
- académique
- exploratoire
- non opérationnel
- sans usage décisionnel automatisé

---

## 🧠 Concept

Transformer des événements dispersés en un graphe structuré :
- signalements
- alertes
- plaintes
- institutions impliquées
- relations temporelles

---

## 📊 Pipeline

1. Extraction de texte (OSINT)
2. Structuration en événements
3. Normalisation
4. Construction de graphe
5. Analyse descriptive
6. Visualisation

---

## 📁 Dataset

- `events.csv` → événements
- `persons.csv` → entités
- `relations.csv` → liens

---

## ⚖️ Éthique
Ce projet ne fait aucune prédiction sur des individus réels.
Il sert uniquement à étudier la structuration de données complexes.
