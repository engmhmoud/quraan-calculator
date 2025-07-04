#!/usr/bin/env python3
"""
Quran Ayah Calculator
A modern desktop application for calculating ayahs between Quran suras

Usage:
    python main.py

Requirements:
    - Python 3.7+
    - customtkinter
    - pillow

Author: AI Assistant
License: MIT
"""

import sys
import os

# Add current directory to Python path to enable imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from main_window import QuranCalculatorApp
    print("✓ All modules loaded successfully")
except ImportError as e:
    print(f"❌ Error importing modules: {e}")
    print("\nPlease install required dependencies:")
    print("pip install -r requirements.txt")
    sys.exit(1)


def check_dependencies():
    """Check if all required dependencies are available"""
    dependencies = ["customtkinter", "PIL"]
    missing = []
    
    for dep in dependencies:
        try:
            __import__(dep)
        except ImportError:
            missing.append(dep)
    
    if missing:
        print(f"❌ Missing dependencies: {', '.join(missing)}")
        print("Please install them using: pip install -r requirements.txt")
        return False
    
    print("✓ All dependencies are available")
    return True


def main():
    """Main function to start the Quran Calculator application"""
    print("🕌 Starting Quran Ayah Calculator...")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    try:
        # Create and run the application
        app = QuranCalculatorApp()
        print("✓ Application initialized")
        print("✓ Starting GUI...")
        
        app.run()
        
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        print("Please check the error details and try again")
        sys.exit(1)
    finally:
        print("🔚 Application closed")


if __name__ == "__main__":
    main() 