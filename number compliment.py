def bitwise_complement(n, bit_width):
    # Create a bitmask with all bits set to 1 for the given bit width
    bitmask = (1 << bit_width) - 1
    # Compute the bitwise complement and mask it to the bit width
    complement = ~n & bitmask
    return complement

# Test cases
n = 5
bit_width = 4  # Number of bits in the representation
print(f"Bitwise complement of {n} with bit width {bit_width} is {bitwise_complement(n, bit_width)}")

n = 7
bit_width = 3
print(f"Bitwise complement of {n} with bit width {bit_width} is {bitwise_complement(n, bit_width)}")
