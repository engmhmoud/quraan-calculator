#!/usr/bin/env python3
"""
Quran Ayah Calculator - NiceGUI Version with Arabic Support
A modern web-based application for calculating ayahs between Quran suras

Usage:
    python main_nicegui.py

Requirements:
    - Python 3.7+
    - nicegui
    - pillow

Author: AI Assistant
License: MIT
"""

from nicegui import ui, app
from typing import List, Optional
import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Add static file route for the local font
app.add_static_files('/fonts', os.path.dirname(os.path.abspath(__file__)))

from quran_data import SURAS, get_sura_names, get_sura_by_name
from calculator import calculator


class QuranCalculatorNiceGUI:
    """Main application class for Quran Calculator using NiceGUI with Arabic support"""
    
    def __init__(self):
        self.sura_names = get_sura_names()
        self.language_mode = "arabic"  # Set to Arabic only
        self.sura_options = self.prepare_sura_options()
        self.setup_ui()
        
    def prepare_sura_options(self):
        """Prepare sura options for Arabic display"""
        options = []
        for num, sura in SURAS.items():
            # Format: "1. الفاتحة" (Arabic only)
            display_name = f"{num}. {sura['arabic']}"
            options.append(display_name)
        return options
    
    def get_sura_name_from_option(self, option_text):
        """Extract the English sura name from the selected option"""
        if not option_text:
            return None
        
        # Extract the sura number from the option text
        try:
            sura_num = int(option_text.split('.')[0])
            return SURAS[sura_num]['name']
        except (ValueError, IndexError, KeyError):
            return None

        
    def setup_ui(self):
        """Setup the user interface with Arabic support"""
        # Set page configuration
        ui.page_title('حاسبة آيات القرآن الكريم')
        
        # Custom CSS for modern styling with Arabic support
        ui.add_head_html('''
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap');
            
            @font-face {
                font-family: 'RobotoLocal';
                src: url('/fonts/roboto_font.ttf') format('truetype');
                font-weight: normal;
                font-style: normal;
            }
            .rtl {
                direction: rtl;
            }
            
            .main-container {
                max-width: 1000px;
                margin: 0 auto;
                padding: 20px;
                font-family: 'RobotoLocal', sans-serif;
                direction: rtl;
            }
            .arabic-text {
                font-family: 'Amiri', serif;
                font-size: 1.2em;
                direction: rtl;
                text-align: right;
                color: #2E8B57;
                font-weight: 500;
            }
            .sura-name-arabic {
                font-family: 'Amiri', serif;
                font-size: 1.1em;
                color: #2E8B57;
                margin: 5px 0;
            }
            .header-title {
                color: #2E8B57;
                text-align: center;
                margin-bottom: 10px;
            }
            .header-subtitle {
                color: #666666;
                text-align: center;
                margin-bottom: 30px;
            }
            .input-section {
                background: white;
                border-radius: 10px;
                padding: 30px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                margin-bottom: 20px;
            }
            .result-section {
                background: white;
                border-radius: 10px;
                padding: 30px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                min-height: 300px;
            }
            .sura-input-row {
                display: flex;
                align-items: center;
                margin-bottom: 20px;
                gap: 20px;
                
            }
            .sura-label {
                width: 120px;
                font-weight: bold;
                font-size: 14px;
            }
            .calculate-btn {
                background: #2E8B57 !important;
                color: white !important;
                font-weight: bold !important;
                font-size: 16px !important;
                padding: 15px 30px !important;
                border-radius: 8px !important;
                margin: 20px 10px !important;
            }
            .clear-btn {
                background: #808080 !important;
                color: white !important;
                font-weight: bold !important;
                font-size: 14px !important;
                padding: 10px 20px !important;
                border-radius: 8px !important;
                margin: 10px !important;
            }

            .result-title {
                color: #2E8B57;
                font-size: 24px;
                font-weight: bold;
                text-align: center;
                margin-bottom: 20px;
            }
            .result-total {
                color: #2E8B57;
                font-size: 28px;
                font-weight: bold;
                text-align: center;
                margin: 20px 0;
            }
            .result-details {
                margin-top: 20px;
                padding: 20px;
                background: #f8f9fa;
                border-radius: 8px;
            }
            .sura-item {
                padding: 8px 0;
                border-bottom: 1px solid #eee;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .sura-item-english {
                flex: 1;
            }
            .sura-item-arabic {
                font-family: 'Amiri', serif;
                color: #2E8B57;
                font-size: 1.1em;
                margin-left: 10px;
            }
            .page-range-info {
                background: #e8f5e8;
                padding: 15px;
                border-radius: 8px;
                margin: 15px 0;
                border-left: 4px solid #2E8B57;
            }
            .welcome-message {
                text-align: center;
                color: #2E8B57;
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 20px;
            }
            .instruction-list {
                list-style: none;
                padding: 0;
                margin: 20px 0;
            }
            .instruction-list li {
                padding: 8px 0;
                font-size: 14px;
                color: #333;
            }
            .stats-info {
                text-align: center;
                color: #666;
                font-size: 12px;
                margin-top: 20px;
            }
            /* Select dropdown styling for Arabic text */
            .q-field--filled .q-field__control {
                font-family: 'RobotoLocal', sans-serif;
                direction: rtl;
                text-align: right;
            }
            .q-item__label {
                font-family: 'RobotoLocal', sans-serif;
                direction: rtl;
                text-align: right;
            }
            .q-field__label {
                direction: rtl;
                text-align: right;
                font-family: 'RobotoLocal', sans-serif;
            }
            .q-field__input {
                direction: rtl;
                text-align: right;
                font-family: 'RobotoLocal', sans-serif;
            }
            .q-select .q-field__input {
                direction: rtl;
                text-align: right;
            }
            .q-menu .q-item {
                direction: rtl;
                text-align: right;
            }
        </style>
        ''')
        
        with ui.column().classes('main-container'):
            # Header
            self.setup_header()
            
            # Input section
            self.setup_input_section()
            
            # Results section
            self.setup_results_section()
            
            # Footer
            self.setup_footer()
            
    def setup_header(self):
        """Setup application header with Arabic support"""
        ui.html('<div class="arabic-text" style="text-align: center; font-size: 1.8em; margin: 20px 0; font-weight: bold;">حاسبة آيات القرآن الكريم</div>')
        ui.html('<p class="header-subtitle" style="text-align: center; color: #666666;">احسب عدد الآيات بين أي سورتين من القرآن الكريم</p>')
        
    def setup_input_section(self):
        """Setup input fields and buttons with Arabic support"""
        with ui.card().classes('input-section'):
            ui.html('<h3 style="color: #333; margin-bottom: 20px; font-weight: bold;">اختر أو ابحث عن سورتين لحساب الآيات بينهما:</h3>')
                    
            # First sura selection
            with ui.row().classes('sura-input-row rtl'):
                ui.html('<div class="sura-label">السورة الأولى:</div>')
                self.sura1_select = ui.select(
                    options=self.sura_options,
                    with_input=True,
                    label='اختر أو ابحث عن السورة الأولى...'
                ).style('width: 400px')
                
            # Second sura selection  
            with ui.row().classes('sura-input-row rtl'):
                ui.html('<div class="sura-label">السورة الثانية:</div>')
                self.sura2_select = ui.select(
                    options=self.sura_options,
                    with_input=True,
                    label='اختر أو ابحث عن السورة الثانية...'
                ).style('width: 400px')
                
            # Buttons
            with ui.row().style('justify-content: center; margin-top: 20px'):
                ui.button('احسب الآيات', on_click=self.calculate_ayahs).classes('calculate-btn')
                ui.button('مسح', on_click=self.clear_inputs).classes('clear-btn')
                
    def setup_results_section(self):
        """Setup results display section"""
        with ui.card().classes('result-section'):
            ui.html('<h2 style="text-align: center; color: #333; margin-bottom: 20px;">نتيجة الحساب</h2>')
            
            self.result_container = ui.column()
            self.show_welcome_message()
            
    def setup_footer(self):
        """Setup application footer"""
        ui.html('''
        <div style="text-align: center; margin-top: 20px; padding: 20px; color: #888; font-size: 10px;">
            © 2024 حاسبة آيات القرآن الكريم - مبنية بـ Python و NiceGUI
        </div>
        ''')
        
    def show_welcome_message(self):
        """Show welcome message in results area"""
        self.result_container.clear()
        
        with self.result_container:
            ui.html('<div class="welcome-message">مرحباً بكم في حاسبة آيات القرآن الكريم!</div>')
            
            ui.html('''
            <ul class="instruction-list">
                <li>📖 اختر أو ابحث عن سورتين لحساب الآيات بينهما</li>
                <li>📋 استخدم القوائم المنسدلة لتصفح جميع السور الـ 114 باللغة العربية</li>
                <li>🔍 اكتب للبحث وتصفية السور في الوقت الفعلي</li>
                <li>🔢 ستظهر النتائج إجمالي الآيات ونطاقات الصفحات الفعلية والتفاصيل</li>
                <li>📄 حساب الصفحات يعتمد على الصفحات الأولى للسور من المصحف القياسي 604 صفحة</li>
                <li>🔄 انقر على "مسح" لإعادة تعيين النموذج</li>
            </ul>
            ''')
            
            ui.html('''
            <div class="stats-info">
                <strong>إحصائيات القرآن الكريم:</strong><br>
                • إجمالي السور: 114<br>
                • إجمالي الآيات: 6,236<br>
                • إجمالي الصفحات: 604 (المصحف القياسي)
            </div>
            ''')
            
    def calculate_ayahs(self):
        """Calculate ayahs between two suras"""
        sura1_option = self.sura1_select.value
        sura2_option = self.sura2_select.value
        
        # Extract English sura names from the selected options
        sura1_name = self.get_sura_name_from_option(sura1_option)
        sura2_name = self.get_sura_name_from_option(sura2_option)
        
        # Validate inputs
        if not sura1_name or not sura2_name:
            self.show_error("يرجى اختيار اسمي السورتين")
            return
            
        if sura1_name == sura2_name:
            self.show_error("يرجى اختيار سورتين مختلفتين")
            return
            
        # Perform calculation
        result = calculator.calculate_ayahs_between_suras(sura1_name, sura2_name)
        
        # Display result
        self.display_result(result)
        
    def show_error(self, message: str):
        """Show error message"""
        self.result_container.clear()
        
        with self.result_container:
            ui.html(f'''
            <div style="text-align: center; color: red; font-size: 18px; margin: 50px 0;">
                <strong>خطأ:</strong> {message}
            </div>
            ''')
            
    def display_result(self, result_data: dict):
        """Display calculation result with Arabic support and actual page information"""
        self.result_container.clear()
        
        with self.result_container:
            if not result_data.get("success", False):
                error_msg = result_data.get('error', 'Unknown error')
                ui.html(f'''
                <div style="text-align: center; color: red; font-size: 18px; margin: 50px 0;">
                    <strong>خطأ:</strong> {error_msg}
                </div>
                ''')
                return
                
            # Display total ayahs (main result)
            ui.html(f'<div class="result-total">إجمالي الآيات: {result_data["total_ayahs"]}</div>')
            
            # Display actual pages instead of estimated
            total_pages = result_data.get("total_pages", 0)
            page_range = result_data.get("page_range", {})
            
            if total_pages > 0 and page_range:
                ui.html(f'''
                <div style="text-align: center; color: #2E8B57; font-size: 20px; font-weight: bold; margin: 10px 0;">
                    نطاق الصفحات: {total_pages} صفحة (من صفحة {page_range.get("start_page", 0)} إلى صفحة {page_range.get("end_page", 0)})
                </div>
                ''')
            
            # Display range information with Arabic names
            start_sura = result_data["start_sura"]
            end_sura = result_data["end_sura"]
            
            range_text = f'''
            <div style="text-align: center; font-size: 16px; margin: 20px 0;">
                <div style="margin-bottom: 10px;">
                    <strong>من السورة {start_sura["number"]}:</strong> {start_sura["name"]}
                    <div class="sura-name-arabic">{start_sura["arabic"]}</div>
                    <small>(صفحة {start_sura["page_start"]})</small>
                </div>
                <div style="margin-top: 15px;">
                    <strong>إلى السورة {end_sura["number"]}:</strong> {end_sura["name"]}
                    <div class="sura-name-arabic">{end_sura["arabic"]}</div>
                    <small>(صفحة {end_sura["page_start"]})</small>
                </div>
            </div>
            '''
            ui.html(range_text)
            
            # Display number of suras
            ui.html(f'''
            <div style="text-align: center; font-size: 18px; font-weight: bold; margin: 20px 0;">
                عدد السور: {result_data["number_of_suras"]}
            </div>
            ''')
            
            # Display page calculation info with actual page data
            if "page_info" in result_data:
                page_info = result_data["page_info"]
                ui.html(f'''
                <div class="page-range-info">
                    <strong>📄 معلومات الصفحات:</strong><br>
                    • إجمالي الصفحات المقدرة: {page_info["total_pages"]}<br>
                    • من الصفحة الأولى للسورة الأولى: {page_info["start_page"]}<br>
                    • إلى الصفحة الأولى للسورة الأخيرة: {page_info["end_page"]}<br>
                    • طريقة الحساب: {page_info["calculation_method"]}<br>
                    • إجمالي صفحات القرآن: {page_info["total_quran_pages"]}
                </div>
                ''')
            
            # Display detailed sura list with Arabic names and page info
            with ui.expansion("إظهار قائمة السور التفصيلية", icon='list').classes('result-details'):
                for sura in result_data['included_suras']:
                    page_info = f"صفحة {sura['page_start']}" if sura.get('page_start') else "صفحة غير محددة"
                    
                    ui.html(f'''
                    <div class="sura-item">
                        <div class="sura-item-english">
                            <strong>{sura["number"]}. {sura["name"]}</strong><br>
                            <small>{sura["ayahs"]} آية، {page_info}</small>
                        </div>
                        <div class="sura-item-arabic">{sura["arabic"]}</div>
                    </div>
                    ''')
                    
    def clear_inputs(self):
        """Clear input fields and reset results"""
        self.sura1_select.value = None
        self.sura2_select.value = None
        self.show_welcome_message()


def main():
    """Main function to start the application"""
    import argparse
    import sys
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Quran Ayah Calculator - Modern web-based app')
    parser.add_argument('--port', '-p', type=int, default=8080, 
                       help='Port number to run the web server (default: 8080)')
    parser.add_argument('--no-browser', action='store_true',
                       help='Don\'t automatically open browser')
    
    args = parser.parse_args()
    
    print("🕌 Starting Quran Ayah Calculator (NiceGUI)...")
    print("=" * 50)
    print(f"📡 Server will run on port: {args.port}")
    
    try:
        # Create the application
        app_instance = QuranCalculatorNiceGUI()
        print("✓ Application initialized")
        print("✓ Starting web server...")
        
        # Run the application
        ui.run(
            title='Quran Ayah Calculator',
            port=args.port,
            show=not args.no_browser,
            reload=False,
            dark=False
        )
        
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        print("Please check the error details and try again")
        sys.exit(1)


if __name__ == "__main__":
    main() 