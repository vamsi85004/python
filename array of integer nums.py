def two_sum(nums, target):
    # Create a dictionary to store the indices of the elements
    num_map = {}
    
    # Iterate through the list
    for i, num in enumerate(nums):
        diff = target - num
        
        if diff in num_map:
            return [num_map[diff], i]
        
        num_map[num] = i

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output should be [0, 1]
