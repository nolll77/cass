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

Lorsqu'on cherche à fusionner l'information policière, juridique et civile, on se heurte à des modèles culturels extrêmement différents. La CGIP doit se positionner par rapport à ces architectures internationales. Le tableau ci-dessous confronte la logique de la France (Silo) face au pragmatisme (UK) et à l'État social intégré (Scandinavie : Suède, Danemark, Norvège, Finlande).

| Axe d'analyse | 🇫🇷 France | 🇬🇧 Royaume-Uni | 🇸🇪🇩🇰🇳🇴🇫🇮 Scandinavie |
| :--- | :--- | :--- | :--- |
| **Philosophie (Le point clé)** | "Le droit structure les données" | "Le risque structure les décisions" | "Le social structure la prévention" |
| **Centralisation des données** | Faible (Silos institutionnels forts) | Moyenne (National Crime Database, MASH) | Très élevée (Identifiants nationaux structurés) |
| **Interopérabilité des institutions** | Faible | Bonne | Très bonne |
| **Vision "Individu Global"** | Faible (Logique dossier) | Moyenne | Élevée (Trajectoire sociale continue) |
| **IA Judiciaire / Risk Scoring** | Faible (Aide statistique) | Moyenne-Élevée (Risk of reoffending) | Modérée (Encadré mais fluide) |
| **Prévention Sociale** | Moyenne | Moyenne | Très élevée |
| **Surveillance Algorithmique** | Faible | Moyenne | Faible-Moyenne |

### Analyse du positionnement de la CGIP : Le "Modèle Hybride Idéal (France + Scandinavie)"

Le vrai changement paradigmatique de la CGIP n'est pas "l'IA" en tant que technologie (qui n'est qu'un outil de calcul), mais la bascule d'une gestion statique (France) vers une carte vivante des trajectoires (Scandinavie).

La CGIP assume de s'inspirer du "Care" scandinave, mais en le protégeant techniquement :
- **Ce que la CGIP refuse de la France :** L'aveuglement temporel et l'impossibilité de croiser les signaux faibles (Social/École/Police) à cause de l'enfermement dans la logique du "Dossier Séparé".
- **Ce que la CGIP prend du Royaume-Uni (🇬🇧) :** Le scoring pragmatique de la trajectoire pour alerter rapidement sur une récidive potentielle (Modèle de Hawkes).
- **L'Inspiration Ultime (🇸🇪 Scandinavie) :** L'approche longitudinale continue. Voir l'enfant vulnérable en amont du système policier grâce à l'interconnexion École-Justice.
- **La limite Européenne (RGPD) :** En Europe, l'IA ne peut pas (et ne doit pas) remplacer le juge. Le système ne prend aucune décision automatique, il génère des niveaux d'alerte (Rouge/Orange/Vert) qui atterrissent exclusivement sur le bureau d'un humain. Le profilage automatique décisionnel est structurellement bloqué (Kill-Switch).

---

## 5. Focus Analytique : La Macro-Gouvernance (France vs UK vs Pays Nordiques)

Conformément à l'analyse proactive, l'étude des modèles étatiques révèle que la technologie seule ne résout rien. C'est l'architecture institutionnelle qui conditionne l'algorithme.

### (1) Analyse Individuelle des Modèles
*   **🇫🇷 France (Le Modèle Cloisonné)** : Données en silos stricts (Police $\neq$ Justice $\neq$ Social). Aucune interopérabilité automatique. Forte dépendance au traitement manuel.
*   **🇬🇧 Royaume-Uni (Le Modèle Multi-Agences)** : Logique de *Risk Engine*. Le *Safeguarding Hub* connecte Police, Social et Santé pour évaluer le risque de récidive ou de mise en danger. Automatisation moyenne.
*   **🇳🇴🇸🇪🇩🇰 Nordiques (Le Modèle National Unifié)** : Identité unique (Personnummer). Le Data Hub national fusionne toutes les données du citoyen. Automatisation élevée, couverte par un fort "Trust in State".

