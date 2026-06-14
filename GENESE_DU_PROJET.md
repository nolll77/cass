# GENÈSE DU PROJET - ANALYSE DES ÉCHANGES FONDATEURS

Ce document est le réceptacle absolu de la mémoire du projet. Il capture et analyse 100% des concepts issus de la discussion d'origine avec l'IA. Il a vocation à grandir au fur et à mesure de l'ingestion des archives.

---

## BLOC 1 : L'Étincelle du Projet - L'Affaire Lyhanna et la Faillite des Silos

### 1. La matière brute fournie
Le point de départ du projet s'ancre dans le réel et le tragique. La discussion s'ouvre sur :
- Des liens institutionnels pointant vers les bases de données actuelles (Cassiopée, le logiciel de rédaction des procédures, et ViCLAS pour les crimes en série).
- Un corpus massif d'articles de presse (BFMTV, Le Figaro) disséquant l'affaire de la disparition de la jeune Lyhanna (11 ans).
- Un exercice de "recoupement" demandé à l'IA pour dénombrer exactement les plaintes et signalements visant le principal suspect (Jérôme B.), père de famille de 41 ans.

### 2. L'analyse du problème (L'effondrement du système)
Le recoupement de l'IA a mis en évidence la réalité factuelle suivante :
- **3 plaintes pour viols** (2022 pour des faits de 2020, 2025, 2026).
- **2 à 3 signalements / alertes** (2017 pour relation avec mineure, 2020 avec licenciement scolaire pour comportement inapproprié, 2026 via une éducatrice).

**Le constat d'échec :** Ces 5 à 6 événements distincts, bien que graves, ont été traités de manière isolée par des acteurs différents (Éducation Nationale, Aide Sociale à l'Enfance, Gendarmerie, Parquet de différentes juridictions). Parce qu'ils n'ont pas été corrélés, le suspect a conservé une apparente impunité jusqu'au drame.

### 3. Ce que cela fonde pour le Projet (La vision CGIP)
Ce premier échange est la **Preuve de Concept (Proof of Need)** du projet.
Il démontre par l'exemple que :
1. Le stockage d'informations dans des silos verticaux (un logiciel pour la police, un registre pour l'école, un dossier pour l'aide sociale) est mathématiquement incapable de prévenir les crimes complexes.
2. Le système n'a pas besoin de *plus* de données. La donnée était déjà là. Il a besoin d'une **topologie différente** pour que la donnée se rencontre.
3. Le projet doit construire un moteur capable de relier un "licenciement scolaire" à une "plainte classée sans suite" pour faire clignoter un signal d'alerte rouge avant que le pire n'arrive. C'est l'essence même du passage à une architecture de Graphe.

---

## BLOC 2 : Le Contraste des Moyens et la Chronologie Structurée

### 1. La matière brute fournie
Ce deuxième échange poursuit l'analyse de l'affaire Lyhanna avec :
- Un nouvel article du Figaro détaillant l'immense dispositif de recherche *a posteriori* (170 à 180 gendarmes, plongeurs, hélicoptères, 400 km² fouillés).
- Une exigence de "recoupement strict" demandée à l'IA pour séparer formellement ce qui relève de la procédure **Officielle (Judiciaire)** et de l'alerte **Non-officielle (Administrative/Sociale)**.
- Une frise chronologique détaillée reliant chaque événement à l'âge des victimes (de 7 à 17 ans).

### 2. L'analyse du problème (Le paradoxe asymétrique)
Ce bloc met en lumière une faille asymétrique de l'État :
- **L'hyper-réactivité physique a posteriori :** Dès que le drame est public, l'État déploie une force logistique colossale pour chercher un corps.
- **L'hypo-réactivité informationnelle a priori :** Avant le drame, l'État n'a pas été capable de croiser 6 événements distincts étalés sur 9 ans.

### 3. Ce que cela fonde pour le Projet
- **La justification éthique :** Le projet CGIP vise à rééquilibrer cette asymétrie. Il est plus éthique, moins coûteux, et plus protecteur de déployer de la puissance de calcul (GNN, IA) en prévention pour relier des dossiers informatiques, que de déployer des centaines de gendarmes en réaction dans les forêts.
- **L'exigence de structuration par l'IA :** L'échange montre comment une IA conversationnelle (LLM) parvient très facilement à extraire et lier des entités ("1 victime = 1 affaire", âges, dates) à partir d'articles de presse ou de rapports non structurés. Cela valide techniquement l'idée que la plateforme CGIP devra inclure une couche NLP (Natural Language Processing) pour ingérer et structurer des procès-verbaux textuels massifs.

