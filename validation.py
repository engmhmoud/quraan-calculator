"""
Validation Module
User input validation and UX enhancement utilities
"""

from quran_data import get_sura_names, is_valid_sura_name
from difflib import get_close_matches


class InputValidator:
    """Validates user input and provides suggestions"""
    
    def __init__(self):
        self.sura_names = get_sura_names()
        
    def validate_sura_name(self, name: str) -> dict:
        """
        Validate sura name and provide suggestions if invalid
        
        Returns:
            dict: validation result with suggestions
        """
        name = name.strip()
        
        if not name:
            return {
                "valid": False,
                "error": "Sura name cannot be empty",
                "suggestions": []
            }
            
        if is_valid_sura_name(name):
            return {
                "valid": True,
                "error": None,
                "suggestions": []
            }
            
        # Find close matches
        suggestions = get_close_matches(
            name, 
            self.sura_names, 
            n=3, 
            cutoff=0.6
        )
        
        return {
            "valid": False,
            "error": f"'{name}' is not a valid sura name",
            "suggestions": suggestions
        }
        
    def get_autocomplete_suggestions(self, partial_name: str, limit: int = 5) -> list:
        """Get autocomplete suggestions for partial sura name"""
        if len(partial_name) < 2:
            return []
            
        partial_name = partial_name.lower()
        suggestions = []
        
        # Exact prefix matches first
        for name in self.sura_names:
            if name.lower().startswith(partial_name):
                suggestions.append(name)
                
        # Then substring matches
        if len(suggestions) < limit:
            for name in self.sura_names:
                if (partial_name in name.lower() and 
                    name not in suggestions):
                    suggestions.append(name)
                    
        return suggestions[:limit]
        
    def validate_calculation_input(self, sura1: str, sura2: str) -> dict:
        """Validate both sura inputs for calculation"""
        sura1 = sura1.strip()
        sura2 = sura2.strip()
        
        # Check if both inputs provided
        if not sura1 or not sura2:
            return {
                "valid": False,
                "error": "Please enter both sura names",
                "suggestions": {
                    "sura1": [] if sura1 else ["Al-Fatiha", "Al-Baqarah", "Aal-e-Imran"],
                    "sura2": [] if sura2 else ["Ya-Sin", "Ar-Rahman", "Al-Mulk"]
                }
            }
            
        # Check if same sura
        if sura1.lower() == sura2.lower():
            return {
                "valid": False,
                "error": "Please enter two different suras",
                "suggestions": {
                    "sura1": [],
                    "sura2": []
                }
            }
            
        # Validate individual suras
        sura1_validation = self.validate_sura_name(sura1)
        sura2_validation = self.validate_sura_name(sura2)
        
        if not sura1_validation["valid"] or not sura2_validation["valid"]:
            errors = []
            if not sura1_validation["valid"]:
                errors.append(f"First sura: {sura1_validation['error']}")
            if not sura2_validation["valid"]:
                errors.append(f"Second sura: {sura2_validation['error']}")
                
            return {
                "valid": False,
                "error": "; ".join(errors),
                "suggestions": {
                    "sura1": sura1_validation["suggestions"],
                    "sura2": sura2_validation["suggestions"]
                }
            }
            
        return {
            "valid": True,
            "error": None,
            "suggestions": {"sura1": [], "sura2": []}
        }


# Global validator instance
validator = InputValidator() 