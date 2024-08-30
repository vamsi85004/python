def search_range(nums, target):
    def find_first_position():
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                if mid == 0 or nums[mid - 1] != target:
                    return mid
                right = mid - 1
        return -1

    def find_last_position():
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    return mid
                left = mid + 1
        return -1

    first_pos = find_first_position()
    if first_pos == -1:
        return [-1, -1]

    last_pos = find_last_position()
    return [first_pos, last_pos]

# Example usage
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(search_range(nums, target))  # Output: [3, 4]