---

## BLOC 3 : La Structuration en Graphe (Mind Map) et la Désambiguïsation

### 1. La matière brute fournie
Ce troisième échange est une correction et un affinage du précédent.
- L'utilisateur insiste pour que l'IA corrige son tableau afin d'isoler parfaitement les événements "non officiels" souvent oubliés ou écrasés par les événements officiels ultérieurs (ex: l'alerte de 2020 par rapport à la plainte déposée en 2022).
- L'IA génère ensuite une "Carte Mentale" (Mind Map) qui regroupe les événements par "Victime / Dossier" (1 dossier pour l'adolescente de 17 ans, 1 dossier pour la lycéenne, etc.) menant à 6 clusters d'affaires distincts gravitant autour du même suspect.

### 2. L'analyse du problème (Le bruit et la confusion des données)
Ce bloc illustre la difficulté de la "Désambiguïsation". Dans la vraie vie (et dans les bases de données), les affaires s'entremêlent. L'alerte scolaire de 2020 peut être confondue avec les faits de viols de 2020. Sans une structure stricte centrée sur la victime ou le dossier indépendant, le système (humain ou machine) risque de fusionner deux événements distincts à tort, ou de noyer une information mineure sous une procédure majeure.

### 3. Ce que cela fonde pour le Projet
- **Validation du Graphe par l'exemple :** La "Carte Mentale" demandée n'est rien d'autre que l'arbre topologique (le Graphe) que Neo4j va construire dans le logiciel final. Ce passage démontre qu'il est beaucoup plus facile et naturel d'appréhender le risque systémique d'un suspect quand l'information est structurée sous forme de nœuds gravitant autour de lui (réseau de victimes), plutôt que sous forme de liste tabulaire chronologique.

---

## BLOC 4 : Topologie ASCII et Vulnérabilités Systémiques

### 1. La matière brute fournie
Ce quatrième échange franchit un cap analytique majeur. Il contient :
- Une représentation textuelle et conceptuelle (ASCII Art) du réseau criminel présumé, articulé non pas autour des relations entre victimes, mais autour des **contextes de vulnérabilité** (École, Domicile, Espace public) liés au suspect central.
- Une liste formelle de **8 vulnérabilités systémiques** de l'appareil d'État, générée par l'IA en réponse à la chronologie des faits.

**Le Schéma ASCII d'origine :**
```text
                  [ SUSPECT ]
                        │
   ┌────────────────────┼────────────────────┐
   │                    │                    │
[Milieu scolaire]   [Domicile]      [Espace public]
   │                    │                    │
17 ans (2017)      enfant 7 ans        Lyhanna (11 ans)
lycéenne (2020)    enfant 10–11 ans     (disparition 2026)
                   mineure 2026
```

### 2. L'analyse du problème (La dissection de l'échec d'État)
Les 8 points soulevés par l'IA d'origine sont le diagnostic clinique exact de la maladie que la plateforme CGIP doit soigner :
1. **Fragmentation (Silos) :** Police vs École vs Parquet.
2. **Délais (Latence) :** Années entre signalement et enquête.
3. **Seuil de preuve élevé :** Le pénal bloque l'action préventive.
4. **Absence de profil de risque centralisé :** Pas de vision cumulative.
5. **Zone grise institutionnelle :** Licenciements scolaires non judiciarisés.
6. **Sortie des radars (Classement sans suite) :** Pertes de continuité.
7. **Aveuglement temporel :** Traitement "dossier par dossier" au lieu d'une trajectoire.
8. **Tension éthique :** Présomption d'innocence vs Protection.

### 3. Ce que cela fonde pour le Projet (La Roadmap Fonctionnelle)
Ces 8 points ne sont pas juste des constats, ce sont les **Spécifications Fonctionnelles** de la CGIP. 
- Le schéma ASCII prouve que le modèle de données doit reposer sur des nœuds de `Contexte` (Lieu/Institution) autant que sur des Nœuds de `Personne`.
- La tension "Charge de preuve vs Prévention" justifie de manière éclatante l'existence de la **Couche E (Moteur DPIA)** et de la **Couche F (Kill-Switch)** du projet. Le système doit pouvoir évaluer un profil de risque sans pour autant court-circuiter les règles pénales.

