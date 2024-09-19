def reshape_matrix(matrix, r, c):
    original_rows = len(matrix)
    original_cols = len(matrix[0]) if original_rows > 0 else 0
    
    if original_rows * original_cols != r * c:
        return matrix  
    
    flat_list = [element for row in matrix for element in row]
    
    reshaped_matrix = []
    for i in range(r):
        reshaped_matrix.append(flat_list[i * c:(i + 1) * c])
    
    return reshaped_matrix

original_matrix = [[1, 2], [3, 4]]
new_rows = 1
new_cols = 4
result = reshape_matrix(original_matrix, new_rows, new_cols)
print(result)  # Output: [[1, 2, 3, 4]]
