# 🖥️ Spécificités Windows vs Linux - Guide détaillé

## 🪟 WINDOWS - Points spécifiques

### 1. Installation Python sur Windows

**Téléchargement** :
- https://www.python.org/downloads/
- Clique sur "Download Python 3.10.x" (le grand bouton jaune)
- Sélectionne "Windows installer (64-bit)" si tu as un PC récent

**Installation - ÉTAPES ESSENTIELLES** :

```
1. Double-clique le fichier .exe téléchargé
2. ⚠️ TRÈS IMPORTANT - Coche CETTE CASE :
   ☑ Add Python to PATH
3. Clique "Install Now" (installation rapide)
4. Attends la fin (2-3 minutes)
5. Ferme la fenêtre
```

**Vérification** :
```powershell
# Ouvre PowerShell (Win + R, tape powershell)
python --version
# Doit afficher : Python 3.10.x
```

### 2. Chemin des fichiers Windows (PATH)

**Problème courant** : "python: command not found"

**Cause** : Python pas dans le PATH Windows

**Solution** :
1. Panneau de contrôle → Paramètres systèmes avancés
2. Variables d'environnement → New → 
   - Variable name : PYTHON
   - Variable value : C:\Python310
3. Redémarre PowerShell
4. Réessaie `python --version`

### 3. Dossiers spécifiques Windows

```
Emplacements recommandés :

C:\Applis\EMSP\              ← Racine du projet
├── app.py
├── EMSP_v0.1.xlsx
└── emsp_app/

Ou :

C:\Users\[nom]\AppData\Local\emsp\    ← Pour l'utilisateur seul

Éviter :
❌ C:\Program Files\emsp\    (problèmes de droits)
❌ C:\Users\[nom]\Desktop\   (pas sécurisé pour serveur)
```

### 4. Serveur sur Windows - Services

**Lancer l'app manuellement** :
```powershell
cd C:\Applis\EMSP
python lancer_application.py
```

**Lancer l'app au démarrage (Windows)** :

**Option A : Raccourci au démarrage**
1. Win + R → `shell:startup`
2. Crée un fichier `start_emsp.bat` :
```batch
@echo off
cd C:\Applis\EMSP
python lancer_application.py
pause
```
3. Place ce fichier dans le dossier startup

**Option B : Task Scheduler (PLUS ROBUSTE)**
1. Win + R → `taskschd.msc`
2. Créer une tâche simple :
   - Nom : "Démarrer EMSP"
   - Déclencheur : "Au démarrage"
   - Action : 
     - Programme : `C:\Python310\python.exe`
     - Arguments : `C:\Applis\EMSP\lancer_application.py`
   - Utilisateur : Compte spécifique (voir section 6)

### 5. Firewall Windows - Configuration

**Le problème** : Les autres postes ne peuvent pas accéder à l'appli

**Solution complète** :

1. Ouvre **Windows Defender Firewall** :
   - Win + R → `wf.msc`

2. **Autoriser une application** :
   - À gauche : "Autoriser une application"
   - Clique "Allow another app"
   - Sélectionne python.exe (C:\Python310\python.exe)
   - Coche "Private" (réseau local)
   - Clique "Add"

3. **Sinon, crée une règle personnalisée** :
   - À gauche : "Inbound Rules" → "New Rule"
   - Port
   - TCP, port 5000
   - Allow the connection
   - Toutes les parties (Domain, Private, Public - mais décoche Public si sécurité)

### 6. PowerShell vs Command Prompt

**Utilise PowerShell (meilleur)** :
```powershell
# Plus moderne, plus de fonctionnalités
python --version
pip install Flask
```

**Si tu dois utiliser Cmd** :
```cmd
REM Exact même commandes, mais interface moins bonne
python --version
pip install Flask
```

---

## 🐧 LINUX - Points spécifiques

### 1. Installation Python sur Linux

**Ubuntu/Debian** :
```bash
sudo apt update
sudo apt install python3.10 python3-pip python3-venv
python3 --version
```

**Fedora/CentOS** :
```bash
sudo dnf install python3.10 python3-pip
python3 --version
```

**Depuis source** :
```bash
wget https://www.python.org/ftp/python/3.10.13/Python-3.10.13.tgz
tar xzf Python-3.10.13.tgz
cd Python-3.10.13
./configure --prefix=/opt/python3.10
make
sudo make install
/opt/python3.10/bin/python3 --version
```

