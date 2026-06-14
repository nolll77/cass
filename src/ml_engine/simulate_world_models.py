import json
from datetime import datetime

# ==========================================
# DONNÉES DE BASE (Le profil de P001)
# ==========================================
# E001: 2017 - Signalement police (Paris)
# E002: 2018 - Classement sans suite justice (Paris)
# E003: 2020 - Alerte educative (Toulouse)
# E004: 2020 - Licenciement administratif (Toulouse)
# E006: 2024 - Signalement social (Lille)
# E008: 2026 - Disparition police (Fleurance)

class ProfileP001:
    def __init__(self):
        self.institutional_events = [
            {"year": 2017, "type": "police_signal", "severity": 2, "region": "Paris"},
            {"year": 2018, "type": "justice_dismissal", "severity": 1, "region": "Paris"},
            {"year": 2020, "type": "school_alert", "severity": 2, "region": "Toulouse"},
            {"year": 2020, "type": "admin_dismissal", "severity": 1, "region": "Toulouse"},
            {"year": 2024, "type": "social_signal", "severity": 3, "region": "Lille"},
        ]
        # Données de surveillance (uniquement accessibles par la Chine)
        self.lifestyle_data = [
            {"year": 2019, "type": "cctv_proximity_school", "frequency": "high"},
            {"year": 2021, "type": "social_media_crawling", "risk_flag": True},
            {"year": 2023, "type": "mobility_pattern_anomaly", "severity": 4}
        ]

# ==========================================
# MODÈLES MATHÉMATIQUES (XGBoost Simulé)
# ==========================================

def calculate_base_risk(events):
    """Calcul de base: Somme pondérée par la sévérité et la proximité temporelle"""
    score = 0
    for e in events:
        score += e['severity'] * 10
    return min(score, 100)

def simulate_france_legacy(profile):
    """France actuelle : Cloisonnement total (Silos)."""
    # La Justice ne voit que l'événement de 2018. Le Social ne voit que 2024.
    justice_view = [e for e in profile.institutional_events if e['type'] == 'justice_dismissal']
    social_view = [e for e in profile.institutional_events if e['type'] == 'social_signal']
    
    # Score calculé en 2025 (avant le drame de 2026)
    justice_score = calculate_base_risk(justice_view) # 10/100
    social_score = calculate_base_risk(social_view)   # 30/100
    
    return {
        "model": "France (Legacy/Cassiopée)",
        "score_2025": max(justice_score, social_score),
        "visibility": "Fragmentée (10-30%)",
        "action": "Aucune alerte globale. Aveuglement par silo."
    }

def simulate_uk_mash(profile):
    """Royaume-Uni (MASH) : Multi-Agency local, mais limité par la région."""
    # Le MASH de Lille (où P001 est en 2024) voit le Social local, peut-être la Police nationale,
    # mais perd les signaux faibles scolaires de Toulouse (2020) si non transférés.
    mash_view = [e for e in profile.institutional_events if e['region'] in ['Lille', 'Paris']]
    
    # Bonus de co-localisation des agences (Social + Police partagent)
    base_score = calculate_base_risk(mash_view)
    multi_agency_bonus = 15 if len(set(e['type'] for e in mash_view)) > 1 else 0
    
    final_score = min(base_score + multi_agency_bonus, 100) # 20 (Paris) + 10 (Paris) + 30 (Lille) = 60 + 15 = 75
    
    return {
        "model": "Royaume-Uni (MASH)",
        "score_2025": final_score,
        "visibility": "Régionale Multi-Agences (70%)",
        "action": "Intervention sociale locale déclenchée, mais pattern national raté."
    }

def simulate_china_psb(profile):
    """Chine (Public Security Bureau) : Fusion Totale (Institutionnel + Lifestyle)."""
    # Voient absolument tout, institutionnel + vie privée
    all_events = profile.institutional_events + profile.lifestyle_data
    
    base_score = calculate_base_risk(profile.institutional_events) # 20+10+20+10+30 = 90
    
    # Multiplicateur dystopique via Lifestyle Tracking (Computer Vision, Mobilité)
    lifestyle_multiplier = 1.0
    for l in profile.lifestyle_data:
        lifestyle_multiplier += 0.3 # +30% par flag comportemental
        
    final_score = min(base_score * lifestyle_multiplier, 100)
    
    return {
        "model": "Chine (Public Security Bureau)",
        "score_2025": final_score,
        "visibility": "Totale (100% Institution + 100% Privé)",
        "action": "Arrestation préventive/Internement avant même qu'un délit soit commis (Score artificiellement boosté par la mobilité)."
    }

def simulate_cgip(profile):
    """CGIP (Notre architecture) : Graphe National + Limitation Juridique."""
    # Voit tous les événements institutionnels nationaux
    all_inst_events = profile.institutional_events
    
    # NE VOIT PAS la donnée lifestyle (Kill-Switch RGPD)
    base_score = calculate_base_risk(all_inst_events) # 90
    
    # Graph Centrality (Convergence Multi-sources)
    institutions_involved = len(set(e['type'] for e in all_inst_events)) # Police, Justice, School, Admin, Social = 5
    graph_bonus = institutions_involved * 5 # +25
    
    raw_score = base_score + graph_bonus # 115
    
    # Rule Engine (Contraintes juridiques)
    # L'IA est cappée et ne peut pas dépasser 95 sans validation humaine
    final_score = min(raw_score, 95)
    
    return {
        "model": "France (CGIP)",
        "score_2025": final_score,
        "visibility": "National Institutionnel (100% Inst, 0% Privé)",
        "action": "Alerte CRITIQUE envoyée à un Magistrat. Vue 360° sans violer la vie privée citoyenne."
    }

if __name__ == "__main__":
    p001 = ProfileP001()
    
    results = [
        simulate_france_legacy(p001),
        simulate_uk_mash(p001),
        simulate_china_psb(p001),
        simulate_cgip(p001)
    ]
    
    print(json.dumps(results, indent=2, ensure_ascii=False))
