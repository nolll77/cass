-- CGIP : Core System of Record Schema (PostgreSQL)
-- Ce fichier fige la vérité administrative absolue.
-- Il garantit l'intégrité relationnelle avant tout export vers la couche Graphe (Neo4j).

-- Extension pour générer des UUIDs robustes
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ==========================================
-- 1. TABLE: institutions (Les acteurs de terrain)
-- ==========================================
CREATE TABLE IF NOT EXISTS institutions (
    institution_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50) NOT NULL CHECK (type IN ('police', 'justice', 'school', 'hospital', 'social')),
    location VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- ==========================================
-- 2. TABLE: persons (Identités physiques)
-- ==========================================
CREATE TABLE IF NOT EXISTS persons (
    person_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    full_name VARCHAR(255) NOT NULL,
    date_of_birth DATE,
    gender VARCHAR(50),
    nationality VARCHAR(100),
    risk_flag BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- ==========================================
-- 3. TABLE: events (La timeline centrale)
-- ==========================================
-- Tout signalement, de la simple alerte scolaire à la condamnation.
CREATE TABLE IF NOT EXISTS events (
    event_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    person_id UUID NOT NULL REFERENCES persons(person_id) ON DELETE CASCADE,
    event_type VARCHAR(100) NOT NULL,
    severity INT CHECK (severity >= 1 AND severity <= 5),
    event_date DATE NOT NULL,
    institution_id UUID REFERENCES institutions(institution_id) ON DELETE SET NULL,
    description TEXT,
    source_system VARCHAR(100), -- Ex: 'N-SIS', 'Cassiopée', 'LPC'
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- ==========================================
-- 4. TABLE: cases (Regroupement légal)
-- ==========================================
-- Une 'Affaire' qui regroupe plusieurs événements.
CREATE TABLE IF NOT EXISTS cases (
    case_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    status VARCHAR(50) NOT NULL CHECK (status IN ('open', 'closed', 'under_investigation')),
    start_date DATE NOT NULL,
    end_date DATE,
    lead_institution UUID REFERENCES institutions(institution_id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- ==========================================
-- 5. TABLE: case_event_link (Table de jointure)
-- ==========================================
CREATE TABLE IF NOT EXISTS case_event_link (
    case_id UUID REFERENCES cases(case_id) ON DELETE CASCADE,
    event_id UUID REFERENCES events(event_id) ON DELETE CASCADE,
    PRIMARY KEY(case_id, event_id)
);

-- ==========================================
-- 6. TABLE: interactions (Le socle pré-Graphe)
-- ==========================================
-- Capture les relations connues (familiales, sociales, professionnelles) 
-- qui seront transformées en arrêtes Neo4j (:CONNECTED_TO).
CREATE TABLE IF NOT EXISTS interactions (
    interaction_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    person_a UUID NOT NULL REFERENCES persons(person_id) ON DELETE CASCADE,
    person_b UUID NOT NULL REFERENCES persons(person_id) ON DELETE CASCADE,
    interaction_type VARCHAR(100) NOT NULL,
    interaction_date DATE,
    strength FLOAT CHECK (strength >= 0.0 AND strength <= 1.0),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_different_persons CHECK (person_a != person_b)
);

-- ==========================================
-- INDEXATION POUR PERFORMANCES (Avant ML/Graphe)
-- ==========================================
CREATE INDEX idx_events_person_id ON events(person_id);
CREATE INDEX idx_events_institution_id ON events(institution_id);
CREATE INDEX idx_interactions_person_a ON interactions(person_a);
CREATE INDEX idx_interactions_person_b ON interactions(person_b);
