# Building Windows Executable - Step-by-Step Guide

## ⚠️ Important: Platform Requirement

**You MUST build the Windows executable ON a Windows machine.** PyInstaller creates executables for the platform it's running on. A Linux build will NOT work on Windows, even if you rename it to `.exe`.

## Prerequisites (Windows)

1. **Windows 10/11** (64-bit recommended)
2. **Python 3.7+** installed from [python.org](https://python.org)
   - ✅ Check "Add Python to PATH" during installation
3. **Command Prompt** or **PowerShell**

## Step-by-Step Build Process

### Step 1: Setup Project
```cmd
# Download or clone the project to your Windows machine
# Navigate to the project directory
cd path\to\quran-calculator
```

### Step 2: Install Dependencies
```cmd
# Install build dependencies
pip install -r requirements-build.txt
```

### Step 3: Build Executable
Choose one of these methods:

#### Method A: Automated Build (Easiest)
```cmd
build_exe.bat
```

#### Method B: Python Script
```cmd
python build_exe_simple.py
```

#### Method C: Manual PyInstaller
```cmd
pyinstaller --onefile --windowed --name=QuranCalculator main_nicegui.py
```

### Step 4: Test Executable
```cmd
# Navigate to dist folder
cd dist

# Run the executable
QuranCalculator.exe
```

## Expected Results

✅ **Success Indicators:**
- File created: `dist\QuranCalculator.exe`
- Size: ~35-40 MB
- Opens browser automatically when run
- Shows "Windows executable ready for distribution!"

❌ **Common Issues:**
- Missing dependencies → Install `requirements-build.txt`
- Python not in PATH → Reinstall Python with PATH option
- Antivirus blocking → Add exception for project folder

## Distribution

Once built successfully:
1. **Share the .exe file** - It's completely standalone
2. **No installation required** for end users
3. **Works on any Windows machine** (7, 8, 10, 11)
4. **File size** will be 35-40 MB (includes everything)

## Cross-Platform Notes

- **Linux build** → Creates `QuranCalculator` (Linux binary)
- **Windows build** → Creates `QuranCalculator.exe` (Windows binary)
- **macOS build** → Creates `QuranCalculator` (macOS binary)

**You cannot use a Linux executable on Windows, even with renaming!**

## Troubleshooting

### Issue: "Python not recognized"
**Solution:** Add Python to PATH or reinstall Python

### Issue: "pyinstaller not found"
**Solution:** 
```cmd
pip install pyinstaller
```

### Issue: Antivirus flags executable
**Solution:** 
- This is normal for PyInstaller executables
- Add exception in your antivirus
- For distribution, consider code signing

### Issue: Large file size
**Solution:** 
- 35-40 MB is normal for NiceGUI apps
- Includes complete web framework
- Cannot be reduced significantly

## Alternative: Online Conversion Services

❌ **DO NOT USE** online "Linux to Windows" converters:
- They don't work for executables
- Security risk
- Will not function properly

## Need Help?

If you encounter issues:
1. Check this guide's troubleshooting section
2. Verify you're on Windows
3. Ensure Python 3.7+ is properly installed
4. Try the automated batch file method first

---

**Remember: Always build executables on the target platform!** 