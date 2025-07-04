# -*- mode: python ; coding: utf-8 -*-
import os
import sys
from pathlib import Path

# Get the directory where this spec file is located
spec_root = os.path.dirname(os.path.abspath(SPEC))

block_cipher = None

# Define the main script
main_script = os.path.join(spec_root, 'main_nicegui.py')

# Data files to include
datas = [
    # Include the Roboto font file
    (os.path.join(spec_root, 'roboto_font.ttf'), '.'),
    # Include NiceGUI static files
    ('venv/Lib/site-packages/nicegui/static', 'nicegui/static'),
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
    [main_script],
    pathex=[spec_root],
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
    console=False,  # Set to False for windowed app, True for console debugging
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # You can add an .ico file path here if you have an icon
) 