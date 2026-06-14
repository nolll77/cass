# SOCLE FORMEL (Lexique Pur)

**RÈGLE D'ARBITRAGE :** Domaine exclusif de "L'Abstraction Absolue". La moelle technique du flux narratif.
Applique le Standard des 9 Tags (Le DAG d'Ingénierie Ultime).

## Éléments Techniques Extraits

### 1. Constitution d'un Dataset par Text & Data Mining (TDM) OSINT
1. **Quoi :** Pipeline d'extraction et de structuration d'entités nommées (NER) à partir d'articles de presse et de registres publics.
2. **Pourquoi :** Le système judiciaire (Cassiopée) étant fermé, la seule méthode pour objectiver les failles (récidives, plaintes multiples) est de reconstruire les liens via l'OSINT (Open Source Intelligence).
3. **Inputs :** Corpus de textes non structurés (articles web BFM, Figaro, rapports publics).
4. **Outputs :** Table relationnelle stricte : `[Entité_ID] -> [Date] -> [Type_Signalement/Plainte] -> [Statut_Judiciaire]`.
5. **Dépendance Amont :** Scraping légal et parsers de texte.
6. **Dépendance Aval :** Modèle de graphes pour identifier les clusters de récidive.
7. **Complexité Algorithmique :** *Loi de la désambiguïsation.* Au-delà de quelques centaines d'articles, le système ne pourra plus faire la différence entre deux "Jérôme B." homonymes. Le coût de calcul explosera pour déterminer si deux faits divers parlent du même individu ou non.
8. **Contraintes & Hypothèses :** *Le mur de l'anonymisation.* Les médias modifient les prénoms (ex: Rosa*) ou cachent les noms de famille (Jérôme B.). L'algorithme devra croiser des données géographiques (ex: Fleurance, Gers) et temporelles (ex: licencié en 2020) pour forcer la jonction d'identité, au risque de créer des faux positifs.
9. **Limites / Biais (Edge Cases) :** *Le biais du "Fait Divers Sanglant".* La base de données ne reflètera jamais la réalité des violences, car elle ne capte que le "bruit médiatique" (les cas extrêmes). Les milliers de plaintes classées sans suite qui ne finissent pas en drame seront invisibles à l'algorithme.

### 2. Modélisation Topologique des Failles Institutionnelles (Latence Cumulative)
1. **Quoi :** Graphe bipartite mesurant la distance et le temps de transmission entre les "Signaux" (Plaintes/Alertes) et les "Silos Institutionnels" (Éducation, Justice, Social).
2. **Pourquoi :** Démontrer mathématiquement que la lenteur et la déperdition d'information ne sont pas des erreurs humaines, mais des propriétés structurelles du système (absence de profil global de risque).
3. **Inputs :** Chronologies d'affaires pénales (Dates de signalements, classements, réouvertures).
4. **Outputs :** Métrique de "Latence Cumulative" et identification des "Nœuds Morts" (là où l'alerte s'arrête).
5. **Dépendance Amont :** Séquençage temporel strict des dossiers judiciaires de la presse.
6. **Dépendance Aval :** Simulation de "Profils de Risque Cumulatif".
7. **Complexité Algorithmique :** *La fragmentation de la clé primaire.* Sans identifiant unique partagé entre l'Éducation Nationale et la Justice, la réconciliation informatique d'un comportement scolaire suspect avec une plainte pénale s'apparente à une complexité quadratique coûteuse (O(N²)).
8. **Contraintes & Hypothèses :** *Le mur du secret professionnel et la zone grise.* L'outil ne verra pas ce qui ne passe pas le seuil judiciaire. Des signaux forts (licenciement administratif) n'ont pas de traduction pénale automatique, créant des trous noirs dans la donnée.
9. **Limites / Biais (Edge Cases) :** *Le faux négatif par "classement sans suite".* Lorsqu'une affaire est classée faute de preuves immédiates, le système institutionnel remet le compteur de risque à zéro. L'algorithme devra forcer la "mémoire" de ces signaux pour identifier la vraie dynamique de récidive.

### 3. Entity Resolution & Predictive Risk Modeling (La Fusion des Signaux)
1. **Quoi :** Pipeline algorithmique combinant la résolution d'entités (Entity Resolution) et l'analyse de graphes pour lier des événements historiques dispersés et générer une alerte de "Revue Humaine".
2. **Pourquoi :** Le système (Cassiopée) étant conçu pour la procédure (dossier par dossier) et non pour le profilage, il faut une surcouche analytique pour fusionner les "bouts de puzzle" en un réseau relationnel.
3. **Inputs :** Événements bruts non reliés (Alerte scolaire 2020, Plainte 2022, Signalement 2026).
4. **Outputs :** "Score de Risque Cumulatif" (Trigger event) déclenchant une "Revue Humaine Prioritaire", sans inférence de culpabilité ni jugement moral.
5. **Dépendance Amont :** Désambiguïsation réussie des entités (TDM OSINT) et modélisation topologique (Latence).
6. **Dépendance Aval :** Visualisation chronologique des clusters de récurrence.
7. **Complexité Algorithmique :** *L'Explosion Combinatoire.* Sans ID unique national, chaque nouvel événement (ou article de presse) doit être comparé à l'intégralité de la base avec des modèles probabilistes spatio-temporels. 
8. **Contraintes & Hypothèses :** *Le biais du rétroviseur (Hindsight Bias).* L'algorithme doit être construit pour tourner en "temps simulé" (step-by-step), l'empêchant d'utiliser la connaissance du drame final pour justifier le regroupement des signaux faibles passés.
9. **Limites / Biais (Edge Cases) :** *La reproduction des biais sociaux.* (Leçon du *Allegheny Family Screening Tool*) : Si historiquement un groupe ou une population fait l'objet de plus de signalements administratifs, l'algorithme sur-ciblera ce groupe de manière auto-réalisatrice, créant de l'injustice systémique.

### 4. Justice Knowledge Graph & Architecture JOS (Le Graphe Global)
1. **Quoi :** Modélisation théorique d'un "Justice Operating System" (JOS) reposant sur une architecture Big Data : Ingestion (Kafka) -> Federated Data Lake -> Data Access Layer RGPD -> Graph DB (Neo4j) -> ML Layer (GraphSAGE/GAT). Contrairement au système Palantir américain (fusion massive), il s'agit d'un **graphe fédéré** cloisonné par finalité.
2. **Pourquoi :** Démontrer mathématiquement et architecturalement la différence entre une base de données relationnelle "par dossier" (Cassiopée) et une base orientée graphe (Neo4j) capable de résoudre nativement la fragmentation via *Link Prediction*.
3. **Inputs :** Données hétérogènes multi-sources modélisées dans une table SQL `Event` universelle (École, Police, Justice, Apps de prévention).
4. **Outputs :** Graphe unifié permettant aux modèles de Graph Neural Networks (GNN) de calculer un `Link_Score` pour relier des affaires.
5. **Formulation Mathématique (Message Passing GNN) :** L'embedding d'un dossier $v$ à l'étape $k$ s'écrit $h_v^{(k)} = \sigma \left( W \cdot \text{AGG}({h_u^{(k-1)} : u \in N(v)}) \right)$.
6. **Link Prediction :** Le but n'est pas de prédire un crime, mais de relier des dossiers isolés. $P(Case_i \leftrightarrow Case_j | graph) = \sigma(emb_i \cdot emb_j)$.
7. **L'IA des Trajectoires (Temporal GNN - TGN) :** Pour modéliser la chronologie et l'accélération des événements, le graphe statique est insuffisant. Le système doit basculer sur un graphe dynamique intégrant le temps : *Event stream → dynamic graph → evolving embeddings*.
8. **Complexité Algorithmique :** *L'Explosion des Features.* Le modèle nécessite le calcul dynamique de features temporelles (accélération des incidents, `time_decay_score = exp(-Δt)`), comportementales (répétition du même type de victime) et réseau (centralité de degré).
9. **Contraintes & Hypothèses (Le Rule Engine et les Zones IA) :** Le modèle intègre une couche de contraintes juridiques stricte basée sur la législation européenne (RGPD, CNIL, AI Act). L'IA est sectorisée :
   - **Zone 1 (Safe) :** Nettoyage, Entity Resolution, extraction NLP (Autorisé).
   - **Zone 2 (Gris Clair) :** Link Prediction (GNN) avec validation humaine et sous-graphe explicatif obligatoire (Toléré sous conditions).
   - **Zone 3 (Interdite) :** Décision automatisée (Art. 22 RGPD) et profilage prédictif individuel (Bloqué par le *Data Access Layer*).
   Le système européen doit *détecter des situations*, et non *prédire des individus*.

### Modèle de Tagging
Pour chaque nouvel élément technique :
1. **Quoi :**
2. **Pourquoi :**
3. **Inputs :**
4. **Outputs :**
5. **Dépendance Amont :**
6. **Dépendance Aval :**
7. **Complexité Algorithmique :** [Ancrage Terrain]
8. **Contraintes & Hypothèses :** [Vulgarisation Métier]
9. **Limites / Biais (Edge Cases) :** [Angles morts de la vraie vie]
