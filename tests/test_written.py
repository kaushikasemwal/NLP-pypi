"""
Tests for written number conversion functionality.
"""

import pytest
from numeric_converter import written_number_to_int


class TestWrittenNumberToInt:
    """Test class for written_number_to_int function."""

    def test_valid_written_numbers(self, valid_written_numbers):
        """Test conversion of valid written numbers."""
        for written, expected in valid_written_numbers:
            result = written_number_to_int(written)
            assert result == expected, f"written_number_to_int('{written}') should return {expected}, got {result}"

    def test_case_insensitive(self):
        """Test that the function handles different cases correctly."""
        test_cases = [
            ("FIVE", 5),
            ("Five", 5),
            ("TEN", 10),
            ("Ten", 10),
            ("TWENTY", 20),
            ("Twenty", 20)
        ]
        
        for written, expected in test_cases:
            result = written_number_to_int(written)
            assert result == expected, f"written_number_to_int('{written}') should return {expected}, got {result}"

    def test_invalid_written_numbers_return_none(self, invalid_written_numbers):
        """Test that invalid written numbers return None."""
        for invalid_written in invalid_written_numbers:
            result = written_number_to_int(invalid_written)
            assert result is None, f"written_number_to_int('{invalid_written}') should return None, got {result}"

    def test_empty_string(self):
        """Test that empty string returns None."""
        assert written_number_to_int("") is None

    def test_none_input(self):
        """Test that None input returns None."""
        assert written_number_to_int(None) is None

    def test_boundary_values(self):
        """Test boundary values (lowest and highest supported numbers)."""
        assert written_number_to_int("zero") == 0
        assert written_number_to_int("twenty") == 20

    def test_teens_numbers(self):
        """Test all teen numbers (11-19)."""
        teens = [
            ("eleven", 11),
            ("twelve", 12),
            ("thirteen", 13),
            ("fourteen", 14),
            ("fifteen", 15),
            ("sixteen", 16),
            ("seventeen", 17),
            ("eighteen", 18),
            ("nineteen", 19)
        ]
        
        for written, expected in teens:
            result = written_number_to_int(written)
            assert result == expected, f"written_number_to_int('{written}') should return {expected}, got {result}"

    def test_unsupported_numbers(self):
        """Test numbers outside the supported range."""
        unsupported = [
            "twenty-one",
            "thirty",
            "hundred",
            "thousand",
            "million",
            "negative",
            "minus one"
        ]
        
        for unsupported_num in unsupported:
            result = written_number_to_int(unsupported_num)
            assert result is None, f"written_number_to_int('{unsupported_num}') should return None for unsupported number"