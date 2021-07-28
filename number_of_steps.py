
'''

Problem
You are given two arrays a and b. In each step, you can set a[i]=a[i]-b[i].
Determine the minimum number of steps that are required to make all a's equal.

Print the minimum number of steps that are required to make all a's equal.
If it is not possible, then print -1.

Sample input
2
5 6
4 3

Sample output
-1

Sample Input
5
5 7 10 5 15
2 2 1 3 5

Sample Output
8
'''



def num_steps(a, b, target):
    steps = 0
    for i in range(n):
        if(a[i]==target):
            continue
        if((a[i]-b[i])<target):
            return -1
        if(b[i]==0):
            return -1
        if(((a[i]-target)%b[i])):
            return -1
        steps = steps + int((a[i]-target)/b[i])
    return steps

n = int(input())
a = input()
a = list(map(int, a.split(' ')))
b = input()
b = list(map(int, b.split(' ')))

min_diff = 5001
min_num = 5001
found = False
for i in range(n):
    if a[i]<b[i]:
        print(num_steps(a,b,a[i]))
        found = True
        break
    if(a[i]>=b[i] and (a[i]-b[i])<min_diff):
        min_diff = a[i] - b[i]
    if(a[i]<min_num):
        min_num = a[i]

if(not found):
    x = num_steps(a, b, min_diff)
    y = num_steps(a, b, min_num)

    if x==-1:
        print(y)
    elif y==-1:
        print(x)
    else:
        print(min(x,y))
