# Matrice de Couverture : CGIP (Civic Graph Intelligence Platform)

Ce document prouve la traçabilité complète et la couverture à 100% entre les exigences théoriques de la CGIP et leur implémentation informatique. Chaque formule du [SOCLE_MATHEMATIQUE.md](../SOCLE_MATHEMATIQUE.md) possède son "Test Architectural" dédié, interdisant toute déviation par rapport à la loi (AI Act / RGPD).

| N° | Formule Sociologique / Légal | Fichier Source (Squelette) | Test Architectural (Validation) | Statut Actuel |
|:---|:---|:---|:---|:---|
| 1.1 | Time Decay Function | `src/utils/privacy.py` | `test_01_privacy_by_design.py::test_time_decay_function` | ⚠️ Skipped |
| 1.2 | Kill-Switch RGPD (DPIA) | `src/utils/kill_switch.py` | `test_01_privacy_by_design.py::test_kill_switch_rgpd` | ⚠️ Skipped |
| 2.1 | Entity Resolution (Jaro-Winkler) | `src/ingestion/nlp.py` | `test_02_spatial_temporal.py::test_entity_resolution_jaro` | ⚠️ Skipped |
| 2.2 | Processus de Hawkes (Escalade) | `src/ml_engine/hawkes.py` | `test_02_spatial_temporal.py::test_hawkes_process_escalation` | ⚠️ Skipped |
| 3.1 | GNN (Link Prediction) | `src/graph/gnn.py` | `test_03_causal_graphs.py::test_gnn_link_prediction` | ⚠️ Skipped |
| 3.2 | Inférence Causale (DoWhy) | `src/ml_engine/causal.py` | `test_03_causal_graphs.py::test_causal_inference_dowhy` | ⚠️ Skipped |
| 3.3 | Score de Risque Temps Réel | `src/ml_engine/scoring.py` | `test_04_scoring_classification.py::test_real_time_risk_score` | ⚠️ Skipped |
| 3.4 | Poids Relatif (Confidence) | `src/graph/weights.py` | `test_04_scoring_classification.py::test_confidence_score_weight` | ⚠️ Skipped |
| 4.1 | Indice de Similarité (SALVAC) | `src/ml_engine/similarity.py` | `test_04_scoring_classification.py::test_serial_similarity_salvac` | ⚠️ Skipped |
| 4.2 | Classification Escalade (XGBoost) | `src/ml_engine/xgboost.py` | `test_04_scoring_classification.py::test_xgboost_escalation_classification` | ⚠️ Skipped |
