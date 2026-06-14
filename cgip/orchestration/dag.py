from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

# Ceci est un DAG d'orchestration simulant le pipeline de données industriel
with DAG("justice_knowledge_pipeline", start_date=datetime(2026, 6, 14), schedule_interval="@daily") as dag:
    ingest = DummyOperator(task_id="ingest_kafka")
    process = DummyOperator(task_id="spark_cleaning")
    build_graph = DummyOperator(task_id="neo4j_graph_build")
    train_gnn = DummyOperator(task_id="train_temporal_gnn")
    compute_scores = DummyOperator(task_id="compute_systemic_scores")

    ingest >> process >> build_graph >> train_gnn >> compute_scores
