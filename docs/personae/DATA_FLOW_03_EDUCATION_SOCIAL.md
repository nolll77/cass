# Flux de Données : Éducation & Travailleurs Sociaux (Niveau 2)

Ce document illustre le traitement des données pour les acteurs de terrain : Directeurs d'école, Aide Sociale à l'Enfance (ASE), et personnel éducatif. 
L'ingénierie doit garantir un fonctionnement en **"Écriture Seule" (Chambre Noire)** : ils alimentent l'IA en "Signaux Faibles", mais ne peuvent jamais requêter la base pour protéger le secret de l'instruction et ne pas stigmatiser préventivement les citoyens.

## Diagramme Séquentiel de l'Ingestion Aveugle

Le diagramme montre comment le signalement est traité par le pipeline NLP (Natural Language Processing), anonymisé, puis digéré par le Graphe sans jamais renvoyer d'informations accusatoires à l'émetteur.

```mermaid
sequenceDiagram
    autonumber
    actor T as Travailleur Social / École
    participant API as API Ingestion (Write-Only)
    participant NLP as Pipeline NLP (Extraction LLM)
    participant S as Sas Cryptographique (Hachage)
    participant G as Base Neo4j (Graphe)

    T->>API: 1. Saisit un rapport libre: "Léo a un comportement morbide"
    
    rect rgb(200, 200, 200)
        Note over API,T: LA CHAMBRE NOIRE (Aucun retour visuel)
        API-->>T: 2. "Rapport transmis et sécurisé." (Fin de la session)
    end
    
    rect rgb(250, 230, 200)
        Note over API,S: TRANSFORMATION ET ANONYMISATION
        API->>NLP: 3. Envoi du texte brut
        NLP->>NLP: 4. Extraction des Entités (Sujet: Léo, Concept: Violence latente)
        NLP->>S: 5. Requête d'Anonymisation
        S->>S: 6. Hash(Léo) = #L44B
    end
    
    S->>G: 7. Création du Nœud "Signalement École" lié à #L44B
    
    rect rgb(150, 200, 150)
        Note over G,G: LE DROIT À L'OUBLI (Time-To-Live)
        G->>G: 8. Ajout de la balise TTL = 365 Jours
        G-->>G: 9. Au bout de 1 an sans nouveau fait policier -> Nœud Effacé
    end
```

## Description Technique du Flux

1. **La Frappe Clavier (Étape 1)** : Le professionnel n'a pas accès à un logiciel complexe de police. Il utilise un portail sécurisé institutionnel très simple où il tape son texte en langage naturel.
2. **Fermeture de la Session (Étape 2)** : Le système est asynchrone. Dès l'envoi, la connexion est coupée. L'école ne sera jamais avertie si ce rapport a déclenché l'arrestation des parents de l'élève. C'est essentiel pour maintenir la confiance locale et la sérénité pédagogique.
3. **Le Pipeline IA (Étapes 3-4)** : Le modèle de langage (LLM) lit la phrase, comprend le contexte sémantique, et la décompose en composants graphiques (Nœuds et Arêtes).
4. **Anonymisation Légale (Étapes 5-6)** : La plateforme CGIP (qui appartient potentiellement à la Justice/Police) n'a pas le droit de détenir une base de données d'écoliers en clair. Le Sas Cryptographique transforme l'identité de l'élève en "Hash" mathématique indéchiffrable.
5. **Droit à l'Oubli Automatisé (Étapes 8-9)** : Neo4j possède une mécanique de "Time-To-Live". Si ce signalement reste isolé pendant un an, il sera automatiquement balayé de la base de données. Il n'y aura aucun "casier algorithmique" perpétuel. L'IA oublie les signaux faibles qui ne se transforment pas en délits.
