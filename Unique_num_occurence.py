'''problem: Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
Input: arr = [1,2,2,1,1,3]
Output: true
1= 3
2=2
3=1

Input: arr = [1,2]
Output: false
1=1
2=1
'''
#algo: first check for frequencies and check if they are same or not in an array
#hashmap, thats dictionary
def check(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        else:
            seen.add(num)
    return None

s = [2, 2, 1, 3, 3, 5]
print("The duplicate number in the array is:", check(s))













#class Solution:
 #   def uniqueOccurrences(self, arr: List[int]) -> bool:

