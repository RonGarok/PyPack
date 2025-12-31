# -*- mode: python ; coding: utf-8 -*-

import os

block_cipher = None

project_dir = os.path.abspath(".")
assets_dir = os.path.join(project_dir, "assets")

a = Analysis(
    ['app.py'],
    pathex=[project_dir],
    binaries=[],
    datas=[
        ('core/*.py', 'core'),
        ('ui/*.py', 'ui'),
        ('ui/tabs/*.py', 'ui/tabs'),
        ('config.json', '.'),
        (os.path.join(assets_dir, 'pypack.ico'), 'assets'),
    ],
    hiddenimports=[
        'deep_translator',
        'xmlrpc',
        'xmlrpc.client',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PyPack',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon=os.path.join(assets_dir, 'pypack.ico'),
    onefile=True,  # ← LE MODE ONE-FILE
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='PyPack'
)