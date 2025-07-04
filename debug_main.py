#!/usr/bin/env python3
"""
Debug version of Quran Calculator to identify the exact error location
"""

import sys
import os
import traceback

# Add current directory to Python path to enable imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    """Main function to start the Quran Calculator application with detailed error tracking"""
    print("🕌 Starting Quran Ayah Calculator (Debug Mode)...")
    print("=" * 50)
    
    try:
        print("Step 1: Importing customtkinter...")
        import customtkinter as ctk
        print("✓ customtkinter imported successfully")
        
        print("Step 2: Importing main_window...")
        from main_window import QuranCalculatorApp
        print("✓ main_window imported successfully")
        
        print("Step 3: Creating application instance...")
        app = QuranCalculatorApp()
        print("✓ Application instance created")
        
        print("Step 4: Starting application...")
        app.run()
        
    except Exception as e:
        print(f"❌ Detailed error information:")
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {str(e)}")
        print("\nFull traceback:")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main() 