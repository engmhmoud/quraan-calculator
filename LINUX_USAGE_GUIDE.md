# Running Quran Calculator on Linux

You have **3 different ways** to run the Quran Calculator on Linux. Choose the method that works best for you.

## Method 1: Run the Standalone Executable (Recommended)

The PyInstaller executable includes everything needed and doesn't require Python dependencies.

### Quick Start
```bash
# Make executable (if needed)
chmod +x dist/QuranCalculator

# Run the app (default port 8080)
./dist/QuranCalculator

# Run on custom port (if 8080 is busy)
./dist/QuranCalculator --port 8081

# Run without opening browser automatically
./dist/QuranCalculator --no-browser

# Show help
./dist/QuranCalculator --help
```

### Features
- ✅ **No dependencies** - Everything bundled
- ✅ **Fast startup** - Pre-compiled
- ✅ **Portable** - Single file distribution
- ✅ **File size** - ~35 MB (includes web framework)

### Access the App
1. Run the executable
2. **Open browser** to: `http://localhost:8080`
3. The app will automatically open your default browser

---

## Method 2: Run Python Script Directly

Use the source code directly with Python (requires dependencies).

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app (default port 8080)
python main_nicegui.py

# Run on custom port
python main_nicegui.py --port 8081

# Run without opening browser
python main_nicegui.py --no-browser

# Show help
python main_nicegui.py --help
```

### Features
- ✅ **Smaller footprint** - Uses system Python
- ✅ **Easy debugging** - Source code access
- ✅ **Customizable** - Modify code easily
- ❌ **Requires Python** - Must have dependencies installed

---

## Method 3: Development Mode

For development and testing.

### Setup
```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run with auto-reload
python main_nicegui.py
```

### Features
- ✅ **Isolated environment** - Clean dependencies
- ✅ **Auto-reload** - Changes update automatically
- ✅ **Safe testing** - Doesn't affect system Python

---

## Troubleshooting

### Issue: "Permission denied"
```bash
# Fix permissions
chmod +x dist/QuranCalculator
```

### Issue: "Port already in use"
**EASY FIX**: Use a different port!
```bash
# Use port 8081 instead
./dist/QuranCalculator --port 8081
# OR
python main_nicegui.py --port 8081
```

**Alternative**: Kill the process using port 8080:
```bash
# Check what's using port 8080
sudo netstat -tlnp | grep :8080

# Kill process if needed
sudo kill <process_id>

# Or kill all QuranCalculator processes
pkill -f QuranCalculator
```

### Issue: "Browser doesn't open automatically"
Manually open: `http://localhost:8080`

### Issue: "Executable not found"
Make sure you're in the project directory:
```bash
# Check current directory
pwd
# Should show: /path/to/quran-calculator

# List files
ls dist/
# Should show: QuranCalculator
```

---

## System Requirements

### Minimum Requirements
- **Linux** - Any modern distribution
- **RAM** - 200 MB (when running)
- **Storage** - 50 MB free space
- **Browser** - Any modern browser (Firefox, Chrome, etc.)

### Tested Distributions
- ✅ Ubuntu 20.04+
- ✅ Debian 10+
- ✅ CentOS 7+
- ✅ Fedora 30+
- ✅ Arch Linux

---

## Features on Linux

### Arabic Support
- ✅ **RTL Layout** - Right-to-left text direction
- ✅ **Arabic Fonts** - Proper Arabic typography
- ✅ **Unicode** - Full Arabic character support

### Performance
- **Startup Time** - 2-3 seconds
- **Memory Usage** - ~150-200 MB
- **CPU Usage** - Low (web server + browser)

### Network
- **Local Only** - Binds to localhost:8080
- **No Internet** - Works completely offline
- **Firewall** - No external connections needed

---

## Distribution on Linux

### For End Users
1. **Share the executable** - `dist/QuranCalculator`
2. **No installation** - Just download and run
3. **Self-contained** - All dependencies included

### For System-Wide Installation
```bash
# Copy to system directory
sudo cp dist/QuranCalculator /usr/local/bin/

# Make accessible globally
QuranCalculator
```

### Create Desktop Entry
Create `~/.local/share/applications/quran-calculator.desktop`:
```ini
[Desktop Entry]
Name=Quran Calculator
Name[ar]=حاسبة آيات القرآن
Comment=Calculate ayahs between Quran suras
Comment[ar]=احسب الآيات بين سور القرآن
Exec=/path/to/dist/QuranCalculator
Icon=application-x-executable
Terminal=false
Type=Application
Categories=Education;Religion;
```

---

## Command Line Options

### Run in Background
```bash
# Run without blocking terminal
./dist/QuranCalculator &

# Run with nohup (continues after logout)
nohup ./dist/QuranCalculator &
```

### Custom Port (Python version only)
```bash
# Modify main_nicegui.py to change port
python main_nicegui.py
```

---

## Comparison: Executable vs Python

| Feature | Executable | Python Script |
|---------|------------|---------------|
| Dependencies | ❌ None needed | ✅ Requires Python + packages |
| File Size | ❌ ~35 MB | ✅ ~100 KB (source only) |
| Startup Speed | ✅ Fast | ❌ Slower (import time) |
| Customization | ❌ Limited | ✅ Full source access |
| Distribution | ✅ Single file | ❌ Multiple files + deps |
| Updates | ❌ Rebuild needed | ✅ Edit source directly |

---

## Quick Reference

```bash
# Most common usage (default port 8080)
chmod +x dist/QuranCalculator && ./dist/QuranCalculator

# If port 8080 is busy, use different port
./dist/QuranCalculator --port 8081

# Available command line options
./dist/QuranCalculator --help
```

Then open in your browser:
- Default: **http://localhost:8080**
- Custom: **http://localhost:[YOUR_PORT]**

**Happy calculating! 🕌** 