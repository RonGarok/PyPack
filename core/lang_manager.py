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
        json.dump(config, f, indent=4)