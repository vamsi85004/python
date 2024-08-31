def is_palindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

def backtrack(s, start, path, result):
    if start == len(s):
        result.append(path[:])
        return
    
    for end in range(start, len(s)):
        if is_palindrome(s, start, end):
            path.append(s[start:end + 1])
            backtrack(s, end + 1, path, result)
            path.pop()

def palindrome_partitioning(s):
    result = []
    backtrack(s, 0, [], result)
    return result

# Example usage:
s = "aab"
partitions = palindrome_partitioning(s)
print("Palindrome partitions of", s, "are:", partitions)
