# Fiche Technique & Cartographie du Codebase (CASS V3)

Le projet **CASS (Civic Graph Intelligence Platform)** possède dorénavant une profondeur d'ingénierie qui le classe dans le sommet absolu de la "Tech for Good & Security". Ce socle est gigantesque, implacable, et 100% prêt à être pris en main par n'importe quel développeur d'élite.

Cette fiche cartographie l'architecture absolue (V3) répartie dans le repository :

## 1. Flux & API (Ingestion)
- `src/api/swagger/api_niveau_2_social.yaml` : L'endpoint "Chambre Noire" avec payload chiffré JWE.
- `src/api/swagger/api_niveau_1_justice.yaml` : L'endpoint de la Justice avec contrat strict (NATINF, Rôles).
- `src/kafka/topology.yml` : Les flux Kafka avec les Dead-Letter Queues et rétentions strictes.

## 2. IA Neuro-Symbolique & Confidentialité Différentielle
- `src/ml_engine/nlp/system_prompts.json` & `src/ml_engine/nlp/ner_extractor.py` : Le parseur NLP "Garde-Fous" pour extraire les entités sans halluciner d'intentions.
- `src/ml_engine/graph/entity_resolver.py` : L'algorithme mathématique de dédoublonnage (Jaro-Winkler + CosineSim + Decay).
- `src/ml_engine/symbolic/legal_reasoner.py` : Le pare-feu logique codé en dur sur le Code Pénal.
- `src/ml_engine/graph/differential_privacy_gnn.py` : L'injection de bruit mathématique (k-anonymat) dans le modèle prédictif.

## 3. Bases de Données (Ontologie)
- `src/db/sql/01_schema_niveau_0.sql` : Base PostgreSQL avec politiques Row-Level Security bloquant les lectures non autorisées par un JWT "Magistrat".
- `src/db/neo4j/01_init_graph.cypher` : Initialisation Neo4j incluant la fonction APOC de "Time-To-Live" (Droit à l'oubli temporel).

## 4. Cryptographie & MLOps Extrême
- `src/security/blockchain_audit.py` : Simulation du registre de preuves Hyperledger pour tracer le Magistrat sans inscrire d'identité RGPD.
- `src/security/homomorphic_matcher.py` : Distance de Hamming calculée sur des chaînes de texte FHE chiffrées de bout en bout.
- `infra/mlops_shadow_pipeline.yml` : Pipeline CI/CD qui bloque les modèles ML s'ils présentent un biais d'équité géographique (Disparate Impact Analysis).

## 5. Infrastructure & UI (Air-Gapped / Contrefactuel)
- `infra/docker-compose.yml` : Simulation "Air-Gapped" avec des VLANs (net_core_data sans internet) et réservation de GPU.
- `docs/ui/FRONTEND_ARCHITECTURE_SPECS.md` & `docs/ui/COUNTERFACTUAL_DASHBOARD_SPECS.md` : Spécifications UI pour le moteur WebGL du Magistrat et la "What-If Analysis" (Explicabilité dynamique).
