# Inventory App

Application web de gestion d’inventaire développée avec **Django** et **Bootstrap 5**.

---

## Sommaire

- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
  - [Installation recommandée avec pipenv](#installation-recommandée-avec-pipenv)
- [Utilisation](#utilisation)
- [Gestion des dépendances](#gestion-des-dépendances)
- [Auteur](#auteur)

---

## Fonctionnalités

- Ajouter, modifier et supprimer des produits
- Visualiser la liste des produits
- Interface utilisateur moderne et responsive (Bootstrap 5)
- Gestion des utilisateurs via l’interface d’administration Django

---

## Prérequis

- Python 3.8 ou supérieur
- [pip](https://pip.pypa.io/en/stable/) ou [pipenv](https://pipenv.pypa.io/en/latest/)
- Git

---

## Installation

### Installation recommandée avec pipenv

1. **Cloner le repository**
   ```sh
   git clone <URL_DU_REPO>
   cd <nom_du_dossier>
   ```

2. **Installer pipenv** (si besoin) :
   ```sh
   pip install pipenv
   ```

3. **Créer l'environnement virtuel** :
   ```sh
   pipenv shell
   ```

4. **Installer les dépendances principales** :
   ```sh
   pipenv install django pillow django-crispy-bootstrap5 
   ```


5. **Créer les migrations**
   ```sh
   python manage.py makemigrations
   ```

6. **Appliquer les migrations** :
   ```sh
   python manage.py migrate
   ```

7. **Créer un superutilisateur** :
   ```sh
   python manage.py createsuperuser
   ```

8. **Lancer le serveur** :
   ```sh
   python manage.py runserver
   ```

---

## Utilisation

- Accéder à l’application : [http://localhost:8000/](http://localhost:8000/)
- Accéder à l’interface d’administration : [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## Gestion des dépendances

- **Pipfile** : décrit les dépendances principales et de développement du projet (remplace `requirements.txt`).
- **Pipfile.lock** : fige précisément les versions de chaque dépendance pour garantir la reproductibilité de l’environnement.

Pour ajouter d'autres dépendances, utilise par exemple :
```sh
pipenv install <nom_du_paquet>
```

Pour générer un `requirements.txt` à partir de pipenv :
```sh
pipenv lock --requirements > requirements.txt
```

---

## Auteur

- Sawadogo Souleymane

---

_N’hésite pas à adapter ce fichier selon tes besoins spécifiques !_
