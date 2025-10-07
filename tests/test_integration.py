"""
Integration tests for the numeric_converter package.

These tests verify that all components work together correctly.
"""

import pytest
from numeric_converter import roman_to_int, written_number_to_int, __version__


class TestIntegration:
    """Integration tests for the entire package."""

    def test_package_version(self):
        """Test that package version is accessible and valid."""
        assert __version__ is not None
        assert isinstance(__version__, str)
        assert len(__version__) > 0

    def test_both_functions_work_together(self):
        """Test that both conversion functions can be used together."""
        # Convert same logical number using both functions
        assert roman_to_int("IV") == written_number_to_int("four")
        assert roman_to_int("V") == written_number_to_int("five")
        assert roman_to_int("IX") == written_number_to_int("nine")
        assert roman_to_int("X") == written_number_to_int("ten")
        assert roman_to_int("XX") == written_number_to_int("twenty")

    def test_function_independence(self):
        """Test that functions don't interfere with each other."""
        # These should not affect each other
        roman_result = roman_to_int("XIV")
        written_result = written_number_to_int("fourteen")
        
        assert roman_result == 14
        assert written_result == 14
        
        # Test error in one doesn't affect the other
        with pytest.raises(ValueError):
            roman_to_int("IIII")
        
        # This should still work
        assert written_number_to_int("five") == 5

    def test_import_structure(self):
        """Test that all expected functions are importable."""
        from numeric_converter import roman_to_int, written_number_to_int
        
        # Functions should be callable
        assert callable(roman_to_int)
        assert callable(written_number_to_int)

    def test_readme_examples(self):
        """Test the examples from the README work correctly."""
        # Examples from README should work
        assert roman_to_int("IV") == 4
        assert roman_to_int("IX") == 9
        assert roman_to_int("MCMXC") == 1990
        
        assert written_number_to_int("five") == 5
        assert written_number_to_int("twenty") == 20
        assert written_number_to_int("invalid") is None
        assert written_number_to_int("negative one") is None

    def test_comprehensive_workflow(self):
        """Test a comprehensive workflow using both functions."""
        # Simulate a real-world usage scenario
        test_data = [
            ("Roman: XIV", "written: fourteen", 14),
            ("Roman: XX", "written: twenty", 20),
            ("Roman: V", "written: five", 5),
        ]
        
        for roman_input, written_input, expected in test_data:
            # Extract actual values (simulating parsing)
            roman_val = roman_input.split(": ")[1]
            written_val = written_input.split(": ")[1]
            
            roman_result = roman_to_int(roman_val)
            written_result = written_number_to_int(written_val)
            
            assert roman_result == expected
            assert written_result == expected
            assert roman_result == written_result