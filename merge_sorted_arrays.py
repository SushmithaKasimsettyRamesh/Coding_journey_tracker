def merge_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Add remaining elements from list1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # Add remaining elements from list2
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list


# Example usage:
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print("Merged list:", merge_sorted_lists(list1, list2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
