def concatenate_strings(*args):
    # Join all strings in the args tuple into a single string
    return ''.join(args)

def main():
    # Prompt the user to enter multiple strings
    print("Enter strings to concatenate (type 'done' to finish):")
    
    strings = []
    while True:
        user_input = input("Enter a string: ")
        if user_input.lower() == 'done':
            break
        strings.append(user_input)
    
    # Concatenate all strings entered by the user
    result = concatenate_strings(*strings)
    
    # Output the concatenated result
    print(f"The concatenated string is: '{result}'")

if __name__ == "__main__":
    main()
