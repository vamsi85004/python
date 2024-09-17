def longest_palindromic_substring(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if not s:
        return ""

    longest = ""
    for i in range(len(s)):
        # Odd length palindromes (single character center)
        pal1 = expand_around_center(i, i)
        if len(pal1) > len(longest):
            longest = pal1

        # Even length palindromes (two character center)
        pal2 = expand_around_center(i, i + 1)
        if len(pal2) > len(longest):
            longest = pal2

    return longest

def main():
    input_string = input("Enter a string to find the longest palindromic substring: ")
    result = longest_palindromic_substring(input_string)
    print(f"The longest palindromic substring is: {result}")

if __name__ == "__main__":
    main()
