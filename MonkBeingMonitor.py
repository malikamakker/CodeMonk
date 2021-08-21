'''
Monk being the monitor of the class needs to have all
the information about the class students. He is very busy
with many tasks related to the same, so he asked his friend
Mishki for her help in one task. She will be given heights
of all the students present in the class and she needs to
choose 2 students having heights h1 and h2 respectively,
such that h1>h2 and difference between the number of
students having height h1 and number of students having
height h2 is maximum.

Note: The difference should be greater than 0.

As Mishki has never been a monitor of the class, help her
in the same. If there exists such students, then print the
required difference else print "-1" (without quotes).

Sample Input
1
6
3 1 3 2 3 2

Sample Output
2
'''

def find_max_diff(count, first, last):
    if first<last:
        if count[first][0] < count[last][0]:
            return count[last][1] - count[first][1]
        else:
            return max(find_max_diff(count, first+1, last), find_max_diff(count,first, last-1))
    else:
        return -1

def take_second(pair):
    return pair[1]


for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    arr.sort()

    count = []
    similar_number = arr[0]
    ctr = 0
    for num in arr:
        if num == similar_number:
            ctr += 1
        else:
            count.append((similar_number, ctr))
            ctr = 1
            similar_number = num
    count.append((similar_number, ctr))
    print(find_max_diff(sorted(count, key=take_second), 0, len(count)-1))
