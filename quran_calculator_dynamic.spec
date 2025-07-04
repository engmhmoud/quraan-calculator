# -*- mode: python ; coding: utf-8 -*-
import os
import sys
from pathlib import Path

block_cipher = None

# Data files to include
datas = [
    # Include the Roboto font file
    ('/data/projects/more/quran-calculator/roboto_font.ttf', '.'),
    # Include NiceGUI static files
    ('/home/sabry/.local/share/virtualenvs/quran-calculator-IltadaL2/lib/python3.12/site-packages/nicegui/static', 'nicegui/static'),
]

# Hidden imports for NiceGUI
hiddenimports = [
    'nicegui',
    'uvicorn',
    'uvicorn.server',
    'uvicorn.protocols.http.auto',
    'uvicorn.protocols.websockets.auto',
    'fastapi',
    'starlette',
    'pydantic',
    'websockets',
    'websockets.server',
    'websockets.client',
    'multipart',
    'python_multipart',
    'email_validator',
    'watchfiles',
    'httptools',
    'aiofiles',
    'jinja2',
    'orjson',
    'ujson',
    'markupsafe',
    'typing_extensions',
]

a = Analysis(
    ['{str(main_script)}'],
    pathex=['{str(current_dir)}'],
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
    [],
    name='QuranCalculator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Set to True for debugging
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Add .ico file path here if you have an icon
)
