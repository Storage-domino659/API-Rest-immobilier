# Etude-de-Cas-dsflow

Problématique
Dans le cadre d’un projet de création d’une application web de gestion immobilière, on nous demande de créer un ensemble de microservices. Ces microservices doivent permettre à un utilisateur de renseigner un bien immobilier avec les caractéristiques suivantes : nom, description, type de bien, ville, pièces, caractéristiques des pièces, propriétaire) et de consulter les autres biens disponibles sur la plateforme.

Nous souhaitons proposer aux utilisateurs les fonctionnalités suivantes :
Un utilisateur peut modifier les caractéristiques d’un bien (changer le nom, ajouter une pièce, etc… )
Les utilisateurs peuvent renseigner/ modifier leurs informations personnelles sur la plateforme (nom, prénom, date de naissance)
Les utilisateurs peuvent consulter uniquement les biens d’une ville particulière
Fonctionnalité bonus : Un propriétaire ne peut modifier que les caractéristiques de son bien sans avoir accès à l’édition des autres biens.
Objectif
Créer un microservice avec une API REST qui permet aux utilisateurs de réaliser toutes les fonctionnalités citées ci-dessus. Il n’est pas demandé de développer l’interface.

Choix technologiques
Langage : Python
Framework : Flask
Base de données : MySQL
Pas de Front
Livrable
Transmettre le code sous la forme d’un repository git (sur github par exemple), le Readme contiendra toutes les instructions pour pouvoir le faire tourner en local.

Critères d’évaluation
Méthodologie
de gestion de projet, cela devra être reflété dans l’historique Git
Modèle de données utilisé
Structuration de l’API REST
Structuration/ Architecture du code

Installation
pip install -r requirement.md

Sql install
Executer la DB et le CONTENT de bdd.sql dans MySQL

Lancer WampServer ou autres solutions

Changer user passeword dans bdd.py si nécessaire


Je n'ai pas fais de doc précises mais un modèle de chaque commande a exécuté pour communiquer avec l'api sont présent sous les fonctions concernés dans user.py et property.py.
Il faut éxécuter le dossier api.py afin de faire marcher l'api.


Piste d'amélioration:
- Utiliser autre chose que f-string pour empêcher injection de SQL dans la BDD
- Cryptage mdp avec clée SSH (par exemple)
- Ajouter des messages erreurs et confirmation lorsque un PUT POST OU DELETE se passe bien
- Préciser à l'utilisateur ce qu'il manque lorsqu'il se trompe sur une requête
- Ajouter un système de token ou de login pour pas que l'utilisateur ait a rentrer pseudo password a chaque requête (me parait plus logique de le construire coté client)
- Permettre à l'utilisateur de modifier plusieurs data sur un appartement ou son profil en même temps (pour ca je verrai aussi a l'aide d'une interface front ou l'utilisateur a toutes les données qui lui sont retransmis et il a juste à modifier celles qu'il souhaite. Cela me paraissait moins logique sous forme de requête)
- Interface graphique
- Faire des testes afin de vérifier que toutes les fonctionnalités marchent (via Postman)
- Rendre les Pseudos unique ou trouver une solution pour éviter les doublons afin d'avoir une db saine.