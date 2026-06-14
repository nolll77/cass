<div align="center">
  <h1>🏛️ Civic Graph Intelligence Platform (CGIP)</h1>
  <p><b>Le Cerveau Artificiel Institutionnel : Graphes Causaux, Inférence Structurelle et IA Constitutionnelle.</b></p>
  <br>
  <img src="https://img.shields.io/badge/Status-Research_%26_Architecture-blue.svg" alt="Status">
  <img src="https://img.shields.io/badge/Architecture-Distributed_Graph_Platform-orange.svg" alt="Architecture">
  <img src="https://img.shields.io/badge/Paradigm-Compliance--By--Design-brightgreen.svg" alt="Paradigm">
  <img src="https://img.shields.io/badge/Core-PyTorch_Geometric_%7C_Neo4j_%7C_DoWhy-purple.svg" alt="CoreTech">
</div>

---

## 📖 1. Préambule Épistémologique : L'Échec des Silos Tabulaires

Le projet **Cass / CGIP** naît d'un constat systémique profond sur le fonctionnement de l'appareil d'État (Justice, Police, Éducation, Services Sociaux). Régulièrement, des tragédies institutionnelles se produisent non pas parce que l'information n'existait pas, mais parce qu'elle était **fragmentée**, dispersée dans des silos étanches et statiques.

### 1.1. La nature du fractionnement institutionnel
Historiquement, les bases de données gouvernementales sont conçues selon un paradigme **tabulaire** et **procédural**. 
*   **2020** : L'Éducation Nationale enregistre un signalement isolé (relation adulte/mineure) classé sans suite judiciaire.
*   **2022** : La Police Nationale enregistre une plainte tardive, sur des faits anciens, avec un nom de suspect mal orthographié.
*   **2024** : Les Services Sociaux émettent une alerte sur un comportement inquiétant.

Dans un paradigme tabulaire (SQL, registres administratifs), ces trois lignes n'ont **aucune existence topologique commune**. Elles existent dans des espaces de stockage différents. Le lien qui les unit est invisible à l'œil nu. 

### 1.2. Le Changement de Paradigme : La Réalité est un Graphe
La **Civic Graph Intelligence Platform** acte une rupture paradigmatique : la réalité sociale et criminelle n'est pas une table de données, c'est un **graphe orienté et dynamique**. L'individu, l'événement, l'adresse, la plainte sont des nœuds (`Nodes`). Leurs relations temporelles et hiérarchiques sont des arêtes (`Edges`). 

La mission de la CGIP est d'opérer la translation de cette réalité fragmentée vers une **vérité topologique unifiée**.

---

## ⚖️ 2. Le "Pacte Faustien" de l'IA et l'IA Constitutionnelle

Utiliser l'IA pour traiter les données judiciaires relève traditionnellement du "pacte faustien" :
*   *Soit* on optimise mathématiquement la prédiction (Police Prédictive, *Minority Report*), ce qui conduit inévitablement à un profilage illégal, un biais algorithmique massif et une violation des Droits de l'Homme.
*   *Soit* on interdit l'IA, et les institutions continuent de laisser passer des drames par cécité systémique.

### 2.1. Compliance is moved BEFORE computation
La CGIP résout cette aporie en modifiant l'architecture logicielle : **la contrainte constitutionnelle n'est pas une surcouche de vérification a posteriori, elle est le moteur d'exécution (Runtime).** 
Le système ne peut pas mathématiquement compiler une requête ou une inférence qui violerait le RGPD, car les poids du réseau neuronal et l'architecture du pipeline de données sont régis par un système de **Kill Switch** matériel et logiciel. Le profilage prédictif individuel est physiquement impossible par design. Ce que le système audite, ce n'est pas la probabilité qu'un individu commette un crime, mais **la probabilité qu'une structure institutionnelle souffre d'un angle mort**.

---

## 🏗️ 3. L'Architecture Multi-Couches (A à H)

