# Socle Mathématique et Algorithmique (Formulaire CGIP)

> **GUIDE DE CONSTRUCTION (MANIFESTE DU SOCLE)**
> 
> **Qu'est-ce qu'un Socle (ou Lexique Formel) ?**
> C'est le référentiel absolu et purgé de tout bruit narratif. Il extrait, nettoie et standardise la "moelle technique", mathématique ou algorithmique du projet CGIP pour la rendre exploitable par des machines (code) ou des pairs (ingénieurs, magistrats).
> 
> **Le Standard des 9 Tags (Le DAG d'Ingénierie Ultime) :**
> Chaque algorithme de la CGIP est lu et implémenté comme une fonction autonome sécurisée grâce à 9 clés :
> 1. **Quoi :** La définition mécanique (ce que la formule calcule).
> 2. **Pourquoi :** L'objectif institutionnel ou judiciaire (à quoi ça sert dans le système).
> 3. **Inputs (Entrées) :** Les données brutes (événements, scores).
> 4. **Outputs (Sorties) :** Le format mathématique du résultat retourné.
> 5. **Dépendance Amont :** Quelle autre formule doit obligatoirement être calculée *avant*.
> 6. **Dépendance Aval :** Quelle(s) formule(s) utiliseront ce résultat *après*.
> 7. **Complexité Algorithmique :** Ordre de grandeur informatique (Big O).
> 8. **Contraintes & Hypothèses (Assumptions) :** Postulats traduits dans le strict contexte de la Police et de la Justice.
> 9. **Limites / Biais (Edge Cases) :** Les cas réels où la formule "craque" ou devient absurde.

---

## 1. Gouvernance et Privacy by Design

### Time Decay Function (Droit à l'oubli algorithmique)
**Formule :**
$$
\Huge C(t) = C_0 \cdot e^{-\lambda \cdot \Delta t}
$$
*   **Quoi :** Décroissance exponentielle du poids d'une relation (Edge) dans le graphe.
*   **Légende :** $C(t)$ : Confidence Score actuel, $C_0$ : Poids initial brut de l'événement (ex: 0.4 pour un signalement école), $\lambda$ : coefficient de demi-vie légale, $\Delta t$ : temps écoulé depuis l'événement.
*   **Pourquoi :** Encoder la prescription légale et le droit à l'oubli dans les mathématiques. Un incident mineur vieux de 10 ans sans récidive doit disparaître des radars pour protéger la vie privée.
*   **Inputs :** Timestamp de l'événement, Timestamp actuel, Poids légal brut $C_0$.
*   **Outputs :** Scalaire positif $\in [0, 1]$ représentant la force résiduelle de la preuve.
*   **Dépendance Amont :** Le Moteur de Confiance (Confidence Engine).
*   **Dépendance Aval :** Agrégation de Risque, Processus de Hawkes.
*   **Complexité Algorithmique :** O(1) — Une multiplication instantanée.
*   **Contraintes & Hypothèses (Assumptions) :** Le risque de récidive à risque d'un individu s'évapore mécaniquement et prévisiblement avec le temps s'il ne fait pas de nouvelles vagues dans le système institutionnel.
*   **Limites / Biais (Edge Cases) :** Si un agresseur part vivre à l'étranger pendant 10 ans (donc zéro signalement en France), le système va mathématiquement effacer son passif. À son retour, il sera vu à tort par la machine comme un profil totalement vierge et inoffensif.

### Le Kill-Switch RGPD (DPIA Constraint)
**Formule :**
$$
\Huge K(R) = \begin{cases} 1 & \text{si } \sum w_i R_i < \theta_{legal} \\ 0 & \text{sinon (Block)} \end{cases}
$$
*   **Quoi :** Fonction indicatrice (Gate) qui coupe l'exécution d'un thread Python.
*   **Légende :** $K(R)$ : Interrupteur, $R_i$ : métriques de risque RGPD (automatisation, données mineurs, volume), $\theta_{legal}$ : plafond légal d'intrusion autorisé.
*   **Pourquoi :** C'est le verrou de l'IA Constitutionnelle. Interdire physiquement au serveur de croiser des données si la requête du policier glisse vers un profilage de masse illégal ("Minority Report").
*   **Inputs :** Métadonnées de la requête en cours (Quels types de nœuds sont interrogés ? Y a-t-il des mineurs impliqués ?).
*   **Outputs :** Binaire (0 = Erreur système forcée, 1 = Poursuite de l'inférence).
*   **Dépendance Amont :** Moteur GNN.
*   **Dépendance Aval :** Interface utilisateur (Affichage du graphe ou Écran Rouge d'interdiction).
*   **Complexité Algorithmique :** O(1) — Vérification booléenne pure.
*   **Contraintes & Hypothèses (Assumptions) :** La délicate balance entre le respect de la vie privée et la nécessité d'une enquête policière peut être résumée par un simple score arithmétique rigide.
*   **Limites / Biais (Edge Cases) :** En cas de disparition d'enfant avec urgence vitale extrême (Alerte Enlèvement), si le plafond légal est codé de manière trop stricte, l'algorithme paralysera l'ordinateur du magistrat, l'empêchant techniquement de trouver le ravisseur.

---

## 2. Inférence Spatiale et Temporelle

### Entity Resolution (Distance de Jaro-Winkler)
**Formule :**
$$
\Huge d_{jw} = d_j + (\ell \cdot p \cdot (1 - d_j))
$$
*   **Quoi :** Mesure de similarité textuelle favorisant les chaînes qui commencent par les mêmes caractères.
*   **Légende :** $d_{jw}$ : Score final, $d_j$ : distance de Jaro basique, $\ell$ : longueur du préfixe commun, $p$ : constante de pondération.
*   **Pourquoi :** Briser la faille des silos administratifs : la machine doit comprendre que le dossier "Jérôme B." tapé à la gendarmerie et la fiche "J. B." mal orthographiée par le directeur de l'école concernent exactement la même personne.
*   **Inputs :** Strings (chaînes de caractères hachées partelles, noms, adresses).
*   **Outputs :** Probabilité de fusion $\in [0, 1]$.
*   **Dépendance Amont :** Base de données Neo4j brutes.
*   **Dépendance Aval :** Création d'une arête `IS_SAME_PERSON` dans le graphe.
*   **Complexité Algorithmique :** O(|s1| * |s2|) — Simple et efficace.
*   **Contraintes & Hypothèses (Assumptions) :** Les erreurs de saisie des fonctionnaires de police ou d'éducation suivent des règles de fautes de frappe ou d'abréviations (typo) logiques et prévisibles.
*   **Limites / Biais (Edge Cases) :** Impuissant face aux homonymes parfaits : si un "Martin Dubois" habite à Montestruc-sur-Gers, et qu'un autre "Martin Dubois" (sans aucun lien) habite dans la ville d'à côté, le système va fusionner leurs vies pénales et ruiner la réputation de l'un des deux.

### Processus de Hawkes (Détection de l'Escalade)
**Formule :**
$$
\Huge \lambda(t) = \mu + \sum_{t_i < t} \alpha \cdot e^{-\beta(t - t_i)}
$$
*   **Quoi :** Modèle de processus ponctuel auto-excitant mesurant l'intensité temporelle d'événements stochastiques.
*   **Légende :** $\lambda(t)$ : Taux de dangerosité à l'instant $t$, $\mu$ : bruit de fond (hasard), $t_i$ : timestamp des faits passés, $\alpha$ : saut d'intensité à chaque fait, $\beta$ : vitesse de retombée de l'urgence.
*   **Pourquoi :** Capter mathématiquement la "vélocité" à risque. Trois signalements administratifs en 10 ans, c'est du bruit. Trois signalements en 6 mois, c'est une escalade (effet de réplique sismique) qui précède un drame.
*   **Inputs :** Vecteur des dates (timestamps) des incidents liés au suspect.
*   **Outputs :** Score d'escalade (scalaire dynamique).
*   **Dépendance Amont :** Entity Resolution (pour lier les faits à une seule personne).
*   **Dépendance Aval :** Moteur d'Alerte Globale.
*   **Complexité Algorithmique :** O(E²) — E étant le nombre d'événements pour une personne, le calcul est quasi instantané.
*   **Contraintes & Hypothèses (Assumptions) :** Le passage à l'acte d'un prédateur agit comme un tremblement de terre : chaque agression augmente mécaniquement l'excitation de l'individu et provoque des répliques de plus en plus rapprochées dans le temps.
*   **Limites / Biais (Edge Cases) :** Un agresseur très intelligent, froid et méthodique, qui s'oblige de manière psychopathe à agir seulement une fois tous les 5 ans de manière métronomique, aura un score d'escalade de 0 et sera totalement invisible pour cette formule.

---

## 3. Graphes Causaux et Topologie

### Graph Neural Network (Link Prediction)
**Formule :**
$$
\Huge \hat{y}_{u,v} = \sigma(\mathbf{z}_u^T \mathbf{z}_v) \quad \text{avec} \quad \mathbf{Z} = GNN(\mathbf{A}, \mathbf{X})
$$
*   **Quoi :** Calcul de la probabilité de l'existence d'une arête (lien) entre deux nœuds en effectuant un produit scalaire sur leurs vecteurs latents générés par un réseau de neurones sur graphe.
*   **Légende :** $\hat{y}_{u,v}$ : probabilité d'un lien caché entre personne $u$ et événement $v$, $\mathbf{z}$ : vecteur latent (embedding), $\mathbf{A}$ : topologie du graphe (adjacence), $\mathbf{X}$ : traits connus.
*   **Pourquoi :** Révéler le "chaînon manquant" et automatiser l'analyse sérielle. Le GNN remplace mathématiquement et instantanément les "156 items d'analyse manuelle" du système SALVAC en trouvant des similarités de Modus Operandi (Lieux, Heures, Cibles) enfouies dans la topologie.
*   **Inputs :** Matrice d'adjacence globale (Les écoles, les adresses, les victimes), Matrice des poids du Time Decay.
*   **Outputs :** Probabilité $P_{link} \in [0, 1]$ (Score latent de sérialité).
*   **Dépendance Amont :** Base complète Neo4j, Entity Resolution.
*   **Dépendance Aval :** Inférence Causale (DoWhy).
*   **Complexité Algorithmique :** O(V + E) en inférence par couche — Très rapide pour interroger la base, mais l'entraînement préalable du modèle sur les serveurs nécessite de gros GPUs.
*   **Contraintes & Hypothèses (Assumptions) :** Si la personne A et la personne B fréquentent exactement le même réseau de lieux sociaux toxiques, au même moment, avec les mêmes modes opératoires (patterns), elles partagent la même sphère de risque.
*   **Limites / Biais (Edge Cases) :** Le danger absolu de la corrélation illusoire : l'algorithme va relier artificiellement un plombier innocent à un réseau à risque uniquement parce qu'il a été embauché pour réparer l'évier du collège à l'heure exacte d'une agression dans la cour.

### Inférence Causale (Backdoor Criterion - DoWhy)
**Formule :**
$$
\Huge P(Y \mid do(X)) = \sum_Z P(Y \mid X, Z) P(Z)
$$
*   **Quoi :** Isoler l'effet causal pur d'une variable $X$ sur $Y$ en bloquant mathématiquement toutes les autres portes de corrélation fallacieuses $Z$ (confounders).
*   **Légende :** $do(X)$ : forcer mathématiquement la survenue de la cause, $Z$ : variables de confusion bloquant le chemin 'Backdoor'.
*   **Pourquoi :** Agir comme le cerveau logique du magistrat. C'est l'antidote à l'erreur du plombier (Limites du GNN). L'algorithme doit prouver que la topologie causale (qui est là, qui fait quoi) valide l'alerte, et non pas une simple coïncidence de lieu.
*   **Inputs :** Le DAG (Graphe Orienté Acyclique) des règles judiciaires, La probabilité issue du GNN.
*   **Outputs :** Validation ou invalidation booléenne de la prédiction GNN.
*   **Dépendance Amont :** GNN (Link Prediction).
*   **Dépendance Aval :** L'Alerte "REVUE HUMAINE RECOMMANDÉE".
*   **Complexité Algorithmique :** O(V + E) — Parcours de graphe pour trouver les chemins bloqués (ultra-rapide).
*   **Contraintes & Hypothèses (Assumptions) :** Le comité d'éthique et les enquêteurs qui ont dessiné à la main les règles du DAG ont réussi l'exploit intellectuel de lister absolument TOUTES les variables de la vie réelle pouvant créer une fausse coïncidence.
*   **Limites / Biais (Edge Cases) :** S'il manque une seule petite variable clé non-renseignée (ex: "le suspect a un frère jumeau"), le modèle causal sera aveugle, la formule validera la corrélation toxique, et le plombier finira en garde à vue.

---

## 4. Modélisation du Risque et Alerting

### 4.1. Extraction des Features (Feature Engineering)
Avant le scoring, le pipeline extrait trois types de dimensions du flux Kafka :
*   **Temporelles :** nb événements 30j/90j, accélération des événements, intervalle moyen entre incidents.
*   **Sociales (Graph) :** Degree centrality, nb de connexions multi-institutions, clusters suspects.
*   **Comportementales :** Répétition du type d’événements, escalade de gravité, multi-sources concordantes.

### 4.2. Score de Risque Temps Réel (Event-Driven)
**Formule :**
$$
\Huge S_{risk} = 0.35 \cdot R_{temp} + 0.30 \cdot R_{graph} + 0.20 \cdot W_{trend} + 0.15 \cdot S_{cross}
$$
*   **Quoi :** Addition linéaire pondérée de 4 macro-features calculées à la volée.
*   **Légende :** $S_{risk}$ : Score total. $R_{temp}$ : Risque Temporel (accélération). $R_{graph}$ : Risque Topologique (centralité/connexions). $W_{trend}$ : Escalade de la gravité (Severity Trend). $S_{cross}$ : Signaux multi-sources (Cross-source signals : École + Police).
*   **Pourquoi :** Éviter l'effet "boîte noire" d'un réseau de neurones pur. Fournir au magistrat un calcul mathématique décryptable (SHAP).
*   **Avertissement Légal (Axiome RGPD) :** Ce score de risque évalue une **Situation** (un `[Event]` ou un `[ContextNode]`), il n'évalue **JAMAIS un Individu** (`[Person]`). Profiler pénalement un individu via un algorithme est illégal en Europe (Zone Rouge).
*   **Outputs :** Un score continu qui détermine le niveau d'alerte.
    *   $S_{risk} > 0.85$ : 🔴 NIVEAU ROUGE (Urgence Magistrat).
    *   $S_{risk} > 0.65$ : 🟠 NIVEAU ORANGE (Surveillance Humaine).
    *   $S_{risk} \le 0.65$ : 🟢 NIVEAU VERT (Passif).
*   **Dépendance Amont :** Processus de Hawkes, Inférence Causale.
*   **Dépendance Aval :** Interface Dashboard (Notification à l'utilisateur final).
*   **Complexité Algorithmique :** O(N) — Simple somme, calcul immédiat.

---

## 5. Le Système ML de Détection de Signaux Faibles (Deep Dive)

Conformément au Bloc 18, voici l'ingénierie précise des "Features" (caractéristiques mathématiques) extraites du Data Lake et du Graph pour alimenter le moteur ML. L'objectif de ce modèle n'est pas de dire "X est coupable", mais de répondre à la question probabiliste : **"Quelle est la probabilité que cette trajectoire d'événements mineurs débouche sur un événement grave (Sévérité > 8) dans les 6 prochains mois ?"**

### 5.1. Le Feature Engineering (L'Art de quantifier le comportement)

Le pipeline calcule un vecteur de 12 dimensions pour chaque Nœud Personne `[P]` sur des fenêtres glissantes ($t_{30}$, $t_{90}$, $t_{365}$ jours).

#### 🟡 Catégorie A : Les Features Temporelles (Le Rythme)
Ces variables mesurent l'accélération (Modèle de Hawkes).
1. `event_frequency_90d` : Nombre total d'événements (toutes sources confondues) dans les 90 derniers jours.
2. `days_since_last_event` : Temps écoulé depuis le dernier signal. Plus il est court, plus la chaleur est forte.
3. `escalation_slope` : La dérivée (pente) de la gravité des événements. Si l'individu passe d'une bagarre (gravité 2) à un port d'arme (gravité 6), la pente est fortement positive.

#### 🟡 Catégorie B : Les Features Graphe & Réseau (L'Environnement)
Ces variables captent le "Gang" ou l'influence du milieu via l'algorithme *Node2Vec*.
4. `degree_centrality` : Nombre de liens directs du nœud `[P]`.
5. `risk_proximity_score` : Le PageRank inversé calculant la distance (nombre de sauts) entre `[P]` et des individus déjà classés "Rouge". (Si les 3 meilleurs amis de X sont incarcérés, son risque environnemental explose).
6. `triadic_closure_rate` : À quelle vitesse le réseau à risque autour de `[P]` se referme et se densifie.

#### 🟡 Catégorie C : Les Features Multi-Sources (La Transversalité)
C'est ici que l'approche CGIP pulvérise l'approche "Silo" de la Police.
7. `source_diversity_index` : Le nombre d'institutions différentes ayant émis un signal sur `[P]`.
   - *Exemple* : 3 plaintes police = Biais local (Indice faible). 1 alerte école + 1 urgence hôpital + 1 main courante = Convergence de crise (Indice maximal).
8. `institutional_contradiction` : Différence de sévérité entre les signaux de l'École et ceux de la Justice. (Révèle l'aveuglement judiciaire).

### 5.2. L'Algorithme de Classification (XGBoost)

Le modèle qui ingère ces 12 Features n'est pas un Réseau de Neurones Profond (Deep Learning), car la loi européenne exige une **Explicabilité Totale (XAI)**.
- **Le Choix** : `XGBoost` (Gradient Boosting Tree) ou `LightGBM`.
- **Pourquoi ?** : Les arbres de décision sont insensibles à la variance spatiale, gèrent parfaitement les données manquantes (courantes en administration), et surtout, ils supportent la librairie **SHAP (SHapley Additive exPlanations)**.

### 5.3. Le Bouclier Juridique : SHAP (Explicabilité)

Lorsqu'un Magistrat (Zone Rouge) reçoit l'alerte sur son Dashboard, le système XGBoost crache un score de risque de `0.88`. S'il s'arrête là, c'est de la surveillance de masse illégale.
**La compliance RGPD impose d'afficher le diagramme de force SHAP :**
- 🟥 Pousse le risque vers le HAUT (+0.40) : `source_diversity_index` = 3 (L'école, l'hôpital et la police ont tous les trois sonné l'alarme en moins de 30 jours).
- 🟥 Pousse le risque vers le HAUT (+0.30) : `escalation_slope` = +2.5 (La gravité des actes monte).
- 🟦 Pousse le risque vers le BAS (-0.15) : `risk_proximity_score` = Faible (La personne n'a aucun lien avec un réseau à risque existant).

👉 **Conclusion du Magistrat** : Il ne s'agit pas d'un profil de "gang", mais d'une crise familiale ou personnelle grave et isolée en pleine explosion temporelle. Il peut ordonner une mesure d'assistance éducative ciblée. Le code a aidé la justice, sans la remplacer.

---

## 6. La Mathématique des Poids (Weights) et du Temps (Time Decay)

La CGIP ne croit jamais aveuglément une donnée. Chaque relation (Arête) dans le graphe Neo4j possède un poids dynamique ($W_{edge}$) qui évolue selon la source et le temps. C'est l'essence même du "Privacy by Design".

### 6.1. L'Équation du Poids Relatif (Confidence Score)

Lorsqu'un nœud `[Personne]` est relié à un `[Event]`, le poids de l'arête est calculé ainsi :
$$ W_{edge} = \text{Reliability}_{source} \times \text{Confidence}_{nlp} \times \text{Decay}(t) $$

1. $\text{Reliability}_{source}$ (La fiabilité juridique) :
   - Condamnation (Cassiopée) = $1.0$
   - Plainte en cours (TAJ) = $0.8$
   - Signalement Administratif (École/Social) = $0.5$
   - Témoignage Civil Tech / Main Courante = $0.3$
2. $\text{Confidence}_{nlp}$ : Le score de certitude généré par l'algorithme d'Entity Resolution. S'il n'est sûr qu'à 85% que "J. Dupont" est "Jean Dupont", on multiplie par $0.85$.

### 6.2. Le "Droit à l'Oubli" Mathématique (Time Decay)

Pour respecter le RGPD et la prescription pénale, un signalement ne peut pas avoir un impact infini dans le temps. L'algorithme applique une décroissance exponentielle :
$$ \text{Decay}(t) = e^{-\lambda \Delta t} $$
- $\Delta t$ : Le temps écoulé depuis l'événement (en mois ou années).
- $\lambda$ : La constante de demi-vie légale.
  - *Crime grave* : Demi-vie de 10 ans ($\lambda$ très faible).
  - *Bagarre scolaire* : Demi-vie de 6 mois ($\lambda$ très élevé).

**Conséquence Légale** : Une rumeur ou un petit signalement scolaire ($0.5$), s'il n'est pas réitéré, verra son poids tendre vers zéro en quelques mois. Le graphe "oublie" naturellement les individus inoffensifs, empêchant le fichage permanent. À l'inverse, 4 signalements scolaires dans le même mois verront leurs poids s'additionner pour déclencher l'anomalie.
*   **Contraintes & Hypothèses (Assumptions) :** Une lente accumulation de signaux faibles (ex: 4 alertes scolaires à +1) est mathématiquement symptomatique d'une faille systémique nécessitant une intervention, au même titre qu'un signal fort isolé.
*   **Limites / Biais (Edge Cases) :** Un individu innocent victime de harcèlement (ex: faux signalements anonymes répétés par un voisin vengeur) verra son score $S_{vuln}$ exploser artificiellement et déclenchera une alerte prioritaire, à moins que le *Confidence Score* ne vienne diviser le poids de ces rumeurs par zéro en amont.

### Indice de Similarité Sérielle (Héritage SALVAC / ViCLAS)
**Formule :**
$$
\Huge S_{serial}(A, B) = \frac{\sum_{k=1}^{156} w_k \cdot \delta(A_k, B_k)}{\sum_{k=1}^{156} w_k}
$$
*   **Quoi :** Calcul d'une similarité de Jaccard/Cosinus pondérée entre deux affaires $A$ et $B$ sur les 156 variables comportementales (Modus Operandi). 
*   **Légende :** $S_{serial}$ : Indice de similarité (ex: 0.87), $k$ : les 156 items (heure, arme, type de victime), $\delta$ : fonction d'égalité (1 si match, 0 sinon), $w_k$ : poids de l'item (un "rituel" a plus de poids qu'une "heure de la journée").
*   **Pourquoi :** Capter la logique d'analyse originelle de SALVAC (Comparaison pair-à-pair de crimes violents). Dans la CGIP, cette équation n'est plus calculée à la main mais est internalisée et calculée par les *Embeddings* du GNN sur chaque nœud événement.
*   **Inputs :** Les métadonnées structurées de deux événements distincts (qu'ils viennent de Cassiopée ou de la Civil Tech).
*   **Outputs :** Probabilité de lien sériel $\in [0, 1]$.
*   **Dépendance Amont :** Ingestion NLP (Transformation des textes en vecteurs).
*   **Dépendance Aval :** GNN (Création d'une arête probabiliste `IS_SIMILAR_TO`).
*   **Complexité Algorithmique :** O(1) pour deux affaires, mais O(N²) pour comparer toute une base SQL. D'où l'absolue nécessité d'utiliser un Graphe.
*   **Contraintes & Hypothèses (Assumptions) :** Un individu/à risque est psychologiquement routinier. Il reproduit des schémas d'action (idiosyncrasie) identifiables statistiquement.
*   **Limites / Biais (Edge Cases) :** Si l'auteur modifie intentionnellement ou par accident son mode opératoire d'une victime à l'autre (ex: change de véhicule), le score $\delta$ s'effondre et SALVAC devient aveugle. La CGIP devra compenser cela avec les liens contextuels (DoWhy).

---

## 5. Machine Learning & XAI (Détection de Trajectoires à Risque)

### Modèle de Classification d'Escalade (Gradient Boosting / GNN)
**Formule Objective (Objectif ML) :**
$$
\Huge \hat{y} = f(X_{temp}, X_{comp}, X_{graph}, X_{geo})
$$
*   **Quoi :** Estimer la probabilité qu'une trajectoire d'événements s'aggrave (escalade significative) dans les 12 prochains mois ($y=1$ si escalade grave, $y=0$ sinon). Produit un *Risk Score* et ses valeurs SHAP (Explainability).
*   **Légende :** $\hat{y}$ : Probabilité d'escalade, $X_{temp}$ : Features temporelles (fréquence, accélération), $X_{comp}$ : Features comportementales (répétition même contexte), $X_{graph}$ : Features de graphe (centralité, connexions à risque), $X_{geo}$ : Densité spatiale.
*   **Pourquoi :** Fournir une alerte probabiliste à la justice sans recourir à la justice prédictive. Ce système (idéalement un modèle robuste comme XGBoost ou Random Forest) n'évalue pas "le danger moral de la personne", mais la "vélocité statistique de son historique administratif".
*   **Inputs :** Unité d'observation matricielle (`person_event_window`) agglomérant sur une fenêtre de 6-24 mois les signalements scolaires, policiers et judiciaires.
*   **Outputs :** Probabilité de risque $\in [0, 1]$ et un vecteur de justification (ex: `+0.31 → répétition contexte`, `-0.05 → absence antécédents graves`).
*   **Dépendance Amont :** Graphes Causaux, Feature Engineering Pipeline.
*   **Dépendance Aval :** Interface Enquêteur (Human Alerting).
*   **Complexité Algorithmique :** Rapide en production (arbres de décision ou inférence GNN de type Node2Vec/GraphSAGE).
*   **Contraintes & Hypothèses (Assumptions) :** Le modèle assume que des labels purement administratifs ($y=1$ pour multi-plaintes ou affaire sensible) sont une approximation suffisante du risque à risque futur d'une trajectoire.
*   **Limites / Biais (Edge Cases) :** Le risque de prophétie autoréalisatrice et les biais de signalement (over-policing sur certaines populations). La machine peut confondre forte corrélation et causalité, transformant un faisceau de rumeurs en "escalade", d'où la nécessité absolue de l'XAI (Explainable AI - SHAP) et de la Revue Humaine.


## X. Algorithmes de Scoring & Graphes Avancés

### 1. Variables (Features) du Graphe
- **Centralité** : Degree (Nombre de plaintes) et Betweenness (Le suspect est-il le pont entre plusieurs affaires séparées ?).
- **Proximité (Distance)** : Nombre de "sauts" entre deux victimes présumées.

### 2. Modèles de Scoring
L'architecture prévoit 3 niveaux de modélisation :
- **Baseline** : Régression Logistique (Score de risque interprétable mathématiquement de 0 à 100).
- **Standard** : Random Forest / XGBoost.
- **Deep Learning / GNN** : Graph Neural Networks et Node2Vec (Vecteurs d'intégration des nœuds) pour détecter des clusters cachés.

## X. Vecteur de Caractéristiques (Feature Vector)

Pour qu'un individu soit scoré par les modèles ML (Baseline ou XGBoost), les tables relationnelles sont écrasées (Feature Engineering) dans un tenseur ou un dictionnaire JSON plat.
Exemple d'input mathématique pour l'inférence :
```json
{
  "events_5y": 5,
  "max_severity": 5,
  "institutions_count": 4,
  "time_between_events_mean_months": 14,
  "graph_degree": 8,
  "signalements_count": 3
}
```
Ce vecteur est la "traduction" algébrique du comportement humain.

## X. Mise en Perspective des Algorithmes de Scoring

L'analyse internationale révèle l'usage d'outils de scoring existants :
- **Outils locaux (UK)** : Séries de règles semi-automatiques (ex: VAR / DASH pour les violences domestiques).
- **Hotspot Policing (USA)** : Modèles prédictifs basés sur des zones géographiques (souvent biaisés algorithmiquement).

**La différence CGIP** : Notre modèle mathématique XGBoost / GNN se démarque de l'approche américaine car il n'évalue jamais des "zones" (Hotspot) ou des probabilités de récidive pures, mais des **réseaux d'événements avérés** (Graph Centrality) pour éviter les biais sociologiques.

## X. Formulaire Officiel du Scoring de Risque

Le pseudo-code nous donne les équations réelles à implémenter :

### 1. Proximité Graphe (Victim Proximity Score)
Pour toute victime `v` dans le graphe connectée au suspect `p` à une distance `d <= 2` :
`Score_prox = Σ (1 / (d + 1))`
Ce calcul normalisé prouve l'encerclement d'un individu par des victimes sans lien apparent.

### 2. Contraintes Juridiques (Clamp & Poids)
Le `raw_score` issu de XGBoost subit un filtre pénal brutal :
- **Règle de Multiplicité** : Si `event_count < 2` (source unique), alors `Score = Score * 0.7`. (Évite la condamnation algorithmique sur dénonciation calomnieuse unique).
- **Règle d'Alerte** : Si `Score > 0.90` (Seuil critique), le système est mis en pause et renvoie le flag `CRITICAL_REVIEW_REQUIRED` au lieu de déclencher une action directe.

## X. La Couche d'Intégration Vectorielle (Embeddings)

Le schéma fige l'utilisation des algorithmes de plongement de graphe.
Les algorithmes comme **GraphSAGE** ou **Node2Vec** sont mandatés pour transformer le sous-graphe d'un individu en un vecteur dense unidimensionnel (`vector[128]`). 
C'est ce vecteur de 128 dimensions, couplé aux features tabulaires SQL, qui sera injecté dans l'arbre de décision final (XGBoost).

## X. Hyperparamètres du Modèle d'Évaluation (XGBoost)

Le pseudo-code fige les hyperparamètres de base du modèle XGBoost Classifier. Il est volontairement bridé (max_depth faible) pour éviter l'overfitting et garder une certaine explicabilité (SHAP).
```python
model = xgb.XGBClassifier(
    max_depth=4,         # Bridé pour éviter la "boîte noire" trop profonde
    n_estimators=200,    # Robustesse statistique
    learning_rate=0.05   # Apprentissage conservateur
)
```


## XI. Équations du Graph Neural Network (GraphSAGE)

Pour extraire l'ADN social des suspects (Centralité et Proximité à risque) de manière prédictive, la CGIP utilise l'algorithme **GraphSAGE**. Contrairement à un GCN transductif, GraphSAGE permet de générer des vecteurs d'apprentissage (Embeddings) "à la volée" pour de nouveaux profils sans ré-entraîner toute la base de données.

### 1. L'Équation d'Agrégation (Message Passing)
Un individu s'imprègne du risque de son entourage direct. À chaque itération $k$, l'algorithme agrège les vecteurs des voisins $\mathcal{N}(v)$ de la personne $v$ :

$$ h_{\mathcal{N}(v)}^{k} = 	ext{AGGREGATE}_{k} \Big( \{ h_u^{k-1}, orall u \in \mathcal{N}(v) \} \Big) $$

*(La fonction AGGREGATE peut être une moyenne (`Mean`), un réseau de neurones (`Pool`), ou un LSTM. La CGIP utilise la moyenne pour l'explicabilité juridique).*

### 2. L'Équation de Mise à Jour (Update)
Une fois les "messages" du voisinage reçus, on fusionne l'ancienne signature à risque de l'individu avec la nouvelle, via une matrice de poids $W^k$ et une fonction d'activation non-linéaire $\sigma$ (ex: ReLU) :

$$ h_v^k = \sigma \Big( W^k \cdot 	ext{CONCAT} ig( h_v^{k-1}, h_{\mathcal{N}(v)}^k ig) \Big) $$

### 3. La Synthèse Absolue (Vector[128])
Après $K=2$ itérations (pour voir "l'ami de l'ami"), le vecteur final $z_v$ contient toute l'information topologique. Il a une dimension exacte de 128.

$$ z_v = h_v^K \quad 	ext{avec} \quad z_v \in \mathbb{R}^{128} $$

**Règle d'Encapsulation** : $z_v$ n'est pas un score de condamnation. C'est un vecteur mathématique neutre qui est ensuite passé au **XGBoost Classifier** (Chapitre X), seul habilité à formuler la probabilité, elle-même soumise au **Bouclier Légal**.
