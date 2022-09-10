## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

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

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
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
- Lancer une requête sur la table des profils, `select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

Fichier des variables environnements local sont disponibles à l'adresse : `oc_lettings_site/settings/.env`

**Particularités :**  
oc_lettings_site/settings contient plusieurs fichiers.
local.py est le fichier de setting local et du docker.
heroku.py est le fichier de setting pour l'application heroku.

le fichier **init**.py dans le dossier settings permet d'utiliser le code de l'un ou l'autre en fonction de l'environnement utilisé.

le fichier .env doit contenir au minimum les lignes suivantes en mode local : (Bien entendu ce sont de fausses données)  
`SECRET_KEY='fp$9^59[3]sriajg$_%]=5trot9g!1qa@ew(o-1#@=&4%=hp46(s'`
`ALLOWED_HOSTS=localhost,127.0.0.1,[::1],0.0.0.0,.herokuapp.com` # Cette ligne est facultative en mode debug=True

Ou l'environnement doit les définir. Au choix, l'environnement sera toujours prioritaire.

**Pré-requis :**

- Un compte/acces Github
- Un compte/acces CircleCi
- Un Compte/acces DockerHub
- Un Compte/Acces Heroku
- Un Compte/Acces Sentry

### Description du fonctionnement du Pipeline CircleCi

#### Lors d'un commit sur n'importe quelle branche autre que la master :

- workflow 'test-the-application' du Pipeline (le dépôt) Python-OC-Lettings-FR.
  - Il est décomposé en différents 'jobs':
    - test :
      - va lancer les tests (via pytests)
      - contrôler le linting PEP8 via Flake8

#### Lors d'un commit sur la branche master :

- le workflow push-the-application va se lancer
  - Sa réussite du job ‘test’, va déclencher:
    - build push docker:
      - Cela va créer une image docker et l'uploader sur le docker hub.
      - Il y aura 2 push identiques mais tagué différemment (1 hash du commit et 1 lastest le dernier)
        Cela a pour but de facilité le déploiement rapide en local sur la dernière version.
    - deploy:
      Va lancer le build de l'application sur Heroku via Git.

---

## CircleCi :

Paramétrage nécessaire :

Création des variables d'environnement au niveau du projet :

- Dans **Projets**:
- Cliquez sur `Project Settings` (Les 3 petits points)
- Cliquez sur `Environment Variables`
- Cliquez sur `Add Environment Variables`

| Nom des Variables | Description                             | Valeurs à renseigner                                                         |
| ----------------- | --------------------------------------- | ---------------------------------------------------------------------------- |
| DOCKER_USER       | User Docker Hub                         | `marinebdlt`                                                                 |
| PASSWORD          | Token Dockerhub ou Mdp                  |`Papapapa1218*`   |
| HEROKU_API_KEY    | API Token Heroku                        | `3860530-81a3-4da2-a2e1-cf77cea0fbcf`                                       |
| SENTRY_DSN        | URL Sentry                              | `https://c572ef3b0f2340a6ad81447ba2d16b1c@o1401908.ingest.sentry.io/6734060` |
| SECRET_KEY        | DJANGO SECRET_KEY                       | `fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s`                         |
| ENV_NAME          | Le nom de l'environnement de production | `heroku `         |

---

## Github :

[Github Repository](https://github.com/marinebdlt/Python-OC-Lettings-FR) permet de faire le versionning de notre projet/application.

---

## Docker Hub :

[Docker-Hub marinebdlt Repository](https://hub.docker.com/repository/docker/marinebdlt/lettings) permet de stocker en ligne l'image docker de notre application.

La commande unique pour récupération de l'application en local et son démarrage immédiat est :

`docker run --pull always -p 8000:8000 --name P13-Application marinebdlt/lettings:lastest`

- P13-Application est le nom de l'application docker
- marinebdlt est le compte du Hub Docker
- lastest peux être remplacé par le hash du commit. Comme son nom l'indique lastest est le dernier commit.

---

## Heroku :

[L'application sur Heroku](https://oc-lettings-app.herokuapp.com/)

Heroku permet d'heberger notre application.
En cas de necessité ou en cas de suppression, il faut créer l'application 'oc-lettings-512'.  
Info pour que l'application fonctionne, il faut définir plusieurs variables. C'est le workflows CircleCI qui s'en charge.
Les variables sont :

- SENTRY_DSN
- SECRET_KEY

---

## Sentry :

Sentry permet de faire le [monitoring de l'application](https://sentry.io/organizations/openclassrooms-zm/projects/oc-lettings/?project=6734060).

Elle permet également de détecter des éventuels bug/issues.

Mais il faut pour cela intégrer le sentry-sdk et la variable dans settings.py (heroku.py dans notre application).
