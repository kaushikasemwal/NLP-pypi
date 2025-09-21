"""

Write a python code that converts a Roman numeral to an integer and

a written number (like "one", "two", etc.) to an integer.

"""
def roman_to_int(s):
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
    for char in reversed(s):
        curr_value = roman_numerals[char]
        if curr_value < prev_value:
            total -= curr_value
        else:
            total += curr_value
        prev_value = curr_value
    return total

def written_number_to_int(s):
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
        "ten": 10
    }
    return written_numbers.get(s, -1)

# Test the functions
if __name__ == "__main__":
    # Test Roman numeral conversion
    print("Roman numeral tests:")
    print(f"IV = {roman_to_int('IV')}")
    print(f"IX = {roman_to_int('IX')}")
    print(f"LVIII = {roman_to_int('LVIII')}")
    print(f"MCMXC = {roman_to_int('MCMXC')}")
    
    # Test written number conversion
    print("\nWritten number tests:")
    print(f"one = {written_number_to_int('one')}")
    print(f"five = {written_number_to_int('five')}")
    print(f"ten = {written_number_to_int('ten')}")
    print(f"invalid = {written_number_to_int('invalid')}")
