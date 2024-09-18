def fibonacci(n):
    """Generate Fibonacci sequence up to the n-th term."""
    fib_sequence = []
    a, b = 0, 1

    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b  # Update values for next Fibonacci number

    return fib_sequence

def fibonacci_at_position(position):
    """Return the Fibonacci number at a specific position (0-indexed)."""
    if position < 0:
        raise ValueError("Position cannot be negative.")
    if position == 0:
        return 0
    if position == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, position + 1):
        a, b = b, a + b

    return b

# Example usage
num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
fib_sequence = fibonacci(num_terms)
print(f"Fibonacci sequence up to {num_terms} terms: {fib_sequence}")

position = int(input("Enter the position to get the Fibonacci number (0-indexed): "))
fib_number = fibonacci_at_position(position)
print(f"The Fibonacci number at position {position} is: {fib_number}")
