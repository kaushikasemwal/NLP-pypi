"""
Tests for Roman numeral conversion functionality.
"""

import pytest
from numeric_converter import roman_to_int


class TestRomanToInt:
    """Test class for roman_to_int function."""

    def test_valid_roman_numerals(self, valid_roman_numerals):
        """Test conversion of valid Roman numerals."""
        for roman, expected in valid_roman_numerals:
            result = roman_to_int(roman)
            assert result == expected, f"roman_to_int('{roman}') should return {expected}, got {result}"

    def test_case_insensitive(self):
        """Test that the function handles different cases correctly."""
        test_cases = [
            ("iv", 4),
            ("IX", 9),
            ("lviii", 58),
            ("MCMXC", 1990),
            ("McmXc", 1990)
        ]
        
        for roman, expected in test_cases:
            result = roman_to_int(roman)
            assert result == expected, f"roman_to_int('{roman}') should return {expected}, got {result}"

    def test_empty_string(self):
        """Test that empty string returns 0."""
        assert roman_to_int("") == 0

    def test_invalid_roman_numerals_raise_errors(self, invalid_roman_numerals):
        """Test that invalid Roman numerals raise ValueError."""
        for invalid_roman in invalid_roman_numerals:
            with pytest.raises(ValueError) as excinfo:
                roman_to_int(invalid_roman)
            
            # Check that the error message is informative
            assert invalid_roman in str(excinfo.value), f"Error message should mention '{invalid_roman}'"

    def test_invalid_characters(self):
        """Test that invalid characters raise ValueError."""
        invalid_chars = ["IAB", "XYZ", "123", "IVXB"]
        
        for invalid in invalid_chars:
            with pytest.raises(ValueError) as excinfo:
                roman_to_int(invalid)
            assert "Invalid Roman numeral character" in str(excinfo.value)

    def test_complex_valid_numerals(self):
        """Test complex but valid Roman numerals."""
        complex_cases = [
            ("MCDXLIV", 1444),      # 1000 + 400 + 40 + 4
            ("MCMLIV", 1954),       # 1000 + 900 + 50 + 4
            ("MMCDXLIV", 2444),     # 2000 + 400 + 40 + 4
            ("MMMCMXCIX", 3999),    # 3000 + 900 + 90 + 9
            ("CDXLIV", 444),        # 400 + 40 + 4
            ("CMXC", 990),          # 900 + 90
        ]
        
        for roman, expected in complex_cases:
            result = roman_to_int(roman)
            assert result == expected, f"roman_to_int('{roman}') should return {expected}, got {result}"

    def test_subtractive_notation(self):
        """Test proper subtractive notation handling."""
        subtractive_cases = [
            ("IV", 4),      # 5 - 1
            ("IX", 9),      # 10 - 1
            ("XL", 40),     # 50 - 10
            ("XC", 90),     # 100 - 10
            ("CD", 400),    # 500 - 100
            ("CM", 900),    # 1000 - 100
        ]
        
        for roman, expected in subtractive_cases:
            result = roman_to_int(roman)
            assert result == expected, f"roman_to_int('{roman}') should return {expected}, got {result}"