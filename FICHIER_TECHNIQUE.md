# RÉFÉRENTIEL TECHNIQUE CONTINU

Ce document a pour but d'extraire et de synthétiser toutes les exigences techniques, les architectures de données et les règles d'ingénierie qui émergent de la genèse du projet. Il complète le README et le socle mathématique en se basant sur les cas réels.

---

## 1. Modélisation de la Donnée (Cas d'usage : Affaire Lyhanna)

L'ingestion de la matière brute issue du premier échange démontre les nécessités techniques de l'ontologie du système. La base orientée graphe (Neo4j) doit pouvoir représenter la complexité suivante pour combattre les silos.

### 1.1 Entités requises (Nodes)
- **Personne** : Les individus impliqués. Le système doit gérer les homonymies partielles et les fautes de frappe ("Bob" vs "Robert").
- **Événement Judiciaire** : Plainte enregistrée, classement sans suite, enquête en cours.
- **Événement Administratif / Social** : Signalement informel, alerte d'une éducatrice, licenciement pour motif comportemental (Éducation Nationale).
- **Institution** : École, Brigade de Gendarmerie, Tribunal, Service Social.

### 1.2 Relations requises (Edges)
- `[Personne] -[:VISÉ_PAR]-> [Plainte/Signalement]`
- `[Institution] -[:ÉMET]-> [Signalement]`
- `[Personne] -[:EMPLOI_AU_SEIN_DE]-> [Institution]`
- `[Institution] -[:CLASSE_SANS_SUITE]-> [Plainte]`