La CGIP est une plateforme de niveau "Palantir-Foundry", conçue pour ingérer des flux massifs, générer des embeddings complexes, bloquer les anomalies éthiques et fournir une interface de Case Management à l'opérateur humain. Elle est découpée en 6 strates conceptuelles et opérationnelles.

### 🟦 Couche A : Le Socle Ontologique (Graph Core)
C'est la couche immuable. Elle est agnostique au Machine Learning. Elle se contente de modéliser les événements sous forme de triplets `(Sujet) -> [RELATION] -> (Objet)`. Elle ingère les flux de Kafka et construit un graphe dans **Neo4j**.
*   **Objectif** : Restructurer la réalité en abolissant les silos spatiaux.

### 🧠 Couche B : Inférence Structurelle (Graph Neural Networks - GNN)
L'intelligence du système réside ici. Basée sur *PyTorch Geometric*, cette couche apprend la forme géométrique des dossiers judiciaires. 
Un GNN ne lit pas du texte, il lit de la topologie. Si le réseau détecte un sous-graphe "A", et un autre sous-graphe "B" qui possèdent exactement les mêmes "voisins" temporels et événementiels, le GNN effectue une **Link Prediction** (Prédiction de Lien). 
*   **Objectif** : Dire à l'enquêteur : *"Malgré les fautes de frappe et l'espacement de 4 ans, il y a 92% de chances que ces deux entités soient la même personne."*

### 🔬 Couche D : Le Moteur Causal (Do-Calculus & DAG)
L'IA statistique classique est stupide : elle confond corrélation et causalité (ex: "les parapluies causent la pluie"). Pour contrer cela, la couche D intègre des **Direct Acyclic Graphs (DAG)** et de l'inférence causale (librairie *DoWhy*).
Cette couche simule des interventions mathématiques (`P(Y | do(X))`) pour garantir que les relations identifiées par le GNN ont un sens logique et chronologique.
*   **Objectif** : Forcer la machine à s'expliquer de manière déterministe et scientifique.

### 🧬 Couche BD : Fusion Causal-GNN (L'Innovation Core)
C'est le sommet de l'intelligence artificielle de la CGIP : le `causal_gnn.py`. Il applique une `Causal Alignment Loss`. Mathématiquement, cela signifie que si le GNN trouve une corrélation forte mais que le moteur causal dit "c'est temporellement ou physiquement impossible", la perte de la fonction bondit vers l'infini.
*   **Objectif** : Une IA incapable d'halluciner des relations absurdes.

### 🛡️ Couche E : Moteur de DPIA & Gouvernance RGPD
C'est le premier pare-feu éthique. Le Data Protection Impact Assessment (DPIA) est codé en heuristiques. Avant que le graphe ne passe dans le GNN, le module `E_gdpr_engine` scanne les nœuds. Présence de données de santé ? +40 de risque. Profilage automatisé ? +20 de risque. Traitement de masse ? +20. 
*   **Objectif** : Attribuer un niveau de risque juridique strict et documenté (LOW, MEDIUM, HIGH) à chaque micro-batch d'analyse.

### 🛑 Couche F : L'Enforcement et le Kill Switch
Là où les plateformes classiques envoient une simple notification de "Warning", la CGIP possède un véritable `kill_switch.py`. Si le moteur DPIA (Couche E) détecte un risque critique de discrimination ou de profilage arbitraire, une **Exception Runtime** est levée et le pipeline de calcul est immédiatement et physiquement sectionné.
*   **Objectif** : Un système qui s'arrête de fonctionner plutôt que de violer la loi. L'IA sous séquestre constitutionnel.

### 🎯 Couches G & H : Opérations, Alerting et Case Management
Le résultat final de tout ce travail n'est pas un pourcentage balancé au visage d'un juge. C'est l'intégration dans un **Case Management System** (un dossier). 
Si l'Alerting Engine identifie une `CRITICAL_ALERT`, il ouvre un `Workspace` d'investigation propre, avec une piste d'audit (Audit Trail) complète détaillant pourquoi le système a lié ces événements. L'humain (policier, juge, travailleur social) reprend le contrôle total.

