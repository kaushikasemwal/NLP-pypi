# Numeric Converter

A Python package for converting Roman numerals and written numbers to integers.

## Features

- **Roman Numeral Conversion**: Convert Roman numerals (I, V, X, L, C, D, M) to integers with strict validation
- **Written Number Conversion**: Convert written numbers ("one", "two", etc.) to integers
- **Robust Validation**: Prevents invalid Roman numeral patterns (IIII, VV, etc.)
- **Error Handling**: Proper validation and error messages for invalid inputs
- **Comprehensive Coverage**: Supports numbers from zero to twenty for written numbers
- **Modern Development**: Fast `uv` workflow and comprehensive `pytest` test suite
- **100% Test Coverage**: Thoroughly tested with professional test infrastructure

## Installation

```bash
pip install numeric-converter
```

## Quick Start

```python
from numeric_converter import roman_to_int, written_number_to_int

# Convert Roman numerals
print(roman_to_int("IV"))        # Output: 4
print(roman_to_int("IX"))        # Output: 9
print(roman_to_int("MCMXC"))     # Output: 1990

# Invalid Roman numerals raise ValueError
try:
    print(roman_to_int("IIII"))  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")

# Convert written numbers
print(written_number_to_int("five"))     # Output: 5
print(written_number_to_int("twenty"))   # Output: 20
print(written_number_to_int("invalid"))  # Output: None
print(written_number_to_int("negative one"))  # Output: None
```

## API Reference

### `roman_to_int(s)`

Convert a Roman numeral string to an integer.

**Parameters:**
- `s` (str): Roman numeral string (e.g., 'IV', 'IX', 'MCMXC')

**Returns:**
- `int`: The integer value of the Roman numeral

**Raises:**
- `ValueError`: If the input contains invalid Roman numeral patterns

**Validation Rules:**
- I, X, C can be repeated up to 3 times consecutively
- V, L, D should never be repeated
- Only valid subtractive combinations allowed (IV, IX, XL, XC, CD, CM)
- Invalid patterns like IIII, VV, IC, VL raise ValueError

**Examples:**
```python
>>> roman_to_int('IV')
4
>>> roman_to_int('LVIII')
58
>>> roman_to_int('MCMXC')
1990
>>> roman_to_int('IIII')  # Invalid pattern
Traceback (most recent call last):
ValueError: Invalid repetition in Roman numeral: IIII
```

### `written_number_to_int(s)`

Convert a written number word to an integer.

**Parameters:**
- `s` (str): Written number word (e.g., 'one', 'two', 'ten')

**Returns:**
- `int or None`: The integer value of the written number, or None if not found

**Supported Numbers:**
- zero through twenty (0-20)
- Case-insensitive input

**Examples:**
```python
>>> written_number_to_int('five')
5
>>> written_number_to_int('FIFTEEN')
15
>>> written_number_to_int('invalid')
None
>>> written_number_to_int('negative one')
None
```

## Roman Numeral Rules

The package follows standard Roman numeral conversion rules:

- **Basic Symbols**: I=1, V=5, X=10, L=50, C=100, D=500, M=1000
- **Additive Principle**: When a smaller numeral appears after a larger one, add them (VI = 6)
- **Subtractive Principle**: When a smaller numeral appears before a larger one, subtract it (IV = 4)

## Development

### Modern Setup (Recommended - using uv)

`uv` is a fast, modern replacement for pip and venv. It's much faster and simpler to use.

```bash
# Install uv (if not already installed)
pip install uv

# Create virtual environment
python -m uv venv

# Activate environment
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\Activate.ps1  # On Windows PowerShell

# Install in development mode with all dependencies
python -m uv pip install -e ".[dev]"
```

### Traditional Setup (Alternative)

If you prefer the traditional approach:

```bash
# Clone the repository
git clone https://github.com/kaushikasemwal/numeric-converter.git
cd numeric-converter

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\Activate.ps1  # On Windows PowerShell

# Install in development mode
pip install -e ".[dev]"
```

### Running Tests

This project uses `pytest` for testing with comprehensive test coverage.

```bash
# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run tests with coverage report
pytest --cov=src/numeric_converter --cov-report=term-missing

# Run specific test file
pytest tests/test_roman.py

# Run specific test class
pytest tests/test_roman.py::TestRomanToInt

# Run specific test method
pytest tests/test_roman.py::TestRomanToInt::test_valid_roman_numerals
```

**Test Structure:**
```
tests/
├── __init__.py              # Test package initialization
├── conftest.py              # Shared test fixtures and configuration
├── test_roman.py            # Tests for Roman numeral conversion
├── test_written.py          # Tests for written number conversion
└── test_integration.py      # Integration tests for the entire package
```

### Code Quality

```bash
# Format code with black
black src/

# Lint code with flake8
flake8 src/

# Type checking with mypy
mypy src/
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### v0.1.4
- **Enhanced**: Added comprehensive `pytest` test infrastructure with 100% coverage
- **Improved**: Professional test structure with `tests/` directory and proper fixtures
- **Better**: Removed old test files for cleaner project structure
- **Added**: Detailed testing documentation with multiple test running options

### v0.1.3
- **Enhanced**: Added modern `uv` workflow support for faster development setup
- **Improved**: Updated development documentation with both uv and traditional approaches
- **Better**: Faster dependency installation and environment setup for contributors

### v0.1.2
- **Enhanced**: Added comprehensive Roman numeral validation
- **Improved**: Prevents invalid patterns like IIII, VV, LLLL according to standard rules
- **Better**: Validates subtractive combinations (only IV, IX, XL, XC, CD, CM allowed)
- **Robust**: Raises ValueError for malformed Roman numerals instead of silent errors

### v0.1.1
- **Improved**: `written_number_to_int()` now returns `None` for invalid inputs instead of `-1`
- **Better**: Clearer distinction between valid results and invalid inputs
- **Fixed**: Prevents confusion between negative numbers and invalid inputs

### v0.1.0
- Initial release
- Roman numeral to integer conversion
- Written number to integer conversion
- Comprehensive error handling
- Full test coverage