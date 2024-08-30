def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    
    # Traverse both lists and append the smaller element to the merged list
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    # If there are remaining elements in list1, add them to the merged list
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    
    # If there are remaining elements in list2, add them to the merged list
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    return merged_list