---

## BLOC 5 : La Tension Éthique et le Mythe de la "Vue Globale"

### 1. La matière brute fournie
Ce cinquième échange aborde frontalement la question de la responsabilité de la justice et du design de l'appareil d'État.
- L'utilisateur interroge la responsabilité individuelle : *"C'est la faute de la magistrate d'Auch ?"*
- L'IA démontre qu'il ne s'agit pas d'une faute humaine, mais d'une **limite structurelle** (la magistrate n'a pas accès à un fichier centralisé national ni aux alertes scolaires lointaines).
- L'IA décrit ensuite de manière hypothétique ce que serait une "Vue globale centralisée" parfaite.
- Enfin, l'IA dresse la liste des 5 raisons pour lesquelles ce système centralisé n'existe pas en France : Protection des libertés, Risque de fausses corrélations, Fragmentation volontaire (séparation des pouvoirs), RGPD, et la Logique de la justice (qui juge des actes concrets, pas des profils).

### 2. L'analyse du problème (Le "Minority Report" vs l'État de Droit)
Ce bloc pose la plus grande difficulté philosophique et juridique du projet. 
Si on construit la CGIP comme un "Aspirateur Total" qui fusionne tout en un profil permanent de suspicion, on viole frontalement les principes fondamentaux du Droit Européen (Présomption d'innocence, droit à l'oubli). À l'inverse, si on maintient les silos tels quels, des drames se reproduiront à cause de la "fragmentation volontaire".

### 3. Ce que cela fonde pour le Projet
- **L'Équilibre Algorithmique :** Le projet CGIP n'est pas là pour remplacer la justice ou juger sur des probabilités. C'est un outil de **Détection de Signaux Faibles**, pas une machine à condamner.
- **Le Cadre Légal By Design :** Les 5 obstacles soulevés (RGPD, Fausses corrélations...) sont en réalité les "murs porteurs" de l'architecture. La plateforme doit intégrer la protection de la vie privée directement dans ses équations et son code source (*Privacy by Design*).

---

## BLOC 6 : L'Analyse Internationale et le Modèle Machine Learning

### 1. La matière brute fournie
Ce sixième échange est extrêmement riche et clôture l'analyse de l'affaire Lyhanna pour ouvrir sur la Data Science pure. Il contient :
- **Un Benchmark International** : Une comparaison de la gestion des signaux faibles dans 5 pays (UK, Pays-Bas, Danemark, USA, France), montrant que la France a le modèle le plus "segmenté" pour protéger les libertés.
- **Le Schéma des Flux (ASCII)** : Une modélisation de la circulation de l'information en France, illustrant comment une alerte initiale se divise en 3 tuyaux isolés (ASE, Parquet, Fichiers de Police) sans jamais fusionner.
- **La Chronologie ASCII** : Une représentation visuelle du temps de 2017 à 2026, mettant en évidence les incertitudes de l'affaire (la mineure de 2026 est-elle la même que celle de la plainte ?).
- **Le Cadre Machine Learning** : Une proposition technique pointue de 5 algorithmes d'IA (Scoring, Anomaly Detection, Analyse Temporelle, Graphe, Entity Resolution) pour traiter ce type de données.

**La Chronologie d'origine (simplifiée) :**
```text
2017 ─ ⚠️ Signalement (Adolescente 17 ans) → Classé sans suite (2018)
2020 ─ ⚠️ Alerte scolaire (Lycéenne) → Licenciement
       └─ 👧 Faits allégués (Enfant de 7 ans) au domicile
2022 ─ ⚖️ Dépôt de plainte (Enfant de 7 ans, faits 2020) → Enquête
2024 ─ 👧 Faits allégués (Enfant ~10-11 ans) → Plainte Août 2025
2026 ─ ⚠️ Signalement éducatif (Mineure)
       ├─ ⚖️ Nouvelle plainte (Mineure) lors d'une soirée
       └─ 🚨 Disparition de Lyhanna (11 ans)
```

