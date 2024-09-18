def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Strings must be of the same length")
    
    distance = sum(c1 != c2 for c1, c2 in zip(s1, s2))
    return distance

try:
    print(hamming_distance("karolin", "kathrin"))  # Output: 3
    print(hamming_distance("1011101", "1001001"))  # Output: 3
    print(hamming_distance("2173896", "2233796"))  # Output: 3
    print(hamming_distance("abc", "abcd"))         # This will raise an exception
except ValueError as e:
    print(e)
