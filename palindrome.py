# 12321, reverse should be same
# 124421
#Complexity : for the loop its, o(n) and for other operations, its 0(1)
#bool represents, if the function returns true/false


def palindrome(a) -> bool:
    length = len(a)
    for i in range(length // 2):
        if a[i] != a[length - i - 1]:
            return False
    return True


#Testing
b = input()
print(palindrome(b))


#usage of if_name=="_main_"
'''
if __name__ == "__main__":
    user_input = input("Enter a word to determine palindrome: ")
    result = palindrome(user_input)
    if result:
        print(" a palindrome")
    else:
        print("not a palindrome")
'''




'''
logic: 124421,
Index: 012345
here, a[1] =a[4]
len = 6
len//2 =6//2=3
arr[i] = arr[len - i - 1]
arr[2] = arr[6-2-1] = arr[3]
'''