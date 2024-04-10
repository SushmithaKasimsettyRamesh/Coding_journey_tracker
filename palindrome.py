# 12321, reverse should be same
# 124421

def palindrome(a):
    length = len(a)
    for i in range(length // 2):
        if a[i] != a[length - i - 1]:
            return False
    return True


#Testing
b = [1,2,3,4]
c = [1,2,4,4,2,1]
d = [1,2,3,2,1]

output1 = palindrome(b)
output2 = palindrome(c)
output3 = palindrome(d)


print(output1)
print(output2)
print(output3)


'''
logic: 124421,
Index: 012345
here, a[1] =a[4]
len = 6
arr[i] = arr[len - i - 1]
arr[2] = arr[6-2-1] = arr[3]
'''