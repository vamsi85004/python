def max_subarray_sum(nums):
    if not nums:
        return 0

    # Initialize the variables
    max_current = max_global = nums[0]
    
    # Iterate through the array
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        max_global = max(max_global, max_current)
    
    return max_global

# Example usage
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(nums))  # Output: 6
