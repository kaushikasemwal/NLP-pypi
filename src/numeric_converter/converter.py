"""
Converter functions for Roman numerals and written numbers.
"""


def roman_to_int(s):
    """
    Convert a Roman numeral string to an integer with validation.
    
    Args:
        s (str): Roman numeral string (e.g., 'IV', 'IX', 'MCMXC')
        
    Returns:
        int: The integer value of the Roman numeral
        
    Raises:
        ValueError: If the input contains invalid Roman numeral patterns
        
    Examples:
        >>> roman_to_int('IV')
        4
        >>> roman_to_int('MCMXC')
        1990
        >>> roman_to_int('IIII')  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ValueError: Invalid repetition in Roman numeral: IIII
    """
    if not s:
        return 0
        
    # Validate the Roman numeral format
    def validate_roman_numeral(roman):
        import re
        
        # Check for invalid characters
        if not re.match(r'^[IVXLCDM]+$', roman.upper()):
            raise ValueError(f"Invalid Roman numeral character in: {roman}")
        
        # Check for invalid repetitions
        # I, X, C can repeat up to 3 times
        if re.search(r'I{4,}|X{4,}|C{4,}', roman.upper()):
            raise ValueError(f"Invalid repetition in Roman numeral: {roman}")
        
        # V, L, D should never repeat
        if re.search(r'V{2,}|L{2,}|D{2,}', roman.upper()):
            raise ValueError(f"Invalid repetition in Roman numeral: {roman}")
        
        # Check for invalid subtractive combinations
        # Valid subtractive: IV, IX, XL, XC, CD, CM
        # Invalid: IL, IC, ID, IM, VL, VC, VD, VM, etc.
        invalid_patterns = [
            r'IL', r'IC', r'ID', r'IM',  # I can only subtract from V and X
            r'VL', r'VC', r'VD', r'VM',  # V cannot be subtractive
            r'XD', r'XM',                # X can only subtract from L and C
            r'LC', r'LD', r'LM',         # L cannot be subtractive
            r'DM'                        # D cannot be subtractive
        ]
        
        for pattern in invalid_patterns:
            if re.search(pattern, roman.upper()):
                raise ValueError(f"Invalid subtractive combination in Roman numeral: {roman}")
    
    # Validate the input
    validate_roman_numeral(s)
    
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(s.upper()):
        curr_value = roman_numerals[char]
        if curr_value < prev_value:
            total -= curr_value
        else:
            total += curr_value
        prev_value = curr_value
        
    return total


def written_number_to_int(s):
    """
    Convert a written number word to an integer.
    
    Args:
        s (str): Written number word (e.g., 'one', 'two', 'ten')
        
    Returns:
        int or None: The integer value of the written number, or None if not found
        
    Examples:
        >>> written_number_to_int('five')
        5
        >>> written_number_to_int('invalid')
        None
        >>> written_number_to_int('negative one')
        None
    """
    if not s:
        return None
        
    written_numbers = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20
    }
    
    return written_numbers.get(s.lower(), None)