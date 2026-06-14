# 🗺️ Pistes Non Explorées (Le Frigo)

Ce document recense 100% des concepts, architectures, modèles et analyses qui ont été proposés lors des itérations de conception mais qui ont été mis "en attente" au profit d'autres priorités d'architecture.

Il s'agit du "frigo" intellectuel du projet CGIP. Lorsqu'un sujet est exploré, il doit être retiré d'ici et impacté dans les 7 autres fichiers fondamentaux.

## 🕰️ Bloc "Faits et Procédures (Affaire L.)"
- [ ] **La chronologie claire année par année** : Une frise temporelle brute nettoyée des répétitions journalistiques.
- [ ] **Le découpage Strict (Officiel vs Rumeur)** : Séparer d'un côté uniquement ce qui est juridiquement officiel (les plaintes) et de l'autre les signaux faibles (alertes internes).
- [ ] **La carte "Une victime = Une affaire"** : Pour ne plus jamais confondre les dossiers entre eux.
- [ ] **La timeline unique "type dossier judiciaire"** : Sans répétition presse, formatée comme une vraie instruction.
- [ ] **Le modèle "Où le système aurait pu intervenir plus tôt"** : L'analyse contrefactuelle (le fameux "What if") prouvant à quel mois de quelle année l'IA aurait levé un drapeau rouge.
- [ ] **Comparaison avec d'autres affaires similaires en France** : Une analyse structurelle pour montrer que ce qui a failli ici a déjà failli ailleurs.

## 🏛️ Bloc "Juridique et Politique Publique"
- [ ] **Les réformes discutées en France sur le "croisement des signalements"** : Ce qui se prépare au niveau de l'administration et comment la CGIP s'inscrit pile dans cette brèche juridique.
- [ ] **Le modèle "corrigé" réaliste** : Comment on implémente la CGIP en France *sans* tomber dans la dérive de la surveillance de masse (sécurité juridique).
- [ ] **Le schéma "Où l'IA peut intervenir sans risque juridique"** : Cartographier exactement les moments de la procédure pénale où l'IA a le droit légal de faire du matching de données.

## 💻 Bloc "Ingénierie, Data et Code"
- [ ] **Le schéma technique "Cloud + Data Lake + Graph DB"** : L'architecture infrastructurelle réelle (serveurs, flux, bases de données) pour implémenter la CGIP.
- [x] **Le pseudo-code du système de scoring** : Comment on code mathématiquement l'escalade temporelle et spatiale du risque. *(Traité dans le Bloc 12)*
- [x] **L'architecture complète "Data Lake + Graph DB + ML pipeline"** : Le schéma d'infrastructure technique de bout en bout pour le ML. *(Traité dans le Bloc 13)*
- [ ] **Génération d'un dataset synthétique (CSV)** : Créer un jeu de données factice complet (person_event_window.csv) respectant la structure de features.
- [x] **Le modèle de données exact (Base SQL + Graph DB)** : Le schéma des tables (Entities, Relationships, Properties) prêt à être injecté dans Neo4j/PostgreSQL. *(Traité dans le Bloc 16)*
- [x] **La version "Temps réel avec IA"** : L'architecture des webhooks et du streaming de données pour générer des alertes automatiques instantanées (Event-Driven Architecture). *(Traité dans le Bloc 15)*
- [ ] **Architecture 100% Cloud Souverain (Architecture Souveraine)** : Les specs pour héberger ça sur SecNumCloud sans AWS/GCP.
- [ ] **Design d'un GNN sur dossiers judiciaires** : Architecture précise du réseau de neurones sur graphe (GraphSAGE / Node2Vec) pour des délits. *(Version mathématique complète à faire).*
- [ ] **Simulation de l'Affaire L. en graphe de données Neo4j** : Transformer l'affaire en une requête Cypher exacte.
- [ ] **Limites juridiques RGPD + CNIL sur ce type d'IA** : Rédiger le mémo légal d'audit de l'architecture.

