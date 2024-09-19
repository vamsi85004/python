def insert_at_position(arr, position, element):
    return arr[:position] + [element] + arr[position:]

my_array = [1, 2, 3, 4]
new_array = insert_at_position(my_array, 2, 10)
print(new_array)  # Output: [1, 2, 10, 3, 4]
