string1 = 'prAcTiCe'

#length of string
print(len(string1))

# Convert to lowercase
print(string1.lower())

# Convert to uppercase
print(string1.upper())

#Returns True if all cased characters in the lowercase
print(string1.islower())

#Returns True if all cased characters in the uppercase
print(string1.isupper())


















list1 = [1, 2, 0]
list2 = [5, 6, 7]

i = 1
e = 'e'
#1]insert, it inserts e to list
list1.insert(i, e)
print(list1)

#2]remove
list1.remove('e')
print(list1)

#3]append
list1.append('sushi')
print(list1)

#4] Extend
# This extends list1 by appending all the elements from list2 to it.
list1.extend(list2)
print(list1)


#sort
list1 =[5,5,7,100,20,63]
list2.sort()
list1.sort()
print(list2)
print(list1)
