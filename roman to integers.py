def roman_to_int(s):
    # Create a dictionary to map Roman numerals to integers
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    # Initialize the integer to 0
    total = 0
    
    # Iterate through the string, checking pairs of characters
    for i in range(len(s)):
        # If this is not the last character and the current value is less than the next one
        if i < len(s) - 1 and roman_dict[s[i]] < roman_dict[s[i + 1]]:
            # Subtract the current value
            total -= roman_dict[s[i]]
        else:
            # Otherwise, add the current value
            total += roman_dict[s[i]]
    
    return total

# Test Cases
print(roman_to_int("III"))       # Output: 3
print(roman_to_int("IV"))        # Output: 4
print(roman_to_int("IX"))        # Output: 9
print(roman_to_int("LVIII"))     # Output: 58
print(roman_to_int("MCMXCIV"))   # Output: 1994
