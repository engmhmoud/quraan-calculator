"""
Quran Calculator Module
Handles calculations for ayahs between suras with actual page information
"""

from quran_data import SURAS, get_sura_number_by_name, is_valid_sura_name


class QuranCalculator:
    """Calculator for Quran ayah calculations with actual page data"""
    
    def __init__(self):
        self.suras = SURAS
        # Quran constants
        self.TOTAL_PAGES = 604  # Standard Mushaf pages
        self.TOTAL_AYAHS = 6236  # Total ayahs in Quran
        self.AVERAGE_AYAHS_PER_PAGE = self.TOTAL_AYAHS / self.TOTAL_PAGES  # ~10.3 ayahs per page
    
    def get_page_range_for_sura(self, sura_num):
        """
        Get the page start for a sura from quran_data (ignoring page_end)
        
        Args:
            sura_num (int): Sura number
            
        Returns:
            tuple: (start_page, None, 1) - simplified to only use start page
        """
        if sura_num not in self.suras:
            return None, None, 0
            
        sura_info = self.suras[sura_num]
        start_page = sura_info["page_start"]
        # Ignore page_end, assume each sura takes 1 page unit
        
        return start_page, None, 1
    
    def calculate_page_range_between_suras(self, start_sura_num, end_sura_num):
        """
        Calculate the page range between two suras using page_start and page_end
        
        Args:
            start_sura_num (int): Starting sura number
            end_sura_num (int): Ending sura number
            
        Returns:
            dict: Page range information using start and end pages
        """
        start_page = self.suras[start_sura_num]["page_start"]
        end_page = self.suras[end_sura_num]["page_end"]
        # Calculate total pages from start of first sura to end of second sura
        total_pages = abs(end_page - start_page) + 1
        
        return {
            "start_page": start_page,
            "end_page": end_page,
            "total_pages": total_pages
        }

    def calculate_ayahs_between_suras(self, sura1_name, sura2_name):
        """
        Calculate the number of ayahs between two suras (inclusive) with actual page data
        Supports both forward and reverse calculation (e.g., from sura 15 to 5 or 5 to 15)
        
        Args:
            sura1_name (str): Name of the first sura
            sura2_name (str): Name of the second sura
            
        Returns:
            dict: Contains result, total_ayahs, actual page ranges, direction, and other details
        """
        # Validate sura names
        if not is_valid_sura_name(sura1_name):
            return {
                "success": False,
                "error": f"'{sura1_name}' is not a valid sura name",
                "total_ayahs": 0,
                "total_pages": 0
            }
        
        if not is_valid_sura_name(sura2_name):
            return {
                "success": False,
                "error": f"'{sura2_name}' is not a valid sura name",
                "total_ayahs": 0,
                "total_pages": 0
            }
        
        # Get sura numbers
        sura1_num = get_sura_number_by_name(sura1_name)
        sura2_num = get_sura_number_by_name(sura2_name)
        
        # This shouldn't happen since we validated above, but handle it for safety
        if sura1_num is None or sura2_num is None:
            return {
                "success": False,
                "error": "Could not find sura numbers",
                "total_ayahs": 0,
                "total_pages": 0
            }
        
        # Determine calculation direction and order
        is_forward = sura1_num < sura2_num
        direction = "forward" if is_forward else "reverse"
        
        # For calculation purposes, always use the correct chronological order
        start_sura = min(sura1_num, sura2_num)
        end_sura = max(sura1_num, sura2_num)
        
        # Calculate total ayahs and collect sura information
        total_ayahs = 0
        included_suras = []
        
        for sura_num in range(start_sura, end_sura + 1):
            sura_info = self.suras[sura_num]
            sura_ayahs = sura_info["ayahs"]
            start_page, _, sura_pages = self.get_page_range_for_sura(sura_num)
            
            total_ayahs += sura_ayahs
            included_suras.append({
                "number": sura_num,
                "name": sura_info["name"],
                "arabic": sura_info["arabic"],
                "ayahs": sura_ayahs,
                "page_start": start_page,
                "page_end": None, # Simplified to None
                "total_pages": sura_pages
            })
        
        # Calculate actual page range for the entire range
        page_range = self.calculate_page_range_between_suras(start_sura, end_sura)
        
        # Create direction-aware description
        if is_forward:
            direction_description = f"من السورة {sura1_num} إلى السورة {sura2_num} (ترتيب أمامي)"
        else:
            direction_description = f"من السورة {sura1_num} إلى السورة {sura2_num} (ترتيب عكسي)"
        
        return {
            "success": True,
            "total_ayahs": total_ayahs,
            "total_pages": page_range["total_pages"],
            "page_range": page_range,
            "direction": direction,
            "is_forward": is_forward,
            "direction_description": direction_description,
            "original_order": {
                "first_sura": sura1_num,
                "second_sura": sura2_num
            },
            "calculation_order": {
                "start_sura": start_sura,
                "end_sura": end_sura
            },
            "start_sura": {
                "number": start_sura,
                "name": self.suras[start_sura]["name"],
                "arabic": self.suras[start_sura]["arabic"],
                "ayahs": self.suras[start_sura]["ayahs"],
                "page_start": self.suras[start_sura]["page_start"],
                "page_end": None # Simplified to None
            },
            "end_sura": {
                "number": end_sura,
                "name": self.suras[end_sura]["name"],
                "arabic": self.suras[end_sura]["arabic"],
                "ayahs": self.suras[end_sura]["ayahs"],
                "page_start": self.suras[end_sura]["page_start"],
                "page_end": None # Simplified to None
            },
            "first_selected_sura": {
                "number": sura1_num,
                "name": self.suras[sura1_num]["name"],
                "arabic": self.suras[sura1_num]["arabic"],
                "ayahs": self.suras[sura1_num]["ayahs"],
                "page_start": self.suras[sura1_num]["page_start"],
                "page_end": None # Simplified to None
            },
            "second_selected_sura": {
                "number": sura2_num,
                "name": self.suras[sura2_num]["name"],
                "arabic": self.suras[sura2_num]["arabic"],
                "ayahs": self.suras[sura2_num]["ayahs"],
                "page_start": self.suras[sura2_num]["page_start"],
                "page_end": None # Simplified to None
            },
            "included_suras": included_suras,
            "number_of_suras": len(included_suras),
            "page_info": {
                "total_pages": page_range["total_pages"],
                "start_page": page_range["start_page"],
                "end_page": page_range["end_page"],
                "total_quran_pages": self.TOTAL_PAGES,
                "calculation_method": "الصفحات الأولى للسور من المصحف القياسي"
            }
        }
    def get_sura_info(self, sura_name):
        """Get detailed information about a sura including Arabic name and page info"""
        sura_num = get_sura_number_by_name(sura_name)
        if sura_num:
            sura = self.suras[sura_num]
            start_page, _, total_pages = self.get_page_range_for_sura(sura_num)
            return {
                "number": sura_num,
                "name": sura["name"],
                "arabic": sura["arabic"],
                "ayahs": sura["ayahs"],
                "page_start": start_page,
                "page_end": None, # Simplified to None
                "total_pages": total_pages
            }
        return None
    
    def search_suras(self, query):
        """Search for suras by name (for autocomplete) including Arabic names"""
        query = query.lower()
        matches = []
        
        for num, sura in self.suras.items():
            if query in sura["name"].lower():
                matches.append({
                    "number": num,
                    "name": sura["name"],
                    "arabic": sura["arabic"],
                    "ayahs": sura["ayahs"]
                })
        
        return sorted(matches, key=lambda x: x["number"])


# Create a global calculator instance
calculator = QuranCalculator() 