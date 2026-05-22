# 📋 Guide Complet des Prérequis - Installation EMSP & GMAO

## 🎯 Vue d'ensemble

Ce guide couvre :
1. **Versions Python compatibles/incompatibles**
2. **Gestion des versions multiples**
3. **Droits utilisateur et permissions**
4. **Infrastructure serveur et réseau**
5. **Accès et connexions distantes**
6. **Checklist pré-installation**

---

# 1. PYTHON - VERSIONS ET COMPATIBILITÉ

## ✅ Versions RECOMMANDÉES

| Version | Statut | Raison |
|---------|--------|--------|
| Python 3.9 | ✅ Excellente | LTS, stable, support long terme |
| Python 3.10 | ✅ Excellente | Version actuelle stéable |
| Python 3.11 | ✅ Bonne | Dernière version (un peu plus rapide) |
| Python 3.8 | ⚠️ OK | Limite inférieure (dépendances vieilles) |

## ❌ Versions INCOMPATIBLES / À ÉVITER

| Version | Problème |
|---------|----------|
| Python 2.7 | ❌ ARRÊTÉE depuis 2020 - NE PAS UTILISER |
| Python 3.0-3.7 | ❌ Obsolètes - dépendances manquantes |
| Python 3.12+ | ⚠️ Possible mais non testé - certaines libs en retard |

## 🔍 Comment vérifier la version installée

**Sur Windows (PowerShell)** :
```powershell
python --version
# ou
python -V
```

**Sur Linux/Mac (Terminal)** :
```bash
python3 --version
```

---

# 2. SCÉNARIO 1 : Python EST DÉJÀ INSTALLÉ

## A. Si c'est Python 3.8 ou plus récent → ✅ C'EST BON

**La bonne nouvelle** : Vous pouvez utiliser la version existante.

**Vérification** :
```powershell
python --version
# Affichage attendu : Python 3.8.x / 3.9.x / 3.10.x / 3.11.x
```

**Installation des dépendances** :
```powershell
pip install -r requirements.txt
```

C'est tout ! Passez à la section 3.

---

## B. Si c'est Python 2.7 ou Python 3.0-3.7 → ⚠️ INCOMPATIBLE

**Le problème** : Version trop ancienne.

### **Option 1 : Installer une nouvelle version (RECOMMANDÉ)**