## 🌍 Bloc "Systèmes Internationaux et Étrangers"
- [ ] **Les Pays-Bas (L'approche Jeugdzorg)** : Analyse du système néerlandais de signalements jeunesse et de la gestion des "signaux préoccupants".
- [x] **Comparaison Chine / USA / UK** : Positionnement de la France face au modèle de surveillance, prédictif ou pragmatique. *(Traité dans le Bloc 14)*
- [x] **Comparaison France / UK / Scandinavie** : Modèle hybride idéal Europe basé sur l'administration-providence et le Care. *(Traité dans le Bloc 15)*
- [ ] **Analyse : pourquoi l'UE bloque structurellement une IA type UK/US** : Le choc juridique entre le risk-based policing et les traités européens.
- [ ] **Architecture technique : système "prévention sans surveillance massive"** : Comment coder les limites éthiques scandinaves.
- [x] **Architecture RGPD compatible (version réaliste Europe)** : Spécifications exactes de conformité CNIL. *(Version stricte UE traitée dans le Bloc 17 - Zones Vert/Jaune/Rouge)*.
- [ ] **Simulation complète d'un cas multi-institutions (3 systèmes)** : Dérouler l'affaire L. dans Cassiopée, MASH UK, et Modèle Suédois.
- [x] **Version "industrie type Palantir / police analytics"** : Construire la maquette avec des outils Big Data existants. *(Traité dans le Bloc 16 via Benchmark)*
- [ ] **Exemple concret de pipeline "Safe Scoring"** : Coder l'architecture avec isolation de la Zone Jaune.
- [x] **Modèle de graphe de données "Idéal Européen"** : Spécification d'un graphe respectant les limites RGPD par design. *(Traité dans le Fichier Technique)*
- [x] **Système ML de détection de signaux faibles** : Architecture de l'IA (Features, Scoring, Poids). *(Traité dans le Socle Mathématique)*
- [x] **Schéma technique complet (Data Lake Justice + AI Layer)** : Cartographie de déploiement cloud souverain. *(Traité dans Fichier Technique - Mermaid)*
- [ ] **Le Danemark (L'intégration par Registre National)** : Comment les Danois interconnectent l'administration, la santé, et le social pour la protection de l'enfance, avec ses effets et ses limites éthiques.


- [ ] Produire un schéma SQL + Graph DB exact (tables + edges)
- [ ] Écrire un pseudo-code complet de scoring ML (Ex: Node2Vec)
- [ ] Maquetter une version 'temps réel streaming Kafka + alert engine'

- [x] Implémenter la version `Neo4j ready (Cypher)` du dataset
- [ ] Coder le script pour générer le dataset de 10 000 lignes simulées réalistes
- [ ] Écrire le pseudo-code complet du modèle XGBoost d'après ces features
- [ ] Rédiger le pipeline industriel `Kafka -> Lake -> Graph -> ML` en pseudo-code

- [ ] Concevoir un "best-of architecture mondiale hybride idéale" (Diagramme)
- [ ] Coder un système de scoring type UK DASH + graph ML
- [ ] Construire une simulation temps réel (streaming + alert engine) complète
- [ ] Rédiger une analyse des risques juridiques européens (RGPD + AI Act)

- [ ] Modéliser la version GNN pure (Graph Neural Network complet)
- [ ] Détailler l'architecture Kafka temps réel
- [ ] Générer un dataset de training massif à 1 Million de lignes simulées
- [ ] Rédiger une analyse des biais et erreurs types (False Positives / False Negatives)

- [ ] Modéliser une architecture hybride "Europe idéale vs monde réel"
- [x] Lancer une simulation mathématique d'un système "Chinois" vs "UK" sur notre dataset P001
- [ ] Achever le Pipeline temps réel complet (Kafka + Graph + ML + Alerting)
- [ ] Écrire l'Analyse stricte des risques juridiques (RGPD vs AI Act vs US Law)

- [ ] Modéliser le pipeline Kafka + Spark + Graph + ML (Architecture Temps Réel)
- [ ] Écrire les mathématiques et le pseudo-code complet du modèle GNN (Graph Neural Network)
- [ ] Réaliser le dump importable "Neo4j Complet" du dataset synthétique

- [x] Concevoir l'architecture Kafka streaming temps réel (Event-driven)
- [x] Détailler le modèle GNN (Graph Neural Network) pour les liens de risque
- [x] Rédiger un document de design "Compatible CNIL / RGPD strict"
- [ ] Créer une simulation visuelle complète E2E d'un cas (Timeline + Scoring + Graph)

- [ ] Modéliser à quoi ressemblerait une version 100% acceptable juridiquement en France (Documentation).
- [ ] Analyser techniquement les outils de scoring spécifiques du UK.
- [ ] Concevoir le design d'un modèle hybride "Prévention sans profilage individuel".

- [ ] Réaliser une simulation complète d'un cas dossier complexe (Timeline + Détection GNN + Alertes) dans le pipeline Cloud Souverain.
- [ ] Étudier les mathématiques du Temporal Clustering pour la prédiction de crise à très court terme.
- [ ] Détailler l'architecture "Hardware Security Module (HSM)" et le chiffrement End-to-End.

- [ ] Modéliser un Temporal GNN (TGN) complet : Event stream -> dynamic graph -> evolving embeddings.
- [ ] Concevoir l'architecture du Subgraph Justification Engine (Moteur d'Explicabilité).
- [ ] Analyser les méthodes pour rendre le modèle de clustering CNIL-compatible sans perdre 80% de performance.