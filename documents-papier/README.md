# Documents papier - GMAO Comores

Jeu de fiches papier à remplir à la main sur le terrain (choix du traitement papier),
puis à reporter dans la GMAO. Chaque fiche est calée sur un écran de l'outil et porte
la mention de correspondance pour la traçabilité fiche ↔ écran.

Format : HTML source (modifiable) + PDF A4 prêt à imprimer. Conventions respectées :
zéro emoji, dates JJ/MM/AAAA, palette alignée sur l'outil (#1F4E79), champs ★ initiative
(hors document source) en rouge.

## Les 6 documents

| # | Document | Fichier | Écran / champs GMAO | Place dans le flux |
|---|----------|---------|---------------------|--------------------|
| 1 | Fiche d'inventaire équipement | `fiche-inventaire-equipement` | EQUIPEMENTS (27 champs) | Mise en inventaire |
| 2 | Fiche d'intervention | `fiche-intervention` | INTERVENTIONS | Maintenance corrective / curative |
| 3 | Fiche de maintenance préventive | `fiche-maintenance-preventive` | MAINT_PREV | Maintenance préventive planifiée |
| 4 | Fiche de réception (PV simplifié) | `fiche-reception` | (amont) alimente EQUIPEMENTS | Réception achat / don |
| 5 | Fiche de réforme / sortie DEEE | `fiche-reforme-deee` | EQUIPEMENTS (Réformé / Date de réforme) | Fin de cycle / élimination |
| 6 | Mode opératoire de saisie | `mode-operatoire-saisie` | transversal (relie fiches et écrans) | Procédure |

## Flux de référence (cycle de vie de l'équipement)

Réception (4) → Mise en inventaire (1) → Maintenance préventive (3) et corrective (2)
→ Réforme / DEEE (5). Le mode opératoire (6) décrit comment reporter chaque fiche dans l'outil.

Référence schéma de données : `../data-models/data-dictionary-EQUIPEMENTS.md`
Sources documentaires : rapports de mission P. Lopes (Expertise France), Annexe 4 (modèle d'inventaire),
mode opératoire Asset+ (CHU Bordeaux), recommandations 9-1 (acquisition), N°4 (dons), N°5 (DEEE).

Webcreatys SAS - v1.0 - 04/06/2026
