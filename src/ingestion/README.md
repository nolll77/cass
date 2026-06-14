# Module d'Ingestion : Architecture Temps Réel (Kafka)

Le système nerveux de la CGIP repose sur une architecture orientée événements (Event-Driven). L'architecture globale (SQL, Graphe, ML XGBoost, GNN, Kafka, RGPD) est interfacée de bout en bout pour garantir une réaction en temps réel tout en respectant un encadrement légal strict.

## La Mécanique d'Orchestration

1. **Le Producteur (`kafka_producer.py`)** : Il simule une source d'information sur le terrain (police, école, travailleurs sociaux) qui émet un signalement. Le script encapsule la donnée brute dans une métadonnée stricte et infalsifiable (`source`, `timestamp`) avant de la propulser sur le topic central Kafka.
2. **Le Consommateur (`kafka_consumer.py`)** : Il agit comme un routeur asynchrone permanent (Daemon). Dès qu'un signalement est capté, la cascade d'exécution suivante se déclenche implacablement :
   - **Étape 1 : Le Sas Juridique** -> Anonymisation cryptographique de l'identité via le module `rgpd_anonymizer.py`.
   - **Étape 2 : L'Écriture Légale** -> Enregistrement de l'événement anonymisé dans la base SQL "System of Record" (Vérité administrative).
   - **Étape 3 : Le Contexte Topologique** -> Mise à jour du Graphe de connaissances Neo4j (Création de nœuds et d'arêtes).
   - **Étape 4 : Le Jugement Algorithmique** -> Seulement après la mise à jour des structures de vérité, le modèle ML (XGBoost / Rule Engine) est sollicité pour évaluer le nouvel état de risque de l'individu.

Le résultat de la compilation asynchrone produit des alertes de ce type :
`🚨 [ALERTE ROUGE] Score critique détecté (0.94). Transfert immédiat au Magistrat de permanence.` 

La chaîne s'exécute en quelques millisecondes. L'intelligence artificielle intervient toujours en bout de chaîne, garantissant que ses calculs probabilistes s'appuient sur la topologie la plus fraîche et sécurisée possible.
