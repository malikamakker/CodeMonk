'''
Given N points located on the co-ordinate plane, where the ith
point is located at co-ordinate (xi,yi) , you need to answer q queries.

In the ith query, you shall be given an integer ri, and
considering you draw a circle centered at the origin (0,0)  with radius ri,
you need to report the number of points lying inside or on the
circumference of this circle.

For each query, you need to print the answer on a new line.

Sample Input
5
1 1
2 2
3 3
-1 -1
4 4
2
3
32

Sample Output
3
5

'''

import math

points = []
for i in range(int(input())):
    points.append(tuple(map(lambda x: abs(int(x)), input().split(' '))))
    x2 = points[-1][0] ** 2
    y2 = points[-1][1] ** 2
    points[-1] = math.sqrt(x2 + y2)

points = sorted(points)


def binary_search(array, radius, start, stop):
    req = -1
    if stop >= 0 and start < len(array) and start <= stop:
        mid = int((start + stop) / 2)
        if (mid + 1) < len(array):
            if array[mid] <= radius and array[mid + 1] > radius:
                return mid
        else:
            if array[mid] <= radius:
                return mid

        if array[mid] < radius:
            req = binary_search(array, radius, mid + 1, stop)
        else:
            req = binary_search(array, radius, start, mid - 1)
    return req


for i in range(int(input())):

    radius = int(input())

    x = binary_search(points, radius, 0, len(points) - 1)

    if x == -1:
        print(0)
        continue

    print(x + 1)
