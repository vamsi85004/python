def number_to_hexadecimal(number):
    """
    Convert an integer to its hexadecimal representation.

    :param number: int, the number to convert
    :return: str, the hexadecimal representation of the number
    """
    return hex(number)

# Example usage:
number = 255
hexadecimal = number_to_hexadecimal(number)
print(hexadecimal)  # Output: '0xff'
