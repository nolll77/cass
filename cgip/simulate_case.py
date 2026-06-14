import sys
import os
import time

# Ajout du dossier courant au path pour les imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Modules factices importés pour l'architecture
from core.graph.graph_model import Graph
from modules.E_gdpr_engine.dpia_scoring import dpia_score, evaluate_risk
from modules.F_autoblocking.kill_switch import KillSwitch, enforce
from modules.G_alerting.alert_engine import evaluate_alert
from modules.H_case_management.case_system import Case

def log(step, message):
    print(f"\n[ÉTAPE {step}] {message}")
    time.sleep(1)

def run_simulation():
    print("="*70)
    print("   CGIP SIMULATOR - SCÉNARIO D'ESCALADE (AFFAIRE L.)   ")
    print("="*70)

    # 1. Initialisation
    log("1", "Initialisation du Graphe Unifié (Couche A)...")
    graph = Graph()

    # Flux chronologique (Inspiré des 8 failles systémiques)
    events = [
        {"id": "EVT_2017", "year": 2017, "source": "Aide Sociale", "type": "Signalement mineur", "entities": ["Adolescente", "J.B."], "weight": 0.4},
        {"id": "EVT_2020", "year": 2020, "source": "Éducation Nationale", "type": "Alerte comportementale", "entities": ["Lycéenne", "M. B."], "weight": 0.5},
        {"id": "EVT_2022", "year": 2022, "source": "Police Nationale", "type": "Plainte classée", "entities": ["Enfant C.", "Jérôme B."], "weight": 0.8}
    ]

    log("2", "Ingestion des données fragmentées (Silos brisés)...")
    for ev in events:
        print(f"   -> Ingestion: {ev['source']} ({ev['year']}) - {ev['type']}")
        for ent in ev["entities"]:
            graph.add_node(ent)
            graph.add_edge(ev["id"], ent, "INVOLVED_IN")

    # 2. Privacy By Design (Time Decay & DPIA)
    log("3", "Privacy By Design : Time Decay & DPIA (Couches E & F)...")
    print("   -> [Gouvernance] Application du Time Decay sur EVT_2017 : le poids passe de 0.4 à 0.05.")
    
    kill_switch = KillSwitch()
    score = dpia_score(data_type="SENSITIVE_DATA", scale=3, automation=True, profiling=False)
    risk_level = evaluate_risk(score)
    print(f"   -> DPIA Score calculé : {score}/100 ({risk_level})")
    
    decision = "WARN" if risk_level == "MEDIUM_RISK" else "ALLOW"
    if risk_level == "HIGH_RISK": decision = "BLOCK"

    try:
        enforce(decision, pipeline="GNN_Analysis", kill_switch=kill_switch)
        print("   -> Decision Gate: ALLOWED (Inférence autorisée sans profilage pénal).")
    except Exception as e:
        print(f"   -> [ARRET D'URGENCE] {str(e)}")
        return

    # 3. Intelligence Artificielle (Les 5 algorithmes)
    log("4", "Inférence Machine Learning (Entity Resolution & Hawkes)...")
    print("   -> [NLP] Entity Resolution : La machine calcule 98% de probabilité que 'J.B.', 'M. B.' et 'Jérôme B.' soient la même entité topologique.")
    print("   -> [Hawkes Process] Détection Temporelle : L'intervalle se réduit (3 ans, puis 2 ans). Le modèle détecte une vélocité d'escalade.")
    print("   -> [Causal GNN] Vérification causale : La structure du réseau de contexte (Spatio-Social) valide la corrélation latente.")
    
    simulated_ml_output = {
        "pattern": "temporal_escalation_on_minors",
        "risk_score": 88,
        "causal_link_confirmed": True
    }

    # 4. Alerte finale
    log("5", "Moteur d'Alerte Finale (Couche G & H)...")
    alert_level = evaluate_alert(simulated_ml_output)
    
    # Remplacement pour affichage métier spécifique au nouveau design
    if alert_level == "CRITICAL_ALERT":
        alert_level = "REVUE HUMAINE RECOMMANDÉE"
        
    print(f"   -> Alert Engine a déclenché : [ {alert_level} ]")

    if alert_level in ["REVUE HUMAINE RECOMMANDÉE", "ESCALATION"]:
        print("   -> Création automatique du Case Virtual Workspace.")
        investigation_case = Case("CASE_ANALYSE_L")
        for ev in events:
            investigation_case.add_event(ev)
            
        print("\n   [Rapport d'Audit du Dossier]")
        audit = investigation_case.audit_trail()
        for k, v in audit.items():
            print(f"      - {k}: {v}")

    print("\n" + "="*70)
    print(" SIMULATION TERMINÉE : Le fractionnement institutionnel a été vaincu.")
    print(" La machine n'a pas prédit de culpabilité, mais a forcé la réunion")
    print(" des silos AVANT le drame de 2026.")
    print("="*70)

if __name__ == "__main__":
    run_simulation()
