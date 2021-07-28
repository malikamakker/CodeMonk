'''
A large binary number is represented by a string A of size N
and comprises of 0s and 1s. You must perform a cyclic shift on
this string.

You performed the shift infinite number of times and each time
you recorded the value of the binary number represented by the
string. The maximum binary number formed after performing (possibly 0)
the operation is B. Your task is to determine the number of cyclic
shifts that can be performed such that the value represented by
the string A will be equal to B for the Kth time.


Sample Input
2
5 2
10101
6 2
010101

Sample Output
9
3
'''

n = int(input())

for i in range(n):
    str = list(input().split())
    n = int(str[0])
    k = int(str[1])

    bin_str = input()
    num = int(bin_str, 2)
    count = 0
    mask = 2**(len(bin_str))
    shifts = []
    b = num
    shifts.append(0)
    max_pos = []
    max_pos.append(0)
    for j in range(len(bin_str)-1):
        if ((num<<1) & mask):
            num = ((num<<1)&(mask-1)) + 1
        else:
            num = (num<<1)&(mask-1)
        tmp = b
        b = max(b, num)
        if tmp!=b:
            shifts = []
            shifts.append(j+1)
            max_pos = []
            max_pos.append(j+1)
        elif b==num:
            shifts.append(j+1 - max_pos[-1])
            max_pos.append(j+1)
    if len(shifts):
        complete_rounds = int(k/len(shifts))
        if k%len(shifts)==0:
            complete_rounds = complete_rounds - 1
        extra_shifts = k - complete_rounds*len(shifts)
        sum_of_extra_shifts = sum(shifts[:extra_shifts])

        print(len(bin_str)*complete_rounds+sum_of_extra_shifts)
    else:
        print(0)
