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
- [ ] **Les réformes discutées en France sur le "croisement des signalements"** : Ce qui se prépare au niveau de l'État et comment la CGIP s'inscrit pile dans cette brèche juridique.
- [ ] **Le modèle "corrigé" réaliste** : Comment on implémente la CGIP en France *sans* tomber dans la dérive de la surveillance de masse (sécurité juridique).
- [ ] **Le schéma "Où l'IA peut intervenir sans risque juridique"** : Cartographier exactement les moments de la procédure pénale où l'IA a le droit légal de faire du matching de données.

## 💻 Bloc "Ingénierie, Data et Code"
- [ ] **Le schéma technique "Cloud + Data Lake + Graph DB"** : L'architecture infrastructurelle réelle (serveurs, flux, bases de données) pour implémenter la CGIP.
- [x] **Le pseudo-code du système de scoring** : Comment on code mathématiquement l'escalade temporelle et spatiale du risque. *(Traité dans le Bloc 12)*
- [ ] **L'architecture complète "Data Lake + Graph DB + ML pipeline"** : Le schéma d'infrastructure technique de bout en bout pour le ML.
- [ ] **Génération d'un dataset synthétique (CSV)** : Créer un jeu de données factice complet (person_event_window.csv) respectant la structure de features.
- [ ] **Le modèle de données exact (Base SQL + Graph DB)** : Le schéma des tables (Entities, Relationships, Properties) prêt à être injecté dans Neo4j/PostgreSQL.
- [ ] **La version "Temps réel avec IA"** : L'architecture des webhooks et du streaming de données pour générer des alertes automatiques instantanées (Event-Driven Architecture).

## 🌍 Bloc "Systèmes Internationaux et Étrangers"
- [ ] **Les Pays-Bas (L'approche Jeugdzorg)** : Analyse du système néerlandais de signalements jeunesse et de la gestion des "signaux préoccupants".
- [ ] **Le Danemark (L'intégration par Registre National)** : Comment les Danois interconnectent l'administration, la santé, et le social pour la protection de l'enfance, avec ses effets et ses limites éthiques.
