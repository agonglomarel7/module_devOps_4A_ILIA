# module_devOps

# TD n°1 : Manipuler un dépôt de code source avec Git

# Commandes Git : Explications et Différences

## 1. Différence entre `git reset HEAD^1` et `git revert [last_commit]`

### **`git reset HEAD^1`**
- **Description** : Supprime complètement le dernier commit, ainsi que ses modifications, de l’historique Git local.  
- **Impact** : 
  - Après cette commande, le commit précédent devient le dernier commit.
  - Si des fichiers modifiés dans ce commit existent encore dans le répertoire de travail, ils seront déplacés dans la **staging area** (zone d’index).
- **Usage** :
  ```bash
  git reset HEAD^1
  ```
  Supprime le dernier commit.

- **Attention** : Cette commande réécrit l’historique et peut poser des problèmes si vous avez déjà partagé votre travail.

---

### **`git revert [last_commit]`**
- **Description** : Crée un nouveau commit pour annuler les modifications du dernier commit, sans réécrire l’historique.  
- **Impact** : 
  - L'historique Git reste intact.
  - Le commit annulé est suivi d’un nouveau commit précisant l’annulation.

- **Usage** :
  ```bash
  git revert [last_commit]
  ```
  Annule les modifications apportées par le commit `[last_commit]`.

- **Quand utiliser ?**
  - **`git reset`** : Utilisé pour corriger des erreurs localement avant de partager.
  - **`git revert`** : Utilisé pour annuler des modifications dans un projet déjà partagé avec d'autres.

---

## 2. À quoi sert `git fetch` ?

- **Description** : Télécharge les branches et les données depuis le dépôt distant, sans intégrer automatiquement les modifications dans votre branche locale.  
- **Usage** :
  ```bash
  git fetch
  ```
  Récupère les mises à jour du dépôt distant.

- **Différence avec `git pull`** :
  - `git fetch` : Récupère les changements, mais ne les fusionne pas automatiquement avec votre branche locale.
  - `git pull` : Récupère les changements et fusionne automatiquement les modifications avec la branche locale.

- **Cas d'utilisation** :
  - Examiner les changements sur le dépôt distant avant de les intégrer localement.

---

## 3. Commandes spécifiques : 
### `git checkout main`
- **Description** : Bascule vers la branche nommée `main`.  
- **Usage** :
  ```bash
  git checkout main
  ```
  - Si vous êtes dans une autre branche, cette commande vous place sur la branche `main`.
  - Si vous avez des modifications non enregistrées, Git demandera de les **stager**, **commiter** ou **stash** avant le changement.

---

### `git rebase bugFix`
- **Description** : Rebase (réapplique) les commits de la branche actuelle sur ceux de la branche `bugFix`.  
- **Usage** :
  ```bash
  git rebase bugFix
  ```
- **Fonctionnement** :
  - Reorganise les commits pour que la branche courante intègre les commits de `bugFix` avant les siens.
  - Cela crée un historique plus linéaire, évitant les "merge commits".

- **Attention** :
  - Réécrit l’historique de commits.
  - À éviter si vous avez partagé votre branche avec d'autres.

---

## Résumé des Commandes

| Commande                | Action                                                                                           |
|-------------------------|--------------------------------------------------------------------------------------------------|
| `git reset HEAD^1`      | Supprime complètement le dernier commit localement (réécrit l’historique).                      |
| `git revert [last_commit]` | Annule un commit en créant un nouveau commit d’annulation (ne modifie pas l’historique).       |
| `git fetch`             | Récupère les données distantes sans les fusionner dans la branche locale.                       |
| `git checkout main`     | Change de branche pour `main`.                                                                  |
| `git rebase bugFix`     | Rebase la branche actuelle sur `bugFix`, créant un historique linéaire.                         |

--- 


# TD n°2 : GitHub Action, Issue and Pull Request

  Dans ce Td, nous allons manipuler un dépôt de code source avec l'outil Git.

  Ci-joint le prénom et le nom des chaque membre du projet

  - Marel AGONGLO
    - Spécialité : ILIA
    - [Lien Git](https://github.com/agonglomarel7/)
  - Johanu GANDONOU

    ![Logo du projet](https://www.u-bourgogne.fr/wp-content/uploads/LOGO_ub_jpeg_filet_orange_2019.jpg)


# Statuts actions

Ce projet est actuellement en développement Nous allons automatiser notre dépôt
