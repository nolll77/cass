# Architecture Front-End de la CGIP

Ce document spécifie la pile technologique et l'ergonomie (UI/UX) pour le développement des interfaces du Ministère de la Justice et de l'Intérieur.

## Stack Technologique Requise
- **Framework Core** : React 18+ avec TypeScript (Typage strict obligatoire).
- **State Management** : Zustand (Léger et optimisé pour les re-renders rapides).
- **Visualisation de Graphe** : `Sigma.js` ou `deck.gl` (WebGL obligatoire). La CGIP manipulera des graphes de 100 000+ nœuds, les librairies SVG classiques (D3.js basique) crasheront le navigateur.
- **Temps Réel** : WebSockets (Socket.io) pour afficher les alertes IA dès qu'elles sont streamées depuis Kafka.
- **Sécurité Client** : Le navigateur DOIT posséder le certificat mTLS de la carte professionnelle (Agent). Aucun token JWT dans le `localStorage`.

## Système de Couleurs (UI Sémantique)
L'UI doit être visuellement explicite pour éviter les erreurs d'interprétation juridique :
- 🔴 **Rouge Pénal (#E53935)** : Représente les faits confirmés par la Justice (Casiers, Condamnations). *En clair*.
- ⬛ **Noir Social (#212121)** : Représente les signalements faibles (École, Aide Sociale). *Par défaut, ces nœuds n'affichent AUCUN texte, juste une icône de cadenas (Privacy by Design)*.
- 🟡 **Jaune Alerte (#FFB300)** : Le Nœud Racine de l'alerte prédictive.

## Composants Majeurs

### 1. `<AlertInbox />`
Un fil d'actualité listant les IDs chiffrés : "Alerte Criticité Rouge : #A8X9".
L'utilisateur clique pour ouvrir l'espace de travail.

### 2. `<GraphVisualizer />`
Le composant central WebGL.
- **Force-Directed Layout** : Les nœuds connectés s'attirent. Un individu ayant des liens avec de multiples affaires pénales sera visuellement "aspiré" vers le centre du graphe (Gravité massique).
- **Time Slider** : Une barre temporelle en bas. Le Magistrat peut la glisser vers la gauche pour voir à quoi ressemblait le graphe 2 ans auparavant (Temporal Graph Networks).

### 3. `<JudicialActionPanel />`
Panneau latéral droit persistant.
Boutons :
1. `[DÉCHIFFRER L'ANONYMAT]` -> Déclenche le flux d'audit Blockchain et l'appel API PostgreSQL Niveau 0.
2. `[REJETER L'ALERTE]` -> Envoie un feedback au modèle GraphSAGE (False Positive).
