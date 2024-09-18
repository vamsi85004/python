def find_disappeared_numbers(nums):
    n = len(nums)
    num_set = set(range(1, n + 1))
    
    num_set -= set(nums)
    
    return list(num_set)

test_cases = [
    [4, 3, 2, 7, 8, 1]
]

results = [find_disappeared_numbers(nums) for nums in test_cases]

for nums, result in zip(test_cases, results):
    print(f"For nums = {nums}, the disappeared numbers are {result}")
