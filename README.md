# Numeric Converter

A Python package for converting Roman numerals and written numbers to integers.

## Features

- **Roman Numeral Conversion**: Convert Roman numerals (I, V, X, L, C, D, M) to integers with strict validation
- **Written Number Conversion**: Convert written numbers ("one", "two", etc.) to integers
- **Robust Validation**: Prevents invalid Roman numeral patterns (IIII, VV, etc.)
- **Error Handling**: Proper validation and error messages for invalid inputs
- **Comprehensive Coverage**: Supports numbers from zero to twenty for written numbers

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

### Setting up for Development

```bash
# Clone the repository
git clone https://github.com/yourusername/numeric-converter.git
cd numeric-converter

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black src/
flake8 src/
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