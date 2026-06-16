-- Schéma de Base de Données Souveraine (Niveau 0)
-- PostgreSQL avec Row-Level Security (RLS) obligatoire.

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Table des Citoyens (Vérité Légale)
CREATE TABLE t_person_civil (
    civil_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    hashed_graph_id VARCHAR(256) UNIQUE NOT NULL, -- Pointeur vers Neo4j
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    birth_date DATE,
    social_security_hash VARCHAR(256),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table des Procédures Officielles
CREATE TABLE t_official_case (
    case_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    source_system VARCHAR(50) NOT NULL, -- ex: CASSIOPEE, TAJ
    procedure_number VARCHAR(100) UNIQUE NOT NULL,
    natinf_code INTEGER,
    status VARCHAR(50) DEFAULT 'OPEN',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE t_person_case_link (
    civil_id UUID REFERENCES t_person_civil(civil_id),
    case_id UUID REFERENCES t_official_case(case_id),
    role VARCHAR(50),
    PRIMARY KEY (civil_id, case_id)
);

-- -----------------------------------------------------------------------------
-- SÉCURITÉ LIGNE-À-LIGNE (ROW-LEVEL SECURITY)
-- Interdit à quiconque de lire la table 't_person_civil' sans un token de Magistrat.
-- -----------------------------------------------------------------------------

ALTER TABLE t_person_civil ENABLE ROW LEVEL SECURITY;

-- Politique de lecture : Seul un Magistrat authentifié ou le système d'ingestion peut lire.
CREATE POLICY "magistrate_select_policy" ON t_person_civil
    FOR SELECT
    USING (current_setting('request.jwt.claim.role', true) = 'MAGISTRAT_LEVEL_0');

-- -----------------------------------------------------------------------------
-- AUDIT TRIGGERS
-- Interdiction de supprimer un dossier sans trace.
-- -----------------------------------------------------------------------------

CREATE TABLE t_audit_log (
    audit_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    action VARCHAR(50),
    target_table VARCHAR(50),
    executed_by UUID, -- ID du Magistrat/Opérateur
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
