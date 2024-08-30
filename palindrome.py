def is_palindrome(x):
    # Negative numbers are not palindromes
    if x < 0:
        return False
    
    # Convert the number to a string
    x_str = str(x)
    
    # Check if the string is the same forwards and backwards
    return x_str == x_str[::-1]

# Test Cases
print(is_palindrome(121))  # Output: True
print(is_palindrome(-121))  # Output: False
print(is_palindrome(10))  # Output: False
print(is_palindrome(12321))  # Output: True
