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

## 3. Les Systèmes Étrangers de Fusion de Données (Le Contre-Modèle et l'Inspiration)

Lorsqu'on cherche à fusionner l'information policière, juridique et civile, on se heurte à des modèles culturels extrêmement différents. La CGIP doit se positionner par rapport à ces architectures internationales.

### A. Le Modèle Américain : Privatisé et Algorithmique (Boîte Noire)
- **Les Outils :** Palantir (Gotham), COMPAS (Correctional Offender Management Profiling for Alternative Sanctions), PredPol.
- **La Logique :** Fusion de données massives (Police locale, FBI, Douanes, réseaux sociaux) opérée par des géants du privé. La "Predictive Policing" détermine où envoyer les patrouilles, et le "Risk Assessment" calcule informatiquement le risque de récidive pour la justice.
- **Le Problème (Pourquoi la CGIP s'y oppose) :** Le système est une "Boîte Noire" couverte par le secret industriel. L'algorithme COMPAS, par exemple, s'est révélé massivement biaisé (racisme algorithmique). La CGIP exige au contraire un **Socle Mathématique Open Source** et une XAI (Explainable AI).

### B. Le Modèle Chinois : Le Panoptique (Surveillance de Masse)
- **Les Outils :** IJOP (Integrated Joint Operations Platform), Social Credit System.
- **La Logique :** L'État-plateforme fusionne absolument tout. Données bancaires, caméras de reconnaissance faciale, dossiers médicaux, casiers judiciaires, historique internet. L'analyse comportementale (GNN, Machine Learning) alerte la police en temps réel avant la commission d'un crime (notamment utilisé au Xinjiang).
- **Le Problème (Pourquoi la CGIP s'y oppose) :** C'est l'antithèse absolue de notre modèle éthique. Il n'y a ni séparation des pouvoirs, ni anonymisation, ni RGPD. C'est l'exemple parfait d'un système où *l'Identity Resolution Layer* est utilisé pour le contrôle total plutôt que pour la protection ciblée.

### C. Le Modèle Anglo-Scandinave : L'Approche "Care" (Inspiration)
- **Les Outils :** MASH (Multi-Agency Safeguarding Hubs) au Royaume-Uni, et l'intégration par *Personnummer* en Suède.
- **La Logique :** En Angleterre, face à des tragédies similaires (Affaire Baby P), l'État a créé des cellules MASH où la police, les travailleurs sociaux, l'hôpital et l'école partagent physiquement et informatiquement leurs bases de données sur les enfants vulnérables. En Scandinavie, l'identifiant unique national permet de tracer le parcours d'un citoyen sans les lourdeurs de dédoublonnage français.
- **La Limite (Où la CGIP prend le relais) :** Ces systèmes reposent encore massivement sur des "cellules de crise humaines". La CGIP est la version **technologique automatisée et temps réel** d'un MASH, capable de traiter à l'échelle nationale ce qu'un MASH fait à l'échelle locale.

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
