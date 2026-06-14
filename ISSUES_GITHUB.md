# ARCHIVE DÉTAILLÉE DES ISSUES GITHUB (CGIP)

Ce fichier contient la liste exhaustive des issues à générer sur GitHub pour le développement de la Civic Graph Intelligence Platform (CGIP).
L'objectif est d'organiser le projet open-source / institutionnel en séparant clairement le code technique (ouvert aux contributions Data Science) et la gouvernance légale (réservée aux concepteurs / magistrats).

## MILESTONE : Setup, DevOps & Infrastructure
### Issue — [DevOps] #001 — Structure du dépôt & Pipeline CI/CD ✅ [FERMÉE]
**Labels:** setup, devops, difficulty: easy
- **Statut :** L'arborescence (`src/`, `data/`, `docs/`, `tests/`) et le fichier `requirements.txt` ont été créés et documentés dans le README.

### Issue — [Infra] #002 — Environnement Neo4j Local (Docker Compose)
**Labels:** setup, database, difficulty: medium
- **Contexte Analytique :** La plateforme nécessite un moteur de graphe pour fonctionner.
- **Périmètre Technique (Ouvert aux contributions) :** Création du `docker-compose.yml` instanciant Neo4j (avec plugin APOC) et Kafka pour l'ingestion asynchrone.
- **Périmètre Gouvernance (Réservé à l'Auteur) :** Pas de rédaction requise.

### Issue — [Infra] #002b — Setup Data Lake (AWS S3 / MinIO local)
**Labels:** setup, data-engineering, difficulty: medium
- **Contexte Analytique :** Déployer la "Mémoire Brute" de la justice avant tout traitement NLP ou Graph.
- **Périmètre Technique (Ouvert aux contributions) :** Configuration d'un bucket object storage (ex: MinIO pour le local) pour stocker les documents PDF, PV et historiques non structurés.
- **Périmètre Gouvernance (Réservé à l'Auteur) :** Verrouillage IAM strict : ce Data Lake contient la donnée non anonymisée.

## MILESTONE : Couche A - Socle Ontologique (Neo4j)
### Issue — [Data] #003 — Implémentation du Schéma GraphQL / Cypher
**Labels:** ontology, database, difficulty: medium
- **Contexte Analytique :** Définir la structure des nœuds (`Person`, `Event`, `ContextNode`) et des relations (`VISE_PAR`, `HAPPENED_IN`).
- **Périmètre Technique (Ouvert aux contributions) :** Scripts Python/Cypher pour contraindre la base de données (Indexes, Unique Constraints).
- **Périmètre Gouvernance (Réservé à l'Auteur) :** Validation finale des champs autorisés pour garantir qu'aucune donnée ethno-raciale ou interdite ne peut être stockée dans le schéma.

### Issue — [Data] #004 — Ingestion Sécurisée et Hachage (Privacy)
**Labels:** security, pipeline, difficulty: hard
- **Contexte Analytique :** Les identifiants réels ne doivent pas transiter en clair dans le système de machine learning.
- **Périmètre Technique (Ouvert aux contributions) :** Développement d'un pipeline d'ingestion qui hache l'identité (SHA-256 avec sel) avant l'insertion en base.
- **Périmètre Gouvernance (Réservé à l'Auteur) :** Conservation locale des clés de salage hors du dépôt GitHub.

### Issue — [Data] #004b — Connecteurs Silos (Cassiopée, TAJ, FIJAISV, SALVAC)
**Labels:** integration, data-engineering, difficulty: hard
- **Contexte Analytique :** La plateforme doit se sur-coupler au labyrinthe des "Systèmes de Gestion" existants pour fusionner leurs signaux.
- **Périmètre Technique (Ouvert aux contributions) :** Développement d'ETL ou connecteurs API sécurisés pour extraire les métadonnées de Cassiopée (Justice), du TAJ (Police), du FIJAISV, et potentiellement s'interfacer avec SALVAC, afin de les transformer en Graphe.
- **Périmètre Gouvernance (Réservé à l'Auteur) :** Validation CNIL stricte. La CGIP ne duplique pas les bases massives, elle ne stocke que les pointeurs hachés nécessaires à la détection des trajectoires (Data Mesh).

### Issue — [Data] #004c — Connecteurs Civil Tech (Mémo de Vie, App-Elles)
**Labels:** integration, data-engineering, open-source, difficulty: hard
- **Contexte Analytique :** Capter les signaux faibles à la source (bottom-up), avant même leur judiciarisation.
- **Périmètre Technique (Ouvert aux contributions) :** Développement d'API REST pour permettre aux applications civiles d'envoyer (avec le consentement cryptographique de l'utilisateur) des preuves structurées vers le Graphe CGIP.
- **Périmètre Gouvernance (Réservé à l'Auteur) :** Définir le standard de consentement RGPD (Opt-in) pour qu'une victime accepte que son journal "Mémo de Vie" soit scanné par la CGIP à la recherche de signaux de risque.

## MILESTONE : Couches E & F - Gouvernance & Privacy by Design
### Issue — [Gov] #005 — Moteur de Time Decay (Droit à l'oubli algorithmique)
**Labels:** governance, math, difficulty: medium
- **Contexte Analytique :** Implémenter mathématiquement la prescription légale. Le lien entre un acteur et un événement doit s'estomper avec le temps.
- **Périmètre Technique (Ouvert aux contributions) :** Code de la décroissance exponentielle `C(t) = C0 * e^(-lambda * t)` applicable sur les relations `VISE_PAR`.
- **Périmètre Gouvernance (Réservé à l'Auteur) :** Paramétrage strict de la demi-vie (`lambda`) en fonction de la loi (ex: prescription de 10 ans pour les délits majeurs).

### Issue — [Gov] #006 — Moteur DPIA et Kill-Switch
**Labels:** governance, security, difficulty: hard
- **Contexte Analytique :** Le système doit s'auto-bloquer s'il risque de générer un profilage interdit.
- **Périmètre Technique (Ouvert aux contributions) :** Écriture du `kill_switch.py` qui intercepte les requêtes Python et lève une exception `DPIABlockError` si le score de risque légal dépasse un seuil.
- **Périmètre Gouvernance (Réservé à l'Auteur) :** Définition de la matrice de risque (Qu'est-ce qui constitue un "High Risk" ?).

## MILESTONE : Couches B & D - Inférence IA & Causalité
### Issue — [ML] #007 — Identity Resolution Layer (Dédoublonnage Bayesien)
**Labels:** ai, nlp, difficulty: hard
- **Contexte Analytique :** C'est le cœur de la bascule "Dossier" vers "Individu". Savoir que "Jérôme B." (dossier Police) et "J.B." (signalement école) sont la même entité.
- **Périmètre Technique (Ouvert aux contributions) :** Implémentation d'algorithmes de Probabilistic Matching (ex: Jaro-Winkler, Bayesian Record Linkage, Embeddings LLM) pour fusionner les identités hachées.
- **Périmètre Gouvernance (Réservé à l'Auteur) :** Définition du seuil d'acceptation (ex: 95% de certitude requise pour fusionner deux profils) pour éviter l'erreur sur la personne.

### Issue — [Data] #007b — Création du Feature Store (ML-Ready)
**Labels:** data-engineering, ml, difficulty: medium
- **Contexte Analytique :** Préparer la matrice structurée pour les modèles IA.
- **Périmètre Technique (Ouvert aux contributions) :** Script PySpark ou Pandas (`build_features.py`) qui extrait de Neo4j les features temporelles, comportementales et de graphe (centralité) pour générer le dataset d'entraînement.
- **Périmètre Gouvernance (Réservé à l'Auteur) :** Validation des colonnes (interdiction des données raciales ou syndicales).

### Issue — [ML] #008 — Modélisation du Graphe Causal (DoWhy)
**Labels:** ai, math, difficulty: hard
- **Contexte Analytique :** Éviter les corrélations absurdes. S'assurer que A implique B chronologiquement et contextuellement.
- **Périmètre Technique (Ouvert aux contributions) :** Intégration de la librairie `DoWhy` pour formaliser l'analyse des antécédents (DAG : Directed Acyclic Graph).
- **Périmètre Gouvernance (Réservé à l'Auteur) :** Note éthique stipulant que ce calcul ne vaut pas preuve légale, mais uniquement outil d'orientation pour l'enquêteur.

## MILESTONE : Couche G - Modèles de Risque & Alerting
### Issue — [ML] #009 — Détection de l'escalade (Processus de Hawkes)
**Labels:** ai, math, difficulty: hard
- **Contexte Analytique :** Modéliser la fréquence et l'accélération d'événements liés à un profil (ex: 1 événement en 2017, puis 2 en 2020, = accélération).
- **Périmètre Technique (Ouvert aux contributions) :** Implémentation du processus de Hawkes.
- **Périmètre Gouvernance (Réservé à l'Auteur) :** Validation fonctionnelle.

### Issue — [ML] #010 — Moteur d'Agrégation (Cumulative Vulnerability Score)
**Labels:** ai, scoring, difficulty: medium
- **Contexte Analytique :** Calculer un score de risque cumulatif basé sur des "Trigger Events" (Sentinelles) plutôt qu'une boîte noire incompréhensible (Deep Learning).
- **Périmètre Technique (Ouvert aux contributions) :** Implémentation d'une fonction d'accumulation (ex: Signalement +1, Plainte +3, Répétition +2) et définition des seuils de basculement (0-2: OK, 3-4: Revue, 5+: Alerte).
- **Périmètre Gouvernance (Réservé à l'Auteur) :** S'assurer que le système renvoie la string explicite `REVUE_HUMAINE_RECOMMANDEE` et déporte la décision finale sur le magistrat, sans présumer de la culpabilité.

### Issue — [ML] #010b — Entraînement du Modèle Baseline Tabulaire (XGBoost)
**Labels:** ai, ml-model, difficulty: medium
- **Contexte Analytique :** L'entraînement du premier algorithme prédictif (Gradient Boosting) basé sur la matrice `person_event_window` pour estimer la probabilité d'escalade.
- **Périmètre Technique (Ouvert aux contributions) :** Script d'entraînement Python (XGBoostClassifier) avec calibration, validation croisée, et extraction des features (temporelles, comportementales, graphe, géo).
- **Périmètre Gouvernance (Réservé à l'Auteur) :** Validation des labels d'entraînement ($y=1$ pour affaire sensible/multi-plaintes) et certification de l'absence de variables éthiquement proscrites.

### Issue — [Gov] #010c — Implémentation de la Couche XAI (SHAP Values)
**Labels:** governance, ai, explainability, difficulty: hard
- **Contexte Analytique :** Éviter l'effet boîte noire du modèle XGBoost ou GNN.
- **Périmètre Technique (Ouvert aux contributions) :** Calcul et exposition API des valeurs SHAP (Feature Importance Locale) pour chaque prédiction, avec un traducteur humain (ex: `+0.31 → fréquence d'événements`).
- **Périmètre Gouvernance (Réservé à l'Auteur) :** L'interface finale ne doit PAS afficher un score brut sans afficher immédiatement les 3 facteurs principaux (Top Drivers) qui l'expliquent.

## MILESTONE : Couche H - Case Management System
### Issue — [XAI] #011 — Dashboard Enquêteur (Vue Graphe & SHAP)
**Labels:** frontend, xai, difficulty: medium
- **Contexte Analytique :** Fournir l'interface "Human-in-the-Loop".
- **Périmètre Technique (Ouvert aux contributions) :** App Streamlit ou React/FastAPI. Affichage au centre du graphe (les dossiers liés) et sur le côté l'explicabilité SHAP (`+0.31 -> répétition`).
- **Périmètre Gouvernance (Réservé à l'Auteur) :** Le bouton d'action doit être un "Kill-Switch" d'invalidation humaine pour forcer l'IA à apprendre de ses erreurs.

## MILESTONE : Couche Temps Réel (Event-Driven)
### Issue — [Data] #012 — Ingestion Streaming (Kafka)
**Labels:** data-engineering, streaming, difficulty: hard
- **Contexte Analytique :** Remplacer les requêtes batch (Dossiers) par un flux continu (Événements).
- **Périmètre Technique (Ouvert aux contributions) :** Setup d'un topic Kafka pour ingérer en temps réel les signaux de la Civil Tech ou de l'École et déclencher la pipeline d'Entity Resolution à la volée.
- **Périmètre Gouvernance (Réservé à l'Auteur) :** Gestion de la surcharge (Rate limiting) pour éviter des attaques DDoS via faux signalements civils.

### Issue — [ML] #013 — Moteur Anomaly Detection Temps Réel
**Labels:** ml, anomaly-detection, difficulty: medium
- **Contexte Analytique :** Lever une alerte avant même que le modèle temporel lourd n'ait convergé.
- **Périmètre Technique :** Modèle `Isolation Forest` sur le flux Kafka.

## MILESTONE : Le Double Modèle de Données (Dual Truth)
### Issue — [Data] #014 — Déploiement Base SQL (Vérité Administrative)
**Labels:** data-engineering, sql, difficulty: easy
- **Contexte Analytique :** Créer la source de "Vérité Froide" (Les événements réels).
- **Périmètre Technique :** Schéma PostgreSQL (Tables `Person`, `Institution`, `Event`, `Legal_Case`, `Alert`).

### Issue — [Data] #015 — Ontologie Graphe Neo4j (Vérité Analytique)
**Labels:** data-engineering, neo4j, difficulty: medium
- **Contexte Analytique :** Traduire les Events en un graphe continu.
- **Périmètre Technique :** Création des nœuds et des arêtes factuelles et latentes (`HAS_EVENT`, `RISK_SIGNAL`).

### Issue — [ML] #016 — Pipeline Feature Engineering
**Labels:** ml, data-engineering, difficulty: medium
- **Contexte Analytique :** Transformer les événements bruts en matrices mathématiques pour XGBoost/Hawkes.
- **Périmètre Technique :** Code Python calculant sur des fenêtres glissantes (30j/90j) les features Temporelles, Sociales (Centralité) et Comportementales.

### Issue — [ML] #020 — Entraînement Modèle XGBoost et Explicabilité SHAP
**Labels:** ml, model-training, difficulty: hard
- **Contexte Analytique :** Construire le moteur de prédiction principal (Zone Jaune) qui lira les Features générées par l'Issue #016.
- **Périmètre Technique :** Entraînement du modèle `XGBClassifier` sur des données historiques. Implémentation de la librairie `shap` pour générer le diagramme de force (*Force Plot*) justifiant légalement chaque alerte pour le magistrat.

### Issue — [Graph] #021 — Déploiement de l'Ontologie Cypher (Zone Verte vs Jaune)
**Labels:** graph-db, data-engineering, difficulty: medium
- **Contexte Analytique :** Inscrire le "Privacy by Design" en dur dans la structure Neo4j.
- **Périmètre Technique :** Script d'initialisation Cypher (`CREATE CONSTRAINT`). Mise en place des nœuds `OfficialEvent` et `AdminSignal`. Création de l'index TTL (`Time-To-Live`) automatique sur les arêtes latentes générées par le ML pour assurer l'oubli automatique des fausses suspicions.

### Issue — [Legal] #017 — Moteur de Conformité (Garde-Fou Zone Rouge)
**Labels:** legal, security, difficulty: hard
- **Contexte Analytique :** Empêcher techniquement l'IA de prendre une décision ou de "prédire" une personne.
- **Périmètre Technique :** Implémentation du `kill_switch.py`. L'algorithme doit bloquer toute requête tentant d'exécuter une sanction automatique ou un profilage individuel non supervisé.

### Issue — [Legal] #018 — Gouvernance et Contrôle d'Accès (RBAC Multi-Agences)
**Labels:** legal, security, infrastructure, difficulty: medium
- **Contexte Analytique :** Définir "Qui a le droit de voir quoi ?" pour éviter le Registre National Orwellien.
- **Périmètre Technique :** Implémenter un système de *Role-Based Access Control* stricts au-dessus du Graph. Un policier ne voit pas les notes du psychologue scolaire, il ne voit que le "Niveau d'Alerte" global de la situation.

### Issue — [DevOps] #019 — Infrastructure as Code (SecNumCloud)
**Labels:** devops, infrastructure, security, difficulty: hard
- **Contexte Analytique :** Préparer le déploiement sur un Cloud souverain européen (OVH/Scaleway) respectant les directives CNIL.
- **Périmètre Technique :** Scripts Terraform pour provisionner les clusters Kubernetes (Kafka, Postgres, Neo4j, FastAPI) avec chiffrement AES-256 at-rest.

### Issue — [Front] #011 — API Backend FastAPI
**Labels:** backend, api, difficulty: easy
- **Contexte Analytique :** Permettre l'interrogation du graphe de manière standardisée.
- **Périmètre Technique (Ouvert aux contributions) :** Création des endpoints REST (`/api/cases`, `/api/alerts`, `/api/graph`).
- **Périmètre Gouvernance (Réservé à l'Auteur) :** Imposer les JWT Tokens et RBAC (Role-Based Access Control) interdisant à un agent administratif de voir les détails judiciaires.

### Issue — [Front] #012 — Dashboard Graphe Interactif (React / D3.js)
**Labels:** frontend, dataviz, difficulty: medium
- **Contexte Analytique :** Permettre à un magistrat de visualiser *pourquoi* le système a levé une alerte (Explainable AI).
- **Périmètre Technique (Ouvert aux contributions) :** Interface React utilisant D3.js ou React Flow pour afficher les nœuds suspects et leurs liens de manière lisible.
- **Périmètre Gouvernance (Réservé à l'Auteur) :** Cadrage UX : l'interface ne doit pas ressembler à un "tableau de chasse", mais à un outil d'analyse réseau neutre.

## MILESTONE : Simulation & End-to-End
### Issue — [Testing] #013 — Simulation complète (Scénario Affaire L.)
**Labels:** testing, end-to-end, difficulty: medium
- **Contexte Analytique :** Prouver que la CGIP aurait pu alerter avant le drame de 2026 en ingérant la timeline factice de 2017 à 2022.
- **Périmètre Technique (Ouvert aux contributions) :** Script Python de test E2E qui déclenche l'intégralité du pipeline sur le dataset mocké.
- **Périmètre Gouvernance (Réservé à l'Auteur) :** Fourniture des données simulées (totalement anonymisées et générées synthétiquement) pour ne pas utiliser de vraies données de victimes.

### Issue — [Gov] #014 — Human Decision Layer & XAI (Explainable AI)
**Labels:** governance, audit, difficulty: hard
- **Contexte Analytique :** L'IA ne juge pas, elle alerte. Le magistrat doit comprendre *pourquoi* le score est élevé.
- **Périmètre Technique (Ouvert aux contributions) :** Implémentation de logs d'audit (Traçabilité) et d'un rapport XAI généré avec chaque alerte (ex: "Score = 0.87 CAR 3 signalements en 18 mois").
- **Périmètre Gouvernance (Réservé à l'Auteur) :** Verrouillage juridique interdisant au système de prendre une décision automatisée privative de liberté.

### Issue — [API] #015 — Boucle de Retour (Alerting vers l'École/Police)
**Labels:** api, backend, difficulty: medium
- **Contexte Analytique :** Résolution du "Casse #5". Si le Graphe détecte un danger, il doit notifier les émetteurs de signaux faibles (ex: l'infirmière scolaire) pour qu'ils ne restent pas dans l'ignorance.
- **Périmètre Technique (Ouvert aux contributions) :** Création d'une API d'alerting (Webhook/Email sécurisé) pour redescendre l'information vers les points d'entrée du système.
- **Périmètre Gouvernance (Réservé à l'Auteur) :** Définition juridique stricte de *qui* a le droit de recevoir cette alerte retour (secret de l'instruction vs protection de l'enfance).
