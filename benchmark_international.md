# Benchmark International et Analyse de l'Écosystème (Systèmes Étatiques vs CGIP)

Ce document recense, compare et analyse les différents systèmes étatiques et outils policiers évoqués lors de la conception de la **CGIP (Civic Graph Intelligence Platform)**. L'objectif est de comprendre pourquoi les approches actuelles, même à l'étranger, ne répondent qu'imparfaitement au problème de la "fragmentation des signaux" mis en lumière par l'affaire Lyhanna.

## 1. L'Approche Sérielle (Canada, Belgique vs France)

### Le pionnier : ViCLAS (Canada / Belgique / International)
- **Quoi :** *Violent Crime Linkage Analysis System*. Développé en 1992 par la Gendarmerie Royale du Canada et adopté par la Belgique en 2003.
- **Fonctionnement :** Basé sur un questionnaire manuel extrêmement exhaustif (156 variables : victime, âge, lieu, heure, contrainte, discours, moyens de transport, etc.).
- **Objectif :** Comparer les affaires entre elles pour relier des crimes sexuels ou violents non élucidés, en s'appuyant sur l'idiosyncrasie (la signature comportementale) de l'auteur.
- **Limite :** C'est du "Machine Learning avant l'heure" mais qui repose sur un encodage humain fastidieux, souvent biaisé par la subjectivité de l'enquêteur ou réduit par la quantité massive d'items.

### La version française : SALVAC
- **Quoi :** *Système d'Analyse des Liens de la Violence Associée aux Crimes*. Importé du Canada (dérivé de ViCLAS) et géré par l'OCRVP.
- **Base de données :** Environ 13 000 affaires enregistrées. Géré par un groupe très restreint (7 analystes).
- **Le problème structurel :** SALVAC ne voit *que* les affaires pénales lourdes enregistrées (viols, meurtres). Il compare `AFFAIRE A <-> AFFAIRE B` pour trouver une *Similarité Criminelle*. Il est aveugle aux signaux faibles, aux incidents scolaires ou aux alertes des services sociaux. Il ne détecte pas une "trajectoire" de risque de manière globale, il détecte un tueur en série déjà en action.

## 2. Le Labyrinthe Français (L'Approche Administrative)

La France souffre d'une sur-fragmentation de ses silos institutionnels. Le problème n'est pas le manque de données, mais l'incapacité à les croiser en temps réel :
- **Cassiopée (Justice) :** Système de gestion administrative des procédures. Il gère des *dossiers*, pas des *biographies criminelles*.
- **TAJ (Police/Gendarmerie) :** Traitement des Antécédents Judiciaires. Essentiellement une base de consultation locale post-plainte.
- **FIJAISV (Condamnations) :** Fichier des auteurs d'infractions sexuelles. Il exige une condamnation ou une mise en examen grave. Un simple signalement classé sans suite n'y figure pas.

**Le Paradoxe :** Aucun de ces systèmes ne fait de la fusion longitudinale multi-institutions. Ils répondent tous à un morceau du problème, mais aucun ne rassemble le puzzle. Face à une chronologie éparse (Signalement en 2017 -> École en 2020 -> Plainte en 2022), le système reste muet.

## 3. L'Émergence de la Civil Tech (La Couche Victimes)

