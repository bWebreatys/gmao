# GMAO - Gestion de la Maintenance des Appareils Opérationnels

## 📋 Description

Outil de gestion de maintenance pour le parc d'équipements biomédicaux et matériel des services généraux aux Comores.

**Statut:** Version 0.1 - Prototype pour élicitation et discussion

### Fonctionnalités couvertes

- **Gestion d'équipements** : Inventaire biomédical par établissement
- **Gestion de matériel** : Composants défectueux, packages
- **Gestion d'outillage** : Matériel des services généraux
- **Maintenance préventive** : Calendrier de maintenance planifiée
- **Interventions** : Historique des réparations (préventives et correctives)
- **Gestion des pièces** : Stock et suivi des consommables
- **Alertes** : Non-conformités et équipements critiques
- **Tableaux de bord** : KPIs de disponibilité, délais, coûts
- **Consolidation nationale** : Vue multi-établissements

## 🚀 Démarrage rapide

### Prérequis
- Python 3.8+
- Flask
- openpyxl

### Installation
```bash
# 1. Cloner le repo
git clone https://github.com/bWebreatys/gmao.git
cd gmao

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer l'application
python lancer_gmao.py

# 4. Ouvrir le navigateur
# http://127.0.0.1:5000
```

## 📁 Structure du projet

```
gmao/
├── README.md                          # Ce fichier
├── requirements.txt                   # Dépendances Python
├── GMAO_v0.1.xlsx                    # Données (évolutif)
├── app.py                            # Serveur Flask
├── lancer_gmao.py                    # Lanceur avec ouverture navigateur
├── data-models/
│   ├── data-dictionary.md            # Dictionnaire des données
│   ├── inventory-mapping.md          # Mapping avec fiche inventaire
│   └── screen-list.md                # Liste des écrans de saisie
├── documentation/
│   ├── GMAO-guide-utilisateur.docx   # Guide utilisateur
│   ├── GMAO-guide-admin.docx         # Guide administrateur
│   └── formules-gmao.txt             # Formules Excel
├── reference-data/
│   ├── fiche-inventaire-comores.xlsx # Fiche actuellement utilisée
│   └── data-mapping.md               # Correspondance données
└── templates/
    ├── base.html                     # Layout principal
    ├── equipements_list/form         # Écrans équipements
    ├── materiels_list/form           # Écrans composants/packages
    ├── outillage_list/form           # Écrans outillage
    ├── maint_prev_list/form          # Écrans maintenance préventive
    ├── interventions_list/form       # Écrans interventions
    ├── pieces_list/form              # Écrans pièces détachées
    ├── fournisseurs_list/form        # Écrans fournisseurs
    ├── techniciens_list/form         # Écrans techniciens
    └── ...
```

## 📊 Onglets Excel - Données

| Onglet | Description | Statut |
|--------|-------------|--------|
| **ACCUEIL** | Navigation principale | ✅ |
| **EQUIPEMENTS** | Inventaire biomédical | ✅ |
| **COMP_PACKAGES** | Composants défectueux + Packages | ✅ |
| **OUTILLAGE** | Matériel services généraux | ✅ |
| **MAINT_PREV** | Plan de maintenance préventive | ✅ |
| **INTERVENTIONS** | Historique interventions | ✅ |
| **FOURNISSEURS** | Référentiel prestataires/contrats | ✅ |
| **PIECES** | Stock pièces détachées | ✅ |
| **TECHNICIENS** | Référentiel techniciens | ✅ |
| **ALERTES** | Non-conformités et anomalies | ✅ |
| **BILANS_GMAO** | Tableaux de bord KPIs | ✅ |
| **NOMENCLATURE** | Documentation formules | ✅ |
| **LISTES** | Listes déroulantes (masqué) | ✅ |

## 🎯 Points clés pour l'élicitation

### Données actuellement modélisées

**Équipements biomédicaux** :
- ✅ Code équipement, désignation, fabricant, modèle
- ✅ Numéro de série, année d'achat
- ✅ Localisation (établissement, service, bureau)
- ✅ État, statut (disponible/en réparation/immobilisé)
- ✅ Historique des interventions

