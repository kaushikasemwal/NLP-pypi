import pytest
from numeric_converter import roman_to_int, written_number_to_int


def test_roman_to_int_valid_cases():
    """Tests valid Roman numeral conversions."""
    assert roman_to_int("I") == 1
    assert roman_to_int("IV") == 4
    assert roman_to_int("IX") == 9
    assert roman_to_int("LVIII") == 58
    assert roman_to_int("MCMXCIV") == 1994


def test_roman_to_int_invalid_repetitions():
    """Tests for invalid repetitions like IIII or VV."""
    with pytest.raises(ValueError, match="Invalid repetition"):
        roman_to_int("IIII")
    with pytest.raises(ValueError, match="Invalid repetition"):
        roman_to_int("VV")
    with pytest.raises(ValueError, match="Invalid repetition"):
        roman_to_int("LL")
    with pytest.raises(ValueError, match="Invalid repetition"):
        roman_to_int("DD")


def test_roman_to_int_invalid_subtractive_patterns():
    """Tests for invalid subtractive patterns like IC or VL."""
    with pytest.raises(ValueError, match="Invalid subtractive combination"):
        roman_to_int("IC")
    with pytest.raises(ValueError, match="Invalid subtractive combination"):
        roman_to_int("VL")
    with pytest.raises(ValueError, match="Invalid subtractive combination"):
        roman_to_int("XD")


def test_written_number_to_int_valid_cases():
    """Tests valid written number conversions."""
    assert written_number_to_int("zero") == 0
    assert written_number_to_int("nine") == 9
    assert written_number_to_int("twenty") == 20


def test_written_number_to_int_case_insensitivity():
    """Tests if the function is case-insensitive."""
    assert written_number_to_int("One") == 1
    assert written_number_to_int("TWELVE") == 12


def test_written_number_to_int_invalid_cases():
    """Tests invalid written numbers, which should return None."""
    assert written_number_to_int("twenty-one") is None
    assert written_number_to_int("negative five") is None
    assert written_number_to_int("not a number") is None
