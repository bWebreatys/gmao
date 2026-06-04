#!/usr/bin/env python3
"""
GMAO – Lanceur de l'interface de saisie locale
Double-cliquez sur ce fichier ou lancez : python lancer_gmao.py
"""
import sys, os, subprocess, webbrowser, time, threading
from pathlib import Path

# Vérifications préliminaires
xlsx = Path(__file__).parent / "GMAO_v0.1.xlsx"
app_dir = Path(__file__).parent / "gmao_app"

if not xlsx.exists():
    print(f"ERREUR : fichier Excel introuvable : {xlsx}")
    input("Appuyez sur Entrée pour quitter.")
    sys.exit(1)

try:
    import flask
    import openpyxl
except ImportError as e:
    print(f"ERREUR : module manquant – {e}")
    print("Installez les dépendances : pip install flask openpyxl")
    input("Appuyez sur Entrée pour quitter.")
    sys.exit(1)

print("="*55)
print("  🏥  GMAO – Interface de saisie locale")
print("="*55)
print(f"  Fichier Excel : {xlsx.name}")
print(f"  Adresse      : http://127.0.0.1:5000")
print(f"  Arrêter      : Ctrl+C dans cette fenêtre")
print("="*55 + "\n")

def open_browser():
    time.sleep(1.2)
    webbrowser.open("http://127.0.0.1:5000")

threading.Thread(target=open_browser, daemon=True).start()

os.chdir(app_dir)
sys.path.insert(0, str(app_dir))
from app import app
app.run(debug=False, port=5000, host="127.0.0.1")
