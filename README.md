## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Compte Circle Ci (pour la version Pipeline de déploiement)
- Compte Heroku (pour la version Pipeline de déploiement)
- Compte Sentry (pour la version Pipeline de déploiement)
- Compte Docker Hub (pour la version Pipeline de déploiement)
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.9 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone git@github.com:B-asile/P13_OCL.git'

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site en local

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- Aller dans oc_lettings_site, Settings.py commenter la SECRET_KEY actuelle et dé-commenter celle de Test
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

#### Exécuter le Pipeline de déploiement:
Prerequis Circle Ci:
Dans Project Settings, il faut indiquer les Variables d'environnement suivantes : 
- DOCKER_USER : correspondant au compte user de Docker Hub hébergeant les dockers
- DOCKER_PASS : correspondant au mot de passe du compte ci-dessus
- DEBUG : 'False' pour indiquer que le site est en production (Variable du Settings.py de Django)
- SECRET_KEY : Correspond à la clef nécessaire inscrite dans Settings.py du projet Django
- HEROKU_API_KEY : à récupérer dans les Settings de l'application Heroku

Prerequis HEROKU:
Dans Application Settings, Config Vars, il est nécessaire d'indiquer les variables d'envrionnement suivantes:
- DEBUG : 'False' pour indiquer que le site est en production (Variable du Settings.py de Django)
- SECRET_KEY : Correspond à la clef nécessaire inscrite dans Settings.py du projet Django
- PORT : 8000
- SENTRY_DSN : clef récupérable dans les Settings de l'application de surveillance SENTRY


Pour construire une image du site pour Docker et la pousse vers le registre des conteneurs du Docker Hub
`docker build -t dockeraccount/appname . construire une image`
`docker tag dockeraccount/appname dockeraccount/appname:versiontag`
`docker push dockeraccount/appname:versiontag`

Récupérer l'image du registre sur votre machine locale
`docker pull dockeraccount/appname:versiontag`
lancer le site localement en utilisant l'image
`docker run -p 8000:8000 dockeraccount/appname:versiontag`

le déploiement est configuré de manière à ce que seules les modifications apportées à la branche master dans GitHub 
déclenchent la conteneurisation et le déploiement du site.
Les modifications apportées aux autres branches déclenchent la compilation et les tests (sans déployer le site ou 
effectuer la conteneurisation).
Le pipeline de déploiement se répète à chaque Commit sur GitHub et peux être lancé directement sur CircleCi
La tâche de conteneurisation est exécutée que si la compilation et les tests sont réussies.