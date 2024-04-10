def find_duplicate_number(arr):
    if not arr:
        return None  # Return None if the array is empty
    dup_num = arr[0]  # Assume the first element is the maximum
    for num in arr:
        if num == dup_num:
            dup_num = num  # Update max_num if we find a greater number
    return dup_num

# Example usage:
array = [10, 5, 8, 10, 15]
s=[1,1,1,3,5]
print("The duplicate number in the array is:", find_duplicate_number(s))