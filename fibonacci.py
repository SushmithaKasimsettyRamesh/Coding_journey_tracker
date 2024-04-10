# 0,1,1,2,3,5,8,13,21,
#i.e., 0+1=1, 1+1=2, 2+3=5
#efficient way
num_range = int(input(''))

a =0
b=1

#first two numbers are suppsosed to print
print(a)
print(b)

#Since, two numbers are already there
for x in range(num_range-2):
    c=a+b
    print(c)
    a=b #these gets updated
    b=c