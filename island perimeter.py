def island_perimeter(grid):
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    
    def count_boundary(cell_r, cell_c):
        nonlocal perimeter
        # Count boundaries for a single cell
        boundaries = 4
        if cell_r > 0 and grid[cell_r - 1][cell_c] == 1:
            boundaries -= 1
        if cell_r < rows - 1 and grid[cell_r + 1][cell_c] == 1:
            boundaries -= 1
        if cell_c > 0 and grid[cell_r][cell_c - 1] == 1:
            boundaries -= 1
        if cell_c < cols - 1 and grid[cell_r][cell_c + 1] == 1:
            boundaries -= 1
        perimeter += boundaries
    
    # Iterate through the grid to calculate the perimeter
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                count_boundary(r, c)
    
    return perimeter

# Test cases
grid1 = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]

grid2 = [
    [1]
]

grid3 = [
    [1, 0],
    [0, 1]
]

print(island_perimeter(grid1))  # Output: 12
print(island_perimeter(grid2))  # Output: 4
print(island_perimeter(grid3))  # Output: 6
