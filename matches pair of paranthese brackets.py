def is_valid(s):
    # Dictionary to hold matching pairs of parentheses
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    # Stack to keep track of opening brackets
    stack = []
    
    # Iterate through each character in the string
    for char in s:
        # If the character is a closing bracket
        if char in bracket_map:
            # Pop from stack if it's not empty, otherwise assign a dummy value
            top_element = stack.pop() if stack else '#'
            
            # Check if the popped element matches the corresponding opening bracket
            if bracket_map[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
    
    # Check if the stack is empty (all brackets matched)
    return not stack

# Test Cases
print(is_valid("()"))       # Output: True
print(is_valid("()[]{}"))   # Output: True
print(is_valid("(]"))       # Output: False
print(is_valid("([)]"))     # Output: False
print(is_valid("{[]}"))     # Output: True
