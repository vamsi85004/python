def generate_pascals_triangle(num_rows):
    triangle = []

    for i in range(num_rows):
        # Start with a row with '1' at both ends
        row = [1] * (i + 1)

        # Compute the inner elements of the row
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]

        triangle.append(row)

    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(' '.join(map(str, row)).center(2 * len(triangle)))

# Number of rows for Pascal's Triangle
num_rows = 5

# Generate and print Pascal's Triangle
pascals_triangle = generate_pascals_triangle(num_rows)
print_pascals_triangle(pascals_triangle)
