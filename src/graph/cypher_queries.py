"""
CGIP - Requêtes Cypher (Neo4j)
Ce module contient les requêtes officielles pour construire et interroger le Graphe.
Il traduit les données tabulaires (CSV) en structure réseau (Nodes & Edges).
"""

# 1. INITIALISATION & GOUVERNANCE (CONSTRAINTS)
# Obligatoire avant toute ingestion pour garantir l'intégrité et la conformité RGPD.
INIT_CONSTRAINTS = [
    # Garantir l'unicité des entités pour éviter les doublons après l'Entity Resolution
    "CREATE CONSTRAINT person_id_unique IF NOT EXISTS FOR (p:Person) REQUIRE p.person_id IS UNIQUE;",
    "CREATE CONSTRAINT event_id_unique IF NOT EXISTS FOR (e:Event) REQUIRE e.event_id IS UNIQUE;",
    "CREATE CONSTRAINT inst_id_unique IF NOT EXISTS FOR (i:Institution) REQUIRE i.institution_id IS UNIQUE;",
    
    # TTL (Time-To-Live) : Le Droit à l'Oubli algorithmique encodé dans la base (Index TTL sur les arêtes prédictives)
    # Note: En Neo4j, le TTL natif se met sur les nœuds, pour les arêtes on utilise souvent APOC ou une logique applicative.
    "CREATE INDEX event_date_idx IF NOT EXISTS FOR (e:Event) ON (e.date);"
]

# 2. INGESTION DES NŒUDS (MAPPING DES CSV)

# Ingestion de persons.csv
# On charge l'âge, le rôle et l'historique de risque (qui sera mis à jour dynamiquement)
LOAD_PERSONS = """
LOAD CSV WITH HEADERS FROM 'file:///persons.csv' AS row
MERGE (p:Person {person_id: row.person_id})
SET p.age = toInteger(row.age),
    p.role = row.role,
    p.occupation = row.occupation,
    p.risk_history_count = toInteger(row.risk_history_count);
"""

# Ingestion de events.csv
# Séparation entre OfficialEvent (Police/Justice) et AdminSignal (École/Social)
LOAD_EVENTS = """
LOAD CSV WITH HEADERS FROM 'file:///events.csv' AS row
WITH row,
     CASE WHEN row.source_institution IN ['police', 'justice'] THEN 'OfficialEvent'
          ELSE 'AdminSignal' END AS EventLabel
CALL apoc.create.node(['Event', EventLabel], {
    event_id: row.event_id,
    type: row.event_type,
    date: date(row.date),
    severity_score: toInteger(row.severity_score),
    location: row.location,
    description: row.description
}) YIELD node
RETURN count(node);
"""

# Ingestion de institutions.csv
LOAD_INSTITUTIONS = """
LOAD CSV WITH HEADERS FROM 'file:///institutions.csv' AS row
MERGE (i:Institution {institution_id: row.institution_id})
SET i.type = row.type,
    i.location = row.location,
    i.priority_level = row.priority_level;
"""

# 3. INGESTION DES ARÊTES (GRAPH EDGES)

# Ingestion de relations.csv
# Cette requête lie dynamiquement les Nœuds en fonction du relation_type
LOAD_RELATIONS = """
LOAD CSV WITH HEADERS FROM 'file:///relations.csv' AS row
MATCH (source) WHERE source.person_id = row.source OR source.event_id = row.source
MATCH (target) WHERE target.person_id = row.target OR target.event_id = row.target

// Utilisation d'APOC pour créer une arête dynamique à partir du nom contenu dans le CSV
CALL apoc.create.relationship(source, toUpper(row.relation_type), {
    strength: toFloat(row.strength),
    created_at: date()
}, target) YIELD rel
RETURN count(rel);
"""

# 4. REQUÊTES D'INFÉRENCE & D'ANALYSE (ML FEATURES)

# Calculer la centralité (Degree) d'une Personne
GET_PERSON_DEGREE = """
MATCH (p:Person {person_id: $person_id})-[r]-()
RETURN count(r) AS degree_centrality;
"""

# Trouver le chemin de risque (La fameuse vision 360)
FIND_RISK_PATH = """
MATCH path = (p:Person {person_id: $person_id})-[:LINKED_EVENT*1..3]-(e:Event)
WHERE e.severity_score >= 3
RETURN path;
"""

# Vérifier la "Convergence Multi-sources" pour l'Alerte (Combien d'institutions différentes touchent ce suspect ?)
CHECK_MULTI_SOURCE_CONVERGENCE = """
MATCH (p:Person {person_id: $person_id})-[:LINKED_EVENT]->(e:Event)
RETURN p.person_id, count(DISTINCT e.source_institution) AS institutions_involved
ORDER BY institutions_involved DESC;
"""
