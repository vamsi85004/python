def count_segments(s):
    # Split the string by whitespace and count the segments
    segments = s.split()
    return len(segments)

def main():
    # Prompt the user to enter a string
    input_string = input("Enter a string to count the number of segments: ")
    
    # Count the number of segments in the input string
    num_segments = count_segments(input_string)
    
    # Output the result
    print(f"The number of segments in the string is: {num_segments}")

if __name__ == "__main__":
    main()
