# AXEL_WEB

Interface Web de gestion des données de l'intelligence artificielle A.X.E.L.

## Getting Started

Penser à spécifier l'interpreteur python du projet (Intrepreter Python 3.6 disponible dans venv2) et à faire l'installation de tous les paquets grâce au fichier requirements.txt afin d'être sûr qu'aucun module ne manque.

```
python -m pip install -r requirements.txt
```

### Prérequis

Aucun prérequis n'est nécessaire pour faire tourner l'application étant donné que tout a été empaqueté dans un environnement virtuel "venv2" disponible ici.

### Installation

Vous avez besoin d'installer ou utiliser une base PostgreSQL afin de pouvoir enregistrer vos objets.
Ne pas oublier les commandes de migration avant de lancer l'application.

```
python manage.py makemigrations
python manage.py migrate
```

Pour lancer le serveur de développement, il vous suffit d'entrer cette commande une fois la migration te le paramètrage de l'interpreteur effectués

```
python manage.py runserver
```

Le serveur se lancera automatiquement sur l'adresse http://localhost:8000 ou http://127.0.0.1:8000

## Lancer les tests

Executez la commande ci-dessous à partir du dossier racine afin de lancer tous les tests du projet.

```
python manage.py test
```

Les tests sont effectués sur les différentes méthodes CRUD des modèles.

## Déploiement

Afin de déployer l'application plusieurs choix s'offrent à nous.

* [NGINX/Gunicorn](https://docs.gunicorn.org/en/latest/deploy.html) - Serveur NGINX
* [AWS](https://aws.amazon.com/fr/) - Amazon Web Services est spécialisée dans les services de cloud computing à la demande pour les entreprises et particuliers.
* [Azure](https://azure.microsoft.com/fr-fr/) - Microsoft Azure est la plate-forme applicative de cloud computing de Microsoft.
* [Heroku](https://www.heroku.com/) - Heroku est une plateforme en tant que service (PaaS) permettant de déployer des applications sur le Cloud très facilement.
* [PythonAnywhere](https://www.pythonanywhere.com/) - PythonAnywhere est un environnement de développement intégré en ligne et un service d'hébergement Web basé sur le langage de programmation Python.

J'ai choisi la solution Heroku pour sa simplicité et sa gratuité.

Tout d'abord installer [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) et creer un compte.

**Ne surtout pas oublier le fichier Procfile ainsi que d'enlever le DEBUG dans les settings.py**

Effectuer les migrations à distance
```
heroku run python manage.py makemigrations -a appname
```
Migrer les modifications à distance
```
heroku run python manage.py makemigrations -a appname
```
Mise à l'echelle Web des dynos
```
heroku ps:scale web=1 -a appname
```

## Outils

* [Python](https://www.python.org/) - Python est un langage de programmation interprété, multi-paradigme et multiplateformes.
* [Django](https://www.djangoproject.com/) - Django est un framework web écrit en Python.
* [Pip](https://pypi.org/project/pip/) - Pip est un gestionnaire de paquets utilisé pour gérer des paquets écrits en Python.
* [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/) - Environnement de Developpement Intégré Python

## Intégration Continue

* [CircleCI](https://circleci.com/) - CircleCI automates your software builds, tests, and deployments.

Execution à chaque "git push" d'un job de lancement de build et de test sur la branche "Production" avant le build de déploiement sur Heroku.

## Monitoring et tracking d'erreurs

* [Sentry](https://sentry.io/) - Sentry est une plate-forme de surveillance des applications qui vous aide à identifier les problèmes en temps réel.

## Review de code

* [CodeFactor](https://www.codefactor.io/) - CodeFactor.io suit automatiquement et en permanence la qualité du code à chaque demande de commit et pull de GitHub ou BitBucket, ce qui permet aux développeurs de logiciels de gagner du temps dans la révision du code et de s'attaquer efficacement à la dette technique.


## Versioning

J'utilise Git pour le versionning et je transfère mes dépôts sur ce compte GitHub.

## Auteurs

* **CHAABI Samy** - *Développeur & Architecte* - [xhackax47](https://github.com/xhackax47)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
