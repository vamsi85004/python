from collections import Counter

def first_unique_character(s):
    """
    Find the first unique character in a string.

    :param s: str, the input string
    :return: str, the first unique character or an empty string if no unique character exists
    """
    char_count = Counter(s)

    for char in s:
        if char_count[char] == 1:
            return char

    return ""

# Example usage:
s1 = "swiss"
print(first_unique_character(s1))  # Output: "w"

s2 = "racecar"
print(first_unique_character(s2))  # Output: "e"

s3 = "aabbcc"
print(first_unique_character(s3))  # Output: ""
