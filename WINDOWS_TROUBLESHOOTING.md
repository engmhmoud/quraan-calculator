# Windows Executable Troubleshooting Guide

## ✅ Build Successful, But App Won't Run?

If you successfully built `QuranCalculator.exe` but it's not running, follow these steps to diagnose and fix the issue.

## 🔍 Step 1: Basic Diagnostics

### Test 1: Check if executable responds
```cmd
# Open Command Prompt and navigate to your project folder
cd path\to\quran-calculator

# Test if the executable shows help (basic functionality test)
dist\QuranCalculator.exe --help
```

**Expected Result:** Should show usage information
```
usage: QuranCalculator.exe [-h] [--port PORT] [--no-browser]

Quran Ayah Calculator - Modern web-based app

options:
  -h, --help            show this help message and exit
  --port PORT, -p PORT  Port number to run the web server (default: 8080)
  --no-browser          Don't automatically open browser
```

### Test 2: Try different port
```cmd
# Try running on a different port
dist\QuranCalculator.exe --port 8081 --no-browser
```

### Test 3: Run with console output
```cmd
# Run without --no-browser to see console output
dist\QuranCalculator.exe --port 8081
```

## 🚨 Common Issues & Solutions

### Issue 1: "Windows cannot access the specified device, path, or file"
**Cause:** Antivirus or Windows security blocking the executable

**Solutions:**
1. **Add exception in Windows Defender:**
   - Open Windows Security → Virus & threat protection
   - Add an exclusion for the entire project folder
   
2. **Add exception in your antivirus software**

3. **Run as Administrator:**
   ```cmd
   # Right-click Command Prompt → "Run as administrator"
   cd path\to\quran-calculator
   dist\QuranCalculator.exe --port 8081
   ```

### Issue 2: "Port 8080 is already in use"
**Solution:** Use a different port
```cmd
dist\QuranCalculator.exe --port 8081
dist\QuranCalculator.exe --port 9000
dist\QuranCalculator.exe --port 3000
```

### Issue 3: Missing Visual C++ Redistributables
**Symptoms:** Executable crashes immediately or shows DLL errors

**Solution:** Install Microsoft Visual C++ Redistributable
- Download from: https://aka.ms/vs/17/release/vc_redist.x64.exe
- Install and restart computer

### Issue 4: "Template not found" or web interface broken
**Cause:** Build script didn't include all NiceGUI files

**Solution:** Rebuild with updated script
```cmd
# Make sure you're using the latest build_exe_simple.py
python build_exe_simple.py
```

### Issue 5: Firewall blocking local connections
**Solution:** Allow through Windows Firewall
- Windows Security → Firewall & network protection
- Allow an app through firewall
- Add your executable

### Issue 6: Browser doesn't open automatically
**Solutions:**
1. **Manually open browser** to: http://localhost:8080 (or your custom port)
2. **Check console output** for the actual URL
3. **Try different browser** (Chrome, Firefox, Edge)

## 🛠️ Debugging Steps

### Debug Method 1: Console Mode
If you built with console disabled, rebuild for debugging:

1. **Edit build_exe_simple.py:**
   ```python
   # Find this line (around line 78):
   '--windowed',
   
   # Comment it out or remove it:
   # '--windowed',
   ```

2. **Rebuild:**
   ```cmd
   python build_exe_simple.py
   ```

3. **Test with console:**
   ```cmd
   dist\QuranCalculator.exe --port 8081
   ```
   Now you'll see detailed error messages!

### Debug Method 2: Check Port Availability
```cmd
# Check if port 8080 is busy
netstat -an | findstr :8080

# Kill process using port (if found)
# Use Task Manager or:
taskkill /F /PID <process_id>
```

### Debug Method 3: Test Dependencies
```cmd
# Navigate to project folder
cd path\to\quran-calculator

# Test Python version directly (for comparison)
python main_nicegui.py --port 8081 --no-browser
```

## 🔧 Advanced Troubleshooting

### Check Windows Event Logs
1. Open **Event Viewer** (Windows + R → eventvwr)
2. Go to **Windows Logs → Application**
3. Look for errors around the time you tried running the app

### Test with Process Monitor
1. Download **Process Monitor** from Microsoft Sysinternals
2. Run it while starting your executable
3. Filter by your executable name
4. Look for "ACCESS DENIED" or "PATH NOT FOUND" errors

### Verify File Integrity
```cmd
# Check if executable is valid
dir dist\QuranCalculator.exe

# Should show a file around 35-40 MB
# If it's much smaller or 0 bytes, rebuild
```

## 🏥 Emergency Fixes

### Quick Fix 1: Portable Python Version
If the executable won't work, use Python directly:
```cmd
# Install Python if not already installed
# Then:
pip install -r requirements.txt
python main_nicegui.py --port 8081
```

### Quick Fix 2: Different Build Method
Try the batch file method:
```cmd
build_exe.bat
```

### Quick Fix 3: Different PyInstaller Options
```cmd
# Manual build with different options
pyinstaller --onefile --console --name=QuranCalculator main_nicegui.py
```

## 📞 Getting Help

### Information to Gather
When asking for help, provide:

1. **Windows Version:** (Windows 10/11, build number)
2. **Error Messages:** Exact text of any errors
3. **Console Output:** What happens when you run with `--help`
4. **File Size:** Size of the generated executable
5. **Antivirus Software:** What antivirus you're using
6. **Build Log:** Output from the build process

### Test Commands
```cmd
# Basic info commands
ver
where python
python --version
dist\QuranCalculator.exe --help
dir dist\
```

## ✅ Success Checklist

Your app should be working when:
- [ ] `QuranCalculator.exe --help` shows usage info
- [ ] Executable runs without errors
- [ ] Browser opens automatically OR you can manually open the URL
- [ ] Web interface loads with Arabic text
- [ ] You can select suras and calculate ayahs

## 🎯 Most Common Solution

**90% of issues are resolved by:**
1. **Adding antivirus exception** for the project folder
2. **Using a different port:** `--port 8081`
3. **Running as Administrator**

Try these three steps first before diving into advanced troubleshooting!

---

**Still having issues?** Try the Python version directly while troubleshooting:
```cmd
python main_nicegui.py --port 8081
```

This will help determine if it's an executable-specific issue or a broader problem. 