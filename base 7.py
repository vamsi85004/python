class Base7Converter:
    def __init__(self):
        pass

    def to_base_7(self, num):
        """Convert an integer to base 7."""
        if num == 0:
            return "0"
        
        negative = num < 0
        num = abs(num)
        base_7 = ""

        while num > 0:
            base_7 = str(num % 7) + base_7
            num //= 7

        return "-" + base_7 if negative else base_7

    def from_base_7(self, base_7_str):
        """Convert a base 7 string to an integer."""
        if base_7_str == "0":
            return 0
        
        negative = base_7_str[0] == "-"
        if negative:
            base_7_str = base_7_str[1:]

        num = 0
        length = len(base_7_str)

        for i, digit in enumerate(base_7_str):
            num += int(digit) * (7 ** (length - i - 1))

        return -num if negative else num

# Example usage
converter = Base7Converter()

# Convert integer to base 7
num = 100
base_7 = converter.to_base_7(num)
print(f"{num} in base 7 is: {base_7}")

# Convert base 7 back to integer
base_7_str = "202"
integer_value = converter.from_base_7(base_7_str)
print(f"{base_7_str} in base 10 is: {integer_value}")
