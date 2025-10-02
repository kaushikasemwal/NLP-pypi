#!/usr/bin/env python3
"""
Test script to verify the numeric_converter package works correctly.
"""

from numeric_converter import roman_to_int, written_number_to_int

def test_roman_conversion():
    """Test Roman numeral conversion."""
    test_cases = [
        ("I", 1),
        ("IV", 4),
        ("V", 5),
        ("IX", 9),
        ("X", 10),
        ("LVIII", 58),
        ("MCMXC", 1990),
        ("MCDLIV", 1454)
    ]
    
    print("Testing Roman numeral conversion:")
    for roman, expected in test_cases:
        result = roman_to_int(roman)
        status = "✓" if result == expected else "✗"
        print(f"  {status} {roman} = {result} (expected {expected})")
    
    # Test invalid Roman numerals
    print("\nTesting invalid Roman numerals:")
    invalid_cases = ["IIII", "VV", "LLLL", "IC", "VL"]
    for case in invalid_cases:
        try:
            result = roman_to_int(case)
            print(f"  ✗ {case} = {result} (unexpected - should be invalid)")
        except ValueError as e:
            print(f"  ✓ {case} -> Error: {str(e)[:50]}...")

def test_written_conversion():
    """Test written number conversion."""
    test_cases = [
        ("zero", 0),
        ("one", 1),
        ("five", 5),
        ("ten", 10),
        ("fifteen", 15),
        ("twenty", 20),
        ("invalid", None),
        ("negative one", None)
    ]
    
    print("\nTesting written number conversion:")
    for written, expected in test_cases:
        result = written_number_to_int(written)
        status = "✓" if result == expected else "✗"
        print(f"  {status} '{written}' = {result} (expected {expected})")

if __name__ == "__main__":
    print("Testing numeric_converter package...\n")
    test_roman_conversion()
    test_written_conversion()
    print("\nAll tests completed!")