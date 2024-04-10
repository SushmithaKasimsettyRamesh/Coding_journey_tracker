# Missing number in a consecutive series
# Approach 1:
def missing_num(a):
    n = len(a) + 1
    original_sum = n * (n + 1) // 2
    result_sum = 0
    for each_element in a:
        result_sum = result_sum + each_element

    difference = original_sum - result_sum
    if difference != len(a):
        return abs(difference)
    else:
        return None

b = [1,2,3,4]
c = [1,3,6,7]

output1 = missing_num(b)
output2 = missing_num(c)

if output1 is not None:
    print(output1)
if output2 is not None:
    print(output2)



'''
Logic:
for consecutive : (n*n(n+1))/2
check for sum originally for consecutive series
check for given array
difference = original sum - given array sum
12233
01234
so , length = n+1 = 5
'''

'''

#Approach 2
def find_missing_number(arr):
    # Sort the array
    arr.sort()

    # Initialize the expected number
    expected_number = arr[0]

    # Iterate through the array
    for num in arr:
        # If the current number is not equal to the expected number,
        # return the expected number as the missing number
        if num != expected_number:
            return expected_number
        # Otherwise, move to the next expected number
        expected_number += 1

    # If no missing number is found, return None
    return None


# Example usage:
array = [1, 2, 4, 5, 6]
missing_number = find_missing_number(array)
print("The missing consecutive number is:", missing_number)


'''