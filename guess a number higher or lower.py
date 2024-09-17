import random

def guess_the_number():
    low = 1
    high = 100
    
    secret_number = random.randint(low, high)
    
    print(f"Guess the number between {low} and {high}.")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            
            if guess < low or guess > high:
                print(f"Please guess a number between {low} and {high}.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} correctly.")
                break 
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    guess_the_number()
