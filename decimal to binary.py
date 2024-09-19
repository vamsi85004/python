def decimal_to_binary(n):
    if n < 0:
        raise ValueError("Negative numbers are not supported.")
    return bin(n).replace("0b", "")

def main():
    try:
        decimal_number = int(input("Enter a decimal number: "))
        binary_number = decimal_to_binary(decimal_number)
        print(f"The binary representation of {decimal_number} is {binary_number}.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
