"""
UI Components Module
Modern UI components using customtkinter for Django-like styling
"""

import customtkinter as ctk
from typing import List, Callable, Optional


class ModernEntry(ctk.CTkEntry):
    """Modern entry widget with validation and autocomplete"""
    
    def __init__(self, master, placeholder_text="", width=300, height=40, **kwargs):
        super().__init__(
            master=master,
            placeholder_text=placeholder_text,
            width=width,
            height=height,
            font=ctk.CTkFont(size=14),
            **kwargs
        )
        self.validation_callback = None
        self.autocomplete_values = []
        self.suggestion_var = ctk.StringVar()
        
    def set_validation(self, callback: Callable[[str], bool]):
        """Set validation callback"""
        self.validation_callback = callback
        
    def set_autocomplete_values(self, values: List[str]):
        """Set autocomplete values"""
        self.autocomplete_values = values
        
    def validate_input(self) -> bool:
        """Validate current input"""
        if self.validation_callback:
            return self.validation_callback(self.get())
        return True


class ModernButton(ctk.CTkButton):
    """Modern button with Django-like styling"""
    
    def __init__(self, master, text="", width=200, height=40, **kwargs):
        super().__init__(
            master=master,
            text=text,
            width=width,
            height=height,
            font=ctk.CTkFont(size=14, weight="bold"),
            corner_radius=8,
            **kwargs
        )


class ModernLabel(ctk.CTkLabel):
    """Modern label with consistent styling"""
    
    def __init__(self, master, text="", font_size=14, font_weight="normal", **kwargs):
        super().__init__(
            master=master,
            text=text,
            font=ctk.CTkFont(size=font_size, weight=font_weight),
            **kwargs
        )


class ModernFrame(ctk.CTkFrame):
    """Modern frame container"""
    
    def __init__(self, master, width=None, height=None, **kwargs):
        # Only pass width and height if they are not None
        frame_kwargs = {"master": master, "corner_radius": 10, **kwargs}
        if width is not None:
            frame_kwargs["width"] = width
        if height is not None:
            frame_kwargs["height"] = height
            
        super().__init__(**frame_kwargs)


class ResultCard(ModernFrame):
    """Card component for displaying calculation results"""
    
    def __init__(self, master, width=600, height=400, **kwargs):
        super().__init__(master=master, width=width, height=height, **kwargs)
        
        # Title label
        self.title_label = ModernLabel(
            self, 
            text="Calculation Result",
            font_size=18,
            font_weight="bold"
        )
        self.title_label.pack(pady=(20, 10))
        
        # Result content frame
        self.content_frame = ctk.CTkScrollableFrame(self, width=550, height=320)
        self.content_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
    def display_result(self, result_data: dict):
        """Display calculation result in the card"""
        # Clear existing content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
            
        if not result_data.get("success", False):
            error_label = ModernLabel(
                self.content_frame,
                text=f"Error: {result_data.get('error', 'Unknown error')}",
                font_size=16,
                text_color="red"
            )
            error_label.pack(pady=20)
            return
            
        # Display total ayahs (main result)
        total_label = ModernLabel(
            self.content_frame,
            text=f"Total Ayahs: {result_data['total_ayahs']}",
            font_size=24,
            font_weight="bold",
            text_color="#2E8B57"
        )
        total_label.pack(pady=(0, 10))
        
        # Display estimated pages
        estimated_pages = result_data.get("estimated_pages", 0)
        if estimated_pages > 0:
            pages_label = ModernLabel(
                self.content_frame,
                text=f"Estimated Pages: {estimated_pages}",
                font_size=20,
                font_weight="bold",
                text_color="#2E8B57"
            )
            pages_label.pack(pady=(0, 20))
        
        # Display range information
        range_text = f"From Sura {result_data['start_sura']['number']}: {result_data['start_sura']['name']}\n"
        range_text += f"To Sura {result_data['end_sura']['number']}: {result_data['end_sura']['name']}"
        
        range_label = ModernLabel(
            self.content_frame,
            text=range_text,
            font_size=14
        )
        range_label.pack(pady=(0, 20))
        
        # Display number of suras
        suras_count_label = ModernLabel(
            self.content_frame,
            text=f"Number of Suras: {result_data['number_of_suras']}",
            font_size=16,
            font_weight="bold"
        )
        suras_count_label.pack(pady=(0, 15))
        
        # Display page calculation info
        if "page_info" in result_data:
            page_info = result_data["page_info"]
            page_calc_text = f"Page Calculation: Based on average {page_info['average_ayahs_per_page']} ayahs per page\n"
            page_calc_text += f"(Standard Mushaf has {page_info['total_quran_pages']} pages total)"
            
            page_calc_label = ModernLabel(
                self.content_frame,
                text=page_calc_text,
                font_size=10,
                text_color="#666666"
            )
            page_calc_label.pack(pady=(0, 15))
        
        # Display detailed sura list
        details_label = ModernLabel(
            self.content_frame,
            text="Included Suras:",
            font_size=14,
            font_weight="bold"
        )
        details_label.pack(pady=(0, 10))
        
        # Create a frame for the sura list
        sura_list_frame = ModernFrame(self.content_frame, width=500)
        sura_list_frame.pack(pady=10, padx=10, fill="x")
        
        for sura in result_data['included_suras']:
            pages = sura.get('estimated_pages', 1)
            sura_text = f"{sura['number']}. {sura['name']} ({sura['ayahs']} ayahs, ~{pages} pages)"
            sura_label = ModernLabel(
                sura_list_frame,
                text=sura_text,
                font_size=12
            )
            sura_label.pack(anchor="w", padx=20, pady=2)


