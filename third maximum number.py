def third_maximum(numbers):
    # Convert the list to a set to remove duplicates
    unique_numbers = set(numbers)
    
    # If there are fewer than 3 unique numbers, return None
    if len(unique_numbers) < 3:
        return None
    
    # Sort the unique numbers in descending order
    sorted_numbers = sorted(unique_numbers, reverse=True)
    
    # Return the third maximum number
    return sorted_numbers[2]

def main():
    # Example list of numbers
    numbers = [3, 1, 4, 4, 5, 2, 5, 6, 7, 6]
    
    # Call the function and get the third maximum number
    result = third_maximum(numbers)
    
    # Output the result
    if result is not None:
        print(f"The third maximum number is: {result}")
    else:
        print("There are fewer than 3 unique numbers.")

if __name__ == "__main__":
    main()
