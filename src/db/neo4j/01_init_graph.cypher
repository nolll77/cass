// Initialisation du Graphe Neo4j (CGIP)
// Ontologie Physique et Contraintes

// 1. Contraintes d'Unicité et Indexation Spatiale/Temporelle
CREATE CONSTRAINT person_hashed_id IF NOT EXISTS FOR (p:Person) REQUIRE p.hashed_id IS UNIQUE;
CREATE CONSTRAINT event_uuid IF NOT EXISTS FOR (e:Event) REQUIRE e.uuid IS UNIQUE;
CREATE CONSTRAINT legal_article IF NOT EXISTS FOR (l:LegalArticle) REQUIRE l.natinf IS UNIQUE;

// Indexation pour les algorithmes GNN et la recherche spatiale
CREATE INDEX person_embedding IF NOT EXISTS FOR (p:Person) ON (p.graph_embedding);
CREATE INDEX event_timestamp IF NOT EXISTS FOR (e:Event) ON (e.timestamp);

// 2. Initialisation de l'Ontologie Juridique (Le Code Pénal en Dur)
// C'est la base de l'IA Neuro-Symbolique.
MERGE (v:LegalArticle {natinf: 28975, name: "Violences Volontaires", severity: 4})
MERGE (m:LegalArticle {natinf: 12345, name: "Menaces de mort", severity: 3})
MERGE (m)-[:PRECURSOR_TO {probability: 0.65}]->(v);

// 3. Implémentation du Droit à l'Oubli (TTL - Time To Live)
// Utilisation du composant APOC de Neo4j pour expirer automatiquement les signaux faibles (Niveau 2)
// Si un nœud 'SocialSignal' n'est pas converti en 'Event' pénal en 365 jours, il est détruit.

CALL apoc.custom.asProcedure(
  'cgip.apply_ttl',
  'MATCH (s:SocialSignal) WHERE s.expire_at < datetime() DETACH DELETE s',
  'read',
  [],
  []
);

// Un trigger cron système appellera `CALL cgip.apply_ttl()` toutes les nuits.
