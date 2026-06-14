# Le Schéma Neo4j (Knowledge Graph Judiciaire)

L'implémentation de l'ontologie complète du graphe judiciaire a été poussée sur le dépôt.

## IMPORTANT : Le Paradigme du Temporal Graph (TGN)
La règle d'or architecturale est que **la temporalité est obligatoire sur toutes les arêtes**. Le modèle GNN ne verra pas qu'un simple graphe statique, il verra le graphe évoluer dans le temps. C'est le seul moyen mathématique de calculer la vélocité d'une enquête ou l'escalade d'une crise.

## Ce qui a été accompli

### 1. Le Code Cypher (Le Moteur)
Le script exécutable `neo4j_schema.cypher` contient :
- **La sécurité de la donnée (Contraintes)** : On force l'unicité des ID (`person_id`, `event_id`, `case_id`) pour éviter que le système Kafka ne duplique des nœuds en cas de désynchronisation.
- **La performance (Index)** : Des index spécifiques ont été placés sur `geo_hash` (pour calculer la proximité spatiale) et sur `timestamp` (pour l'accélération temporelle).
- **Le Pipeline d'Ingestion (MERGE)** : Les commandes d'ingestion "Upsert" (`MERGE`) que le backend Python utilisera pour injecter dynamiquement les plaintes, suspects et lieux ont été codées.

### 2. Diagramme Entité-Relation (Mermaid)
Voici la représentation visuelle de l'ontologie. Note : La temporalité est obligatoire sur TOUTES les arêtes (`timestamp` ou `start_date`), permettant l'analyse temporelle dynamique par le GNN (TGN).

```mermaid
erDiagram
    PERSON {
        string pseudo_id "Haché (RGPD)"
        string age_band "Ex: 30-40"
        string risk_flag "Manuel"
    }
    EVENT {
        string event_id "Identifiant unique"
        string type "Ex: PLAINTE, AUDITION"
        int severity "1 à 5"
        datetime timestamp "Obligatoire"
    }
    CASE {
        string case_id "Dossier Judiciaire"
        string status "OPEN/CLOSED"
        string legal_basis "Article Code Pénal"
    }
    LOCATION {
        string loc_id
        string type "Ex: DOMICILE, ECOLE"
        string geo_hash "Index Spatial"
    }
    INSTITUTION {
        string inst_id
        string ministry "Intérieur, Justice"
    }
    DOCUMENT {
        string doc_id
        string classification_level
    }

    PERSON ||--o{ EVENT : "INVOLVED_IN {role, timestamp}"
    EVENT ||--o{ CASE : "TRIGGERS {delay_hours, timestamp}"
    EVENT }o--|| LOCATION : "OCCURRED_AT {timestamp}"
    PERSON }o--o{ PERSON : "ASSOCIATED_WITH {relation_type, start_date}"
    CASE }o--o{ CASE : "RELATED_TO {confidence_score, timestamp}"
    PERSON }o--o{ DOCUMENT : "MENTIONED_IN {timestamp}"
    EVENT }o--|| INSTITUTION : "REPORTED_BY {timestamp}"
```
