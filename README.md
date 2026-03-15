# Projet-Fanafody-Algo

## Objectif

Cette application aide a trouver une ordonnance (combinaison de medicaments) selon:

- un budget disponible,
- la gravite des symptomes,
- l'efficacite des medicaments sur chaque symptome.

Un patient est considere "gueri" si, pour chaque symptome saisi, la gravite finale est <= 0.

## Nouvelles pages ordonnance

Trois pages ont ete ajoutees:

1. `GET /ordonnances`
    - saisie du budget et des gravites des symptomes.

2. `POST /ordonnances/evaluer` (resultats budget)
    - affiche les ordonnances qui guerissent et restent dans le budget.

3. `POST /ordonnances/evaluer` (fallback moins cher)
    - si aucune ordonnance guerissante n'entre dans le budget, affiche l'ordonnance guerissante la moins chere.

## Algorithme

Le calcul des ordonnances utilise une recherche **recursive** sans import de module externe:

- exploration des combinaisons de medicaments (prendre / ne pas prendre),
- verification de la guerison selon les reductions cumulees,
- extraction:
  - des ordonnances guerissantes dans le budget,
  - de l'ordonnance guerissante la moins chere au global.

Regle de conversion appliquee:

- `efficacite` est stockee sur 0-100,
- la reduction appliquee pendant l'algorithme est `efficacite / 10` (echelle gravite 0-10).