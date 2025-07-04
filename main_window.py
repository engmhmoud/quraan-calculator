"""
Main Application Window
Modern Quran Calculator Desktop Application
"""

import customtkinter as ctk
from ui_components import (
    ModernEntry, ModernButton, ModernLabel, 
    ModernFrame, ResultCard, AutocompleteEntry, SearchableComboBox
)
from calculator import calculator
from quran_data import get_sura_names


class QuranCalculatorApp:
    """Main application class for Quran Calculator"""
    
    def __init__(self):
        # Set appearance mode and color theme
        ctk.set_appearance_mode("light")  # Modes: "System" (default), "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"
        
        # Create main window
        self.root = ctk.CTk()
        self.root.title("Quran Ayah Calculator")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Center the window
        self.center_window()
        
        # Initialize components
        self.setup_ui()
        
        # Get sura names for autocomplete
        self.sura_names = get_sura_names()
        
        # Configure searchable comboboxes
        self.sura1_entry.set_values(self.sura_names)
        self.sura2_entry.set_values(self.sura_names)
        
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        
        # Get window dimensions with fallback values
        width = self.root.winfo_width() or 900
        height = self.root.winfo_height() or 700
        
        # Ensure we have valid dimensions
        if width <= 1:
            width = 900
        if height <= 1:
            height = 700
            
        # Calculate center position
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        # Ensure position is not negative
        x = max(0, x)
        y = max(0, y)
        
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def setup_ui(self):
        """Setup the user interface"""
        # Main container
        self.main_frame = ModernFrame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Header
        self.setup_header()
        
        # Input section
        self.setup_input_section()
        
        # Results section
        self.setup_results_section()
        
        # Footer
        self.setup_footer()
        
    def setup_header(self):
        """Setup application header"""
        header_frame = ModernFrame(self.main_frame)
        header_frame.pack(fill="x", pady=(0, 30))
        
        # Title
        title_label = ModernLabel(
            header_frame,
            text="Quran Ayah Calculator",
            font_size=28,
            font_weight="bold",
            text_color="#2E8B57"
        )
        title_label.pack(pady=20)
        
        # Subtitle
        subtitle_label = ModernLabel(
            header_frame,
            text="Calculate the number of ayahs between any two suras of the Quran",
            font_size=14,
            text_color="#666666"
        )
        subtitle_label.pack(pady=(0, 10))
        
    def setup_input_section(self):
        """Setup input fields and calculate button"""
        input_frame = ModernFrame(self.main_frame)
        input_frame.pack(fill="x", pady=(0, 20))
        
        # Instructions
        instruction_label = ModernLabel(
            input_frame,
            text="Select or search for two suras to calculate ayahs between them:",
            font_size=16,
            font_weight="bold"
        )
        instruction_label.pack(pady=(20, 20))
        
        # Input fields container
        fields_frame = ctk.CTkFrame(input_frame, fg_color="transparent")
        fields_frame.pack(pady=10)
        
        # First sura input
        sura1_label = ModernLabel(fields_frame, text="First Sura:", font_size=14, font_weight="bold")
        sura1_label.grid(row=0, column=0, padx=(20, 10), pady=10, sticky="w")
        
        self.sura1_entry = SearchableComboBox(
            fields_frame,
            placeholder_text="Select or search first sura...",
            width=300,
            values=[]
        )
        self.sura1_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Second sura input
        sura2_label = ModernLabel(fields_frame, text="Second Sura:", font_size=14, font_weight="bold")
        sura2_label.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="w")
        
        self.sura2_entry = SearchableComboBox(
            fields_frame,
            placeholder_text="Select or search second sura...",
            width=300,
            values=[]
        )
        self.sura2_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # Calculate button
        self.calculate_button = ModernButton(
            input_frame,
            text="Calculate Ayahs",
            width=250,
            height=50,
            command=self.calculate_ayahs,
            fg_color="#2E8B57",
            hover_color="#228B22"
        )
        self.calculate_button.pack(pady=20)
        
        # Clear button
        self.clear_button = ModernButton(
            input_frame,
            text="Clear",
            width=150,
            height=35,
            command=self.clear_inputs,
            fg_color="#808080",
            hover_color="#696969"
        )
        self.clear_button.pack(pady=5)
        
    def setup_results_section(self):
        """Setup results display section"""
        # Results card
        self.result_card = ResultCard(self.main_frame, width=800, height=350)
        self.result_card.pack(fill="both", expand=True, pady=10)
        
        # Initially hide results
        self.show_welcome_message()
        
    def setup_footer(self):
        """Setup application footer"""
        footer_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        footer_frame.pack(fill="x", pady=(10, 0))
        
        footer_label = ModernLabel(
            footer_frame,
            text="© 2024 Quran Ayah Calculator - Built with Python & CustomTkinter",
            font_size=10,
            text_color="#888888"
        )
        footer_label.pack(pady=5)
        
    def show_welcome_message(self):
        """Show welcome message in results area"""
        welcome_data = {
            "success": True,
            "total_ayahs": 6236,  # Total ayahs in Quran
            "start_sura": {"number": 1, "name": "Al-Fatiha", "ayahs": 7},
            "end_sura": {"number": 114, "name": "An-Nas", "ayahs": 6},
            "included_suras": [],
            "number_of_suras": 114
        }
        
        # Clear existing content
        for widget in self.result_card.content_frame.winfo_children():
            widget.destroy()
            
        # Welcome message
        welcome_label = ModernLabel(
            self.result_card.content_frame,
            text="Welcome to Quran Ayah Calculator!",
            font_size=20,
            font_weight="bold",
            text_color="#2E8B57"
        )
        welcome_label.pack(pady=(30, 20))
        
        # Instructions
        instructions = [
            "📖 Select or search for two suras to calculate ayahs between them",
            "📋 Click dropdown arrows to see full sura list",
            "🔍 Type to search and filter suras in real-time",
            "🔢 Results will show total ayahs, estimated pages, and detailed breakdown",
            "📄 Page calculation based on standard 604-page Mushaf",
            "🔄 Click 'Clear' to reset the form"
        ]
        
        for instruction in instructions:
            inst_label = ModernLabel(
                self.result_card.content_frame,
                text=instruction,
                font_size=14
            )
            inst_label.pack(pady=5, anchor="w")
            
        # Quick stats
        stats_label = ModernLabel(
            self.result_card.content_frame,
            text=f"\nQuran Statistics:\n• Total Suras: 114\n• Total Ayahs: 6,236\n• Total Pages: 604 (Standard Mushaf)",
            font_size=12,
            text_color="#666666"
        )
        stats_label.pack(pady=20)
        
    def calculate_ayahs(self):
        """Calculate ayahs between two suras"""
        sura1_name = self.sura1_entry.get().strip()
        sura2_name = self.sura2_entry.get().strip()
        
        # Validate inputs
        if not sura1_name or not sura2_name:
            self.show_error("Please enter both sura names")
            return
            
        if sura1_name.lower() == sura2_name.lower():
            self.show_error("Please enter two different suras")
            return
            
        # Perform calculation
        result = calculator.calculate_ayahs_between_suras(sura1_name, sura2_name)
        
        # Display result
        self.result_card.display_result(result)
        
        # Add animation effect
        self.animate_button()
        
    def show_error(self, message):
        """Show error message"""
        error_result = {
            "success": False,
            "error": message,
            "total_ayahs": 0
        }
        self.result_card.display_result(error_result)
        
    def clear_inputs(self):
        """Clear input fields and reset results"""
        self.sura1_entry.clear()
        self.sura2_entry.clear()
        self.show_welcome_message()
        
        # Hide any dropdowns
        self.sura1_entry.hide_dropdown()
        self.sura2_entry.hide_dropdown()
        
    def animate_button(self):
        """Simple button animation effect"""
        original_color = self.calculate_button.cget("fg_color")
        self.calculate_button.configure(fg_color="#32CD32")
        self.root.after(200, lambda: self.calculate_button.configure(fg_color=original_color))
        
    def run(self):
        """Start the application"""
        self.root.mainloop()


def main():
    """Main function to run the application"""
    app = QuranCalculatorApp()
    app.run()


if __name__ == "__main__":
    main() 