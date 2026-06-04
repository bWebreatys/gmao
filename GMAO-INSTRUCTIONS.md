# GMAO – Interface de saisie locale  (v2)

## Contenu du dossier

```
GMAO_v0.1.xlsx          ← Fichier Excel (données + formules)
lancer_gmao.py           ← Double-clic ou : python lancer_gmao.py
gmao_app/
  app.py                 ← Serveur Flask (logique métier complète)
  templates/
    base.html                 gabarit commun, navigation, CSS, modal
    equipements_list/form     🔧 Équipements
    composants_list/form      🔩 Composants (onglet initiative)
    packages_list/form        📦 Packages (onglet initiative)
    maint_prev_list/form      🗓️ Maintenance préventive
    interventions_list/form   🛠️ Interventions
    fournisseurs_list/form    🏢 Fournisseurs
    pieces_list/form          🗄️ Pièces détachées
    techniciens_list/form     👷 Techniciens
```

## Prérequis

```bash
pip install flask openpyxl
```

## Lancement

```bash
python lancer_gmao.py
```
→ Le navigateur s'ouvre sur **http://127.0.0.1:5000**

## Fonctionnalités par écran

| Onglet         | Liste filtrée | Formulaire | Code auto | Formules protégées |
|----------------|:---:|:---:|:---:|:---:|
| EQUIPEMENTS    | ✓   | ✓   | EQ0001   | Nb_Composants, Composant_Defectueux |
| COMPOSANTS     | ✓   | ✓   | COMP001  | Designation_Equip |
| PACKAGES       | ✓   | ✓   | PKG001   | Nb_Equip_Package, Nb_Composants_Def |
| MAINT_PREV     | ✓   | ✓   | MP0001   | Designation, Retard_Jours |
| INTERVENTIONS  | ✓   | ✓   | INT0001  | Designation, Jours_Ouvert |
| FOURNISSEURS   | ✓   | ✓   | FOUR001  | — |
| PIECES         | ✓   | ✓   | PC001    | Alerte_Stock |
| TECHNICIENS    | ✓   | ✓   | TECH01   | Charge_Interventions |

## Règles appliquées

- **Formules jamais écrasées** : les colonnes `=COUNTIF(…)`, `=VLOOKUP(…)` etc. sont
  affichées en lecture seule dans les formulaires et jamais modifiées par l'app.
- **Dates** : saisie et stockage au format `JJ/MM/AAAA` (converti en date Excel native).
- **Champs initiative** ★ : signalés en rouge, ils correspondent aux onglets/colonnes
  ajoutés au-delà du document source GMAO.
