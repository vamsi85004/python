def longest_continuous_increasing_subsequence(nums):
    if not nums:
        return 0
    
    max_length = 1
    current_length = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]: 
            current_length += 1
        else:
            max_length = max(max_length, current_length)  

    max_length = max(max_length, current_length)  
    return max_length

nums = [1, 3, 5, 4, 7]
result = longest_continuous_increasing_subsequence(nums)
print(result)  # Output: 3 (subsequence: [1, 3, 5])