### (2) Confrontation Directe (L'Illusion du Retard Technologique Français)
*   **Le Blocage Français n'est pas technique** : Ce n'est pas parce que les algorithmes français sont moins bons que nous ne détectons pas les signaux faibles. C'est parce que l'architecture légale interdit le croisement de données (absence d'Identité Unique).
*   **La solution technologique (Entity Resolution)** : Pour rattraper la performance scandinave sans enfreindre la Constitution française, la CGIP utilise l'**Entity Resolution**. L'algorithme reconstruit "l'ombre" d'une identité unique à la volée, en contournant le besoin d'un Registre National.

### (3) Le Fil Rouge : La Gouvernance prime sur l'Algorithme
Le fil rouge qui relie les succès de l'Angleterre et de la Scandinavie face aux échecs français tient en trois points non-techniques :
1. **La Gouvernance des données** : "Qui a le droit de voir quoi ?" (Au lieu d'avoir un fichier que tout le monde lit, il faut un système de rôles dynamiques - RBAC).
2. **L'Interopérabilité** : Les systèmes doivent parler la même langue (Kafka / JSON).
3. **La Culture Institutionnelle** : La France punit l'acte final (Répression) là où les Nordiques détectent la trajectoire (Prévention). L'IA de la CGIP est un outil préventif.

---

## 6. Focus Analytique : La "Zone Jaune" Élargie du Modèle UK

Conformément à la doctrine d'analyse proactive, il est crucial d'étudier pourquoi le système du Royaume-Uni se permet une latitude que l'UE interdit.

### (1) Analyse Individuelle (Le modèle OASys / MASH UK)
*   Le Royaume-Uni utilise de l'IA (comme l'outil OASys - Offender Assessment System) pour calculer très précisément le *Risk of Reoffending*.
*   Contrairement à la France, ces scores peuvent être utilisés directement par un juge pour justifier le refus d'une libération conditionnelle. L'algorithme se rapproche très dangereusement du jugement individuel (Zone Rouge).

### (2) Confrontation Directe face à la France (Limites du RGPD)
*   **Le principe Européen** : Dans l'UE (et en France), l'IA ne peut pas produire de décision ayant un effet légal *uniquement* par traitement algorithmique (Art 22 du RGPD).
*   La France accepte la *Zone Jaune* (Détection d'anomalies, priorisation de dossiers) mais s'arrête devant la sentence. La machine alerte, l'humain lit le dossier, l'humain juge. Au Royaume-Uni, l'algorithme "juge" presque.

### (3) Le Fil Rouge (L'Axe Anglo-Saxon du "Risk Management")
*   Entre les USA (COMPAS) et le UK (OASys), on retrouve la même obsession : Le **Risk Management**. Le droit anglo-saxon est utilitariste : il préfère anticiper un comportement dangereux par la probabilité mathématique pour protéger la société. Le droit français (latin) est moral : il juge un acte précis déjà commis, présumant l'innocence pour l'avenir.
*   **La Synthèse CGIP** : La CGIP absorbe le Risk Management britannique (pour la rapidité d'alerte), mais refuse son application à l'individu. La CGIP attribue le risque à la *situation environnementale* de l'enfant, jamais à son *âme* criminelle. C'est la seule voie de passage légale en Europe.

---

## 6. Focus Analytique : L'Architecture Palantir / Police Predictive US

Conformément à l'analyse proactive requise par la doctrine du projet, voici la confrontation de la CGIP face au leader mondial de l'intégration de données policières (Palantir Gotham / PredPol).

### (1) Analyse Individuelle du Modèle US
*   **Fonctionnement** : Palantir est une plateforme de "Forward-Chaining". Elle avale des pétaoctets de données non structurées (fichiers de police, appels télécoms, plaques d'immatriculation, réseaux sociaux) et cartographie l'univers entier sans filtre initial.
*   **Objectif** : Révéler le réseau criminel global par force brute algorithmique.

### (2) Confrontation Directe face à la France (L'Incompatibilité CNIL)
*   **Le principe de "Finalité"** : En France, la CNIL exige qu'une donnée collectée pour une raison A (ex: suivi scolaire) ne puisse pas être utilisée pour une raison B (enquête policière) sans cadre légal strict. Palantir brise ce concept en fusionnant tout.
*   **L'Effet Boîte Noire** : Palantir ne donne pas le code de son algorithme. Un magistrat français ne peut pas condamner quelqu'un sur la base d'un calcul propriétaire invérifiable. C'est pourquoi la CGIP exige de l'Open Source et de l'Explicabilité (SHAP).

### (3) Le Fil Rouge Géopolitique : L'Idéologie de la "Data Supremacy"
Si l'on relie les États-Unis (Palantir), le Royaume-Uni (qui a massivement acheté Palantir) et la Chine (qui a sa propre version d'État), on trouve un **fil rouge idéologique profond** : la croyance que "La quantité absolue de données crée la sécurité absolue". 
*   **Le problème** : Cette approche génère une **sur-connexion algorithmique (Apophénie)**. Le logiciel commence à voir des complots criminels là où il n'y a que des coïncidences statistiques, ce qui amène à la discrimination (biais racial de PredPol).
*   **La réponse de la CGIP** : La CGIP s'oppose à la *Data Supremacy* en implémentant une **Data Frugality**. C'est pour cela qu'elle sépare la "Base SQL" (Vérité Légale) de la "Base Graph" (Hypothèse), et impose le "Kill-Switch" (le Droit de bloquer le modèle). La CGIP ne veut pas "tout savoir", elle veut "repérer l'escalade temporelle".

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


# ÉTUDE COMPARATIVE (Règle Proactive) : Fusion Centers (USA) & MASH (UK)

Conformément à la directive d'analyse, l'évocation des systèmes US et UK a déclenché une recherche et une confrontation immédiate.

### 1. Analyse Individuelle
- **Fusion Centers (USA)** : Nés post-9/11, ces centres fusionnent les données de la police fédérale (FBI/DHS) et locale. Ils sont critiqués par l'ACLU pour leur collecte massive, leur dérive vers la surveillance des militants politiques, et leur manque de transparence (absence de "Privacy by Design" natif).
- **Multi-Agency Safeguarding Hubs (MASH) - (UK)** : Nés suite à des drames d'enfants abusés (Baby P), les MASH co-localisent physiquement police, justice, école et services sociaux. Le mythe "le RGPD interdit le partage" y est combattu : le Droit anglais permet le partage d'informations si l'"intérêt vital" de l'enfant est en jeu, sur la base d'un "besoin d'en connaître" (Need-to-Know).

### 2. Confrontation avec le Modèle Français (La CGIP)
- La France souffre d'un cloisonnement extrême (Secret de l'instruction vs Secret médical vs Secret administratif). 
- Le MASH anglais prouve qu'il est légalement possible de partager la donnée sensible en Europe si la loi encadre "l'intérêt vital". 
- Cependant, le Fusion Center américain est le repoussoir absolu : l'État français (CNIL) n'acceptera jamais un tel aspirateur à données sans contrôle.
- **La réponse CGIP** : La plateforme est le compromis parfait. Elle permet l'efficacité d'un MASH (vision 360°) mais remplace la "co-localisation physique humaine" par un **Data Lake crypté par Hachage**. Elle offre la puissance d'un Fusion Center tout en imposant les limites éthiques européennes via un *Kill-Switch* algorithmique.

### 3. Le Fil Rouge
Les USA (2001) et le UK (2007) ont brisé leurs silos d'État **uniquement après un traumatisme national majeur**. Le fil rouge n'est pas la technologie (qui existe déjà), mais le courage politique de décloisonner la donnée. La CGIP anticipe le "traumatisme Lyhanna" pour provoquer cette mutation structurelle en France par la technologie.

# ÉTUDE COMPARATIVE 2 : La Fracture des Systèmes (USA, UK, NL)

### 1. Analyse Individuelle
- **UK (MASH + ViSOR)** : Modèle pragmatique. L'information remonte des écoles/hôpitaux vers un pôle multi-agences. Forte prévention, mais les systèmes restent locaux (pas de graphe national).
- **Pays-Bas (Municipality Data Hubs)** : Modèle social. La municipalité centralise l'action de prévention via des dashboards intégrés ("Data-driven youth care"). C'est une approche locale, très humaine, mais confrontée à des problèmes de RGPD (SyRI).
- **USA (Fusion Centers + Predictive Policing)** : Modèle Big Data. Forte puissance de calcul (Data Lakes), mais fragmentation extrême (Fédéral vs Local) et opacité des modèles algorithmiques (boîtes noires privées) générant de violents biais discriminatoires.

### 2. Confrontation avec le Modèle Français (La CGIP)
Le modèle français ("Preuve → Procédure → Décision") est très protecteur des libertés (transparence juridique élevée, risque de surveillance faible) mais il est aveugle aux signaux faibles. La CGIP est l'architecture hybride parfaite :
- Elle prend **le Workflow multi-agences du UK**.
- Elle prend **l'intégration locale des Pays-Bas**.
- Elle prend **le volume analytique des USA**.
- Elle encastre le tout dans le **modèle juridique Français** (Contrôle total par un juge, Kill-Switch algorithmique).

### 3. Le Fil Rouge
Le "Fil Rouge" global de l'échec occidental est double :
1. **La granularité de la donnée** : Partout dans le monde, la base de données appartient à "l'Institution" (La base de la Police, la base de la Justice). Nulle part la base de données n'appartient à "L'Individu" (Vision Graphe 360).
2. **Le but du système** : Les systèmes informatiques occidentaux ont été codés pour "enquêter après le crime", pas pour l'anticiper.
La CGIP justifie son modèle "Graph First" car c'est la seule topologie mathématique capable de casser le dogme de l'institution au profit de la vision globale de la victime ou du suspect.

# ÉTUDE COMPARATIVE 3 : L'Axe Chinois et le Tableau Périodique Mondial

Suite à l'injection du modèle chinois, le benchmark est désormais complet.

### 1. Analyse Individuelle (Le cas Chinois)
- **Chine (Public Security Bureau)** : Architecture ultra-centralisée. C'est la fusion absolue du Graphe et de la Data. Contrairement au monde occidental, la Chine n'a pas de séparation institutionnelle entre la Police, la Justice, le Social et le Privé. L'IA (Computer Vision, Scoring comportemental) y est massive, et la transparence nulle.

### 2. Confrontation avec le Modèle Français (La CGIP)
Le tableau synthétique est implacable :
- **Centralisation** : Chine (5/5) / UK (3/5) / USA (2/5) / France (1/5).
- **Transparence** : France (5/5) / UK (4/5) / USA (2/5) / Chine (1/5).

La Chine a une *Graph DB Populationnelle* implicite. La CGIP refuse ce modèle. Le Graphe de la CGIP ne contient pas la "Population", il ne contient que les "Dossiers" (les nœuds ne naissent que lorsqu'un événement institutionnel est créé).

### 3. Le Fil Rouge (L'Échec Structurel)
Le fil rouge ultime se dégage : **Ce n'est jamais un problème d'algorithme (ML)**. La réussite de la Chine n'est pas due à un meilleur XGBoost, mais à une structure étatique qui écrase les silos institutionnels par la force. Aux USA et en Europe, la friction juridique bloque cette fusion.
La CGIP est la première architecture à proposer la résolution de ce paradoxe : casser les silos (comme la Chine) tout en garantissant la transparence légale (comme l'Europe) grâce à la *Privacy by Design* (Hachage) et au *Kill-Switch Algorithmique*.