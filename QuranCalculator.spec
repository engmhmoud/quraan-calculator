# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['/data/projects/more/quran-calculator/main_nicegui.py'],
    pathex=[],
    binaries=[],
    datas=[('/data/projects/more/quran-calculator/roboto_font.ttf', '.'), ('/home/sabry/.local/share/virtualenvs/quran-calculator-IltadaL2/lib/python3.12/site-packages/nicegui/static', 'nicegui/static'), ('/home/sabry/.local/share/virtualenvs/quran-calculator-IltadaL2/lib/python3.12/site-packages/nicegui/templates', 'nicegui/templates')],
    hiddenimports=['nicegui', 'uvicorn', 'uvicorn.server', 'uvicorn.protocols.http.auto', 'uvicorn.protocols.websockets.auto', 'fastapi', 'starlette', 'pydantic', 'websockets', 'websockets.server', 'websockets.client', 'multipart', 'python_multipart', 'email_validator', 'watchfiles', 'httptools', 'aiofiles', 'jinja2', 'orjson', 'ujson', 'markupsafe', 'typing_extensions'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='QuranCalculator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