class AutocompleteEntry(ModernEntry):
    """Entry widget with dropdown autocomplete"""
    
    def __init__(self, master, autocomplete_values=None, **kwargs):
        super().__init__(master, **kwargs)
        self.autocomplete_values = autocomplete_values or []
        self.dropdown_frame = None
        self.selected_callback = None
        
        # Bind events
        self.bind("<KeyRelease>", self.on_key_release)
        self.bind("<FocusOut>", self.hide_dropdown)
        
    def set_autocomplete_values(self, values: List[str]):
        """Update autocomplete values"""
        self.autocomplete_values = values
        
    def set_selection_callback(self, callback: Callable[[str], None]):
        """Set callback for when item is selected"""
        self.selected_callback = callback
        
    def on_key_release(self, event):
        """Handle key release for autocomplete"""
        current_text = self.get().lower()
        
        if len(current_text) < 2:
            self.hide_dropdown()
            return
            
        # Filter matches
        matches = [name for name in self.autocomplete_values 
                  if current_text in name.lower()][:5]  # Limit to 5 results
        
        if matches:
            self.show_dropdown(matches)
        else:
            self.hide_dropdown()
            
    def show_dropdown(self, matches: List[str]):
        """Show dropdown with matches"""
        if self.dropdown_frame:
            self.dropdown_frame.destroy()
            
        # Create dropdown frame
        self.dropdown_frame = ctk.CTkFrame(self.master)
        self.dropdown_frame.place(
            x=self.winfo_x(),
            y=self.winfo_y() + self.winfo_height(),
            width=self.winfo_width()
        )
        
        # Add match buttons
        for match in matches:
            btn = ctk.CTkButton(
                self.dropdown_frame,
                text=match,
                height=30,
                font=ctk.CTkFont(size=12),
                command=lambda m=match: self.select_item(m)
            )
            btn.pack(fill="x", padx=2, pady=1)
            
    def hide_dropdown(self, event=None):
        """Hide dropdown"""
        if self.dropdown_frame:
            self.dropdown_frame.destroy()
            self.dropdown_frame = None
            
    def select_item(self, item: str):
        """Select an item from dropdown"""
        self.delete(0, "end")
        self.insert(0, item)
        self.hide_dropdown()
        
        if self.selected_callback:
            self.selected_callback(item) 


