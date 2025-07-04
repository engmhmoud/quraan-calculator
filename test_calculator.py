#!/usr/bin/env python3
"""
Test script for Quran Calculator
Tests the core calculation functionality
"""

from calculator import calculator
from quran_data import SURAS, get_total_ayahs


def test_basic_calculation():
    """Test basic ayah calculation between two suras"""
    print("Testing: Al-Fatiha to Al-Baqarah")
    result = calculator.calculate_ayahs_between_suras("Al-Fatiha", "Al-Baqarah")
    
    if result["success"]:
        print(f"✓ Total ayahs: {result['total_ayahs']}")
        print(f"✓ Number of suras: {result['number_of_suras']}")
        print(f"✓ From Sura {result['start_sura']['number']} to Sura {result['end_sura']['number']}")
    else:
        print(f"❌ Error: {result['error']}")
    print()


def test_invalid_input():
    """Test error handling with invalid input"""
    print("Testing: Invalid sura name")
    result = calculator.calculate_ayahs_between_suras("Invalid-Sura", "Al-Baqarah")
    
    if not result["success"]:
        print(f"✓ Correctly caught error: {result['error']}")
    else:
        print("❌ Should have failed with invalid input")
    print()


def test_same_sura():
    """Test calculation within the same sura"""
    print("Testing: Ya-Sin to Ya-Sin (same sura)")
    result = calculator.calculate_ayahs_between_suras("Ya-Sin", "Ya-Sin")
    
    if result["success"]:
        print(f"✓ Total ayahs in Ya-Sin: {result['total_ayahs']}")
        expected_yasin_ayahs = SURAS[36]["ayahs"]  # Ya-Sin is sura 36
        if result['total_ayahs'] == expected_yasin_ayahs:
            print("✓ Ayah count matches expected value")
        else:
            print(f"❌ Expected {expected_yasin_ayahs}, got {result['total_ayahs']}")
    else:
        print(f"❌ Error: {result['error']}")
    print()


def test_large_range():
    """Test calculation across large range"""
    print("Testing: Al-Fatiha to An-Nas (entire Quran)")
    result = calculator.calculate_ayahs_between_suras("Al-Fatiha", "An-Nas")
    
    if result["success"]:
        total_quran_ayahs = get_total_ayahs()
        print(f"✓ Total ayahs in Quran: {result['total_ayahs']}")
        print(f"✓ Expected total: {total_quran_ayahs}")
        
        if result['total_ayahs'] == total_quran_ayahs:
            print("✓ Full Quran calculation correct!")
        else:
            print(f"❌ Mismatch in total ayah count")
            
        print(f"✓ Number of suras: {result['number_of_suras']}")
    else:
        print(f"❌ Error: {result['error']}")
    print()


def test_reverse_order():
    """Test that order doesn't matter"""
    print("Testing: Reverse order input (An-Nas to Al-Fatiha)")
    result = calculator.calculate_ayahs_between_suras("An-Nas", "Al-Fatiha")
    
    if result["success"]:
        total_quran_ayahs = get_total_ayahs()
        if result['total_ayahs'] == total_quran_ayahs:
            print("✓ Reverse order calculation works correctly!")
        else:
            print(f"❌ Reverse order gave different result")
    else:
        print(f"❌ Error: {result['error']}")
    print()


def main():
    """Run all tests"""
    print("🧪 Testing Quran Calculator Core Functions")
    print("=" * 50)
    
    test_basic_calculation()
    test_invalid_input()
    test_same_sura()
    test_large_range()
    test_reverse_order()
    
    print("✅ All tests completed!")
    print("\nNow you can run the GUI application with:")
    print("python main.py")


if __name__ == "__main__":
    main() 