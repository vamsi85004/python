def has_repeated_substring(s):
    n = len(s)
    
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            substring = s[:i]
            if substring * (n // i) == s:
                return True
    return False

print(has_repeated_substring("abab"))  # True
print(has_repeated_substring("aba"))   # False
print(has_repeated_substring("abcabcabc"))  # True
print(has_repeated_substring("abcd"))  # False