Face à la lenteur des institutions, de nouveaux outils civils émergent (approuvés par le Gouvernement) pour recenser la parole de la victime à la source :
- **App-Elles / UMAY :** Alertes géolocalisées et enregistrements audio en direct.
- **Ti3rs :** Messagerie sécurisée pour parents séparés (historisation des preuves, filtre anti-injures).
- **Mémo de vie :** Coffre-fort numérique pour les victimes (journal, certificats, photos, captures d'écran).

**Le point de rupture :** Ces applications recueillent la donnée la plus brute et la plus précoce. Cependant, elles sont déconnectées de Cassiopée ou SALVAC. 

---

## 4. Comparaison Matricielle des Modèles Étatiques (L'Approche Data)

Lorsqu'on cherche à fusionner l'information policière, juridique et civile, on se heurte à des modèles culturels extrêmement différents. La CGIP doit se positionner par rapport à ces architectures internationales. Le tableau ci-dessous confronte la logique de la France (Silo) face au pragmatisme (UK), au marché (USA) et à l'autoritarisme (Chine).

| Axe d'analyse | 🇫🇷 France | 🇬🇧 Royaume-Uni | 🇺🇸 États-Unis | 🇨🇳 Chine |
| :--- | :--- | :--- | :--- | :--- |
| **Logique Principale** | "On collecte des dossiers isolés" | Compromis pragmatique ("Risk-based policing") | Innovation + Chaos structurel | "On reconstruit un graphe continu de la population" |
| **Architecture (Centralisation)** | Faible (Silos institutionnels forts) | Moyenne (National Crime Database, MASH) | Faible (Fragmentation par État/Comté) | Très élevée (Intégration massive Police/Social/Web) |
| **Interopérabilité des données** | Faible | Bonne | Variable (dépend des juridictions) | Totale |
| **IA Judiciaire / Risk Scoring** | Limitée (Aide statistique) | Modérée (Risk of reoffending, violences dom.) | Forte (COMPAS, libération conditionnelle) | Très forte |
| **Police Prédictive (Hot spots)**| Non | Partielle | Très développée (Palantir, PredPol) | Systématique |
| **Protection des Droits (CNIL)** | Très forte | Forte | Variable | Faible |
| **Vision globale de l'individu** | Faible | Moyenne | Faible-moyenne | Très élevée |

### Analyse du positionnement de la CGIP : Le "Modèle Hybride Idéal"

La CGIP assume de s'inspirer techniquement de l'intégration anglo-saxonne (UK/USA), mais en la soumettant aux garde-fous juridiques français :

- **Ce que la CGIP refuse de la France :** L'aveuglement temporel et l'impossibilité de croiser les signaux faibles (Social/École/Police) à cause de l'enfermement dans la logique du "Dossier".
- **Ce que la CGIP prend du Royaume-Uni (🇬🇧) :** L'idée de décloisonnement physique et informatique (Modèle MASH) pour protéger les personnes vulnérables en croisant les bases.
- **Ce que la CGIP prend des USA (🇺🇸) :** L'architecture analytique de pointe (Data Lake, Graphes, Machine Learning) pour détecter des "patterns" invisibles à l'œil nu.
- **Ce que la CGIP refuse des USA (🇺🇸) :** La "Boîte Noire" privatisée (type Palantir) et les algorithmes prédictifs biaisés qui remplacent le juge. La CGIP impose l'Open Source, le contrôle étatique, et l'Explainable AI (SHAP).
- **L'Antithèse absolue (🇨🇳) :** Le graphe social chinois qui fusionne les données dans un but de contrôle punitif. La CGIP implémente un *Moteur DPIA* (Couche E) et un *Kill-Switch* pour interdire techniquement la surveillance de masse.

## Conclusion : Le Paradigme d'Intégration (CGIP)

Face à ces modèles (Silos Administratifs + Analyse Sérielle Manuelle + Apps Civiles isolées), la CGIP se positionne non pas comme un énième fichier, mais comme une architecture en 5 couches :
1. **Data Ingestion Layer** : Capte Cassiopée et la Civil Tech.
2. **Identity Resolution Layer** : Casse la logique "par dossier" pour fusionner "par individu".
3. **Justice Knowledge Graph** : Mappe le tout.
4. **ML Risk Engine & Investigation AI** : Remplace SALVAC de manière automatisée.
5. **Human Decision Layer** : Redonne le contrôle au magistrat avec une Explainable AI (XAI).

| Caractéristique | Cassiopée / TAJ | SALVAC / ViCLAS | CGIP (La Solution) |
| :--- | :--- | :--- | :--- |
| **Objectif** | Gestion procédurale | Identification de séries criminelles | **Prévention du risque par trajectoire** |
| **Périmètre** | Faits qualifiés judiciairement | Crimes sexuels/violents graves | **Multi-sources (Faible + Fort, Judiciaire + Scolaire)** |
| **Méthode** | Requête SQL classique | Humaine (156 items manuels) | **Graphes Criminels & Processus de Hawkes** |
| **Connectivité** | Silos fermés | Silos fermés | **Data Mesh (Extraction des métadonnées)** |