**Composants & Packages** :
- ✅ Différenciation Composant vs Package
- ✅ Lien équipement → ses composants
- ✅ Défaut identifié, statut (à commander/commandé/remplacé)

**Outillage** :
- ✅ Code, désignation, type d'outil
- ✅ Localisation, état, responsable
- ✅ Historique d'utilisation

**Interventions** :
- ✅ Numéro intervention, date, durée
- ✅ Équipement OU Outillage concerné
- ✅ Type (préventive/corrective), statut
- ✅ Technicien, pièces utilisées, durée

### À clarifier sur place

- ⚠️ **Numérotation** : Comment numéroter les équipements ? (fabricant + N° série ? code interne ?)
- ⚠️ **Criticité** : Classification équipements (critique/important/standard) ?
- ⚠️ **Fournisseurs** : Sont-ils tous les mêmes pour biomédical et services généraux ?
- ⚠️ **Pièces détachées** : Stock centralisé ou par établissement ?
- ⚠️ **Techniciens** : Spécialisations requises (biomédical vs outillage) ?
- ⚠️ **Coûts** : Faut-il tracker heures technicien + pièces pour coûter les interventions ?
- ⚠️ **Contrats** : Y a-t-il des contrats de maintenance avec des prestataires ?
- ⚠️ **Intégration SIH** : Liaison avec le futur DIH (Dossier d'Information Hospitalier) ?

## 📦 Correspondance avec fiche inventaire actuelle

La fiche inventaire actuellement utilisée (`fiche-inventaire-comores.xlsx`) contient **62 lignes** avec les colonnes suivantes. Le mapping vers la structure GMAO v0.1 est documenté dans `/reference-data/data-mapping.md`.

**Colonnes identifiées** :
- Établissement / Service
- Équipement (désignation)
- Fabricant / Modèle
- État (Fonctionnel / Défectueux / En réparation)
- Données d'entretien/maintenance

**À clarifier** :
- [ ] Quels champs de la fiche actuelle sont essentiels ?
- [ ] Quels champs doivent être scindés ou renommés pour la structure GMAO ?
- [ ] Y a-t-il d'autres colonnes à ajouter ?

## 🔧 Configuration

### Base de données
L'outil utilise un **fichier Excel structuré** avec formules, listes déroulantes et mises en forme conditionnelles. Aucune base de données SQL.

### Utilisateurs
- **Techniciens BM** : saisie interventions équipements biomédicaux
- **Techniciens SG** : saisie interventions outillage
- **Admin** : création équipements, gestion stock, paramètres
- **Direction** : consultation tableaux de bord

## 📝 Notes de développement

- **Version** : 0.1 (prototype)
- **Framework** : Flask (Python)
- **Base données** : Excel (openpyxl)
- **Interface** : HTML/CSS/JavaScript
- **Déploiement** : Local (Windows/Linux) ou réseau
- **Robustesse** : 13 onglets, ~600 formules, 0 erreur de validation

## 🤝 Élicitation et feedback

### Phases de discussion

1. **Semaine 1** : Présentation écrans et onglets actuels
2. **Semaine 2** : Collecte remarques par établissement pilote
3. **Semaine 3** : Ajustements et validation
4. **Semaine 4** : Gel de la structure des données et documentation finale

### Points de collecte

Pour chaque onglet, demander :
- [ ] Colonnes manquantes pour votre utilisation ?
- [ ] Colonnes inutiles ou mal nommées ?
- [ ] Champs qui devraient être obligatoires/optionnels ?
- [ ] Validations à mettre en place ?
- [ ] Listes déroulantes à adapter ?

## 📞 Support

Bernard Leglise - Webcreatys SAS
contact@webcreatys.com

---

**Dernière mise à jour** : 22 mai 2026
**Prochaines étapes** : Élicitation sur place (juin-juillet 2026)
**Architecture future** : Recommandations WinDev/web dans la note de cadrage
