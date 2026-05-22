# 📦 Guide Complet d'Installation - GMAO

> **Avant de commencer** : Lire le document `PREREQUIS-INSTALLATION-COMPLET.md` pour les versions Python et droits d'accès.

## 🚀 Installation rapide (5 minutes)

### Pour Windows

```powershell
# 1. Télécharge Python 3.10 (cocher "Add to PATH")
# https://python.org/downloads

# 2. Clone ou télécharge le projet
git clone https://github.com/bWebreatys/gmao.git
cd gmao

# 3. Crée un environnement virtuel (recommandé)
python -m venv venv
.\venv\Scripts\activate

# 4. Installe les dépendances
pip install -r requirements.txt

# 5. Lance l'appli
python lancer_gmao.py

# 6. Ouvre le navigateur
# http://127.0.0.1:5000
```

### Pour Linux/Mac

```bash
# 1. Installe Python 3.10
sudo apt install python3.10 python3-pip

# 2. Clone le projet
git clone https://github.com/bWebreatys/gmao.git
cd gmao

# 3. Crée un environnement virtuel
python3 -m venv venv
source venv/bin/activate

# 4. Installe les dépendances
pip install -r requirements.txt

# 5. Lance l'appli
python lancer_gmao.py

# 6. Ouvre le navigateur
# http://127.0.0.1:5000
```

---

## ⚙️ Configuration détaillée

### Étape 1 : Prérequis

- ✅ Python 3.8+ (vérifie avec `python --version`)
- ✅ pip (vérifie avec `pip --version`)
- ✅ 200 MB espace disque minimum
- ✅ Navigateur web récent

### Étape 2 : Télécharger le projet

**Option A : Avec Git**
```bash
git clone https://github.com/bWebreatys/gmao.git
cd gmao
```

**Option B : Sans Git (télécharge le ZIP)**
1. Va sur https://github.com/bWebreatys/gmao
2. Clique "Code" → "Download ZIP"
3. Décompresse le fichier
4. Va dans le dossier `gmao-main`

### Étape 3 : Environnement virtuel (RECOMMANDÉ)

```bash
# Créer
python -m venv venv

# Activer (Windows)
.\venv\Scripts\activate

# Activer (Linux/Mac)
source venv/bin/activate

# Vérification : prompt doit afficher (venv) en début
(venv) C:\Users\PC\gmao>
```

### Étape 4 : Installer les dépendances

```bash
pip install -r requirements.txt
```

**Cela installe** :
- Flask (serveur web)
- openpyxl (lecture/écriture Excel)
- python-dateutil (gestion des dates)

### Étape 5 : Lancer l'application

```bash
python lancer_gmao.py
```

**Affichage attendu** :
```
* Serving Flask app 'app'
* Environment: production
* Running on http://127.0.0.1:5000
```

### Étape 6 : Accéder via navigateur

**Sur le serveur lui-même** :
```
http://127.0.0.1:5000
```

**Depuis un autre poste (réseau local)** :
```
http://[IP_SERVEUR]:5000
# Par exemple : http://192.168.1.100:5000
```

---

## 📊 Onglets disponibles

Une fois l'app lancée, accède à ces écrans via le menu :

- **Équipements** - Inventaire biomédical
- **Matériels** - Composants et packages
- **Outillage** - Matériel services généraux
- **Maint. Préventive** - Planning maintenance
- **Interventions** - Historique des réparations
- **Pièces** - Stock de pièces détachées
- **Fournisseurs** - Prestataires et contrats
- **Techniciens** - Référentiel techniciens

---

## 🔧 Dépannage

| Problème | Cause | Solution |
|----------|-------|----------|
| "python not found" | Python pas installé ou PATH mal configuré | Réinstalle Python avec "Add to PATH" coché |
| "ModuleNotFoundError: No module Flask" | Dépendances non installées | `pip install -r requirements.txt` |
| "Port 5000 in use" | Autre appli utilise ce port | Ferme autre appli ou change port dans app.py |
| "Connection refused" (autre poste) | Firewall bloque port 5000 | Autorise port 5000 dans Firewall |
| "Excel file not found" | Fichier GMAO_v0.1.xlsx manquant | Télécharge depuis GitHub |

---

## 📡 Accès multi-utilisateurs

### Configuration réseau local

1. **Sur le serveur** : Laisse l'appli tournante
2. **Sur chaque poste client** : 
   - Ouvre navigateur
   - Va à : `http://[IP_SERVEUR]:5000`

### Trouver l'IP du serveur

**Windows** :
```powershell
ipconfig
# Exemple : IPv4 Address ... : 192.168.1.100
```

**Linux** :
```bash
ip addr show
```

---

## 💾 Sauvegarde des données

**CRITIQUE** : Le fichier `GMAO_v0.1.xlsx` contient toutes les données.

### Sauvegarde manuelle

```powershell
# Copie simple
copy GMAO_v0.1.xlsx GMAO_backup_2026-05-22.xlsx
```

---

## 🆘 Support

- **Documentation** : Voir README.md
- **Problèmes d'installation** : Voir `PREREQUIS-INSTALLATION-COMPLET.md`
- **Détails techniques** : Voir `WINDOWS-VS-LINUX-SPECIFIQUE.md`

---

**Status** : ✅ PRÊT POUR COMORES
**Dernière mise à jour** : 22 mai 2026
