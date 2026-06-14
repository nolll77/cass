# Glossaire Officiel de la CGIP

Ce glossaire définit les concepts techniques, juridiques et mathématiques employés dans l'architecture de la Civic Graph Intelligence Platform (CGIP).

## 1. Concepts Technologiques & Données
- **Knowledge Graph (Graphe de Connaissances)** : Base de données (ici Neo4j) qui modélise l'information sous forme de Nœuds (Entités) et d'Arêtes (Relations), optimisée pour détecter des connexions invisibles dans des bases relationnelles classiques.
- **TGN (Temporal Graph Network)** : Un graphe où chaque relation possède obligatoirement une composante temporelle (timestamp). Cela permet d'étudier l'évolution d'un réseau au fil du temps (vélocité, escalade).
- **Architecture Event-Driven (Kafka)** : Architecture logicielle où le système réagit en temps réel à des événements asynchrones (ex: dépôt de plainte) plutôt que d'attendre des traitements par lots (batchs).
- **Data Lake Souverain** : Lac de données hébergé sur une infrastructure certifiée (ex: SecNumCloud) garantissant que les données régaliennes ne quittent pas la juridiction nationale.

## 2. Intelligence Artificielle & Mathématiques
- **GNN (Graph Neural Network)** : Réseau de neurones conçu pour ingérer non pas des tableaux de données plats, mais la *topologie* d'un réseau (qui est connecté à qui).
- **Link Prediction (Prédiction de liens)** : Tâche d'IA consistant à prédire si deux dossiers ou entités, actuellement non connectés dans la base, devraient l'être au vu de leurs caractéristiques (fusion de dossiers).
- **Message Passing** : Le mécanisme mathématique par lequel un GNN met à jour l'état d'un Nœud en agrégeant l'information de tous ses voisins directs.
- **Disparate Impact (Règle des 80%)** : Mesure statistique d'équité. Si un modèle produit un résultat positif pour une population A à un taux inférieur à 80% de celui d'une population B, il y a présomption de biais (variance > 20%).

## 3. Doctrine Juridique & Conformité (AI Act / RGPD)
- **Human-In-The-Loop (HITL)** : Principe fondamental où l'algorithme n'a qu'un rôle consultatif. Une décision finale (ex: ouvrir une enquête, classer sans suite) doit *toujours* être validée par un magistrat humain.
- **Scoring Individuel Automatisé** : Pratique (illégale selon la CGIP et le RGPD) consistant à attribuer à un individu un "score de dangerosité" ou de récidive par une machine.
- **Rule Engine (Firewall Légal)** : Couche de code (les règles métiers) placée à la sortie du modèle ML pour empêcher physiquement l'algorithme de dépasser ses prérogatives (ex: brider une probabilité à 0.99 pour empêcher la "certitude algorithmique").
- **Kill Switch** : Mécanisme d'arrêt d'urgence. Si le *Bias Monitor* détecte une discrimination territoriale ou démographique, il coupe immédiatement l'accès au modèle prédictif.
- **Pacte Faustien / L'Équilibre Constitutionnel** : Le compromis assumé par l'Europe : sacrifier l'efficacité technologique absolue (surveillance massive) au profit d'un cadre légal strict protégeant les libertés individuelles. La CGIP est une tentative d'hybridation pour regagner en efficacité tout en respectant ce cadre.
