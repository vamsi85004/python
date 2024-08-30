def longest_common_prefix(strs):
    # Return an empty string if the input list is empty
    if not strs:
        return ""
    
    # Start with the first string as the prefix
    prefix = strs[0]
    
    # Iterate over the remaining strings
    for s in strs[1:]:
        # Update the prefix by checking how much of it is common with the current string
        while s[:len(prefix)] != prefix:
            # Shorten the prefix by one character each time
            prefix = prefix[:-1]
            # If prefix becomes empty, return ""
            if not prefix:
                return ""
    
    return prefix

# Test Cases
print(longest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))     # Output: ""
print(longest_common_prefix(["interspecies", "interstellar", "interstate"]))  # Output: "inters"
print(longest_common_prefix(["throne", "throne"]))          # Output: "throne"
print(longest_common_prefix([]))                            # Output: ""
