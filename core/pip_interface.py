<<<<<<< HEAD
import subprocess
import shutil

def _get_python():
    """Retourne le Python du système (pas celui de PyInstaller)."""
    return shutil.which("python") or shutil.which("python3")

def list_installed_packages():
    python = _get_python()
    cmd = [python, "-m", "pip", "list", "--format=json"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    import json
    return json.loads(result.stdout)

def install_package(name):
    python = _get_python()
    cmd = [python, "-m", "pip", "install", name]
    subprocess.run(cmd, check=True)

def uninstall_package(name):
    python = _get_python()
    cmd = [python, "-m", "pip", "uninstall", "-y", name]
    subprocess.run(cmd, check=True)
=======
import subprocess
import shutil

def _get_python():
    """Retourne le Python du système (pas celui de PyInstaller)."""
    return shutil.which("python") or shutil.which("python3")

def list_installed_packages():
    python = _get_python()
    cmd = [python, "-m", "pip", "list", "--format=json"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    import json
    return json.loads(result.stdout)

def install_package(name):
    python = _get_python()
    cmd = [python, "-m", "pip", "install", name]
    subprocess.run(cmd, check=True)

def uninstall_package(name):
    python = _get_python()
    cmd = [python, "-m", "pip", "uninstall", "-y", name]
    subprocess.run(cmd, check=True)
>>>>>>> 2474df5d08a01f1f2c138d72edd5319b730733be
