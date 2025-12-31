<<<<<<< HEAD
import json
import os

CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "config.json")
CONFIG_FILE = os.path.abspath(CONFIG_FILE)

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {"language": "fr"}
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
=======
import json
import os

CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "config.json")
CONFIG_FILE = os.path.abspath(CONFIG_FILE)

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {"language": "fr"}
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
>>>>>>> 2474df5d08a01f1f2c138d72edd5319b730733be
        json.dump(config, f, indent=4)