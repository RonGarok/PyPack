import json
import os

# Dossier de configuration persistant (même dans un .exe)
CONFIG_DIR = os.path.join(os.path.expanduser("~"), ".pypack")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

def load_config():
    # Crée le dossier si nécessaire
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)

    # Si pas de config → valeur par défaut
    if not os.path.exists(CONFIG_FILE):
        return {"language": "fr"}

    # Lecture du fichier
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_config(config):
    # Crée le dossier si nécessaire
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)

    # Écriture du fichier
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)
