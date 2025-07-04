# Building Windows Executable for Quran Calculator

This guide explains how to create a standalone Windows executable (.exe) for the Quran Calculator app that can be distributed to users without requiring Python installation.

## Prerequisites

1. **Windows Operating System** (Windows 7 or later)
2. **Python 3.7 or later** installed on your system
   - Download from: https://python.org
   - Make sure to check "Add Python to PATH" during installation
3. **Git** (optional, for cloning the repository)

## Quick Start (Automated Build)

### Option 1: Using the Batch File (Easiest)

1. Open Command Prompt or PowerShell in the project directory
2. Run the automated build script:
   ```cmd
   build_exe.bat
   ```
3. Wait for the build to complete (this may take several minutes)
4. Find your executable in the `dist` folder: `dist/QuranCalculator.exe`

### Option 2: Manual Build Process

1. **Install build dependencies:**
   ```cmd
   pip install -r requirements-build.txt
   ```

2. **Run the build script:**
   ```cmd
   python build_exe.py
   ```

3. **Find your executable:**
   - Location: `dist/QuranCalculator.exe`
   - Size: Approximately 80-120 MB (includes all dependencies)

## Build Process Details

### What the Build Script Does

1. **Dependency Check**: Verifies all required packages are installed
2. **Clean Build**: Removes previous build artifacts
3. **Dynamic Spec Generation**: Creates a PyInstaller specification file with correct paths
4. **Resource Bundling**: Includes:
   - NiceGUI static files (web interface assets)
   - Roboto font file for Arabic text display
   - All Python dependencies
5. **Executable Creation**: Packages everything into a single `.exe` file

### Build Configuration

The build process uses PyInstaller with the following configuration:
- **Single File**: Everything bundled into one executable
- **Windowed Mode**: No console window (set `console=True` in spec for debugging)
- **UPX Compression**: Reduces file size
- **Hidden Imports**: Includes all NiceGUI and FastAPI dependencies

## Troubleshooting

### Common Issues and Solutions

#### 1. "Python is not recognized as an internal or external command"
**Solution**: Python is not in your system PATH
- Reinstall Python and check "Add Python to PATH"
- Or manually add Python to your system PATH

#### 2. "Failed to install dependencies"
**Solutions**:
- Update pip: `python -m pip install --upgrade pip`
- Use virtual environment: 
  ```cmd
  python -m venv venv
  venv\Scripts\activate
  pip install -r requirements-build.txt
  ```

#### 3. "PyInstaller failed" or "Import errors"
**Solutions**:
- Install PyInstaller separately: `pip install pyinstaller`
- Try building with console mode for debugging:
  - Edit `build_exe.py` and set `console=True` in the spec
- Check for missing dependencies and add them to `hiddenimports`

#### 4. "NiceGUI static files not found"
**Solution**: The build script will warn but continue. The app should still work, but might have styling issues.

#### 5. Executable is very large (>150MB)
**Solutions**:
- This is normal for NiceGUI apps due to web dependencies
- Consider using virtual environment to minimize dependencies
- UPX compression is already enabled to reduce size

#### 6. Antivirus flags the executable
**Solution**: This is common with PyInstaller executables
- Add exception in your antivirus software
- Consider code signing for distribution (requires certificate)

### Debug Mode

To build with debug console (helpful for troubleshooting):

1. Edit `build_exe.py`
2. Find the line: `console=False`
3. Change it to: `console=True`
4. Rebuild the executable

This will show a console window with debug output when running the exe.

## Distribution

### Sharing the Executable

1. **Single File Distribution**: Just share `QuranCalculator.exe`
2. **Testing**: Test on a computer without Python to ensure it works standalone
3. **File Size**: The executable will be 80-120 MB due to included web framework
4. **Compatibility**: Works on Windows 7, 8, 10, and 11 (64-bit)

### Creating an Installer (Optional)

For professional distribution, consider creating an installer using:
- **Inno Setup** (free): https://jrsoftware.org/isinfo.php
- **NSIS** (free): https://nsis.sourceforge.io/
- **InstallShield** (commercial)

## Advanced Configuration

### Custom Icon

To add a custom icon:
1. Create or obtain a `.ico` file
2. Edit `build_exe.py` 
3. Change `icon=None` to `icon='path/to/your/icon.ico'`

### Excluding Unnecessary Modules

To reduce file size, you can exclude modules in the spec file:
```python
excludes=['tkinter', 'matplotlib', 'scipy', 'numpy'],
```

### Adding Additional Files

To include additional resources:
```python
datas=[
    ('path/to/file', 'destination'),
    ('config.json', '.'),
]
```

## File Structure After Build

```
project/
├── dist/
│   └── QuranCalculator.exe     # Final executable
├── build/                      # Temporary build files
├── build_exe.py               # Build script
├── build_exe.bat             # Windows batch script
├── requirements-build.txt     # Build dependencies
└── quran_calculator_dynamic.spec  # Generated PyInstaller spec
```

## Performance Notes

- **Startup Time**: First launch may take 5-10 seconds as files are extracted
- **Memory Usage**: Approximately 150-200 MB RAM (includes web server)
- **Antivirus Scanning**: May cause slower startup on first run

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Try building with debug mode enabled
3. Ensure all dependencies are correctly installed
4. Check PyInstaller documentation: https://pyinstaller.org/

---

**Note**: The executable contains a complete web server and browser interface, which is why the file size is larger than typical desktop applications. This is normal for NiceGUI-based applications. 