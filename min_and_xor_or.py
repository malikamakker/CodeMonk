'''
Given an array A of N integers. Find out the minimum value of the following expression
(Ai and Aj) XOR (Ai or Aj
for all valid Ai!=Aj.

Sample Input
2
5
1 2 3 4 5
3
2 4 7

Sample Output
1
3
'''
for j in range(int(input())):
    n = int(input())
    min_val = 1000000000
    arr = list(map(int, input().split(' ')))
    arr.sort()
    for i in range(1, n):
        min_val = min(min_val, arr[i]^arr[i-1])
    print(min_val)
