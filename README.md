# ***LITReview***

## Description

L'application LITReview permet aux utilisateurs de demander et rédiger des avis sur des oeuvres littéraires. Il est également possible de suivre d'autres utilisateurs.

## Installation et configuration

1. **Clôner le dépôt de l'application**

    Clôner le repository ou télécharger le dossier zip depuis github à l'adresse : *<https://github.com/Aura974/P9_ducap_aurore.git>*

2. **Installer l'application**

    * Se placer dans le répertoire de l'application

    * Créer et activer son environnement virtuel :
        *<https://docs.python.org/fr/3/tutorial/venv.html>*

    * Installer les packages requis présents dans le fichier Requirements.txt : `pip install -r Requirements.txt`

3. **Lancer l'application**

    * Se placer dans le sous-répertoire LITReview

    * Lancer la commande : `python manage.py runserver`

    * Ouvrez le lien de la page d'accueil : *<http://127.0.0.1:8000/>*

## Fonctionnement de l'application

L'application ne s'affiche que pour les utilisateurs connectés. La page d'accueil permet ainsi de renseigner ses identifier ou d'aller à la page de création d'utilisateur.

Une fois connecté, l'utilisateur est redirigé sur sa page d'accueil personnalisée, où apparaissent :  
    - les tickets (demandes d'avis) et critiques qu'il a rédigés  
    - les tickets et critiques rédigés par les utilisateurs qu'il suit  
    - les critiques rédigées en réponse à un de ses tickets (même s'il ne suit pas l'utilisateur-auteur)

Depuis cette page, il peut également créer un nouveau ticket ou rédiger une nouvelle critique (qui créera automatiquement un nouveau ticket).

Enfin, l'utilisateur pourra également répondre à des tickets auxquels il n'a pas encore répondu.

L'onglet *posts* affichera uniquement les tickets et critiques rédigés par l'utilisateur.

Enfin, l'onglet abonnement permet de suivre un autre utilisateur ou d'arrêter de le suivre, et de voir les personnes abonnées à l'utilisateur.
