# Profil Utilisateur 2 : L'Enquêteur (Officier de Police Judiciaire)

## 1. Description du Rôle
L'Enquêteur (Policier, Gendarme, Analyste Criminel) est le bras armé de la Civic Graph Intelligence Platform (CGIP). Il mène les enquêtes sur le terrain et rassemble les preuves. 
L'IA lui sert de "moteur de recherche augmenté" pour trouver des liens invisibles entre des milliers de procédures disparates (Bris des silos territoriaux). Cependant, pour respecter la séparation des pouvoirs et la proportionnalité, l'Enquêteur ne possède pas un accès complet au système.

## 2. Matrice des Droits (RBAC)
- **Niveau d'Accès** : Niveau 1 (Limité aux procédures pénales, mains courantes, et bases de données policières type LRPPN/TAJ).
- **Consultation du Graphe** : Partielle. L'Enquêteur voit l'intégralité du Graphe de la "Délinquance", mais les nœuds issus du Niveau 2 (École, ASE, Hôpital) apparaissent sous forme de "Nœuds Noirs" floutés cryptographiquement.
- **Droit d'Écriture** : Enregistreur. L'Enquêteur nourrit massivement la base via la saisie de ses Procès-Verbaux (PV). L'IA extrait automatiquement les entités de ses textes.

## 3. Parcours Utilisateur (User Journey) : "Le Rapprochement Sériel"

Ce parcours montre comment l'Enquêteur utilise l'algorithme d'Entity Resolution et de Graph Analytics pour résoudre une enquête qui stagne (Cold Case ou sérialité invisible).

### Étape 1 : Le Blocage de l'Enquête Locale
Un OPJ enquête sur des dégradations répétées autour d'une installation sportive, commises par un individu se faisant appeler "Le Renard" (Pseudo). Aucune empreinte, aucune correspondance locale dans son logiciel de base de données territorial.

### Étape 2 : Requête dans le Graphe de la CGIP
Il se connecte à la CGIP et crée un "Nœud Dossier" contenant les attributs de son suspect non identifié : `Mode_Operatoire = vandalisme_sportif`, `Pseudo = Le_Renard`, `Localisation = Ville_A`.

### Étape 3 : L'IA propose une Arête Latente (Latent Link)
Le Graph Neural Network analyse ce sous-graphe et le compare aux millions d'autres dossiers nationaux. L'algorithme renvoie un résultat : 
*« Un profil similaire à 88% existe dans la Ville B (à 500km de là), condamné il y a 3 ans sous le nom de "Marc R.". Le Modus Operandi correspond parfaitement (Similarité Cosinus). »*

### Étape 4 : L'Enquêteur relance le terrain
L'Enquêteur clique sur l'arête proposée par l'IA. Le système lui ouvre le vieux dossier de la Ville B, lui fournissant l'identité de Marc R., qui s'avère avoir déménagé récemment dans la Ville A. L'affaire locale est résolue grâce à l'abolition du silo géographique.

## 4. Parcours Utilisateur : "La Limite Légale (Privacy by Design)"

Ce parcours démontre comment le système entrave volontairement l'Enquêteur pour protéger les citoyens contre une surveillance de masse abusive.

### Étape 1 : La Tentative de Profilage
L'Enquêteur enquête sur Marc R., désormais identifié. Il veut fouiller dans son passé pour voir s'il a été signalé lorsqu'il était à l'école ou par les services sociaux de sa commune d'origine.

### Étape 2 : Le Mur de Confidentialité Différentielle (Differential Privacy)
L'Enquêteur tape "Marc R." dans la barre de recherche globale. Le graphe s'affiche : il voit les anciennes condamnations (Niveau 1). 
Cependant, à côté du nœud de Marc R., le système affiche 3 arêtes pointant vers des `Nœuds Noirs` (Anonymisés). Une infobulle indique : 
*« 3 signalements extra-judiciaires existent pour cet individu (Source : Couche Zéro). Contenu verrouillé. »*

### Étape 3 : L'Escalade Procédurale
L'Enquêteur ne peut pas cliquer pour lire ces dossiers d'école. Le système lui interdit d'utiliser des signaux faibles scolaires pour étayer une accusation de vandalisme (Non-proportionnalité). 
S'il estime que ces informations sont absolument vitales (par exemple dans le cas d'une enquête pour terrorisme ou meurtre), il doit utiliser le bouton **« Demander la levée de l'anonymat au Magistrat »**. Seul le Juge pourra déverrouiller la cryptographie (voir Parcours Magistrat). Le pouvoir de fouille généralisée est bloqué par le logiciel lui-même.