Tu vas avoir **deux versions Python côte à côte** (c'est normal et sûr).

**Étapes** :

1. **Télécharge Python 3.10** :
   - Va sur https://www.python.org/downloads/
   - Clique sur "Download Python 3.10.x" (Windows x86-64)
   
2. **Installation importante** :
   ⚠️ **COCHER CETTE CASE** :
   ```
   ☑ Add Python 3.10 to PATH
   ```
   
3. **Installe sans cocher "Disable path length limit"** (à moins que tu saches ce que c'est)

4. **Vérifie l'installation** :
   ```powershell
   python3.10 --version
   # ou simplement
   python --version
   ```

5. **Installe Flask et openpyxl** :
   ```powershell
   pip install -r requirements.txt
   ```

### **Option 2 : Désinstaller l'ancienne version (PLUS COMPLEXE)**

Si tu n'utilises pas Python 2.7 pour autre chose :
- Panneau de contrôle → Programmes → Désinstaller Python 2.7
- Puis installer Python 3.10 (voir Option 1)

**⚠️ Risque** : Des applications anciennes pourraient dépendre de Python 2.7

---

# 3. SCÉNARIO 2 : Python N'EST PAS INSTALLÉ

## A. Installation Windows (recommandé)

**Téléchargement** :
1. Va sur https://www.python.org/downloads/
2. Clique sur le grand bouton jaune "Download Python 3.10"
3. Sauvegarde le fichier `.exe`

**Installation** :
1. Double-clique sur le fichier téléchargé
2. **TRÈS IMPORTANT** : Coche la case :
   ```
   ☑ Add Python to PATH
   ```
3. Clique "Install Now" (installation rapide)
4. Attends la fin

**Vérification** :
```powershell
python --version
# Doit afficher : Python 3.10.x (ou 3.9.x, 3.11.x)
```

---

## B. Installation Linux/Mac

**Linux (Ubuntu/Debian)** :
```bash
sudo apt update
sudo apt install python3.10 python3-pip
python3 --version
```

**Mac (avec Homebrew)** :
```bash
brew install python@3.10
python3 --version
```

---

## C. Installation depuis Microsoft Store (Windows)

Alternative simple sur Windows 10/11 :
1. Ouvre **Microsoft Store**
2. Cherche **"Python 3.10"**
3. Clique "Get" (c'est gratuit)

⚠️ **Attention** : Configure bien le PATH après (voir section prérequis PATH)

---

# 4. GESTION DES VERSIONS MULTIPLES

## Scénario : Tu as Python 2.7 ET Python 3.10

**C'EST NORMAL et SÛRE**. Les deux peuvent coexister.

### **Utiliser la bonne version** :

```powershell
# Utiliser Python 3.10 spécifiquement
python3.10 app.py

# Ou utiliser pip pour Python 3.10
pip3.10 install -r requirements.txt

# Ou utiliser venv (recommandé - voir section 5)
```

### **Vérifier quelle version est utilisée par défaut** :

```powershell
python --version
which python     # Linux/Mac
where python     # Windows
```

Si c'est la mauvaise version → modifie le PATH (voir section 5)

---

# 5. ENVIRONNEMENT VIRTUEL (VENV) - FORTEMENT RECOMMANDÉ

## Pourquoi ?

- ✅ Isole les dépendances du projet
- ✅ Évite les conflits avec d'autres projets Python
- ✅ Facile à supprimer sans affecter le système
- ✅ **Recommandé pour un serveur partagé**

## Comment faire

### **Création du venv** :

```powershell
# Va dans le dossier du projet
cd C:\Users\PC\Documents\emsp

# Crée l'environnement virtuel
python -m venv venv

# Active l'environnement
.\venv\Scripts\activate
# Affichage : (venv) C:\Users\PC\Documents\emsp>

# Installe les dépendances
pip install -r requirements.txt
```

### **Utilisation quotidienne** :

```powershell
# Avant de lancer l'app, toujours faire :
.\venv\Scripts\activate

# Ensuite lancer l'app
python lancer_application.py

# Quand c'est fini :
deactivate
```

### **Sur Linux/Mac** :

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

# 6. DROITS UTILISATEUR - SERVEUR

## 📊 Scénario : Installation sur un serveur partagé

### **Qui doit avoir quels droits ?**

| Rôle | Droits requis | Cas d'usage |
|------|---------------|-----------|
| **Admin serveur** | ✅ Accès complet | Installation, maintenance, sauvegarde |
| **Utilisateur appli** | ⚠️ Lecture seule | Utilisation de l'app via navigateur |
| **Technicien local** | ✅ Lecture/Écriture (dossier projet) | Mises à jour fichiers, redémarrages |

### **Structure des droits recommandée** :

```
C:\Applis\EMSP\
├── app.py                    [Admin: RW, Autres: R]
├── lancer_application.py     [Admin: RW, Autres: R]
├── EMSP_v0.1.xlsx           [Admin: RW, Autres: RW] ⚠️
├── emsp_app/
│   └── templates/           [Admin: RW, Autres: R]
├── logs/                     [Admin: RW, Autres: RW] ⚠️
└── data-backup/             [Admin: RW, Autres: aucun]
```

⚠️ = Doit être éditable par l'appli

### **Configuration sur Windows Server** :

1. **Crée un compte utilisateur dédié** :
   ```
   Utilisateur : emsp-app
   Mot de passe : [complexe, stocké sécurisé]
   Groupe : Users (droits standards)
   ```

2. **Donne les droits** :
   ```
   Dossier EMSP : Properties > Security
   ├─ Administrators    : Full Control
   └─ emsp-app         : Modify (lecture + écriture)
   ```

3. **Lance l'app sous ce compte** :
   - Task Scheduler → New Task
   - Run as : emsp-app
   - Action : python C:\Applis\EMSP\lancer_application.py

---

# 7. ACCÈS UTILISATEURS DISTANTS

## 📱 Scénario : 5 utilisateurs sur 5 postes différents

### **Réseau LOCAL (même établissement)**

**Architecture** :
```
PC SERVEUR (Windows Server ou PC Windows)
    ↑↑↑ Réseau local (câble ou WiFi)
    ├─ Poste 1 : http://192.168.1.100:5000
    ├─ Poste 2 : http://192.168.1.100:5000
    ├─ Poste 3 : http://192.168.1.100:5000
    ├─ Poste 4 : http://192.168.1.100:5000
    └─ Poste 5 : http://192.168.1.100:5000
```

**Prérequis réseau** :
- ✅ Câble Ethernet OU WiFi stable
- ✅ Switch réseau si plus de 4 postes
- ✅ Pas de firewall bloquant port 5000 (voir section 8)

**Configuration Flask** :

Dans `app.py`, lance le serveur comme ceci :

```python
if __name__ == '__main__':
    # Écoute sur TOUS les adaptateurs réseau (pas juste localhost)
    app.run(host='0.0.0.0', port=5000, debug=False)
```

**Comment accéder** :

1. **Trouver l'IP du serveur** :
   ```powershell
   ipconfig
   # Cherche "IPv4 Address" : par exemple 192.168.1.100
   ```

2. **Sur chaque poste client** :
   ```
   Navigateur > Adresse
   http://192.168.1.100:5000
   ```

   **⚠️ Ne PAS utiliser localhost** (ça ne marche que sur le serveur)

**Droits d'accès** :
- ✅ Aucune authentification requise (pas d'identifiants)
- ✅ Chacun peut lire et modifier les données
- ⚠️ **Attention** : Toutes les modifications sont visibles par tous

---

### 📡 Réseau DISTANT (entre établissements)

**⚠️ PLUS COMPLEXE**. Nécessite :

1. **VPN** (Réseau Privé Virtuel)
   - Chaque établissement se connecte à un VPN central
   - Puis accède à http://[IP_VPN]:5000
   
2. **Ou tunneling SSH**
   ```powershell
   ssh -L 5000:192.168.1.100:5000 admin@serveur-comores.org
   ```

3. **Ou application web publique**
   - Déployer sur un serveur avec domaine HTTPS
   - Beaucoup plus complexe (WinDev ou autre)

**Recommandation pour Comores** :
- ✅ **Court terme** : Réseau local par établissement (option 1)
- ✅ **Moyen terme** : VPN pour consolider nationale (option 2)
- ❌ **Public internet** : Non recommandé pour données hospitalières

---

# 8. FIREWALL ET PORTS

## Problème courant

**"Je vois l'app sur le serveur, mais pas sur les autres postes"**

**Cause** : Le firewall bloque le port 5000

### **Solution Windows** :

1. **Ouvre le Firewall Windows** :
   - Recherche "Firewall" dans Windows
   - Clique "Autoriser une application"

2. **Ajoute Python** :
   - Clique "Allow another app"
   - Sélectionne python.exe (C:\Python310\python.exe)
   - Coche "Private networks" (important)
   - Clique "Add"

### **Solution Linux** :

```bash
sudo ufw allow 5000/tcp
sudo ufw allow from 192.168.1.0/24 to any port 5000
```

### **Test de connexion** :

```powershell
# Sur le serveur
telnet 192.168.1.100 5000
# Doit dire "Connected" (pas "Connection refused")
```

---

# 9. SAUVEGARDE DES DONNÉES

## ⚠️ CRITIQUE

Le fichier Excel contient toutes les données :
```
EMSP_v0.1.xlsx  ← FICHIER CRITIQUE !
```

### **Stratégie de sauvegarde** :

| Fréquence | Méthode | Stockage |
|-----------|---------|----------|
| **Quotidienne** | Copie auto (backup.xlsx) | Même serveur + NAS |
| **Hebdomadaire** | Export vers serveur central | Serveur Comores ou cloud |
| **Mensuelle** | Archive (EMSP_2026-05.xlsx) | Disque externe |

### **Configuration backup automatique** :

```python
# À ajouter dans app.py
import shutil
from datetime import datetime

def backup_excel():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    backup_file = f"backups/EMSP_{timestamp}.xlsx"
    shutil.copy("EMSP_v0.1.xlsx", backup_file)
    
# Appeler backup_excel() quand données modifiées
```

---

# 10. CHECKLIST PRÉ-INSTALLATION

## ✅ Avant d'installer

### **Sur le SERVEUR** :

- [ ] **Python 3.8+** installé
  ```powershell
  python --version
  ```

- [ ] **pip** fonctionne
  ```powershell
  pip --version
  ```

- [ ] **Git** optionnel (pour cloner depuis GitHub)
  ```powershell
  git --version
  ```

- [ ] **Dossier dédié créé** :
  ```
  C:\Applis\EMSP\
  ou
  /opt/emsp/
  ```

- [ ] **Droits d'accès vérifiés** :
  ```
  Compte serveur a les droits Modification du dossier
  ```

- [ ] **Port 5000 disponible** :
  ```powershell
  netstat -ano | findstr :5000
  # Doit être vide (pas d'autres applis sur ce port)
  ```

- [ ] **Espace disque suffisant** :
  ```
  Minimum : 100 MB
  Recommandé : 1 GB
  ```

### **Sur les POSTES CLIENTS** :

- [ ] **Navigateur web compatible** :
  - ✅ Chrome 90+
  - ✅ Firefox 88+
  - ✅ Edge 90+
  - ✅ Safari 14+

- [ ] **Connexion réseau testée** :
  ```powershell
  ping 192.168.1.100
  # Doit avoir réponse
  ```

- [ ] **Port 5000 accessible** :
  ```powershell
  telnet 192.168.1.100 5000
  # Doit dire "Connected"
  ```

### **DONNÉES** :

- [ ] **Fichier Excel présent** :
  ```
  EMSP_v0.1.xlsx
  ou
  GMAO_v0.1.xlsx
  ```

- [ ] **Dossier templates** :
  ```
  emsp_app/templates/
  ou
  gmao_app/templates/
  ```

---

# 11. DÉPENDANCES PYTHON - DÉTAIL

## Fichier `requirements.txt`

```
Flask==2.3.0          # Framework web
openpyxl==3.10.0      # Lecture/écriture Excel
python-dateutil==2.8.2 # Manipulation dates
```

### **Installation** :

```powershell
pip install -r requirements.txt

# Ou manuellement
pip install Flask==2.3.0
pip install openpyxl==3.10.0
pip install python-dateutil==2.8.2
```

### **Vérification** :

```powershell
pip show Flask
pip show openpyxl
pip show python-dateutil
```

---

# 12. TROUBLESHOOTING - PROBLÈMES COURANTS

| Problème | Cause | Solution |
|----------|-------|----------|
| "python not found" | Python pas dans PATH | Réinstalle avec "Add to PATH" coché |
| "No module Flask" | pip install pas lancé | `pip install -r requirements.txt` |
| "Port 5000 in use" | Autre appli utilise ce port | Ferme autre appli ou change port (5001) |
| "Connection refused" | Firewall bloque | Autorise port 5000 dans Firewall Windows |
| "Permission denied" | Droits insuffisants | Crée compte dédié avec droits Modify |
| "Excel file corrupted" | Données corrompues | Restaure depuis backup |

---

# 13. RÉSUMÉ - VERSION COURTE

**Pour aller vite** :

1. ✅ **Installer Python 3.10**
   ```powershell
   https://python.org/downloads/
   # Cocher "Add to PATH"
   ```

2. ✅ **Créer dossier projet**
   ```powershell
   C:\Applis\EMSP\
   ```

3. ✅ **Installer dépendances**
   ```powershell
   pip install -r requirements.txt
   ```

4. ✅ **Lancer l'appli**
   ```powershell
   python lancer_application.py
   ```

5. ✅ **Accéder via navigateur**
   ```
   http://127.0.0.1:5000        # Serveur local
   http://192.168.1.100:5000    # Autres postes (remplacer IP)
   ```

---

**Status** : ✅ COMPLET
**Date** : 22 mai 2026
**Prochaine étape** : Étape 2 - Installation détaillée

