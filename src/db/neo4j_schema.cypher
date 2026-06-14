// ==========================================
// SCHÉMA ONTOLOGIQUE NEO4J - CGIP (Couche 3)
// ==========================================
// Exécution recommandée : Neo4j Desktop / AuraDB v5.x
// Description : Définition des contraintes d'unicité, des index spatio-temporels
// et de l'architecture du Graphe de Connaissances Judiciaire.

// ---------------------------------------------------------
// 1. DÉFINITION DES CONTRAINTES D'UNICITÉ (Unique Constraints)
// ---------------------------------------------------------
// Empêche la duplication des nœuds critiques lors du streaming Kafka.

CREATE CONSTRAINT person_id_unique IF NOT EXISTS FOR (p:Person) REQUIRE p.pseudo_id IS UNIQUE;
CREATE CONSTRAINT event_id_unique IF NOT EXISTS FOR (e:Event) REQUIRE e.event_id IS UNIQUE;
CREATE CONSTRAINT case_id_unique IF NOT EXISTS FOR (c:Case) REQUIRE c.case_id IS UNIQUE;
CREATE CONSTRAINT loc_id_unique IF NOT EXISTS FOR (l:Location) REQUIRE l.loc_id IS UNIQUE;
CREATE CONSTRAINT inst_id_unique IF NOT EXISTS FOR (i:Institution) REQUIRE i.inst_id IS UNIQUE;
CREATE CONSTRAINT doc_id_unique IF NOT EXISTS FOR (d:Document) REQUIRE d.doc_id IS UNIQUE;

// ---------------------------------------------------------
// 2. DÉFINITION DES INDEX D'OPTIMISATION (Indexing)
// ---------------------------------------------------------
// Accélère les requêtes du GNN sur la temporalité et la géographie.

CREATE INDEX event_timestamp_idx IF NOT EXISTS FOR (e:Event) ON (e.timestamp);
CREATE INDEX loc_geohash_idx IF NOT EXISTS FOR (l:Location) ON (l.geo_hash);
CREATE INDEX case_status_idx IF NOT EXISTS FOR (c:Case) ON (c.status);

// ---------------------------------------------------------
// 3. EXEMPLE DE PIPELINE D'INGESTION (MERGE Patterns)
// ---------------------------------------------------------
// Cette section illustre comment le 'kafka_consumer.py' injecte la donnée.
// NOTE: La règle de Temporalité Obligatoire est appliquée sur chaque arête.

/*
// A. Création/Mise à jour des Entités (Nodes)
MERGE (p1:Person {pseudo_id: "P-8be71d4"})
  ON CREATE SET p1.age_band = "30-40", p1.risk_flag = "NONE"
  
MERGE (e1:Event {event_id: "EVT-84729"})
  ON CREATE SET e1.type = "PLAINTE", e1.severity = 4, e1.timestamp = datetime("2026-06-14T20:00:00Z")

MERGE (c1:Case {case_id: "DOS-2026-99"})
  ON CREATE SET c1.status = "OPEN", c1.legal_basis = "Art 222-11 Penal"

MERGE (l1:Location {loc_id: "LOC-PARIS-18"})
  ON CREATE SET l1.type = "DOMICILE", l1.geo_hash = "u09j1"

// B. Création/Mise à jour de la Topologie (Edges)
// 1. Rôle de la personne dans l'événement
MERGE (p1)-[inv:INVOLVED_IN]->(e1)
  ON CREATE SET inv.role = "SUSPECT", inv.timestamp = datetime("2026-06-14T20:00:00Z")

// 2. Lien Événement -> Dossier
MERGE (e1)-[trig:TRIGGERS]->(c1)
  ON CREATE SET trig.delay_hours = 0, trig.timestamp = datetime("2026-06-14T20:05:00Z")

// 3. Localisation de l'événement
MERGE (e1)-[occ:OCCURRED_AT]->(l1)
  ON CREATE SET occ.timestamp = datetime("2026-06-14T19:30:00Z")

// 4. Lien Social entre individus (ex: Témoin connaît Suspect)
MERGE (p2:Person {pseudo_id: "P-9xx82"})
MERGE (p2)-[assoc:ASSOCIATED_WITH]->(p1)
  ON CREATE SET assoc.relation_type = "COLLEAGUE", 
                assoc.start_date = date("2025-01-01"), 
                assoc.end_date = null,
                assoc.timestamp = datetime() // Horodatage obligatoire de la détection du lien
*/
