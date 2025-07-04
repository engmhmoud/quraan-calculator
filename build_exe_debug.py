#!/usr/bin/env python3
"""
DEBUG build script for Windows executable - includes console for troubleshooting
Use this when the regular executable won't run to see detailed error messages
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path


def get_nicegui_paths():
    """Find the NiceGUI static and template files directories"""
    try:
        import nicegui
        nicegui_path = Path(nicegui.__file__).parent
        static_path = nicegui_path / 'static'
        templates_path = nicegui_path / 'templates'
        
        paths = {}
        if static_path.exists():
            paths['static'] = str(static_path)
        if templates_path.exists():
            paths['templates'] = str(templates_path)
            
        return paths
    except ImportError:
        pass
    return {}


def check_dependencies():
    """Check if all required dependencies are installed"""
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


def build_debug_executable():
    """Build the executable with console enabled for debugging"""
    print("🔧 Building DEBUG Windows executable...")
    print("=" * 50)
    print("⚠️  This version will show a console window with detailed error messages")
    print("")
    
    # Check dependencies
    if not check_dependencies():
        return False
    
    # Clean previous builds
    clean_build_dirs()
    
    # Get paths
    current_dir = Path(__file__).parent.absolute()
    main_script = current_dir / "main_nicegui.py"
    font_file = current_dir / "roboto_font.ttf"
    nicegui_paths = get_nicegui_paths()
    
    # Build PyInstaller command (NOTE: --console instead of --windowed)
    cmd = [
        sys.executable, '-m', 'PyInstaller',
        str(main_script),
        '--name=QuranCalculator-DEBUG',  # Different name to avoid conflicts
        '--onefile',
        '--console',  # Enable console for debugging
        '--add-data', f'{str(font_file)}:.',
        '--hidden-import=nicegui',
        '--hidden-import=uvicorn',
        '--hidden-import=uvicorn.server',
        '--hidden-import=uvicorn.protocols.http.auto',
        '--hidden-import=uvicorn.protocols.websockets.auto',
        '--hidden-import=fastapi',
        '--hidden-import=starlette',
        '--hidden-import=pydantic',
        '--hidden-import=websockets',
        '--hidden-import=websockets.server',
        '--hidden-import=websockets.client',
        '--hidden-import=multipart',
        '--hidden-import=python_multipart',
        '--hidden-import=email_validator',
        '--hidden-import=watchfiles',
        '--hidden-import=httptools',
        '--hidden-import=aiofiles',
        '--hidden-import=jinja2',
        '--hidden-import=orjson',
        '--hidden-import=ujson',
        '--hidden-import=markupsafe',
        '--hidden-import=typing_extensions',
    ]
    
    # Add NiceGUI files if found
    if nicegui_paths.get('static'):
        cmd.extend(['--add-data', f'{nicegui_paths["static"]}:nicegui/static'])
        print(f"✓ Found NiceGUI static files at: {nicegui_paths['static']}")
    
    if nicegui_paths.get('templates'):
        cmd.extend(['--add-data', f'{nicegui_paths["templates"]}:nicegui/templates'])
        print(f"✓ Found NiceGUI templates at: {nicegui_paths['templates']}")
    
    if not nicegui_paths:
        print("⚠️ Warning: Could not find NiceGUI static or template files")
    
    # Run PyInstaller
    print("🔨 Running PyInstaller (DEBUG mode)...")
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✓ PyInstaller completed successfully")
        
        # Check if executable was created
        import platform
        if platform.system() == 'Windows':
            exe_path = Path('dist') / 'QuranCalculator-DEBUG.exe'
        else:
            exe_path = Path('dist') / 'QuranCalculator-DEBUG'
            
        if exe_path.exists():
            exe_size = exe_path.stat().st_size / (1024 * 1024)  # Size in MB
            print(f"✓ DEBUG executable created: {exe_path} ({exe_size:.1f} MB)")
            print("")
            print("🔍 DEBUG TESTING:")
            print(f"   Run: {exe_path} --help")
            print(f"   Run: {exe_path} --port 8081 --no-browser")
            print("")
            print("💡 This version shows console output for troubleshooting!")
            return True
        else:
            print("❌ Executable not found in dist directory")
            print(f"   Expected: {exe_path}")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"❌ PyInstaller failed with error:")
        if e.stderr:
            print(e.stderr)
        if e.stdout:
            print(e.stdout)
        return False
    except Exception as e:
        print(f"❌ Build failed with error: {e}")
        return False


def main():
    """Main build function"""
    print("🔧 Quran Calculator - DEBUG Executable Builder")
    print("=" * 55)
    print("This builds a version with console output for troubleshooting")
    print("")
    
    if build_debug_executable():
        print("\n🎉 DEBUG Build completed successfully!")
        print("\n🔍 Next steps for troubleshooting:")
        print("1. Run: dist\\QuranCalculator-DEBUG.exe --help")
        print("2. Run: dist\\QuranCalculator-DEBUG.exe --port 8081")
        print("3. Check console output for detailed error messages")
        print("4. If it works, the issue was console vs windowed mode")
        print("\n💡 This debug version will show all error messages!")
    else:
        print("\n❌ DEBUG Build failed. Please check the errors above.")
        sys.exit(1)


if __name__ == "__main__":
    main() 