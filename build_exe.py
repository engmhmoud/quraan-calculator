#!/usr/bin/env python3
"""
Build script for creating Windows executable of Quran Calculator
Automates the PyInstaller build process with proper dependency handling
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path
import pkg_resources


def get_nicegui_static_path():
    """Find the NiceGUI static files directory"""
    try:
        import nicegui
        nicegui_path = Path(nicegui.__file__).parent
        static_path = nicegui_path / 'static'
        if static_path.exists():
            return str(static_path)
    except ImportError:
        pass
    
    # Fallback: try to find in site-packages
    try:
        dist = pkg_resources.get_distribution('nicegui')
        if dist.location:
            static_path = Path(dist.location) / 'nicegui' / 'static'
            if static_path.exists():
                return str(static_path)
    except:
        pass
    
    return None


def create_dynamic_spec():
    """Create a PyInstaller spec file with dynamic paths"""
    current_dir = Path(__file__).parent.absolute()
    main_script = current_dir / "main_nicegui.py"
    nicegui_static = get_nicegui_static_path()
    
    # Build the datas list
    datas = [
        f"    ('{str(current_dir / 'roboto_font.ttf')}', '.'),\n"
    ]
    
    if nicegui_static:
        datas.append(f"    ('{nicegui_static}', 'nicegui/static'),\n")
    
    datas_str = "".join(datas)
    
    spec_content = f"""# -*- mode: python ; coding: utf-8 -*-
import os
import sys
from pathlib import Path

block_cipher = None

# Data files to include
datas = [
    # Include the Roboto font file
{datas_str}]

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
"""
    
    spec_file = current_dir / 'quran_calculator_dynamic.spec'
    with open(spec_file, 'w', encoding='utf-8') as f:
        f.write(spec_content)
    
    return spec_file


def check_dependencies():
    """Check if all required dependencies are installed"""
    # Map package names to their import names
    required_packages = {
        'nicegui': 'nicegui',
        'pillow': 'PIL',
        'pyinstaller': 'PyInstaller'
    }
    missing_packages = []
    
    for package_name, import_name in required_packages.items():
        try:
            __import__(import_name)
        except ImportError:
            missing_packages.append(package_name)
    
    if missing_packages:
        print(f"❌ Missing required packages: {', '.join(missing_packages)}")
        print("Please install them using:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    return True


def clean_build_dirs():
    """Clean previous build directories"""
    dirs_to_clean = ['build', 'dist', '__pycache__']
    
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            print(f"🧹 Cleaning {dir_name} directory...")
            shutil.rmtree(dir_name)


def build_executable():
    """Build the executable using PyInstaller"""
    print("🏗️ Building Windows executable...")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        return False
    
    # Clean previous builds
    clean_build_dirs()
    
    # Create dynamic spec file
    print("📝 Creating PyInstaller spec file...")
    spec_file = create_dynamic_spec()
    print(f"✓ Spec file created: {spec_file}")
    
    # Find NiceGUI static path
    nicegui_static = get_nicegui_static_path()
    if nicegui_static:
        print(f"✓ Found NiceGUI static files at: {nicegui_static}")
    else:
        print("⚠️ Warning: Could not find NiceGUI static files")
    
    # Run PyInstaller
    print("🔨 Running PyInstaller...")
    try:
        cmd = [sys.executable, '-m', 'PyInstaller', str(spec_file)]
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✓ PyInstaller completed successfully")
        
        # Check if executable was created
        exe_path = Path('dist') / 'QuranCalculator.exe'
        if exe_path.exists():
            exe_size = exe_path.stat().st_size / (1024 * 1024)  # Size in MB
            print(f"✓ Executable created: {exe_path} ({exe_size:.1f} MB)")
            print(f"✓ You can now distribute the executable to Windows users!")
            return True
        else:
            print("❌ Executable not found in dist directory")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"❌ PyInstaller failed with error:")
        print(e.stderr)
        return False
    except Exception as e:
        print(f"❌ Build failed with error: {e}")
        return False


def main():
    """Main build function"""
    print("🕌 Quran Calculator - Windows Executable Builder")
    print("=" * 50)
    
    if build_executable():
        print("\n🎉 Build completed successfully!")
        print("\nNext steps:")
        print("1. Test the executable: .\\dist\\QuranCalculator.exe")
        print("2. The exe file is standalone and can be distributed")
        print("3. Users don't need Python installed to run it")
        print("4. Consider creating an installer for easier distribution")
    else:
        print("\n❌ Build failed. Please check the errors above.")
        sys.exit(1)


if __name__ == "__main__":
    main() 