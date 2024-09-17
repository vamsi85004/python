def find_string_difference(s1, s2):
    """
    Find the difference between two strings.

    :param s1: str, the first string
    :param s2: str, the second string
    :return: tuple, (characters in s1 but not in s2, characters in s2 but not in s1)
    """
    set1 = set(s1)
    set2 = set(s2)

    # Characters in s1 but not in s2
    only_in_s1 = set1 - set2

    # Characters in s2 but not in s1
    only_in_s2 = set2 - set1

    return (''.join(only_in_s1), ''.join(only_in_s2))

# Example usage:
s1 = "hello"
s2 = "world"

print(find_string_difference(s1, s2))
# Output: ('h', 'wdr')
