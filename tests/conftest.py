"""
Pytest configuration file.

This file contains shared fixtures and configuration for all tests.
"""

import pytest
from numeric_converter import roman_to_int, written_number_to_int


@pytest.fixture
def valid_roman_numerals():
    """Fixture providing valid Roman numeral test cases."""
    return [
        ("I", 1),
        ("IV", 4),
        ("V", 5),
        ("IX", 9),
        ("X", 10),
        ("XL", 40),
        ("L", 50),
        ("XC", 90),
        ("C", 100),
        ("CD", 400),
        ("D", 500),
        ("CM", 900),
        ("M", 1000),
        ("LVIII", 58),
        ("MCMXC", 1990),
        ("MCDLIV", 1454),
        ("MMXXV", 2025)
    ]


@pytest.fixture
def invalid_roman_numerals():
    """Fixture providing invalid Roman numeral test cases."""
    return [
        "IIII",    # Too many I's
        "VV",      # V cannot repeat
        "LLLL",    # L cannot repeat
        "DD",      # D cannot repeat
        "IC",      # Invalid subtractive combination
        "IM",      # Invalid subtractive combination
        "VL",      # V cannot be subtractive
        "VD",      # V cannot be subtractive
        "LC",      # L cannot be subtractive
        "DM",      # D cannot be subtractive
        "XM",      # Invalid subtractive combination
        "XXXXL"    # Too many X's
    ]


@pytest.fixture
def valid_written_numbers():
    """Fixture providing valid written number test cases."""
    return [
        ("zero", 0),
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9),
        ("ten", 10),
        ("eleven", 11),
        ("twelve", 12),
        ("thirteen", 13),
        ("fourteen", 14),
        ("fifteen", 15),
        ("sixteen", 16),
        ("seventeen", 17),
        ("eighteen", 18),
        ("nineteen", 19),
        ("twenty", 20)
    ]


@pytest.fixture
def invalid_written_numbers():
    """Fixture providing invalid written number test cases."""
    return [
        "invalid",
        "negative one",
        "twenty-one",
        "thirty",
        "hundred",
        "xyz",
        "123",
        "not_a_number"
    ]