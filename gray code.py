def gray_code(n):
    if n == 0:
        return ['0']
    elif n == 1:
        return ['0', '1']
    else:
        # Recursively generate the Gray code sequence for n-1
        prev_gray = gray_code(n - 1)
        
        # Initialize the current Gray code list
        result = []
        
        # Add '0' to the first half
        for code in prev_gray:
            result.append('0' + code)
        
        # Add '1' to the reversed second half
        for code in reversed(prev_gray):
            result.append('1' + code)
        
        return result

# Function to display the Gray code
def print_gray_code(n):
    gray_codes = gray_code(n)
    for code in gray_codes:
        print(code)

# Example usage:
n = 3  # Number of bits
print("Gray code sequence for", n, "bits:")
print_gray_code(n)
