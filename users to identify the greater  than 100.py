def main():
    user_input = input("Enter a list of integers separated by spaces: ")
    
    try:
        numbers = list(map(int, user_input.split()))
    except ValueError:
        print("Please enter valid integers separated by spaces.")
        return
    
    result = ['over' if num > 100 else num for num in numbers]
    
    print("Resulting list:", result)

if __name__ == "__main__":
    main()
    
