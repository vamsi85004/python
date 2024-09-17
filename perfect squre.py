import math

def is_perfect_square(n):
    if n < 0:
        return False
    root = math.isqrt(n)  # Integer square root of n
    return root * root == n

def main():
    number = int(input("Enter a number to check if it's a perfect square: "))
    if is_perfect_square(number):
        print(f"{number} is a perfect square.")
    else:
        print(f"{number} is not a perfect square.")

if __name__ == "__main__":
    main()
