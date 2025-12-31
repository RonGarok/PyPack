import requests
import difflib
import os

CACHE_FILE = "pypi_cache.txt"


def update_cache():
    """
    Télécharge la liste complète des paquets PyPI et la stocke localement.
    """
    print("Mise à jour du cache PyPI...")

    url = "https://pypi.org/simple/"
    r = requests.get(url, timeout=10)

    if r.status_code != 200:
        print("Impossible de mettre à jour le cache PyPI.")
        return

    # Extraction simple des noms de paquets depuis les balises <a>
    lines = r.text.split("\n")
    packages = []

    for line in lines:
        if "<a href=" in line:
            # Exemple : <a href="...">nom</a>
            start = line.find(">") + 1
            end = line.find("</a>")
            name = line[start:end].strip()
            if name:
                packages.append(name)

    # Sauvegarde
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        for p in packages:
            f.write(p + "\n")

    print(f"Cache PyPI mis à jour ({len(packages)} paquets).")


def load_cache():
    """
    Charge la liste des paquets depuis le cache local.
    """
    if not os.path.exists(CACHE_FILE):
        update_cache()

    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


def search_pypi(query: str):
    """
    Recherche intelligente basée sur fuzzy matching.
    """
    if not query:
        return []

    all_packages = load_cache()

    # Fuzzy matching
    matches = difflib.get_close_matches(query, all_packages, n=30, cutoff=0.1)

    return matches


def get_package_info(name: str):
    """
    Infos d'un paquet via l'API JSON officielle.
    """
    url = f"https://pypi.org/pypi/{name}/json"
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            return None
        data = r.json()
    except Exception:
        return None

    info = data.get("info", {})
    return {
        "name": info.get("name"),
        "summary": info.get("summary"),
        "home_page": info.get("home_page"),
        "author": info.get("author"),
        "version": info.get("version"),
    }