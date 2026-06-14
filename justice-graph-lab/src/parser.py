import re
import pandas as pd
import spacy
import dateparser
from datetime import datetime

# Nécessite : python -m spacy download fr_core_news_sm
nlp = spacy.load("fr_core_news_sm")

# =========================
# 1. EXTRACTION DE BASE
# =========================
def extract_sentences(text):
    doc = nlp(text)
    return [sent.text.strip() for sent in doc.sents]

# =========================
# 2. DETECTION D'ÉVÉNEMENTS
# =========================
EVENT_TYPES = [
    "signalement", "alerte", "plainte", "enquête", "condamnation", "incident"
]

def detect_event_type(sentence):
    sentence_lower = sentence.lower()
    for et in EVENT_TYPES:
        if et in sentence_lower:
            return et
    return "unknown"

# =========================
# 3. EXTRACTION DATE
# =========================
def extract_date(sentence):
    match = dateparser.search.search_dates(sentence)
    if match:
        return match[0][1].date().isoformat()
    return None

# =========================
# 4. INSTITUTIONS (simple heuristique)
# =========================
INSTITUTIONS = {
    "école": "education", "lycée": "education", 
    "police": "law_enforcement", "gendarmerie": "law_enforcement",
    "justice": "judicial", "tribunal": "judicial"
}

def detect_institution(sentence):
    s = sentence.lower()
    for k, v in INSTITUTIONS.items():
        if k in s:
            return v
    return "unknown"

# =========================
# 5. SCORE DE CONFIANCE SIMPLE
# =========================
def confidence_score(sentence):
    score = 0.5
    if any(et in sentence.lower() for et in EVENT_TYPES):
        score += 0.2
    if extract_date(sentence):
        score += 0.2
    if detect_institution(sentence) != "unknown":
        score += 0.1
    return round(min(score, 1.0), 2)

# =========================
# 6. CONSTRUCTION EVENT
# =========================
def build_event(event_id, sentence, source):
    return {
        "event_id": event_id,
        "date": extract_date(sentence),
        "event_type": detect_event_type(sentence),
        "institution": detect_institution(sentence),
        "description": sentence,
        "source": source,
        "confidence": confidence_score(sentence)
    }

# =========================
# 7. PIPELINE COMPLET
# =========================
def process_article(text, source_name="unknown"):
    sentences = extract_sentences(text)
    events = []
    event_id = 0
    for s in sentences:
        event = build_event(f"E{event_id}", s, source_name)
        events.append(event)
        event_id += 1
    return pd.DataFrame(events)

# =========================
# 8. EXEMPLE D'UTILISATION
# =========================
if __name__ == "__main__":
    text = """
    En 2020, un signalement a été effectué par un établissement scolaire.
    La police a ouvert une enquête en 2022.
    Une plainte a été déposée en 2023 auprès du tribunal.
    """
    df = process_article(text, source_name="article_1")
    print(df)
