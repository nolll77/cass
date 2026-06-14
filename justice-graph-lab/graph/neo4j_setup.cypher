// =========================
// CLEAN DATABASE (DEV ONLY)
// =========================
MATCH (n) DETACH DELETE n;

// =========================
// CONSTRAINTS
// =========================
CREATE CONSTRAINT person_id IF NOT EXISTS FOR (p:Person) REQUIRE p.person_id IS UNIQUE;
CREATE CONSTRAINT event_id IF NOT EXISTS FOR (e:Event) REQUIRE e.event_id IS UNIQUE;
CREATE CONSTRAINT institution_id IF NOT EXISTS FOR (i:Institution) REQUIRE i.institution_id IS UNIQUE;

// =========================
// NODES - INSTITUTIONS
// =========================
CREATE (:Institution {institution_id:"I1", name:"École", type:"education"});
CREATE (:Institution {institution_id:"I2", name:"Police", type:"law_enforcement"});
CREATE (:Institution {institution_id:"I3", name:"Justice", type:"judicial"});

// =========================
// NODES - EVENTS
// =========================
CREATE (:Event {event_id:"E1", date:"2017-03-01", event_type:"signalement", description:"Signalement initial", confidence:0.6, source:"article_1"});
CREATE (:Event {event_id:"E2", date:"2020-05-10", event_type:"alerte", description:"Alerte institutionnelle", confidence:0.7, source:"article_2"});
CREATE (:Event {event_id:"E3", date:"2022-01-15", event_type:"plainte", description:"Plainte déposée", confidence:0.9, source:"article_3"});

// =========================
// NODES - PERSONS
// =========================
CREATE (:Person {person_id:"P1", role:"victime", approx_age:11});
CREATE (:Person {person_id:"P2", role:"suspect", approx_age:32});

// =========================
// RELATIONS PERSON → EVENT
// =========================
MATCH (p:Person {person_id:"P1"}), (e:Event {event_id:"E1"}) CREATE (p)-[:CONCERNED_BY]->(e);
MATCH (p:Person {person_id:"P1"}), (e:Event {event_id:"E2"}) CREATE (p)-[:CONCERNED_BY]->(e);
MATCH (p:Person {person_id:"P1"}), (e:Event {event_id:"E3"}) CREATE (p)-[:CONCERNED_BY]->(e);
MATCH (p:Person {person_id:"P2"}), (e:Event {event_id:"E1"}) CREATE (p)-[:MENTIONED_IN]->(e);

// =========================
// EVENT → INSTITUTION
// =========================
MATCH (e:Event {event_id:"E1"}), (i:Institution {institution_id:"I1"}) CREATE (e)-[:REPORTED_TO]->(i);
MATCH (e:Event {event_id:"E2"}), (i:Institution {institution_id:"I2"}) CREATE (e)-[:REPORTED_TO]->(i);
MATCH (e:Event {event_id:"E3"}), (i:Institution {institution_id:"I3"}) CREATE (e)-[:REPORTED_TO]->(i);

// =========================
// TEMPORAL LINKS
// =========================
MATCH (e1:Event {event_id:"E1"}), (e2:Event {event_id:"E2"}) CREATE (e1)-[:FOLLOWED_BY]->(e2);
MATCH (e2:Event {event_id:"E2"}), (e3:Event {event_id:"E3"}) CREATE (e2)-[:FOLLOWED_BY]->(e3);
