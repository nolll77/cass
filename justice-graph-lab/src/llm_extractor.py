import json
from openai import OpenAI

client = OpenAI()

SYSTEM_PROMPT = """
Tu es un système d'extraction d'information juridique et institutionnelle.
Tu dois transformer un texte en structure JSON STRICTE.
Règles :
- Ne jamais inventer d'information.
- Utiliser uniquement les informations présentes dans le texte.
- Si une information manque, mettre null.
- Toujours respecter le schéma.
- Extraire : événements, personnes, institutions, relations temporelles.
Sortie UNIQUEMENT en JSON valide.
"""

def build_prompt(text):
    return f"Texte à analyser :\n\n{text}\n\nExtrais :\n- événements\n- personnes\n- institutions\n- relations entre événements\nRetourne un JSON structuré."

def extract_with_llm(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_prompt(text)}
        ],
        temperature=0
    )
    content = response.choices[0].message.content
    try:
        return json.loads(content)
    except Exception as e:
        print("JSON invalide:", e)
        return None
