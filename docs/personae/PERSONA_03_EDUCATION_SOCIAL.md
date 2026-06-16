# Profil Utilisateur 3 : Le Travailleur Social & Personnel Éducatif

## 1. Description du Rôle
Ce profil englobe les Directeurs d'Établissements Scolaires, les Éducateurs Spécialisés, les Assistants Sociaux de l'ASE (Aide Sociale à l'Enfance) et potentiellement le personnel médical.
Dans l'architecture de la CGIP, ces acteurs sont les "Capteurs Périphériques" (Couche Zéro). Ils sont les seuls capables de détecter les "Signaux Faibles" (comportements étranges, bleus inexpliqués, décrochage brutal) qui précèdent souvent une explosion de violence ou la commission d'un crime grave.

## 2. Matrice des Droits (RBAC)
- **Niveau d'Accès** : Écriture Seule (Write-Only). Ce profil opère sur la "Couche Zéro" du réseau.
- **Consultation du Graphe** : Interdite. Le personnel éducatif n'a physiquement aucun accès à l'interface de visualisation du Graphe ou de requêtage de la base Neo4j.
- **Droit d'Écriture** : Partiel. Ils envoient des "Alertes" ou des "Notes de terrain" en langage naturel vers un endpoint sécurisé.
- **Principe Légal** : Pour qu'un directeur d'école soit à l'aise pour signaler un pressentiment sans avoir peur de "détruire la vie d'un élève", il faut que son rapport soit ingéré de façon anonyme et ne déclenche pas l'envoi immédiat de la police, mais alimente le modèle IA dans l'ombre.

## 3. Parcours Utilisateur (User Journey) : "La Détection du Signal Faible"

Ce parcours illustre l'importance capitale du travailleur social pour rompre l'aveuglement temporel du système judiciaire, tout en protégeant son anonymat.

### Étape 1 : Constatation d'un comportement inquiétant
Une éducatrice spécialisée remarque qu'un adolescent, Léo, devient subitement extrêmement agressif avec ses camarades, et dessine des scènes de violence macabres dans ses carnets, sans qu'aucun délit ne soit formellement commis. Elle sait qu'appeler la police serait disproportionné ("il n'a rien fait").

### Étape 2 : Ingestion via le Sas d'Anonymisation
L'éducatrice utilise un portail sécurisé du ministère de l'Éducation relié au pipeline Kafka de la CGIP. Elle y rédige son rapport détaillé en texte libre : *« Léo présente une fascination morbide soudaine, dessine des armes, et refuse de parler de la situation à son domicile. »*
Elle valide. Le rapport disparaît de son écran.

### Étape 3 : Le Traitement en Chambre Noire (Machine Learning)
Le rapport arrive dans le pipeline de la CGIP :
1. **NLP (LLM)** : L'IA extrait les entités (Léo, École X, Maltraitance Suspectée) et structure la phrase en arêtes mathématiques.
2. **Graph Connection** : L'IA insère le Nœud `[Signalement École]` dans le Graphe global.
3. **Le Choc Sériel** : En croisant Léo avec l'adresse de son domicile, l'IA se rend compte que l'adresse est liée à 4 plaintes de voisinage pour violences domestiques (Dossier Police) et que le père de Léo a été récemment signalé par le tribunal (Dossier Justice).

### Étape 4 : L'Alerte au Magistrat (Aucun retour à la source)
L'accumulation des données Police + Justice + École crée une accélération temporelle (Modèle de Hawkes). L'IA génère immédiatement une "Alerte de Criticité Rouge" sur le bureau du Juge (Persona 1).
Le Magistrat verra que c'est le signal de l'éducatrice qui a fait déborder le modèle, et enverra les services sociaux ou la police au domicile pour sauver l'enfant.

**Point Clé du Parcours** : L'éducatrice ne recevra *aucune* notification de l'IA lui disant "votre élève est le fils d'un criminel". Elle reste dans l'ignorance totale (pour ne pas biaiser son travail pédagogique et préserver la confidentialité pénale), mais son acte de saisie a permis d'empêcher un drame.

## 4. Parcours Utilisateur : "Le Droit à l'Oubli (TTL)"

### Étape 1 : Fin de la Fenêtre de Tir
Imaginons que le signalement de l'éducatrice concernant Léo soit isolé (il passait juste une mauvaise semaine, aucun lien avec la police ou la justice).

### Étape 2 : Nettoyage Automatique
Le Nœud `[Signalement École]` est injecté dans le Graphe avec une balise cryptographique "Time-To-Live (TTL) = 365 jours".
Puisqu'aucun autre événement judiciaire n'est venu s'y accrocher pendant un an, la base de données efface mathématiquement et irréversiblement l'alerte à la fin de la période scolaire. L'adolescent n'aura aucun "casier algorithmique" qui le suivra au lycée.