### 2. Droits et permissions Linux

```bash
# Créer utilisateur dédié
sudo useradd -m -s /bin/bash emsp-app
sudo passwd emsp-app  # Définir mot de passe

# Créer dossier projet avec droits
sudo mkdir -p /opt/emsp
sudo chown emsp-app:emsp-app /opt/emsp
sudo chmod 755 /opt/emsp

# Permettre à l'utilisateur de modifier
sudo chmod u+w /opt/emsp
```

### 3. Dossiers spécifiques Linux

```bash
Emplacements recommandés :

/opt/emsp/                    ← Pour application système
├── app.py
├── EMSP_v0.1.xlsx
├── emsp_app/
└── venv/

Ou :

/home/emsp-app/emsp/          ← Pour utilisateur spécifique

Éviter :
❌ /root/emsp/                (utilisateur root)
❌ /tmp/emsp/                 (fichiers supprimés)
```

### 4. Serveur sur Linux - Systemd Service

**Créer un service systemd** (RECOMMANDÉ) :

```bash
sudo nano /etc/systemd/system/emsp.service
```

Contenu :
```ini
[Unit]
Description=EMSP Application
After=network.target

[Service]
Type=simple
User=emsp-app
WorkingDirectory=/opt/emsp
ExecStart=/opt/python3.10/bin/python3 lancer_application.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Activation :
```bash
sudo systemctl daemon-reload
sudo systemctl enable emsp      # Autostart
sudo systemctl start emsp       # Lancer maintenant
sudo systemctl status emsp      # Vérifier
```

### 5. Firewall Linux - Configuration

```bash
# UFW (Uncomplicated Firewall)
sudo ufw allow 5000/tcp
sudo ufw allow from 192.168.1.0/24 to any port 5000

# Iptables (plus complexe)
sudo iptables -A INPUT -p tcp --dport 5000 -j ACCEPT
sudo iptables-save | sudo tee /etc/iptables/rules.v4
```

### 6. Reverse Proxy - Nginx/Apache

**Pour éviter de lancer Flask en port 80** (nécessite root) :

**Nginx** :
```nginx
server {
    listen 80;
    server_name emsp.hopital.km;
    
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
    }
}
```

**Apache** :
```apache
<VirtualHost *:80>
    ServerName emsp.hopital.km
    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:5000/
</VirtualHost>
```

---

## 📊 Tableau comparatif

| Aspect | Windows | Linux |
|--------|---------|-------|
| **Installation** | .exe simple | apt/dnf ou source |
| **Gestion des droits** | GUI facile | Commandes bash |
| **Service/Autostart** | Task Scheduler | Systemd |
| **Firewall** | Defender GUI | UFW/iptables |
| **Chemins** | C:\Applis\ | /opt/ ou /home/ |
| **Ligne de commande** | PowerShell | Bash |
| **Reverse proxy** | IIS | Nginx/Apache |
| **Performance** | Standard | Généralement meilleure |
| **Support** | Grand public | Informaticiens |

---

## 🔧 Troubleshooting croisé

| Problème | Windows | Linux |
|----------|---------|-------|
| "python not found" | Réinstalle avec PATH | `apt install python3.10` |
| "Permission denied" | Droits dossier | `chown emsp-app:emsp-app` |
| "Port 5000 in use" | netstat -ano / taskkill | `lsof -i :5000` / `kill -9 PID` |
| "App ne démarre pas au redémarrage" | Vérifier Task Scheduler | Vérifier `systemctl status` |
| "Pas de connexion réseau" | Firewall Windows | `ufw status` |

---

## ✅ Checklist spécifique

### Windows
- [ ] Python 3.10+ installé avec PATH
- [ ] pip fonctionne
- [ ] Dossier C:\Applis\EMSP\ créé
- [ ] Port 5000 autorisé dans Firewall
- [ ] Démarrage automatique configuré (Task Scheduler ou startup)
- [ ] Backup automatique configuré

### Linux
- [ ] Python 3.10+ installé
- [ ] Utilisateur emsp-app créé
- [ ] /opt/emsp/ créé avec bons droits
- [ ] Systemd service créé et activé
- [ ] UFW firewall permet port 5000
- [ ] Vérification : `systemctl status emsp`

---

**Status** : ✅ COMPLET
**Date** : 22 mai 2026

