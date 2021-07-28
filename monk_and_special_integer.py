'''
Special integer, K, of an array, is an integer such that none
of its subarray of size K has sum of elements greater than X.

Sample Input
4 8
1 2 3 4

Sample Output
2

Explanation
Sum of all subarrays of size 1: 1,2,3,4
Sum of all subarrays of size 2: 3,5,7
Sum of all subarrays of size 3: 6,9
Sum of all subarrays of size 4: 10
So clearly, maximum subarray size, such that all subarrays of
that size have sum of elements less than 8 is 2.
'''

n,x = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))
sums = [0]
k = 0

for i in range(len(arr)):
    total = sums[-1] + arr[i]
    if total>x:
        break
    k = k + 1
    sums.append(total)

while i < len(arr):
    total = sums[-1] -  arr[i-k] + arr[i]
    while(total>x and k>0):
        k = k - 1
        total = total - arr[i - k]
    sums.append(total)
    i = i + 1
print(k)