### 1.3 Contraintes Systèmes (Inputs et Ingestion - Les Silos de l'administration)
Le système doit être conçu pour se sur-coupler au "Labyrinthe" des bases existantes, chacune souffrant de son propre biais de spécialisation :
- **Cassiopée** (Justice) : *Système de Gestion de Procédures*. Il ignore les signaux faibles non-judiciarisés.
- **TAJ** (Traitement d'Antécédents Judiciaires) : Fichier de police/gendarmerie, massivement utilisé mais centré sur l'enquête locale.
- **FIJAISV** : Fichier des condamnés pour violences sexuelles. Inutile pour prévenir l'escalade d'un profil n'ayant jamais été condamné.
- **SALVAC / ViCLAS** (Système d'Analyse des Liens de la Violence) : Le système de rapprochement sériel de la police. Extrêmement puissant (156 items d'analyse comportementale) mais géré manuellement par un groupe restreint d'analystes, et réservé aux crimes violents majeurs.
- **La Civil Tech (Couche Zéro)** : Applications civiles gouvernementales (*App-Elles*, *Mémo de Vie*, *Ti3rs*) recensant les signaux faibles et preuves directement auprès des victimes.

Le pipeline d'ingestion (Couche A) devra donc pouvoir abstraire et standardiser des formats de données très différents, issus de ces vieux systèmes monolithiques ou des APIs modernes de la Civil Tech, en nœuds et arêtes standardisés, pour agir comme une **Super-Couche de Fusion**.

---

## 2. Extraction et Attributs de Nœuds (Enseignements du Bloc 2)

## 1. L'Architecture à 5 Couches (CGIP)

Le système CGIP est structuré selon un paradigme d'intégration globale, divisé en 5 strates étanches :
### 1.1 Data Ingestion Layer (Le défi du Continuum)

Cette couche doit résoudre les **8 Points de Rupture (Casses)** du flux d'information actuel entre l'École, la Police et la Justice :
1. **Casse #1 (École)** : Signal faible non standardisé (texte libre). Nécessite un parser NLP robuste.
2. **Casse #2 (Filtrage)** : Déperdition humaine avant même l'enquête.
3. **Casse #3 (Police)** : Silo opérationnel local.
4. **Casse #4 (Justice)** : Logique "par dossier" (Cassiopée).
5. **Casse #5 (Boucle de retour)** : Aucun retour d'information vers l'école. **(Nécessité de coder une API de notification)**.
6. **Casse #6 (Mémoire)** : Pas de timeline consolidée.
7. **Casse #7 (Identité)** : Orthographes différentes. (Résolu par la Couche 2).
8. **Casse #8 (Légalité)** : Contraintes RGPD bloquantes.

**Schéma de Flux (Le problème à résoudre) :**
```text
[École] --(Texte libre)--> [Police] --(PV)--> [Justice / Cassiopée]
   ^                                                 |
   |_________________________________________________|
            (BOUCLE DE RETOUR INEXISTANTE)
```
3. **Justice Knowledge Graph** (Neo4j)
4. **ML Risk Engine & Investigation AI** (Causalité et Prédiction)
5. **Human Decision Layer** (Alerte et XAI)

### 2.1 Taxonomie Stricte des Événements
Le système technique doit opérer une séparation binaire au niveau de la donnée ingérée :
- `is_official_judicial_procedure` (Boolean) : Ce flag technique est nécessaire pour séparer ce qui relève d'une procédure pénale stricte (Plainte, Enquête) de ce qui relève du signalement administratif (alerte école). C'est crucial pour pondérer le graphe et alimenter le moteur de compliance RGPD.

### 2.2 Propriétés (Properties) des Nœuds Événementiels
La frise chronologique extraite montre que chaque Nœud "Événement" doit posséder des métadonnées fines pour que l'inférence causale (Do-Calculus) fonctionne :
- `date` ou `timestamp` : Indispensable pour respecter la flèche du temps.
- `victim_age_at_time` (Integer) : L'âge de la victime au moment des faits est un discriminant majeur pour évaluer la récurrence ou le profilage du suspect, et pondérer la gravité de l'alerte globale.

### 2.3 Pipeline d'Ingestion NLP (LLM to Graph)
L'exercice de recoupement prouve l'efficacité de l'IA pour traiter du texte. L'architecture doit prévoir un pipeline d'ingestion textuel :
- **Composant requis** : Une brique LLM placée en amont du graphe (ex: Llama 3, Mistral).
- **Fonction** : Analyser des textes bruts ou chaotiques (rapports d'enquêtes, PV scannés) pour en extraire automatiquement :
  - Les entités (NER : Named Entity Recognition).
  - La nature des liens (Relation Extraction).
  - Les chronologies et les caractéristiques des acteurs (âges).
  Ce pipeline permet d'automatiser la création des nœuds et arêtes sans saisie manuelle laborieuse.

---

## 3. Topologie et Désambiguïsation (Enseignements du Bloc 3)

Le troisième échange démontre concrètement l'intérêt d'une base de données graphe pour structurer le chaos et éviter la fusion erronée d'événements.

### 3.1 Nœud "Dossier" (Case Node) vs Nœud "Événement"
La "Carte Mentale" montre qu'un regroupement supérieur est nécessaire.
- **Le Nœud `[Dossier_Investigation]`** : Il regroupe une série de Nœuds `[Événement]` liés à une même victime. Cela permet au GNN (Graph Neural Network) de traiter l'historique non pas comme une soupe d'événements, mais comme des sous-graphes cohérents centrés sur des faits précis.

### 3.2 Le Processus d'Entity Resolution (Dédoublonnage)
La conversation soulève le risque de confondre deux événements (l'alerte scolaire de 2020 et les viols de 2020). L'architecture devra inclure une fonctionnalité clé : **Entity Resolution**.
- Le système doit être capable de séparer deux nœuds temporels proches s'ils ne concernent pas la même victime, ou de les fusionner (Merge) avec un `Confidence Score` si de nouveaux éléments prouvent qu'il s'agit de la même affaire.

### 3.3 Visualisation Graphique (Couche H - Case Management)
L'interface utilisateur finale (le Dashboard Streamlit ou React pour les enquêteurs) devra reprendre exactement le paradigme visuel de "Carte Mentale" validé dans l'échange.
- L'enquêteur ne doit pas voir un tableau SQL. Il doit voir au centre le Nœud `[Suspect]` relié à X clusters (les victimes ou dossiers identifiés) avec une coloration distincte pour le pénal (Officiel) et le signalement (Non Officiel). L'IHM (Interface Homme-Machine) est déjà prototypée philosophiquement ici.

---

## 4. Spécifications Fonctionnelles et Systémiques (Enseignements du Bloc 4)

L'énumération de 8 failles systémiques dans l'échange fournit le cahier des charges exact des fonctionnalités mathématiques et logicielles à développer pour la plateforme.

### 4.1 Modélisation Spatiale et Contextuelle (Le Schéma ASCII)
Le diagramme "Réseau des victimes" impose d'ajouter de nouveaux types de nœuds dans Neo4j :
- **Nœuds de Contexte** : `[Milieu_Scolaire]`, `[Espace_Public]`, `[Domicile]`.
- **L'avantage mathématique (GNN)** : Relier deux victimes non pas directement entre elles, mais indirectement via un nœud "Contexte" ou "Lieu" partagé avec le suspect augmente considérablement le score de similarité cosinus (Cosine Similarity) dans l'Embedding Space du réseau de neurones, permettant à la machine de détecter un *Modus Operandi* invisible à l'œil nu.

### 4.2 L'Architecture contre les Failles (Mapping Technique)
Chaque faille soulevée appelle une réponse architecturale précise dans le code source :
1. **Silos (Faille 1)** -> Base Neo4j unifiée (Couche A).
2. **Aveuglement temporel (Faille 7)** -> Temporal Graph Networks (TGN). Le temps n'est pas une simple valeur, c'est une propriété de la relation (`[VISÉ_PAR {annee: 2020}]`) permettant d'étudier la vélocité et l'évolution d'un comportement.
3. **Sortie des radars (Faille 6)** -> Un événement classé sans suite (`status: CLOSED`) n'est jamais effacé (Soft Delete). Son poids (Weight) dans le graphe est réduit, mais il reste disponible pour de l'inférence ultérieure si un nouveau signal apparaît.
4. **Absence de profil central (Faille 4)** -> Création du Dashboard (Couche H) proposant une "Vue à 360°" agrégeant un Score de criticité hybride, indépendant de la présence ou non de casier judiciaire.
5. **Tension Présomption d'innocence vs Prévention (Faille 8)** -> C'est la justification absolue du **Moteur DPIA (Couche E)** et du **Kill-Switch (Couche F)**. L'algorithme doit bloquer ses propres déductions si elles s'apparentent à du profilage automatisé illégal.

---

## 5. Privacy by Design et Ingénierie des Poids (Enseignements du Bloc 5)

Le cinquième échange sur la tension entre prévention et libertés individuelles dicte les mécanismes de sécurité et de pondération du Graphe.

### 5.1 Gestion des "Fausses Corrélations" (Confidence Score)
Pour éviter qu'un citoyen ne soit "surclassé à risque" à tort (ex: rumeur scolaire fusionnée avec plainte ancienne), l'architecture de données doit introduire le concept mathématique de `Confidence Score` (Score de certitude).
- Chaque nœud `[Signalement]` et chaque arête `[:VISÉ_PAR]` doit comporter un attribut de `Poids` (Weight).
  - Condamnation pénale : `Weight = 1.0`
  - Plainte en cours : `Weight = 0.8`
  - Signalement administratif (École) : `Weight = 0.5`
  - Information anonyme ou rumeur : `Weight = 0.1`
- Le Graph Neural Network (GNN) doit utiliser ces poids dans sa fonction d'activation. Un amas de signaux très faibles (`0.1`) ne doit pas suffire à déclencher l'alerte maximale (Couche G).

### 5.2 Protection RGPD et "TTL" (Time-To-Live)
Pour respecter le droit à l'oubli et éviter le "profilage permanent de suspicion", le graphe ne peut pas conserver une donnée accusatoire *ad vitam æternam* avec la même force si aucune condamnation n'est prononcée.
- **Time Decay Function** : Implémentation mathématique de la décadence temporelle. Le poids d'une arête diminue de façon linéaire ou exponentielle avec le temps s'il n'y a pas de nouvelle occurrence, conformément aux durées de prescription légales.

### 5.3 Architecture Fédérée vs Datalake Monolithique
La "fragmentation institutionnelle volontaire" citée dans l'échange impose des contraintes sur le backend d'ingestion (Couche B) :
- La CGIP ne peut peut-être pas aspirer physiquement et fusionner toutes les données de la Justice et de l'École dans un même disque dur central, pour des raisons de conformité CNIL.
- **L'alternative architecturale** : Une approche de **Graphe Fédéré**. La base Neo4j de la CGIP stocke les *Index* (Pointeurs et Graphes de relations anonymisés), mais va requêter les détails via API sécurisée (avec gestion fine des droits d'accès - ACL) uniquement au moment où l'alerte est déclenchée.

---

## 6. Ingénierie Data Science et Modèles Machine Learning (Enseignements du Bloc 6)

Le sixième échange définit les 5 catégories d'algorithmes mathématiques à implémenter dans les couches d'analyse (Couches B, E et G). Le but n'est pas de "prédire une culpabilité", mais d'émettre l'alerte `REVUE HUMAINE RECOMMANDÉE`.

### 6.1 Algorithmes de Scoring (Trigger Events et Machine Learning)
- **Objectif** : Générer une alerte basée sur la vélocité et l'escalade d'une trajectoire. On ne prédit PAS "un crime" (pas de Minority Report). On estime la probabilité qu'une trajectoire d'événements s'aggrave de façon significative dans les 12 mois.
- **Formulation ML** : $y = 1$ si escalade significative, $y = 0$ sinon.
- **Architecture de la Donnée (Dataset)** : Table `person_event_window` (chaque ligne = une personne observée sur une fenêtre temporelle).
- **Feature Engineering (Le cœur du moteur ML)** :
  1. **Features Temporelles** : Fréquence, accélération, `time_decay_score`.
  2. **Features Comportementales** : Répétition du même contexte, diversité des victimes.
  3. **Features Relationnelles (Graph)** : Centralité du nœud, proximité avec des affaires graves.
  4. **Features Géographiques** : Rayon de dispersion, densité spatiale.
- **Modèles de Classification (Couche G)** : 
  - *Baseline Robuste* : Gradient Boosting (XGBoost, LightGBM) ou Random Forest. Idéal pour les données tabulaires et la calibration.
  - *SOTA (State-of-the-Art)* : Graph Neural Networks (Node2Vec, GraphSAGE) ou Temporal Transformers pour capter les trajectoires complexes.

### 6.2 Détection d'Anomalies (Anomaly Detection)
- **Objectif** : Identifier un individu au comportement statistiquement anormal (non-supervisé).
- **Algorithmes (Couche G)** : `Isolation Forest`, `One-Class SVM`, `Local Outlier Factor (LOF)`.
- **Cas d'usage** : Une concentration inhabituelle de signalements administratifs ou scolaires mineurs (non pénaux) qui sort de la norme statistique de la population.

### 6.3 Modélisation des Séquences Temporelles
- **Objectif** : Comprendre le rythme et l'escalade d'un comportement.
- **Algorithmes** : `Chaînes de Markov`, `Processus de Hawkes` (modélisation d'événements auto-excitants).
- **Cas d'usage** : Si un événement en 2017 est suivi d'une longue pause, puis de 3 événements rapides en 2026, un Processus de Hawkes modélisera cette "accélération" pour déclencher une alerte urgente.

### 6.4 Graph Analytics (Réseau)
- **Objectif** : Détecter les connexions structurelles.
- **Implémentation (Couche A / C)** : Graph Neural Networks (GNN) et algorithmes de graphe (ex: *PageRank*, *Community Detection*) appliqués sur Neo4j.
- **Cas d'usage** : Trouver le lien invisible entre deux victimes (ex: même école, même piscine) qui n'aurait pas été vu dans un tableau SQL.

### 6.5 Entity Resolution (Rapprochement de dossiers) et Pipeline NLP
L'approche de la CGIP repose sur l'extraction d'information depuis du texte non structuré (rapports d'éducateurs, mains courantes). C'est le rôle de l'IA "Secrétaire" (Zone Verte).

**Le Pipeline NLP à 3 étapes :**
1. **Named Entity Recognition (NER)** : Un modèle Transformer (ex: *CamemBERT* ou *Mistral* fine-tuné sur le corpus juridique français) ingère un texte libre et identifie les entités : 
   - *Texte* : "Hier, le petit J. Dupont a violemment poussé un camarade dans la cour du collège Rousseau."
   - *Extraction* : `Personne: J. Dupont`, `Institution: Collège Rousseau`, `Event: Violence physique`.
2. **Relation Extraction (RE)** : Le LLM structure la phrase en triplet sémantique (Sujet - Verbe - Objet) pour Neo4j :
   - `(J. Dupont) -[:IMPLIQUÉ_DANS {role: "Auteur"}]-> (Violence) -[:HAPPENED_IN]-> (Collège Rousseau)`
3. **Entity Resolution (Dédoublonnage Bayesien)** : Le cœur du système pour contourner l'absence d'Identifiant Unique (RGPD).
   - L'algorithme calcule la similarité probabiliste entre "J. Dupont" (Signalement École) et "Jean Dupont" (Plainte TAJ de 2024).
   - *Métrique* : Combinaison de distance lexicale (Jaro-Winkler) et de proximité spatio-temporelle. Si la similarité dépasse $85\%$, le système fusionne (Merge) les deux entités dans le Graphe avec un `Confidence Score` associé.

---

## 7. Predictive Risk Modeling (PRM) et Traitement du Biais (Enseignements du Bloc 7)

Le septième échange introduit des concepts issus d'exemples réels déployés à l'international, notamment l'Allegheny Family Screening Tool (AFST), imposant des gardes-fous stricts.

### 7.1 La Cascade Algorithmique (Le Pipeline)
L'échange valide la chaîne de traitement suivante, qui devient le pipeline canonique de la CGIP :
1. **Entity Resolution** : Dédoublonnage des entités.
2. **Graph Database (Neo4j)** : Restructuration sous forme de réseau.
3. **Analyse Temporelle (Hawkes Process / Survival Analysis)** : Calcul du taux d'escalade.
4. **Scoring Supervisé** : Agrégation en un score hybride.
5. **Output (Alerte Humaine)** : Le système s'arrête là et passe la main à l'humain.

```mermaid
graph TD
    A["Données Brutes Multi-Sources<br/>(Silos Souverains)"] --> B{"Entity Resolution<br/>(Dédoublonnage NLP)"}
    B --> C[/"Graph Database Neo4j<br/>(Topologie)"\]
    C --> D("Analyse Temporelle<br/>(Hawkes Process / Survival Analysis)")
    D --> E("Scoring Supervisé<br/>(Agrégation du Risque cumulatif)")
    E --> F((("⚠️ ALERTE : REVUE HUMAINE RECOMMANDÉE ⚠️")))
    
    style A fill:#f9f9f9,stroke:#333,stroke-width:1px
    style B fill:#d4edda,stroke:#28a745,stroke-width:2px
    style C fill:#cce5ff,stroke:#007bff,stroke-width:2px
    style D fill:#fff3cd,stroke:#ffc107,stroke-width:2px
    style E fill:#fd7e14,stroke:#fff,stroke-width:2px,color:#fff
    style F fill:#dc3545,stroke:#fff,stroke-width:3px,color:#fff
```

### 7.2 L'Alerte et le Dashboard (L'indispensable XAI)
Le système doit être pensé pour lutter contre la "boîte noire", le biais algorithmique et le "Biais du Rétroviseur". 
- L'alerte générée doit afficher un **Risk Score**.
- **SHAP Explainability** : Le dashboard doit impérativement afficher la Feature Importance Locale justifiant l'alerte (ex: `+0.31 → fréquence événements`, `+0.22 → répétition contexte`, `-0.05 → absence antécédents graves`).
- Le statut final de l'interface doit toujours être : `Revue prioritaire recommandée`. La machine dit : "cette trajectoire ressemble statistiquement à des trajectoires à escalade", et déporte la responsabilité juridique sur le magistrat.

### 7.3 Les Modèles Alternatifs de Trajectoire (Survival Analysis)
En plus du Processus de Hawkes, l'échange suggère d'explorer l'Analyse de Survie (Survival Analysis) :
- `Cox Proportional Hazards` ou `Random Survival Forests`.
- Ces algorithmes permettent de répondre à la question : "Quelle est la probabilité qu'un nouvel événement survienne après un premier signalement dans un délai X ?". Ces modèles devront être ajoutés au backlog exploratoire du projet pour la modélisation temporelle.

---

## 8. L'Architecture Complète (Cloud / Data Lake / Graph DB)
*(Le schéma d'architecture complet a été déplacé dans la Section 3.1)*

### Le Rôle Central de l'Entity Resolution (Le palliatif au Registre National)
Dans les pays nordiques, l'interopérabilité est garantie par un "Identifiant Unique" (*Personnummer*). En France, c'est anticonstitutionnel. L'Entity Resolution n'est donc pas une simple "Feature". **C'est la brique fondamentale qui simule mathématiquement un identifiant unique** pour lier le Data Lake (où les dossiers sont isolés et les noms mal orthographiés) et le Graph (où l'individu devient un nœud unique). Si cette couche échoue, tout le modèle IA aval s'effondre.

---

## 9. Dictionnaire de Données (Dualité SQL / Graph)

Pour éviter la "contamination de la preuve", la CGIP utilise deux bases de données distinctes.

#### 1. Modèle SQL (La vérité administrative immuable)
*   **Person** : `person_id`, `national_id_hash`, `birth_date`, `status`
*   **Institution** : `institution_id`, `type`, `name`
*   **Event** : `event_id`, `person_id`, `institution_id`, `event_type`, `severity`, `timestamp`
*   **Legal_Case** : `case_id`, `status`, `offense_type`

#### 2. Modèle Graph (La reconstruction de la réalité)
*   **Nœuds** : `(:Person)`, `(:Institution)`, `(:Event)`, `(:Location)`
*   **Arêtes Factuelles** : `-[:HAS_EVENT]->`, `-[:RECORDED_BY]->`, `-[:ASSOCIATED_WITH]->`, `-[:OCCURRED_AT]->`
*   **Arêtes Latentes (Générées par l'IA)** : `-[:RISK_SIGNAL {weight: 0.7}]->` (Calculées en temps réel par inférence).

#### 3. Payload Kafka (L'Événement Standardisé)
```json
{
  "event_id": "uuid",
  "type": "school_report | police_report | social_report",
  "person_id": "uuid",
  "timestamp": "2026-06-06T10:00:00Z",
  "severity": 3,
  "metadata": {"source": "school", "text": "incident violent"}
}
```

---

## 10. Le Modèle de Graphe "Idéal Européen" (Ontologie Neo4j Pure)

La structuration de la base orientée graphe ne relève pas de la simple optimisation de performance : elle matérialise le cadre légal du RGPD. Voici l'ontologie stricte (Labels, Propriétés, Arêtes) qui sépare la réalité prouvée des déductions de l'IA.

### 10.1. Les Nœuds (Entities)
On sépare strictement les faits judiciaires des signaux faibles de la société civile.
1. `(:Person)` : L'individu.
   - Propriétés : `hashed_id` (L'identité réelle reste dans le coffre SQL), `privacy_tier` (Niveau de protection des données).
2. `(:OfficialEvent)` : Les faits judiciairement validés.
   - Propriétés : `type` (Plainte, Condamnation), `timestamp`, `severity` (1 à 10).
3. `(:AdminSignal)` : Les signaux faibles administratifs.
   - Propriétés : `source` (École, Hôpital), `reliability` (Fiabilité intrinsèque de la source), `timestamp`.
4. `(:Context)` : Les espaces de croisement (Physiques ou virtuels).
   - Propriétés : `category` (Établissement scolaire, Réseau social), `name_hash`.

### 10.2. Les Arêtes Factuelles (Zone Verte)
Ces relations sont créées par le pipeline d'ingestion. Elles représentent la vérité administrative à l'instant T.
- `(Person)-[:INVOLVED_IN {role: "Suspect", status: "Closed"}]->(OfficialEvent)`
- `(Person)-[:MENTIONED_IN {confidence_score: 0.85, time_to_live_days: 180}]->(AdminSignal)`
- `(OfficialEvent)-[:OCCURRED_AT]->(Context)`

### 10.3. Les Arêtes Probabilistes (Zone Jaune ML)
Ces relations sont injectées **par l'IA** (Graph Neural Networks) lors du recalcul nocturne. C'est ici que l'Idéal Européen impose sa loi : **Toutes ces arêtes ont une Date de Péremption (TTL Index)**.
- `(Person)-[:LATENT_RISK_LINK {weight: 0.92, shapley_justification: "Comm_Context"}]->(Person)`
   - *Traduction* : "L'IA suspecte fortement que X et Y travaillent ensemble car ils gravitent autour des mêmes contextes simultanément. Poids : 0.92".
- `(Person)-[:ESCALATING_TOWARDS {hawkes_intensity: 4.5}]->(Context)`
   - *Traduction* : "L'individu X est en train d'intensifier ses actions autour de l'École Z."

> **MÉCANISME DE DÉFENSE (TTL)** : Dans Neo4j, une contrainte `db.index.ttl` est appliquée aux arêtes probabilistes. Si aucune nouvelle preuve factuelle ne vient valider l'intuition de l'IA dans les 30 jours, l'arête `LATENT_RISK_LINK` est automatiquement effacée de la base. L'IA n'a pas le droit de créer une "suspicion permanente" infondée.


## X. Architecture Data Lake & Moteurs de Base de Données

Le système ingère les données selon une hiérarchie stricte :
1. **Data Lake (Stockage Froid)** : S3 / MinIO / HDFS. Conservation immuable (append-only) pour auditabilité CNIL.
   - `/raw/police`, `/raw/justice`, `/raw/education`
   - `/processed/normalized_entities`
2. **Entity Resolution Layer** : Moteur de fusion probabiliste (Modèle de Fellegi-Sunter) et Embeddings BERT.
3. **Graph Database** : Neo4j (privilégié), JanusGraph ou Neptune. Gère les arêtes (`accused_in`, `reported_by`).

## X. Dictionnaire de Données (Schéma Relationnel)

L'architecture s'appuie sur 5 tables primaires avant ingestion dans le Graphe :
1. `events` : L'entité de base. (`event_id`, `person_id`, `event_type`, `date`, `source_institution`, `severity_score`, `location`).
2. `persons` : Entités physiques désambiguïsées. (`person_id`, `age`, `role`, `risk_history_count`).
3. `relations` : La fondation de la table de jointure pour Neo4j. (`source`, `target`, `relation_type`, `strength`).
4. `institutions` : Les acteurs de la Couche Zéro.
5. `risk_snapshots` : L'historisation des scores (Auditabilité CNIL).

## X. Validation Architecturale (L'Exception CGIP)

L'étude des systèmes existants (NCIC aux USA, ViSOR au UK, Municipality Data Hubs aux NL) confirme que notre architecture est techniquement **inédite à l'échelle nationale**.
Ce qui manque partout dans le monde, et que la CGIP implémente :
- Une véritable **Graph Database nationale unifiée**.
- Du **Machine Learning explicable (XAI)** inter-institutions.
- Une **Boucle temps réel** (Kafka) entre la Justice, le Social et l'École.

## X. Pipeline de Scoring (Architecture Logique)

Le flux de traitement d'une prédiction suit un pipeline strict et séquentiel :
1. **Feature Engineering** : Extraction des données tabulaires (ex: `event_count_6m`).
2. **Graph Features** : Interrogation de Neo4j (ex: `degree_centrality`, `betweenness`).
3. **ML Model** : Inférence (XGBoost ou GNN).
4. **Rule Engine (Kill-Switch Légal)** : Application des contraintes RGPD sur le `raw_score`.
5. **Explanation Engine** : Génération des valeurs SHAP (Top facteurs).
6. **Alert Engine** : Routage vers le Magistrat ou le Case Worker selon le seuil.

## X. Validation Dystopique (L'Écueil Chinois)

L'ajout de l'architecture chinoise au benchmark nous donne une spécification en creux de ce que la CGIP **ne doit jamais faire** :
- **Interdiction formelle** de croiser la donnée de la Couche Zéro (Police/Justice/Social) avec de la donnée "Lifestyle" (mobilité, paiements, réseaux sociaux).
- **Interdiction formelle** du ML non-supervisé ou du Computer Vision sur les comportements.
La CGIP est strictement bornée aux événements institutionnels.

## X. Schéma de Données (Core DB SQL vs Graph DB)

Le stockage hybride est officiellement architecturé comme suit :

### 1. SQL Core (PostgreSQL) - "System of Record"
Structure rigide contenant la vérité juridique :
- `persons` : Identité et flag de risque global.
- `institutions` : Les acteurs.
- `events` : La timeline centrale (Signalements, plaintes, etc.).
- `cases` : Le regroupement légal ("L'Affaire" Pénale/Sociale).
- `case_event_link` & `interactions` : Tables de jointure.

### 2. Graph Database (Neo4j) - "Context Engine"
Traduction du SQL en réseau :
- **Nodes** : `Person`, `Event`, `Institution`, `Case`.
- **Edges** : `[:INVOLVED_IN]`, `[:REPORTED]`, `[:CONNECTED_TO]`, `[:CONTAINS]`, `[:INVOLVES]`.

## X. Architecture Big Data (ETL & ML Pipeline)

Le schéma global du système intègre l'écosystème Big Data industriel :
1. **Data Lake (S3/HDFS)** : Reçoit la donnée brute.
2. **Couche ETL (Apache Spark)** : Script PySpark qui nettoie, filtre (ex: `age < 18`), et agglomère les données massives (`groupBy`).
3. **Feature Store (Spark / Feast)** : Stocke les vecteurs d'apprentissage.
4. **Graph DB (Neo4j)** & **ML Training (XGBoost/RF)** : S'alimentent sur le Feature Store.
5. **Risk Scoring Engine** (Batch + Streaming).

## XI. Architecture Streaming Temps Réel (Event-Driven)

La CGIP n'est pas un système de traitement par lots (Batch). C'est une **Architecture Orientée Événements** basée sur Apache Kafka. Dès qu'un acteur de terrain enregistre une information, celle-ci est propulsée dans le système nerveux central.

### Le Pipeline de Consommation Asynchrone
Le `Consumer` Kafka (Script : `kafka_consumer.py`) intercepte le message et orchestre la cascade suivante en millisecondes :
1. **Étape Juridique** : Passage dans le Sas Cryptographique (`rgpd_anonymizer.py`).
2. **Étape System of Record** : Le hachage et l'événement sont validés dans la base **PostgreSQL**.
3. **Étape Contexte** : Les nouveaux nœuds et arêtes sont ajoutés au **Graphe Neo4j**.
4. **Étape Analytique** : Une fois la "vérité" figée, le modèle **XGBoost** (`risk_scorer.py`) est réveillé pour recalculer le score global de l'individu ciblé.

**Orchestration Stricte** : L'IA ne tourne jamais en amont. Elle est toujours la dernière étape de la chaîne, garantissant qu'elle calcule son score sur la topologie la plus fraîche et sécurisée possible.


## XII. Cloisonnement Légal & Traçabilité (Zero Trust)

Face à la "Fragmentation institutionnelle" et aux divers secrets (médical, instruction), l'architecture technique adopte un modèle *Zero Trust*.
- Le Graphe Neo4j stocke les liens, mais les propriétés détaillées des nœuds restent soumises à la clé de déchiffrement du Magistrat.
- La traçabilité est absolue : tout accès par le ML ou un acteur humain laisse une empreinte d'audit (Audit Trail) pour répondre à la CNIL.

## XIII. Infrastructure "Cloud Souverain" et Niveaux de Sécurité

L'architecture physique de la CGIP est pensée pour un déploiement sur un **Cloud de Confiance (SecNumCloud)**, segmenté par ministères (Justice, Intérieur, Social).

### Classification des Données (Zero Trust)
- **🟥 Niveau 0 (Ultra Sensible)** : Secret de l'instruction, données mineurs/santé. *Stockage isolé (Air-gapped logique).*
- **🟧 Niveau 1 (Judiciaire/Police)** : Procédures pénales, TAJ.
- **🟩 Niveau 2 (Administratif)** : Signalements éducatifs, ASE.

### La "Secure Data Fabric"
Au lieu d'une base monolithique, le système utilise une *API Gateway Souveraine* et une *Federation Layer*. Neo4j interroge ces bases via des index et des tokens pseudonymisés (Identity Layer), sans jamais rapatrier la donnée brute textuelle de Niveau 0 dans son moteur de calcul.

## XIV. Pipeline ML Avancé : GNN pour la Fusion de Dossiers

### 1. Nœuds et Arêtes Supplémentaires
Le schéma Neo4j s'enrichit :
- **Nœuds** : `Document`
- **Arêtes** : `(Person)-[MENTIONED_IN]->(Document)`, `(Case)-[RELATED_TO]->(Case)`, `(Case)-[SHARES_EVIDENCE]->(Case)`

### 2. Le Pipeline d'Exécution GNN
```text
[Input Graph] -> [Node Embedding] -> [Message Passing (k hops)] -> [Aggregation (Mean/Attention)] -> [Case-Level Embedding] -> [Link Prediction Head]
```

### 3. Feature Engineering Structurant
- **Temporel** : `delta_time_between_events`, `burst_activity_score`
- **Comportemental** : `escalation_pattern`
- **Topologique** : `PageRank judiciaire`, `degree centrality`

## XV. Modélisation Spécifique d'une Enquête (Cas Type)

### 1. Enrichissement Ontologique (Nœuds & Arêtes)
- **Nœuds Enquête** : `P_Victime`, `P_Témoin`, `Case_0 (Signalement)`, `L1 (Domicile)`.
- **Arêtes Humaines** : `[REPORTED_SIGHTING]`, `[QUESTIONED_BY]`.
- **Arêtes Événementielles** : `[triggers]`, `[expands_scope]`, `[located_at]`.

### 2. Schéma Temporel d'une Enquête
```text
[E1 Disparition] -> triggers -> [E2 Ouverture enquête] -> triggers -> [E3 Perquisition]
                                                                          |
                                                                          v
                                                                     [L1 Domicile]
```

### 3. Les 3 Patterns Cibles du GNN
Le Message Passing du GNN est configuré pour détecter trois anomalies structurelles :
1. **Concentration Spatiale** (ex: Domicile ↔ Zones de recherche ↔ Découverte).
2. **Accélération Temporelle** (Burst Activity).
3. **Convergence des flux** (Plusieurs sous-graphes qui fusionnent).