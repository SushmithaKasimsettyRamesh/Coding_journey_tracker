# returns index position of target if found
def linearsearch(list, target):
    for i in range(0, len(list)):  # to find target starting from 0 to list's length
        if list[i] == target:  # the index or the value has to match to the target
            return i  # coz we want that position
    return None  # if not return none  #use capital N but not small n


# lets verify

def verify(index):
    if index is not None:  # cause it has got some value
        print('target found')  # that means target is found
    else:
        print('target not found')


# take a list and verify
numbers = [1, 2, 3, 4, 5]
# assign results and call linear search and pass the list (numbers) and put the required target
result = linearsearch(numbers, 6)  # 6 is not there, not found

verify(result)
# for the number 4 which is in the list , so it should come found
result = linearsearch(numbers, 4)

verify(result)