class SearchableComboBox(ctk.CTkFrame):
    """A searchable combobox that shows a dropdown list with search functionality"""
    
    def __init__(self, master, values=None, width=300, height=40, placeholder_text="Select or search...", **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)
        
        self.values = values or []
        self.filtered_values = self.values.copy()
        self.selected_value = ""
        self.is_open = False
        self.placeholder_text = placeholder_text
        
        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        
        # Main entry field
        self.entry = ctk.CTkEntry(
            self,
            placeholder_text=placeholder_text,
            font=ctk.CTkFont(size=14),
            height=height-4
        )
        self.entry.grid(row=0, column=0, sticky="ew", padx=2, pady=2)
        
        # Dropdown button
        self.dropdown_button = ctk.CTkButton(
            self,
            text="⌄",
            width=30,
            height=height-4,
            command=self.toggle_dropdown,
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.dropdown_button.grid(row=0, column=1, padx=(0, 2), pady=2)
        
        # Dropdown frame (initially hidden)
        self.dropdown_frame = None
        
        # Bind events
        self.entry.bind("<KeyRelease>", self.on_key_release)
        self.entry.bind("<Button-1>", self.on_entry_click)
        
        # Set initial values
        self.set_values(self.values)
        
    def set_values(self, values):
        """Set the list of values for the combobox"""
        self.values = values
        self.filtered_values = values.copy()
        
    def get(self):
        """Get the current value"""
        return self.entry.get()
        
    def set(self, value):
        """Set the current value"""
        self.entry.delete(0, "end")
        self.entry.insert(0, value)
        self.selected_value = value
        
    def clear(self):
        """Clear the current value"""
        self.entry.delete(0, "end")
        self.selected_value = ""
        
    def on_entry_click(self, event=None):
        """Handle entry click to show dropdown"""
        if not self.is_open:
            self.show_dropdown()
            
    def on_key_release(self, event):
        """Handle key release for filtering"""
        if event.keysym in ['Escape']:
            self.hide_dropdown()
            return
            
        current_text = self.entry.get().lower()
        
        # Filter values based on search text
        if current_text:
            self.filtered_values = [value for value in self.values 
                                  if current_text in value.lower()]
        else:
            self.filtered_values = self.values.copy()
            
        # Update dropdown if open
        if len(current_text) >= 1 and len(self.filtered_values) > 0:
            if self.is_open:
                self.update_dropdown()
            else:
                self.show_dropdown()
        elif len(current_text) == 0:
            self.hide_dropdown()
            
    def toggle_dropdown(self):
        """Toggle dropdown visibility"""
        if self.is_open:
            self.hide_dropdown()
        else:
            self.show_dropdown()
            
    def show_dropdown(self):
        """Show the dropdown list"""
        if self.is_open:
            return
            
        self.is_open = True
        self.dropdown_button.configure(text="⌃")
        
        # Create dropdown frame
        self.dropdown_frame = ctk.CTkScrollableFrame(
            self.master,
            width=self.winfo_width(),
            height=min(200, len(self.filtered_values) * 35 + 10),
            fg_color=("white", "gray20")
        )
        
        # Position dropdown below the combobox
        self.update_idletasks()
        x = self.winfo_x()
        y = self.winfo_y() + self.winfo_height()
        
        self.dropdown_frame.place(x=x, y=y)
        
        # Populate dropdown
        self.update_dropdown()
        
        # Simple global click handler
        self.master.winfo_toplevel().bind("<Button-1>", self.check_click_outside, add="+")
        
    def update_dropdown(self):
        """Update dropdown contents"""
        if not self.dropdown_frame:
            return
            
        # Clear existing items
        for widget in self.dropdown_frame.winfo_children():
            widget.destroy()
            
        # Add filtered items (limit to 20 for better performance)
        for value in self.filtered_values[:20]:
            item_button = ctk.CTkButton(
                self.dropdown_frame,
                text=value,
                height=30,
                anchor="w",
                fg_color="transparent",
                hover_color=("lightgray", "gray30"),
                text_color=("black", "white"),
                command=lambda v=value: self.select_and_close(v)
            )
            item_button.pack(fill="x", padx=2, pady=1)
            
    def select_and_close(self, value):
        """Select an item and close dropdown"""
        self.set(value)
        self.hide_dropdown()
        
    def hide_dropdown(self):
        """Hide the dropdown list"""
        if not self.is_open:
            return
            
        self.is_open = False
        self.dropdown_button.configure(text="⌄")
        
        if self.dropdown_frame:
            self.dropdown_frame.destroy()
            self.dropdown_frame = None
            
        # Remove click handler
        try:
            self.master.winfo_toplevel().unbind("<Button-1>")
        except:
            pass
            
    def check_click_outside(self, event):
        """Simple check for clicks outside"""
        # If dropdown frame exists and click is not on it, close
        if self.dropdown_frame and self.is_open:
            # Get click coordinates
            click_x = event.x_root
            click_y = event.y_root
            
            # Get dropdown bounds
            try:
                dropdown_x = self.dropdown_frame.winfo_rootx()
                dropdown_y = self.dropdown_frame.winfo_rooty()
                dropdown_width = self.dropdown_frame.winfo_width()
                dropdown_height = self.dropdown_frame.winfo_height()
                
                # Get combobox bounds
                combo_x = self.winfo_rootx()
                combo_y = self.winfo_rooty()
                combo_width = self.winfo_width()
                combo_height = self.winfo_height()
                
                # Check if click is inside dropdown or combobox
                in_dropdown = (dropdown_x <= click_x <= dropdown_x + dropdown_width and 
                              dropdown_y <= click_y <= dropdown_y + dropdown_height)
                in_combobox = (combo_x <= click_x <= combo_x + combo_width and 
                              combo_y <= click_y <= combo_y + combo_height)
                
                if not in_dropdown and not in_combobox:
                    self.hide_dropdown()
            except:
                # If any error, just close the dropdown
                self.hide_dropdown() 