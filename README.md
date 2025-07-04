# Quran Ayah Calculator

A modern web-based application for calculating ayahs between Quran suras with beautiful Arabic support.

## Features

- 🕌 **Modern Web Interface**: Built with NiceGUI for a beautiful, responsive design
- 📖 **Arabic Support**: Full RTL support with proper Arabic typography using Amiri font
- 🔍 **Smart Search**: Find suras by typing in Arabic or English with real-time filtering
- 🔢 **Accurate Calculations**: Precise ayah counting between any two suras
- 📄 **Page Information**: Displays actual page ranges from the standard 604-page Mushaf
- 📱 **Cross-Platform**: Runs on Windows, macOS, and Linux
- 🎯 **Standalone Executables**: Create distributable .exe files for Windows

## Installation & Usage

### Option 1: Python Installation

1. **Clone or download this repository**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   python main_nicegui.py
   ```
4. **Open your browser** to `http://localhost:8080`

### Option 2: Windows Executable (For Distribution)

**⚠️ IMPORTANT: You must build the executable ON a Windows machine!**

Create a standalone Windows executable that doesn't require Python installation:

#### Quick Build (Windows Only)
```cmd
# Install build dependencies
pip install -r requirements-build.txt

# Build executable using simplified script
python build_exe_simple.py
```

#### Using Batch File (Windows Only)
```cmd
# Run automated build
build_exe.bat
```

The executable will be created in the `dist/` folder as `QuranCalculator.exe` (approximately 35-40 MB).

**Note:** PyInstaller creates platform-specific executables. A Linux build will NOT work on Windows, even if renamed to `.exe`. 

**📚 Guides:**
- [WINDOWS_BUILD_GUIDE.md](WINDOWS_BUILD_GUIDE.md) - How to build on Windows
- [WINDOWS_TROUBLESHOOTING.md](WINDOWS_TROUBLESHOOTING.md) - Fix issues when exe won't run
- [LINUX_USAGE_GUIDE.md](LINUX_USAGE_GUIDE.md) - Running on Linux

#### Build Requirements
- Python 3.7+ with pip
- All dependencies from `requirements-build.txt`

For detailed build instructions and troubleshooting, see [BUILD_EXECUTABLE.md](BUILD_EXECUTABLE.md).

## File Structure

```
quran-calculator/
├── main_nicegui.py          # Main NiceGUI application
├── calculator.py            # Core calculation engine
├── quran_data.py           # Quran data and metadata
├── ui_components.py        # UI helper components
├── validation.py           # Input validation
├── roboto_font.ttf         # Arabic-compatible font
├── build_exe_simple.py     # Simplified build script
├── build_exe.py            # Advanced build script
├── build_exe.bat           # Windows batch build script
├── requirements.txt        # Runtime dependencies
├── requirements-build.txt  # Build dependencies
└── BUILD_EXECUTABLE.md     # Detailed build guide
```

## Technical Details

### Architecture
- **Frontend**: NiceGUI with Arabic-compatible styling
- **Backend**: FastAPI (integrated with NiceGUI)
- **Data**: Static Quran metadata with sura information
- **Font**: Roboto for UI, Amiri for Arabic text

### Arabic Support
- Right-to-left (RTL) text layout
- Proper Arabic font rendering with Amiri
- Unicode-compliant Arabic text display
- Responsive design for Arabic content

### Distribution
- **Development**: Run directly with Python
- **Production**: Standalone executables for easy distribution
- **Platform Support**: Windows, macOS, Linux

## Quran Statistics

- **Total Suras**: 114
- **Total Ayahs**: 6,236
- **Total Pages**: 604 (standard Mushaf)

## License

MIT License - Feel free to use, modify, and distribute.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

---

**Note**: This application uses the standard 604-page Mushaf pagination for page calculations. The Arabic text display requires a modern browser with proper Unicode support. 