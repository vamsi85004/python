def reverse_string(s, left, right):
    s_list = list(s)
    
    while left < right:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1
    
    return ''.join(s_list)

s = "abcdefg"
left = 2
right = 5
result = reverse_string(s, left, right)
print(result)  # Output: "abfedcg"