---

## 💻 4. L'Infrastructure Logicielle (Enterprise Stack)

La conception du répertoire respecte un design moderne, prêt à l'échelle (Scale-ready) :

```text
cgip/
├── core/
│   └── graph/graph_model.py          # Définition agnostique des graphes temporels
├── modules/
│   ├── B_gnn/                        # Inférence PyTorch Geometric
│   ├── BD_fusion/                    # Fonction de perte causale (Causal Alignment Loss)
│   ├── E_gdpr_engine/                # Algorithme de calcul du DPIA
│   ├── F_autoblocking/               # Logique de Kill Switch & Decision Gate
│   ├── G_alerting/                   # Moteur hybride ML/Heuristique d'escalade
│   └── H_case_management/            # Espace de travail de l'analyste
├── orchestration/
│   ├── pipeline_router.py            # Routeur à Feature Flags (Ablation logicielle)
│   ├── feature_flags.py              # Configuration d'activation des couches (A->F)
│   └── dag.py
├── security/                         # Règles de politiques
├── ontology/                         # Schémas de données graph
├── ui/
│   └── app.py                        # Dashboard analytique Streamlit
└── simulate_case.py                  # Scénario End-to-End d'effondrement des silos
```

---

## 🚀 5. Lancer la Preuve de Conception (Simulation End-to-End)

Pour comprendre l'utilité du système, nous avons encodé un scénario tragiquement banal, connu sous le nom de "Fractionnement Institutionnel". 

### Exécution du simulateur :
Depuis la racine du dépôt, exécutez la commande :
```bash
python cgip/simulate_case.py
```

### Le comportement observable (Logs d'exécution) :
1. **[Ingestion]** : Le graphe unifié absorbe 3 signaux faibles décorrélés : un signalement de l'Éducation Nationale en 2020, une plainte de la Police en 2022, une alerte sociale en 2024.
2. **[DPIA Check]** : Le moteur calcule le risque éthique (Score = 60). Le Kill-Switch émet un `Warning` mais autorise le traitement car le profilage arbitraire est désactivé.
3. **[GNN + Causal Inference]** : L'IA identifie la signature topologique des dossiers. Le GNN affirme à 92% que les identités morcelées désignent la même réalité systémique.
4. **[Audit & Case]** : Une `CRITICAL_ALERT` est levée. L'affaire est consolidée. Le système ouvre automatiquement un rapport (Workspace `CASE_2024_001`).

**Conclusion de la simulation** : Le système force la coopération des acteurs publics **avant** que la situation n'atteigne un point de rupture irrémédiable, sans jamais violer la présomption d'innocence.

---

## 🔮 6. La Future Évolution : "Distributed Production Grade"

Bien que le dépôt actuel soit une preuve conceptuelle massive et fonctionnelle localement, l'architecture a été conçue pour muter en une plateforme asynchrone hautement disponible :

1. **Ingestion Temps Réel** : Remplacement des injections locales par un cluster **Apache Kafka** ou **AWS MSK** pour processer les plaintes et signalements en streaming continu.
2. **Stockage Distribué** : Base de données **Neo4j** en Haute Disponibilité (Cluster HA) gérant des dizaines de millions de nœuds institutionnels.
3. **Calcul Haute Performance** : Moteur GNN distribué (DGL ou TorchServe) capable de mettre à jour les embeddings dynamiquement (Temporal Graph Networks).
4. **Déploiement GitOps** : Infrastructure **Kubernetes** gérée via ArgoCD, permettant la conteneurisation stricte et la séparation des droits entre les nœuds ML et les nœuds RGPD.

> *"Ce système ne remplace pas le juge. Il est l'exosquelette mathématique de l'État de Droit, garantissant que l'oubli et le cloisonnement ne soient plus des fatalités systémiques."*
