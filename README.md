## Contexte

Pour cette séance sur la publication de package, vous travaillerez en équipe.
Chaque équipe devra préparer et publier un package qui lui aura été attribué sur le repo
de test de PyPI (https://test.pypi.org/).

## Objectif final

Pouvoir installer les dépendances du fichier `requirements.repo.txt` via
`pip install -r requirements.repo.txt`.

N.B. : Remarquez que le fichier `requirements.repo.txt` utilise le
repo https://test.pypi.org/simple/ pour installer les dépendances.

Une fois les dépendances installées, vous pourrez normalement exécuter le script `main.py`.

## Étapes pour arriver à l'objectif

**Occupez vous seulement de VOTRE package.**

1. Créez un compte sur https://test.pypi.org/account/register/
2. Implémetez les fonctions de votre package (regarder les tests pour voir ce qui est attendu).
3. Préparez le package de votre équipe à sa publication (en créant un fichier `setup.py`). **Attention, les tests doivent passer sans erreur.**
4. Construisez les distributions de votre package en utilisant `setuptools`.
5. Publiez le package de votre équipe sur https://test.pypi.org/ en utilisant `twine`.
