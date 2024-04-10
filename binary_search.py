# binary serach: it usually breaks the arrays into smaller set until target is found

def binary_search(list, target):
    first = 0  # mentioning the index of the list
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint

        elif list[midpoint] < target:
            first = midpoint + 1

        else:
            last = midpoint - 1

    return None

    # cause the last is lesser , index starts from 0

    # we want something in which first is less than or equal to last

    # floor division = rounds off 7/2=3.5 but 3

    # while loop takes condition and keep executimg the code
    # inside the loop until condtn evaluates to false


'''example: target =6 first=0, last=6
mid=6/2=3
if target = 3, print or return that value, in this case no

if 3>6
3+1, true

if target=2
3-1
till target value is reached

'''


# lets verify

def verify(index):
    if index is not None:  # cause it has got some value
        print('target found')  # that means target is found
    else:
        print('target not found')


# take a list and verify
numbers = [1, 2, 3, 4, 5]
# numbers=[5,4,3,2,1]
# assign results and call linear search and pass the list (numbers) and put the required target
result = binary_search(numbers, 6)  # 6 is not there, not found

verify(result)
# for the number 4 which is in the list , so it should come found
result = binary_search(numbers, 4)

verify(result)