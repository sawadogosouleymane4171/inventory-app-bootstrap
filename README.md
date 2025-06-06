# Inventory App

Application web de gestion d’inventaire développée avec Django et Bootstrap 5.

## Fonctionnalités

- Ajout, modification et suppression de produits
- Visualisation de la liste des produits
- Interface utilisateur moderne et responsive grâce à Bootstrap 5
- Gestion des utilisateurs via l’interface d’administration Django

## Installation

1. **Cloner le repository**
   ```sh
   git clone <URL_DU_REPO>
   cd <nom_du_dossier>
   ```

2. **Installer les dépendances**
   ```sh
   pip install -r requirements.txt
   ```

3. **Appliquer les migrations**
   ```sh
   python manage.py migrate
   ```

4. **Créer un superutilisateur**
   ```sh
   python manage.py createsuperuser
   ```

5. **Lancer le serveur**
   ```sh
   python manage.py runserver
   ```

## Utilisation

- Accéder à l’application sur [http://localhost:8000/](http://localhost:8000/)
- Accéder à l’admin Django sur [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Auteur

- Sawadogo Souleymane

---

N’hésite pas à adapter ce fichier selon tes besoins spécifiques !