### 2. L'analyse du problème (La Finalité de l'IA)
Ce bloc pose une ligne rouge fondamentale pour le projet : la CGIP ne doit **jamais** faire de "justice prédictive" algorithmique (prédire qu'un homme va commettre un crime). Son rôle est strictement de faire de la **Fusion d'Information** pour émettre une alerte très précise : *"REVUE HUMAINE RECOMMANDÉE"*. L'humain (le magistrat) garde toujours le monopole de la décision.

### 3. Ce que cela fonde pour le Projet
- Sur le plan conceptuel, la CGIP se positionne exactement dans l'espace vide laissé par le modèle français. Elle veut apporter la puissance d'analyse centralisée du modèle Britannique (PNC / CP-IS) tout en gardant les garanties constitutionnelles françaises.
- Les 5 catégories d'algorithmes proposés par l'IA d'origine sont les spécifications exactes de la **Couche B** (Entity Resolution) et de la **Couche G** (Scoring de Risque) du projet.

---

## BLOC 7 : Algorithmes Temporels, Benchmark Réel et Biais du Rétroviseur

### 1. La matière brute fournie
Ce septième échange aborde directement l'implémentation algorithmique de la frise chronologique 2017-2026 et explore les précédents internationaux. Il contient :
- **Un choix technologique algorithmique** : Pour analyser cette frise, l'IA propose une combinaison de : Entity Resolution + Analyse Graphe + Processus de Hawkes / Survival Analysis + Scoring supervisé.
- **Le Benchmark "AFST" (Allegheny Family Screening Tool)** : Une référence réelle d'un système de *Predictive Risk Modeling (PRM)* déployé en Pennsylvanie, qui consolide des centaines de variables administratives pour assister les services sociaux.
- **La mise en garde sur les Biais Algorithmiques** : Le risque majeur que l'IA ne fasse que reproduire les discriminations systémiques (sur-surveillance de certaines populations).
- **Le "Biais du Rétroviseur" (Hindsight Bias)** : L'illusion psychologique consistant à croire que "tout était évident" *après* le drame, alors qu'au moment T, les événements semblaient banals ou décorrélés.

### 2. L'analyse du problème (Prédiction vs Fusion)
Ce bloc rappelle une vérité juridique implacable : "Signalement ≠ preuve", "Plainte ≠ condamnation". La plateforme ne doit donc pas baser son fonctionnement sur le postulat que le suspect est coupable. Elle doit baser son fonctionnement sur l'identification d'une vulnérabilité systémique ("plusieurs événements concernant des mineurs sur plusieurs années"). 

Le grand danger d'un outil comme l'AFST est le profilage (predictive policing). L'État français s'y refuse formellement.

### 3. Ce que cela fonde pour le Projet
- **Validation du socle algorithmique** : L'enchaînement `Entity Resolution -> Graph Database -> Hawkes Process -> Alerte` proposé dans l'échange est devenu l'ossature technique formelle de la CGIP. 
- **La ligne rouge du Biais du Rétroviseur** : La CGIP ne cherche pas à deviner l'avenir avec certitude. Son rôle est de corriger le biais du rétroviseur en fournissant à l'enquêteur, *en temps réel*, la vue d'ensemble qu'il n'aurait eue qu'au tribunal, des années plus tard.
- **La nature de l'Alerte** : Le système ne doit générer qu'une seule recommandation : `REVUE HUMAINE RECOMMANDÉE`. Jamais un score de "culpabilité".

---

## BLOC 8 : Le Paradoxe SALVAC/ViCLAS et le Labyrinthe des Fichiers

### 1. La matière brute fournie
Ce huitième échange décortique l'écosystème réel des fichiers de police et de justice en France et à l'international, en se basant sur des articles de presse et des sources gouvernementales (Service Public, Ministère de l'Intérieur, Police Belge) :
- **La distinction Cassiopée / FIJAISV** : Cassiopée stocke les procédures. Le FIJAISV stocke les condamnations. Un suspect avec 5 plaintes non jugées n'est pas dans le FIJAISV.
- **La découverte de ViCLAS / SALVAC** : Le Système d'Analyse des Liens de la Violence Associée aux Crimes (SALVAC en France) fait exactement ce que la CGIP propose : chercher le "pattern" d'un tueur en série en modélisant son comportement (156 items d'analyse). 
- **La réalité opérationnelle de SALVAC** : C'est un outil formidable, mais géré manuellement par 7 analystes pour toute la France, et réservé aux crimes violents "sans mobile" déjà qualifiés.

### 2. L'analyse du problème (La Super-Fragmentation)
Ce bloc révèle la cause profonde du dysfonctionnement de l'État dans l'affaire Lyhanna. Le problème n'est pas le manque d'outils, c'est leur sur-spécialisation en silos :
- `CASSIOPÉE` = Gestion judiciaire pure.
- `TAJ` = Antécédents de police.
- `FIJAISV` = Registre post-condamnation.
- `SALVAC` = Analyse des crimes en série déjà identifiés.
- `Aide Sociale / École` = Alertes administratives locales (hors radar pénal).

Dans le cas de Lyhanna, le suspect naviguait sous le radar de SALVAC (car il n'y avait pas de meurtres en série avérés au départ) et hors du FIJAISV (aucune condamnation). Les signaux faibles (école) ne sont jamais remontés dans ces super-calculateurs.

### 3. Ce que cela fonde pour le Projet
- **Positionnement de la CGIP** : La plateforme n'est pas conçue pour remplacer Cassiopée ou SALVAC. La CGIP est la **Couche de Fusion (Data Mesh)** qui se pose au-dessus de ces silos. 
- **Différentiel Technologique** : Là où SALVAC requiert 7 analystes humains remplissant manuellement 156 items, la CGIP propose une ingestion NLP automatisée et un Graphe probabiliste capable de traiter la masse (les petits signalements) pour déclencher l'alerte *avant* que l'affaire ne relève de SALVAC.

---

## BLOC 9 : Le Benchmark International et la Couche "Civil Tech"

### 1. La matière brute fournie
Ce neuvième échange oppose deux extrêmes du spectre analytique :
- **L'hyper-spécialisation policière (Top-Down)** : SALVAC (France) et ViCLAS (Canada/Belgique) qui cherchent la *similarité criminelle* (Affaire A = Affaire B) sur des meurtres ou viols déjà actés.
- **La Civil Tech (Bottom-Up)** : L'émergence d'applications labellisées par l'État pour protéger et écouter les victimes dès les premiers signaux faibles : *App-Elles*, *UMAY*, *Ti3rs* (messagerie sécurisée anti-injures), et *Mémo de Vie* (coffre-fort numérique de preuves).

### 2. L'analyse du problème (La Déconnexion)
Le débat soulève une vérité cruelle :
- La police a des outils ultra-puissants (SALVAC) mais qui démarrent "trop tard" (après le crime grave).
- Les victimes ont des outils modernes (Mémo de Vie) pour accumuler des signaux faibles (harcèlement, menaces).
- Mais il n'y a **aucun pont** entre la victime qui stocke ses preuves dans *Mémo de Vie* et le système *Cassiopée* du juge.

### 3. Ce que cela fonde pour le Projet
- **Création du Benchmark** : La formalisation d'un document dédié (`BENCHMARK_INTERNATIONAL.md`) pour prouver, exemples étrangers à l'appui, que l'approche "Silo" a atteint ses limites.
- **La Couche Zéro (Civil Tech)** : La CGIP doit prévoir des connecteurs API (avec le consentement de la victime) pour ingérer les données structurées de ces applications civiles, fusionnant ainsi le "Bottom-Up" (la rumeur, la plainte naissante) et le "Top-Down" (la procédure pénale).

---

## BLOC 10 : L'Architecture en 5 couches (CGIP)

### 1. La matière brute fournie
Ce dixième échange propose la synthèse absolue du projet sous la forme d'une architecture informatique idéale en 5 couches. Il définit ces strates technologiques pour la CGIP :
1. Data Ingestion Layer
2. Identity Resolution Layer
3. Justice Knowledge Graph
4. ML Risk Engine & Investigation AI
5. Human Decision Layer

### 2. L'analyse du problème (Logique de Dossier vs Logique d'Individu)
Le texte met le doigt sur le point de rupture conceptuel des systèmes actuels : ils fonctionnent en "logique de dossier". La CGIP, au travers de son *Identity Resolution Layer*, force le passage à une "logique d'individu dans le système". Le but n'est pas de créer une "IA Juge", mais une "IA de Coordination" qui pallie la surcharge cognitive des magistrats.

### 3. Ce que cela fonde pour le Projet
- **Refonte Architecturale** : Le projet adopte officiellement cette architecture en 5 couches comme standard de développement.
- **Gouvernance Humaine (Human-in-the-loop)** : L'IA ne décide jamais. Le *Human Decision Layer* devient une spécification technique opposable (nécessité de XAI - Explainable AI).

---

## BLOC 11 : Les 8 Points de Rupture (Le Continuum Informationnel)

### 1. La matière brute fournie
Ce onzième échange cartographie le flux exact de l'information (École → Police → Justice) et identifie 8 "Casses" (points de rupture) qui expliquent pourquoi l'État échoue à détecter les trajectoires criminelles avant le drame.

### 2. L'analyse du problème (La Séparation des Logiques)
L'analyse montre que le système n'est pas "buggé", il est conçu par design comme une succession de logiques étanches :
- L'École = Logique éducative (signal faible, texte libre)
- La Police = Logique opérationnelle (centrée sur l'affaire locale)
- La Justice = Logique procédurale (Cassiopée, juridique, fermée)

**Le point critique (CASSE #5)** : L'information circule mal de bas en haut, mais elle ne redescend **jamais** (aucune boucle de retour vers l'école ou la police locale).
**Le paradoxe éthique** : Ce morcellement protège les libertés individuelles et empêche la surveillance de masse. La CGIP doit donc résoudre la fragmentation sans devenir "Big Brother".

### 3. Ce que cela fonde pour le Projet
- **La Boucle de Retour (Alerting)** : La CGIP ne doit pas être qu'un aspirateur à données. Elle doit techniquement prévoir un mécanisme de redistribution des alertes vers les émetteurs de signaux faibles (si le seuil juridique le permet).
- **Le Parsing NLP des Signaux Faibles** : (Casse #1) La machine doit être capable d'ingérer du texte libre non standardisé (rapports d'infirmières, mots dans le carnet).

---

## BLOC 12 : L'Éthique Algorithmique et le Modèle ML Réaliste

### 1. La matière brute fournie
Ce douzième échange formalise techniquement la nature du moteur d'IA de la CGIP. Il livre un modèle concret de *Machine Learning* pour la justice avec :
- **L'objectif ML (La variable $y$)** : Le système ne cherche pas à prédire "un crime futur", mais estime la probabilité ($y=1$) qu'une trajectoire administrative subisse une escalade grave dans les 12 mois.
- **La structure du Dataset** : Une matrice `person_event_window` regroupant les signaux temporels, comportementaux, géographiques et les relations de graphe (centralité).
- **Le choix des algorithmes** : Gradient Boosting (XGBoost) en base robuste, et GNN (Graph Neural Networks) en version State-of-the-Art.
- **L'impératif XAI (Explainable AI)** : L'utilisation des valeurs SHAP pour justifier chaque score.

### 2. L'analyse du problème (Science-Fiction vs Réalisme Judiciaire)
Ce bloc tranche un débat philosophique majeur : l'État ne peut pas déployer un système de type "Minority Report" (Boîte noire affirmant "Cet individu est dangereux"). Le modèle ML de la CGIP est un outil purement statistique et administratif.
L'alerte générée par le modèle ne dit pas une vérité morale, elle dit : *"Attention, cette chronologie rassemble toutes les caractéristiques statistiques d'une trajectoire qui dégénère"*.

Les limites soulevées sont les vrais murs porteurs juridiques :
- **Biais de signalement** (sur-représentation de certains profils liés au *sur-policing*).
- **Corrélation $\neq$ Causalité**.
- **Respect de la Présomption d'Innocence**.

### 3. Ce que cela fonde pour le Projet
- **La Couche d'Explicabilité (SHAP)** : Il est formellement interdit de concevoir l'interface utilisateur (Dashboard) sans y intégrer les valeurs SHAP (ex: `+0.31 → fréquence événements`). Le magistrat *doit* voir ce qui a déclenché l'alerte pour pouvoir l'invalider.
- **Le Dataset Synthétique** : La prochaine étape technique de développement sera de générer un dataset synthétique `person_event_window.csv` respectant cette taxonomie pour entraîner notre premier modèle Baseline (XGBoost).
