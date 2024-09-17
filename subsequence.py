def is_subsequence(s1, s2):
    """
    Check if s1 is a subsequence of s2.

    :param s1: str, the subsequence to check
    :param s2: str, the main string
    :return: bool, True if s1 is a subsequence of s2, False otherwise
    """
    # Initialize two pointers
    i, j = 0, 0

    # Iterate through s2 with pointer j
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
        j += 1

    # If all characters of s1 have been found in s2 in order
    return i == len(s1)

# Example usage:
s1 = "abc"
s2 = "aibcdef"

print(is_subsequence(s1, s2))  # Output: True

s1 = "abg"
s2 = "abcdef"

print(is_subsequence(s1, s2))  # Output: True

s1 = "axc"
s2 = "ahbgdc"

print(is_subsequence(s1, s2))  # Output: False
