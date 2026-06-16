# Spécification du Dashboard Contrefactuel (XAI avancée)

L'Explainable AI (XAI) classique se contente de dire "Pourquoi le score est haut".
Le **Dashboard Contrefactuel** permet au Juge de dialoguer avec le modèle IA en se posant la question : *"Que se serait-il passé si... ?"*

## Composant `<ShapWaterfall />`
Ce composant affiche l'impact des variables sur le score de risque (ex: 85%).
- Base Rate: 20%
- Variable A (Antécédents violents) : +40%
- Variable B (Signalement école récent) : +35%
- Variable C (Aucune infraction routière) : -10%
- **Score final = 85%**

## Interaction Contrefactuelle
Dans l'UI, chaque barre du Waterfall Chart ou chaque nœud du Graphe possède un switch `[Toggle Mute]`.

### Cas d'usage (Le Magistrat enquête virtuellement) :
1. Le Magistrat voit que le "Signalement école" pèse lourd (+35%).
2. Il a un doute sur la fiabilité de ce signalement.
3. Il clique sur `[Mute Node]` sur le signalement de l'école.
4. Le système recalcule le score en direct ("What-If analysis").
5. Le score chute de 85% à 50%.
6. **Déduction du Magistrat** : "Toute cette alerte repose presque uniquement sur le rapport de l'école. Si je l'enlève, il n'y a plus d'urgence pénale. Je rejette l'alerte pour protéger cet individu d'une judiciarisation abusive."

## Moteur sous-jacent
Le frontend envoie une requête API de type `POST /v1/xai/counterfactual` avec le payload :
```json
{
  "target_node_id": "#A8X9",
  "exclude_edges": ["edge_55"]
}
```
Le backend (GraphSAGE) ré-exécute une passe d'inférence (Inference Pass) ultra-rapide sans cette arête et retourne le nouveau score.

Ce niveau d'interactivité garantit que l'Humain (Le Juge) reste **actif** dans l'analyse et ne subit pas passivement le score de la machine. C'est l'essence même du respect de l'AI Act.
