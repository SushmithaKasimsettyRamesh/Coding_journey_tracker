'''
OP SHOULD BE
APBQCR #COMBINING EVERYTHING
'''
class Solution: #class
    def merge_alternate(self, w1:str, w2: str) -> str:
        l1 = len(w1)
        print(l1)
        l2 = len(w2)
        print(l2)
        x = min(l1, l2)  # calculating minimum length among 2 words
        print('length_min:', x)
        # we want loop that iterates from index 0 to length of shorter word
        combined = ''
        # if the length of 2 words are equal, w1=w2
        for i in range(x):  # range is used to iterate for for range of numbers but nit single one
            combined += ''.join(w1[i] + w2[i])  # joining 1st indices of 2 words
        # w1!=w2
        if l1 > l2:
            combined += w1[len(w2):]  # selects a slice of w1 starting from the length of w2 and going till the end.
        elif l2 > l1:
            combined += w2[len(w1):]
        print(combined)

        return combined




#example
test = Solution()
result = test.merge_alternate('abc','pqrz1')
print(result)


#context with lengths

'''w1 ='abc'
w2='p'
print(w1[len(w2):])

#if len(w2)>len(w1):
w1='1234'
w2 ='xyz89'

print(w2[len(w1):])

"""output:
bc
9"""'''


