# Dictionnaire de données — Onglet EQUIPEMENTS (GMAO Comores)

Schéma de l'onglet EQUIPEMENTS du classeur `GMAO_v0.1.xlsx`. Document de référence
tracé avec le code (`gmao_app/app.py`, liste `EQ_COLS`) et le formulaire de saisie
(`gmao_app/templates/equipements_form.html`). Toute évolution de structure doit être
répercutée simultanément ici, dans le code et dans le classeur (traçabilité schéma ↔ document).

- Colonnes 1 à 21 : structure de base (cahier des charges).
- Colonnes 19 et 20 : **calculées et protégées** — jamais écrasées par l'application.
- Colonnes 22 à 27 : **★ initiative**, ajoutées d'après le modèle d'inventaire de
  l'Annexe 4 du rapport de mission N°2 (P. Lopes, Expertise France) et le constat terrain.

| Col | Champ | Type | Liste / Source | Origine |
|----:|-------|------|----------------|---------|
| 1 | Code_Equipement | Texte | — | Cahier des charges |
| 2 | Designation | Texte | — | Cahier des charges |
| 3 | Categorie | Liste déroulante | LISTES.Categorie_Equip | Cahier des charges |
| 4 | Criticite | Liste déroulante | LISTES.Criticite | Cahier des charges |
| 5 | Service | Liste déroulante | LISTES.Service | Cahier des charges |
| 6 | Localisation | Texte | — | Cahier des charges |
| 7 | Marque | Texte | — | Cahier des charges |
| 8 | Modele | Texte | — | Cahier des charges |
| 9 | N_Serie | Texte | — | Cahier des charges |
| 10 | Date_Acquisition | Date JJ/MM/AAAA | — | Cahier des charges |
| 11 | Fournisseur | Liste (référentiel) | FOURNISSEURS (clé) | Cahier des charges |
| 12 | Garantie_Fin | Date JJ/MM/AAAA | — | Cahier des charges |
| 13 | Etat | Liste déroulante | LISTES.Etat_Equip | Cahier des charges |
| 14 | Date_Derniere_Maintenance | Date JJ/MM/AAAA | — | Cahier des charges |
| 15 | Prochaine_Maintenance | Date JJ/MM/AAAA | — | Cahier des charges |
| 16 | Periodicite_Mois | Liste déroulante | LISTES.Periodicite | Cahier des charges |
| 17 | Technicien_Referent | Liste (référentiel) | TECHNICIENS (clé) | Cahier des charges |
| 18 | Code_Package | Liste (référentiel) | PACKAGES (clé) | Cahier des charges |
| 19 | Nb_Composants | Calculé (protégé) | — | Cahier des charges |
| 20 | Composant_Defectueux | Calculé (protégé) | — | Cahier des charges |
| 21 | Observation | Texte long | — | Cahier des charges |
| 22 | Nom_Complementaire | Texte | — | ★ initiative |
| 23 | Provenance | Liste déroulante | LISTES.Provenance | ★ initiative |
| 24 | Ile | Liste déroulante | LISTES.Ile | ★ initiative |
| 25 | Conformite_Charte_Dons | Liste déroulante | LISTES.Conformite_Charte | ★ initiative |
| 26 | Reforme | Liste déroulante | LISTES.OuiNon | ★ initiative |
| 27 | Date_Reforme | Date JJ/MM/AAAA | — | ★ initiative |

## Listes déroulantes ajoutées (onglet LISTES)

| Colonne LISTES | Clé | Valeurs |
|---|---|---|
| Q | Provenance | Achat ministère ; Don OMS ; Don Emirats ; Don ONG ; Don diaspora ; Achat établissement ; Autre |
| R | Ile | Ngazidja ; Anjouan ; Mohéli |
| S | Conformite_Charte | Oui ; Non ; Non concerné |
| O | OuiNon (existante, réutilisée par Reforme) | Oui ; Non |

## Traçabilité vers la source documentaire

Les champs ★ initiative répondent aux constats et recommandations des rapports de mission :
- **Provenance** et **Conformité charte des dons** : recommandation N°4 (gestion des dons),
  90 %+ des équipements étant des dons non tracés.
- **Île** : recommandation N°2 (ateliers insulaires) — autonomie et consolidation par île.
- **Réformé / Date de réforme** : recommandation N°5 (traitement et élimination, circuit DEEE).
- **Désignation complémentaire** : libellé explicite, repris du mode opératoire d'inventaire.

**Version** : 4 juin 2026 — généré à partir de `EQ_COLS` (27 colonnes).