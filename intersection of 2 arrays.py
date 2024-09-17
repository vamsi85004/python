def intersection(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    intersection_result = set1.intersection(set2)
    
    return list(intersection_result)

arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 3, 5]

result = intersection(arr1, arr2)
print("Intersection:", result)
