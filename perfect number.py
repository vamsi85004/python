def is_perfect_number(num):
    """Check if a number is a perfect number."""
    if num <= 0:
        return False

    # Calculate the sum of proper divisors
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i

    return divisors_sum == num

# Example usage
number = int(input("Enter a number to check if it is a perfect number: "))
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
