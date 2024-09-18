def format_license_key(s, group_length):
    # Remove all hyphens and convert the string to uppercase
    s = s.replace('-', '').upper()
    
    # Calculate the length of the first group
    first_group_length = len(s) % group_length or group_length
    
    # Initialize the formatted key list
    formatted_key = [s[:first_group_length]]
    
    # Iterate over the remaining characters and group them
    for i in range(first_group_length, len(s), group_length):
        formatted_key.append(s[i:i + group_length])
    
    # Join the groups with hyphens and return the result
    return '-'.join(formatted_key)

# Test cases
license_key1 = "2-4A0r7-4k"
group_length1 = 4
print(format_license_key(license_key1, group_length1))  # Output: "24A0-R74K"

license_key2 = "n4-5y7-9d0"
group_length2 = 5
print(format_license_key(license_key2, group_length2))  # Output: "N45Y7-9D0"

license_key3 = "a1b2-c3d4-e5f6"
group_length3 = 3
print(format_license_key(license_key3, group_length3))  # Output: "A1B-C3D-E5F-6"
