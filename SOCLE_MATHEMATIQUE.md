# Socle Mathématique et Algorithmique (Formulaire CGIP)

> **Abstract (Résumé Exécutif)**
> Ce document est le "Formulaire Légal" du projet. Il fige les équations et les limites algorithmiques de nos modèles d'IA (XGBoost, GraphSAGE). Son but est de prouver mathématiquement qu'aucune décision individuelle automatique (illégale au sens de l'Art. 22 du RGPD) n'est jamais prise. La machine calcule des probabilités de *liens entre dossiers*, jamais des probabilités de *culpabilité individuelle*.

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
>
> **LA LOI DE L'ANCRAGE TERRAIN :**
> Cette loi s'applique de manière totalitaire. La froideur mathématique désincarnée est interdite. Toute abstraction mathématique doit être immédiatement traduite en utilisant exclusivement **les objets réels du terrain étudié** (les individus, les magistrats, les affaires, les condamnations, le TAJ, Cassiopée).

---

## 1. Gouvernance et Privacy by Design

### 1.1 Time Decay Function (Droit à l'oubli algorithmique)
**Formule :**

$$
\Huge C(t) = C_0 \cdot e^{-\lambda \cdot \Delta t}
$$

<br>

*   **Quoi :** Décroissance exponentielle du poids d'une relation (Edge) dans le graphe au fil du temps.

*   **Légende :** 
    *   $C(t)$ : Confidence Score actuel *(ex : la force de la preuve retenue aujourd'hui par le système)*.
    *   $C_0$ : Poids initial brut de l'événement *(ex : le poids de 0.4 accordé à un simple signalement scolaire)*.
    *   $\lambda$ : coefficient de demi-vie légale *(ex : la vitesse à laquelle la justice considère qu'un fait mineur doit être oublié)*.
    *   $\Delta t$ : temps écoulé depuis l'événement *(ex : les 10 années passées sans aucune récidive depuis la dernière bagarre)*.

*   **Pourquoi :** Encoder la prescription légale et le droit à l'oubli dans les mathématiques. Un incident mineur vieux de 10 ans sans récidive doit disparaître des radars pour protéger la vie privée.

*   **Inputs :** Timestamp de l'événement, Timestamp actuel, Poids légal brut $C_0$.

*   **Outputs :** Scalaire positif $\in [0, 1]$ représentant la force résiduelle de la preuve.

*   **Dépendance Amont :** Le Moteur de Confiance (Confidence Engine).

*   **Dépendance Aval :** Agrégation de Risque, Processus de Hawkes.

*   **Complexité Algorithmique :** O(1) — Une multiplication instantanée.

*   **Contraintes & Hypothèses (Assumptions) :** Le risque de récidive d'un individu s'évapore mécaniquement et prévisiblement avec le temps s'il ne fait pas de nouvelles vagues dans le système institutionnel.

*   **Limites / Biais (Edge Cases) :** Si un agresseur part vivre à l'étranger pendant 10 ans (donc zéro signalement en France), le système va mathématiquement effacer son passif. À son retour, il sera vu à tort par la machine comme un profil totalement vierge.

---

### 1.2 Le Kill-Switch RGPD (DPIA Constraint)
**Formule :**

$$
\Huge K(R) = \begin{cases} 1 & \text{si } \sum w_i R_i < \theta_{legal} \\ 0 & \text{sinon (Block)} \end{cases}
$$

<br>

*   **Quoi :** Fonction indicatrice (Gate) matérielle et logicielle qui coupe instantanément l'exécution d'un thread Python si la requête devient illégale.

*   **Légende :** 
    *   $K(R)$ : Interrupteur *(ex : le blocage immédiat de l'écran du policier avec une erreur système)*.
    *   $R_i$ : métriques de risque RGPD *(ex : le volume de données de mineurs interrogées simultanément par l'algorithme)*.
    *   $\theta_{legal}$ : plafond légal d'intrusion autorisé *(ex : le seuil au-delà duquel la requête bascule dans de la surveillance de masse illégale)*.

*   **Pourquoi :** C'est le verrou de l'IA Constitutionnelle. Interdire physiquement au serveur de croiser des données si la requête du policier glisse vers un profilage de masse ("Minority Report").

*   **Inputs :** Métadonnées de la requête en cours (Quels types de nœuds sont interrogés ? Y a-t-il des mineurs impliqués ?).

*   **Outputs :** Binaire (0 = Erreur système forcée, 1 = Poursuite de l'inférence).

*   **Dépendance Amont :** Moteur GNN.

*   **Dépendance Aval :** Interface utilisateur (Affichage du graphe d'enquête ou Écran Rouge d'interdiction).

*   **Complexité Algorithmique :** O(1) — Vérification booléenne pure.

*   **Contraintes & Hypothèses (Assumptions) :** La délicate balance entre le respect de la vie privée et la nécessité d'une enquête policière peut être résumée par un score arithmétique rigide programmé en amont.

*   **Limites / Biais (Edge Cases) :** En cas de disparition d'enfant avec urgence vitale extrême (Alerte Enlèvement), si le plafond légal est codé de manière trop stricte, l'algorithme paralysera l'ordinateur du magistrat, l'empêchant techniquement de trouver le ravisseur.

---

## 2. Inférence Spatiale et Temporelle

### 2.1 Entity Resolution (Distance de Jaro-Winkler)
**Formule :**

$$
\Huge d_{jw} = d_j + (\ell \cdot p \cdot (1 - d_j))
$$

<br>

*   **Quoi :** Mesure de similarité textuelle favorisant les chaînes qui commencent par les mêmes caractères pour repérer les erreurs de saisie.

*   **Légende :** 
    *   $d_{jw}$ : Score final *(ex : la probabilité mathématique que "Jean Dupont" et "J. Dupont" soient la même personne)*.
    *   $d_j$ : distance de Jaro basique *(ex : la similarité brute des lettres tapées par le gendarme)*.
    *   $\ell$ : longueur du préfixe commun *(ex : le fait que les 3 premières lettres soient identiques dans les deux dossiers)*.
    *   $p$ : constante de pondération *(ex : le bonus de confiance accordé aux noms de famille qui commencent exactement pareil)*.

*   **Pourquoi :** Briser la faille des silos administratifs : la machine doit comprendre que le dossier "Jérôme B." tapé à la gendarmerie et la fiche "J. B." mal orthographiée par le directeur de l'école concernent exactement la même personne physique.

*   **Inputs :** Strings (chaînes de caractères hachées partelles, noms, adresses issues de bases différentes).

*   **Outputs :** Probabilité de fusion $\in [0, 1]$.

*   **Dépendance Amont :** Base de données Neo4j brutes issues des silos.

*   **Dépendance Aval :** Création d'une arête `IS_SAME_PERSON` dans le graphe unifié.

*   **Complexité Algorithmique :** O(|s1| * |s2|) — Simple et efficace.

*   **Contraintes & Hypothèses (Assumptions) :** Les erreurs de saisie des fonctionnaires de police ou d'éducation suivent des règles de fautes de frappe ou d'abréviations (typo) logiques et prévisibles.

*   **Limites / Biais (Edge Cases) :** Impuissant face aux homonymes parfaits : si un "Martin Dubois" habite à Montestruc-sur-Gers, et qu'un autre "Martin Dubois" (sans aucun lien) habite dans la ville d'à côté, le système va fusionner leurs vies pénales et ruiner la réputation de l'un des deux.

---

### 2.2 Processus de Hawkes (Détection de l'Escalade)
**Formule :**

$$
\Huge \lambda(t) = \mu + \sum_{t_i < t} \alpha \cdot e^{-\beta(t - t_i)}
$$

<br>

*   **Quoi :** Modèle de processus ponctuel auto-excitant mesurant l'intensité temporelle d'événements stochastiques pour prévoir une explosion de violence.

*   **Légende :** 
    *   $\lambda(t)$ : Taux de dangerosité à l'instant t *(ex : le risque imminent de passage à l'acte violent majeur)*.
    *   $\mu$ : bruit de fond *(ex : le niveau de risque minimal et normal d'un citoyen ordinaire)*.
    *   $t_i$ : timestamp des faits passés *(ex : la date exacte de la dernière plainte classée sans suite)*.
    *   $\alpha$ : saut d'intensité à chaque fait *(ex : la montée d'adrénaline ou de gravité après chaque nouvelle agression)*.
    *   $\beta$ : vitesse de retombée de l'urgence *(ex : la vitesse à laquelle la tension retombe dans les semaines suivant un incident)*.

*   **Pourquoi :** Capter mathématiquement la "vélocité" à risque. Trois signalements administratifs en 10 ans, c'est du bruit. Trois signalements en 6 mois, c'est une escalade (effet de réplique sismique) qui précède un drame qu'il faut empêcher.

*   **Inputs :** Vecteur des dates (timestamps) des incidents liés à un individu dans le graphe.

*   **Outputs :** Score d'escalade (scalaire dynamique).

*   **Dépendance Amont :** Entity Resolution (pour être sûr qu'on lie les faits à une seule et même personne).

*   **Dépendance Aval :** Moteur d'Alerte Globale du Dashboard Magistrat.

*   **Complexité Algorithmique :** O(E²) — E étant le nombre d'événements pour une personne, le calcul est quasi instantané.

*   **Contraintes & Hypothèses (Assumptions) :** Le passage à l'acte d'un prédateur agit comme un tremblement de terre : chaque agression augmente mécaniquement l'excitation de l'individu et provoque des répliques de plus en plus rapprochées dans le temps.

*   **Limites / Biais (Edge Cases) :** Un agresseur très intelligent, froid et méthodique, qui s'oblige de manière psychopathe à agir seulement une fois tous les 5 ans de manière métronomique, aura un score d'escalade de 0 et sera totalement invisible pour cette formule.

---

## 3. Graphes Causaux et Modélisation du Risque

### 3.1 Graph Neural Network (Link Prediction)
**Formule :**

$$
\Huge \hat{y}_{u,v} = \sigma(\mathbf{z}_u^T \mathbf{z}_v) \quad \text{avec} \quad \mathbf{Z} = GNN(\mathbf{A}, \mathbf{X})
$$

<br>

*   **Quoi :** Calcul de la probabilité de l'existence d'une arête (lien) entre deux nœuds en effectuant un produit scalaire sur leurs vecteurs latents générés par un réseau de neurones sur graphe.

*   **Légende :** 
    *   $\hat{y}_{u,v}$ : probabilité d'un lien caché *(ex : les chances statistiques que ce individu soit l'auteur inconnu de cette affaire non-résolue)*.
    *   $\mathbf{z}$ : vecteur latent *(ex : l'empreinte topologique ou le "modus operandi" codé de la personne)*.
    *   $\mathbf{A}$ : topologie du graphe *(ex : le réseau complexe des lieux fréquentés et des personnes croisées)*.
    *   $\mathbf{X}$ : traits connus *(ex : l'âge de l'individu et son casier judiciaire officiel)*.

*   **Pourquoi :** Révéler le "chaînon manquant" et automatiser l'analyse sérielle. Le GNN remplace mathématiquement les "156 items d'analyse manuelle" du système SALVAC en trouvant des similarités de Modus Operandi (Lieux, Heures, Cibles) enfouies dans la topologie des affaires.

*   **Inputs :** Matrice d'adjacence globale (Les écoles, les adresses, les victimes), Matrice des caractéristiques $\mathbf{X}$.

*   **Outputs :** Probabilité $P_{link} \in [0, 1]$ (Score latent de sérialité).

*   **Dépendance Amont :** Base complète Neo4j et calcul de *Time Decay*.

*   **Dépendance Aval :** Inférence Causale (DoWhy) pour vérification.

*   **Complexité Algorithmique :** O(V + E) en inférence par couche — Très rapide pour interroger la base au quotidien, mais l'entraînement préalable du modèle sur les serveurs du Ministère nécessite de gros GPUs.

*   **Contraintes & Hypothèses (Assumptions) :** Si la personne A et la personne B fréquentent exactement le même réseau de lieux sociaux toxiques, au même moment, avec les mêmes modes opératoires (patterns), elles partagent la même sphère de risque pénal.

*   **Limites / Biais (Edge Cases) :** Le danger absolu de la corrélation illusoire : l'algorithme va relier artificiellement un plombier innocent à un réseau à risque uniquement parce qu'il a été embauché pour réparer l'évier du collège à l'heure exacte d'une agression dans la cour.

---

### 3.2 Inférence Causale (Backdoor Criterion - DoWhy)
**Formule :**

$$
\Huge P(Y \mid do(X)) = \sum_Z P(Y \mid X, Z) P(Z)
$$

<br>

*   **Quoi :** Isoler l'effet causal pur d'une variable $X$ sur $Y$ en bloquant mathématiquement toutes les autres portes de corrélation fallacieuses $Z$ (confounders).

*   **Légende :** 
    *   $P(Y \mid do(X))$ : effet causal pur *(ex : la preuve que la présence du individu est vraiment la cause de l'agression, et non une coïncidence géographique)*.
    *   $do(X)$ : forçage mathématique de la cause *(ex : simuler l'impact réel de l'arrivée du individu sur les lieux du crime)*.
    *   $Z$ : variables de confusion *(ex : la densité criminelle naturelle du quartier qui fausse artificiellement l'analyse)*.

*   **Pourquoi :** Agir comme le cerveau logique du magistrat. C'est l'antidote à l'erreur du plombier (Limites du GNN). L'algorithme doit prouver que la topologie causale valide l'alerte, et non pas une simple coïncidence de lieu.

*   **Inputs :** Le DAG (Graphe Orienté Acyclique) des règles judiciaires posées par les experts, La probabilité issue du GNN.

*   **Outputs :** Validation ou invalidation booléenne de la prédiction GNN.

*   **Dépendance Amont :** GNN (Link Prediction).

*   **Dépendance Aval :** Déclenchement de l'Alerte "REVUE HUMAINE RECOMMANDÉE".

*   **Complexité Algorithmique :** O(V + E) — Parcours de graphe pour trouver les chemins bloqués (ultra-rapide).

*   **Contraintes & Hypothèses (Assumptions) :** Le comité d'éthique et les enquêteurs qui ont dessiné à la main les règles du DAG ont réussi l'exploit intellectuel de lister absolument TOUTES les variables de la vie réelle pouvant créer une fausse coïncidence (Unobserved Confounding).

*   **Limites / Biais (Edge Cases) :** S'il manque une seule petite variable clé non-renseignée (ex: "le individu a un frère jumeau"), le modèle causal sera aveugle, la formule validera la corrélation toxique, et le plombier innocent finira en garde à vue.

---

### 3.3 Score de Risque Temps Réel (Event-Driven)
**Formule :**

$$
\Huge S_{risk} = 0.35 \cdot R_{temp} + 0.30 \cdot R_{graph} + 0.20 \cdot W_{trend} + 0.15 \cdot S_{cross}
$$

<br>

*   **Quoi :** Addition linéaire pondérée de 4 macro-features calculées à la volée pour évaluer l'urgence d'une situation.

*   **Légende :** 
    *   $S_{risk}$ : Score total *(ex : le niveau de criticité affiché en rouge sur l'écran du magistrat)*.
    *   $R_{temp}$ : Risque Temporel *(ex : l'accélération brutale des plaintes déposées sur les 30 derniers jours)*.
    *   $R_{graph}$ : Risque Topologique *(ex : le fait d'être soudainement connecté à un réseau criminel très lourd)*.
    *   $W_{trend}$ : Escalade de la gravité *(ex : le passage factuel d'une simple insulte à des violences avec arme)*.
    *   $S_{cross}$ : Signaux multi-sources *(ex : le moment où l'école, l'hôpital et la police sonnent l'alerte simultanément sur le même dossier)*.

*   **Pourquoi :** Éviter l'effet "boîte noire" d'un réseau de neurones pur. Fournir au magistrat un calcul mathématique décryptable (via SHAP) où il peut voir exactement pourquoi le système lance l'alerte.

*   **Inputs :** Les scores issus de Hawkes ($R_{temp}$), du GNN ($R_{graph}$), et l'ingestion Kafka.

*   **Outputs :** Un score continu déterminant le niveau d'alerte (Rouge > 0.85, Orange > 0.65).

*   **Dépendance Amont :** L'ensemble de la stack d'inférence (Hawkes, Entity Resolution).

*   **Dépendance Aval :** Interface Dashboard.

*   **Complexité Algorithmique :** O(N) — Simple somme arithmétique.

*   **Contraintes & Hypothèses (Assumptions) :** Ce score de risque évalue une Situation (un Événement), il n'évalue JAMAIS un Individu, respectant la loi interdisant le profilage pénal individuel.

*   **Limites / Biais (Edge Cases) :** Une pondération linéaire fixe (0.35, 0.30...) est arbitraire : un signalement unique extrêmement grave (ex: tentative de meurtre isolée) pourrait ne pas déclencher le seuil "Rouge" si l'individu a un score topologique et temporel de 0, forçant la justice à rater une alerte critique.

---

### 3.4 Poids Relatif (Confidence Score)
**Formule :**

$$
\Huge W_{edge} = \text{Reliability}_{source} \times \text{Confidence}_{nlp} \times \text{Decay}(t)
$$

<br>

*   **Quoi :** La pondération finale de chaque lien dans la base de données Neo4j, combinant la vérité institutionnelle, l'incertitude informatique, et l'usure du temps.

*   **Légende :** 
    *   $W_{edge}$ : poids dynamique de la relation *(ex : la force totale de l'arête reliant le individu à une victime dans le graphe Neo4j)*.
    *   $\text{Reliability}_{source}$ : fiabilité juridique *(ex : une condamnation définitive par un juge pèse 1.0, un signalement anonyme pèse 0.3)*.
    *   $\text{Confidence}_{nlp}$ : certitude de l'Entity Resolution *(ex : la certitude algorithmique de 85% qu'il s'agit bien de la même personne)*.
    *   $\text{Decay}(t)$ : fonction de droit à l'oubli *(ex : l'effacement progressif du passif avec le passage des années)*.

*   **Pourquoi :** La CGIP ne croit jamais aveuglément une donnée. Cette formule garantit que les erreurs de saisie ou les vieilles rumeurs ne peuvent pas détruire la vie d'un citoyen : leur poids est mathématiquement écrasé.

*   **Inputs :** Origine de la donnée (Cassiopée vs École), Score de Jaro-Winkler, Temps écoulé.

*   **Outputs :** Poids final $W_{edge} \in [0, 1]$.

*   **Dépendance Amont :** Jaro-Winkler, Time Decay.

*   **Dépendance Aval :** GNN (qui utilise $W_{edge}$ comme force de liaison).

*   **Complexité Algorithmique :** O(1).

*   **Contraintes & Hypothèses (Assumptions) :** On suppose que l'institution judiciaire officielle (Cassiopée) détient toujours la vérité absolue (fiabilité 1.0) par rapport aux autres strates de l'administration.

*   **Limites / Biais (Edge Cases) :** Un individu innocent harcelé (ex: multiples faux signalements anonymes par un voisin) verra le volume d'arêtes compenser la faible fiabilité de la source, déclenchant une fausse alerte si on n'applique pas une limite stricte.

---

## 4. Analyse Sérielle et Classification

### 4.1 Indice de Similarité Sérielle (Héritage SALVAC)
**Formule :**

$$
\Huge S_{serial}(A, B) = \frac{\sum_{k=1}^{156} w_k \cdot \delta(A_k, B_k)}{\sum_{k=1}^{156} w_k}
$$

<br>

*   **Quoi :** Calcul d'une similarité de Jaccard/Cosinus pondérée entre deux affaires sur les 156 variables comportementales (Modus Operandi) du système historique SALVAC.

*   **Légende :** 
    *   $S_{serial}$ : Indice de similarité *(ex : la probabilité mathématique que ces deux scènes de crime violentes soient l'œuvre du même tueur en série)*.
    *   $k$ : les 156 items de profilage *(ex : l'heure de l'agression, l'arme utilisée, le profil type de la victime)*.
    *   $\delta(A_k, B_k)$ : fonction d'égalité *(ex : vaut 1 si exactement le même type d'arme a été utilisé, 0 sinon)*.
    *   $w_k$ : poids de l'item *(ex : la présence d'un rituel macabre très rare pèse infiniment plus lourd qu'une simple concordance d'heure de la journée)*.

*   **Pourquoi :** Capter la logique d'analyse originelle du système ViCLAS/SALVAC. La CGIP modernise cette équation en la calculant instantanément sur toute la base via les Embeddings du GNN.

*   **Inputs :** Les métadonnées structurées de deux événements criminels distincts (issus de Cassiopée ou TAJ).

*   **Outputs :** Probabilité de lien sériel $\in [0, 1]$.

*   **Dépendance Amont :** Ingestion NLP (Transformation des Procès-Verbaux en variables structurées).

*   **Dépendance Aval :** Création d'une arête probabiliste `IS_SIMILAR_TO` entre deux scènes de crime.

*   **Complexité Algorithmique :** O(1) pour comparer deux affaires, mais O(N²) pour comparer l'entièreté d'une base SQL nationale (d'où l'usage du Graphe).

*   **Contraintes & Hypothèses (Assumptions) :** Un tueur en série ou un prédateur est psychologiquement routinier. Il reproduit mécaniquement des schémas d'action (idiosyncrasie) identifiables par la statistique.

*   **Limites / Biais (Edge Cases) :** Si l'auteur modifie intentionnellement ou par pur accident son mode opératoire d'une victime à l'autre (ex: change de modèle de voiture pour fuir), le score d'égalité s'effondre et l'algorithme SALVAC devient totalement aveugle.

---

### 4.2 Modèle de Classification d'Escalade (XGBoost)
**Formule Objective :**

$$
\Huge \hat{y} = f(X_{temp}, X_{comp}, X_{graph}, X_{geo})
$$

<br>

*   **Quoi :** Estimer la probabilité qu'une trajectoire d'événements mineurs s'aggrave (escalade) dans les 12 prochains mois, en utilisant un arbre de décision explicable (Gradient Boosting).

*   **Légende :** 
    *   $\hat{y}$ : Probabilité d'escalade *(ex : le risque probabiliste de récidive grave dans l'année)*.
    *   $X_{temp}$ : Features temporelles *(ex : la fréquence frénétique des passages à l'acte le mois dernier)*.
    *   $X_{comp}$ : Features comportementales *(ex : la répétition des mêmes méthodes sur le même profil de victimes)*.
    *   $X_{graph}$ : Features de graphe *(ex : la position centrale de l'individu dans un réseau connu de délinquants)*.
    *   $X_{geo}$ : Densité spatiale *(ex : la concentration géographique extrême des agressions dans un seul quartier)*.

*   **Pourquoi :** Fournir une alerte probabiliste à la justice sans recourir à la justice prédictive. Ce modèle n'évalue pas "le danger moral de la personne", mais la "vélocité statistique de son historique administratif".

*   **Inputs :** Unité d'observation matricielle agglomérant sur une fenêtre de 6 à 24 mois tous les signaux institutionnels.

*   **Outputs :** Probabilité de risque $\in [0, 1]$ et un vecteur de justification explicable (SHAP Values).

*   **Dépendance Amont :** Graphes Causaux, Feature Engineering Pipeline.

*   **Dépendance Aval :** Interface Enquêteur (Alerte Visuelle + Diagramme SHAP).

*   **Complexité Algorithmique :** O(D \cdot \log(N)) pour l'inférence — Extrêmement rapide en production avec XGBoost.

*   **Contraintes & Hypothèses (Assumptions) :** Le modèle assume que des labels purement administratifs (comme le classement d'une affaire) sont une approximation suffisante du risque pénal futur d'une trajectoire.

*   **Limites / Biais (Edge Cases) :** Le danger massif de la "prophétie autoréalisatrice" et du sur-flicage (over-policing). Si un quartier est plus surveillé, la machine captera plus de petits événements ($X_{geo}$), fera exploser la probabilité $\hat{y}$, renvoyant encore plus de police, créant une boucle de rétroaction infinie et biaisée.
