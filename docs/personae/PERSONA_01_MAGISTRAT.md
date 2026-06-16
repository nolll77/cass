# Profil Utilisateur 1 : Le Magistrat (Juge / Procureur)

## 1. Description du Rôle
Le Magistrat (Procureur de la République, Juge d'Instruction ou Juge des Libertés et de la Détention) est la clé de voûte constitutionnelle de la Civic Graph Intelligence Platform (CGIP). 
Dans l'architecture du système, il est le seul à posséder un **Privilège Absolu** (Accès Souverain). La machine ne prend aucune décision légale : elle se contente de calculer des probabilités de risque et de soumettre des "Alertes" au Magistrat, qui seul possède le mandat légal d'agir.

## 2. Matrice des Droits (RBAC)
- **Niveau d'Accès** : Niveau 0 (Secret de l'instruction, données médicales, données sociales de l'Aide Sociale à l'Enfance - ASE).
- **Consultation du Graphe** : Totale. Le Magistrat voit le graphe complet sans aucun floutage ni masque cryptographique.
- **Droit d'Écriture** : Autorité de validation. Le Magistrat peut confirmer ou infirmer une déduction de l'Intelligence Artificielle (Boucle de Rétroaction).
- **Pouvoir de Décryptage** : Il possède la clé asymétrique permettant de lever l'anonymat d'une entité signalée par une école ou un hôpital.

## 3. Parcours Utilisateur (User Journey) : "La Levée d'Anonymat"

Ce parcours illustre la manière dont le Magistrat interagit avec le Tableau de Bord (Dashboard) face à une situation critique générée par la machine.

### Étape 1 : Réception de l'Alerte de Criticité
Le Magistrat se connecte à la plateforme CGIP. Sur son écran d'accueil, une alerte rouge clignote :
*« ALERTE : Trajectoire d'escalade détectée (Probabilité XGBoost : 92%). Score de certitude : Élevé. »*

### Étape 2 : Consultation de l'Explicabilité (Tableau de Bord IA)
Il clique sur l'alerte. Le système ne lui donne pas un nom, mais affiche un sous-graphe de crise (un "Cluster") autour d'un individu appelé "Individu_Hash_A8X9".
Le Magistrat lit la justification algorithmique (Valeurs SHAP) :
- *Facteur aggravant 1* : L'Individu_A8X9 est lié à 3 plaintes pour violence classées sans suite (Zone Police).
- *Facteur aggravant 2* : Le modèle GNN a détecté que cet individu gravite autour de l'École Rousseau.
- *Facteur déclencheur (Processus de Hawkes)* : Hier, un signalement social "anonymisé" a été poussé par le directeur de l'École Rousseau concernant un comportement menaçant. L'accélération temporelle a fait sauter le score de risque au-delà du seuil légal.

### Étape 3 : La Décision Judiciaire (Le Mur de Décision)
L'IA propose le bouton : **« Recommandation : Lever l'anonymat du signalement social pour enquête »**.
Le Magistrat étudie le graphe visuel. Il constate que la loi l'autorise à agir vu la gravité de la prédiction.
Il insère sa carte professionnelle (Authentification forte) et clique sur **« Approuver et Décrypter »**.

### Étape 4 : Le Bris de Silo
Immédiatement, l'Individu_A8X9 devient "Monsieur Jean Dupont". Le signalement anonyme de l'école devient lisible. Le Magistrat rédige un soit-transmis (ordre judiciaire) et l'envoie à la brigade de gendarmerie locale (l'Enquêteur) pour aller vérifier ce qu'il se passe au domicile de Jean Dupont.

## 4. Parcours Utilisateur : "La Boucle de Rétroaction" (Feedback Loop)

### Étape 1 : Le Faux Positif
Le Magistrat reçoit une alerte liant "Jeanne Martin" à un réseau de délinquance financière via une similarité de nom et d'adresses (Entity Resolution).

### Étape 2 : Rejet de la Machine
Après vérification rapide, le Magistrat comprend qu'il s'agit d'une homonymie parfaite que la machine n'a pas pu discerner, ou d'un lien trop faible.

### Étape 3 : Apprentissage Continu
Le Magistrat clique sur **« Faux Positif - Casser l'Arête »**. Il indique la raison : "Homonymie prouvée".
L'IA enregistre ce retour. La base de données Neo4j détruit l'arête probabiliste. Le modèle de Machine Learning intègre cette correction dans ses poids (Loss function) pour ne plus reproduire cette erreur de dédoublonnage à l'avenir. Le citoyen est protégé.
