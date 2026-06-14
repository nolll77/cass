# Le Module d'Audit (Bias Monitor & Kill Switch)

En résumé, le script `bias_monitor.py` calcule en permanence le ratio d'Impact Disparate (variance > 20%) sur la zone géographique (`geo_hash`) et la tranche d'âge (`age_band`). 

Lors des tests, une sur-représentation artificielle d'un code postal a été simulée dans les résultats de l'IA, et le script a immédiatement bloqué le modèle (coupure de l'accès aux enquêteurs) et généré son rapport de conformité JSON. C'est une sécurité absolue.

## Fonctionnement Technique
1. **Calcul du Disparate Impact** : Compare la distribution réelle des prédictions "Haut Risque" par rapport à une distribution équiprobable théorique.
2. **Règle des 80%** : Si une catégorie (âge ou territoire) subit une variance de plus de 20%, le seuil d'alerte est franchi.
3. **Le Kill Switch (Hard Limit)** : La politique de tolérance au biais est de zéro. Le modèle est physiquement déconnecté et renvoie l'erreur `AUDIT_REQUIRED`.
4. **Immuabilité** : Chaque audit génère un rapport JSON horodaté, prêt à être fourni aux autorités de contrôle.
