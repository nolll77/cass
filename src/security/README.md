# Module de Sécurité CNIL / RGPD 

**L'armure juridique de la CGIP est en place.**
Ce module garantit que l'éthique et le droit ne sont pas de simples déclarations d'intention, mais des verrous mathématiques codés en dur dans l'architecture.

L'intégralité du module de sécurité repose sur trois piliers fondamentaux :

## 1. Le Sas Cryptographique (`rgpd_anonymizer.py`)
Désormais, toute identité entrante est broyée mathématiquement via un hachage cryptographique (`HMAC-SHA256`). 
L'Intelligence Artificielle (XGBoost / GNN) et le Graphe (Neo4j) ne traiteront plus jamais un nom en clair comme "Jean Dupont". Le système ne manipulera que des hachages irréversibles (ex: `P-821e50...`). C'est l'implémentation absolue du principe de *Privacy by Design*.

## 2. Le Gardien du Temps (`ttl_manager.py`)
Le "Droit à l'Oubli" est automatisé. Ce script agit comme un Cron Job qui purge physiquement les données obsolètes de la base.
Si un délit mineur dépasse son délai légal de conservation (ex: 3 ans), l'événement est supprimé, forçant ainsi le score de risque calculé par l'IA à s'effondrer instantanément. C'est le garde-fou qui empêche la CGIP de conserver une mémoire illimitée, à l'inverse du système Cassiopée.

## 3. Le RBAC (`access_control.py`)
C'est la séparation des pouvoirs codée en dur. 
- **Le Data Scientist** a accès aux algorithmes et aux données pour entraîner les modèles, mais il est "aveuglé" sur l'identité civile (vue hachée uniquement).
- **Le Magistrat** est le seul humain autorisé à valider les déductions de l'IA. Il détient la clé d'habilitation (`can_trigger_arrest = True` et `can_view_pii = True`) qui lui permet de désanonymiser le profil lorsqu'une **Alerte Critique** est déclenchée.

---
*L'éthique et le droit sont validés. Nous avons posé les rails, les bases SQL, les requêtes Neo4j, et l'armure RGPD.*
