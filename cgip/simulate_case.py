import sys
import os
import time

# Ajout du dossier courant au path pour les imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.graph.graph_model import Graph
from modules.E_gdpr_engine.dpia_scoring import dpia_score, evaluate_risk
from modules.F_autoblocking.kill_switch import KillSwitch, enforce
from modules.G_alerting.alert_engine import evaluate_alert
from modules.H_case_management.case_system import Case

def log(step, message):
    print(f"\n[ÉTAPE {step}] {message}")
    time.sleep(1)

def run_simulation():
    print("="*60)
    print("   CIVIC GRAPH INTELLIGENCE PLATFORM (CGIP) - SIMULATION   ")
    print("="*60)

    # 1. Initialisation du Graphe (Le socle invariant)
    log("1", "Initialisation du Graphe Unifié (Core Level A)...")
    graph = Graph()

    # Flux d'événements fragmentés simulé (Silos institutionnels)
    events = [
        {"id": "EVT_01", "year": 2020, "source": "Education Nationale", "type": "Signalement mineur", "entities": ["Alice", "Bob"]},
        {"id": "EVT_02", "year": 2022, "source": "Police Nationale", "type": "Plainte classée", "entities": ["A.", "Robert"]},
        {"id": "EVT_03", "year": 2024, "source": "Services Sociaux", "type": "Alerte comportement", "entities": ["Alice", "Bob"]}
    ]

    log("2", "Ingestion des données fragmentées dans le graphe...")
    for ev in events:
        print(f"   -> Ingestion: {ev['source']} ({ev['year']}) - {ev['type']}")
        for ent in ev["entities"]:
            graph.add_node(ent)
            graph.add_edge(ev["id"], ent, "INVOLVED_IN")

    # 2. Contrôle de Gouvernance (DPIA & Auto-Blocking)
    log("3", "Évaluation de la Conformité et du Risque (Couches E & F)...")
    kill_switch = KillSwitch()
    
    # Calcul du risque DPIA pour cette analyse
    score = dpia_score(data_type="SENSITIVE_DATA", scale=3, automation=True, profiling=False)
    risk_level = evaluate_risk(score)
    print(f"   -> DPIA Score calculé : {score}/100 ({risk_level})")
    
    decision = "WARN" if risk_level == "MEDIUM_RISK" else "ALLOW"
    if risk_level == "HIGH_RISK": decision = "BLOCK"

    try:
        enforce(decision, pipeline="GNN_Analysis", kill_switch=kill_switch)
        print("   -> Decision Gate: ALLOWED (Traitement autorisé sous contrainte).")
    except Exception as e:
        print(f"   -> [ARRET D'URGENCE] {str(e)}")
        return

    # 3. Simulation de l'Intelligence Artificielle (GNN + Causal)
    log("4", "Inférence Graph Neural Network & Validation Causale (Couches B & D)...")
    print("   -> GNN Embedding: Calcul des structures latentes...")
    print("   -> Causal DAG: Vérification des précédences temporelles (2020 -> 2022 -> 2024)...")
    print("   -> [RÉSULTAT IA] : Le GNN détecte avec 92% de confiance que 'Bob' (EVT_01, EVT_03) et 'Robert' (EVT_02) partagent la même topologie d'interaction avec la mineure 'Alice'/'A.'.")
    
    simulated_gnn_output = {
        "pattern": "repeat_offender",
        "risk_score": 85,
        "causal_link_confirmed": True
    }

    # 4. Alerte et Gestion de Cas (Operations)
    log("5", "Moteur d'Alerte et Investigation (Couches G & H)...")
    alert_level = evaluate_alert(simulated_gnn_output)
    print(f"   -> Alert Engine a déclenché une alerte de type : {alert_level}")

    if alert_level in ["CRITICAL_ALERT", "ESCALATION"]:
        print("   -> Ouverture automatique d'un Workspace d'investigation.")
        investigation_case = Case("CASE_2024_001")
        
        for ev in events:
            investigation_case.add_event(ev)
            
        print("\n   [Rapport d'Audit du Dossier]")
        audit = investigation_case.audit_trail()
        for k, v in audit.items():
            print(f"      - {k}: {v}")

    print("\n" + "="*60)
    print(" SIMULATION TERMINÉE : Le fractionnement institutionnel a été vaincu.")
    print(" L'affaire a été consolidée AVANT d'atteindre le point de non-retour.")
    print("="*60)

if __name__ == "__main__":
    run_simulation()
