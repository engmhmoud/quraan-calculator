@echo off
echo ======================================================
echo Quran Calculator - Windows Executable Builder
echo ======================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://python.org
    pause
    exit /b 1
)

echo Python is installed
echo.

REM Install required dependencies
echo Installing required dependencies...
pip install -r requirements-build.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo Dependencies installed successfully
echo.

REM Run the build script
echo Building executable...
python build_exe.py
if errorlevel 1 (
    echo ERROR: Build failed
    pause
    exit /b 1
)

echo.
echo ======================================================
echo Build completed successfully!
echo The executable is located in the 'dist' folder
echo ======================================================
pause 