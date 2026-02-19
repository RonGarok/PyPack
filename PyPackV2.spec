# -*- mode: python ; coding: utf-8 -*-

import os
from PyInstaller.utils.hooks import collect_submodules

# Collecte automatique des sous-modules Python
hiddenimports = []
hiddenimports += collect_submodules('core')
hiddenimports += collect_submodules('ui')

# Dossiers à inclure
datas = [
    ('core', 'core'),
    ('ui', 'ui'),
    ('assets', 'assets'),
]

block_cipher = None

a = Analysis(
    ['app.py'],  # ton fichier principal
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='PyPackV2',
    debug=False,
    strip=False,
    upx=False,
    console=False,  # mets True si tu veux voir la console
)

