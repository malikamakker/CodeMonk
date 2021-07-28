'''
We have m completely wet clothes out under sunshine waiting to
become dry. we are now at second t1 and it's raining. It's going
to rain again on seconds t2...tn and after each rain clothes will
be completely wet again. Cloth number i needs a1 seconds to become
dry. We can go out and collect all dry clothes at any moment but
can't do this more than g times. What is the maximum number of clothes
we can collect until second tn? Note that the duration of each rain is
almost zero, so we can ignore it. Also collecting clothes does not
take any time from us.

Sample Input
3 3 2
3 5 8
4 1 3

Sample Output
2
'''
def binary_search(array, m, start, stop, interval):
    while stop >= 0 and start < m and start <= stop:
        mid = int((start + stop) / 2)

        if mid < (m - 1):
            if array[mid] <= interval and array[mid + 1] > interval:
                return mid + 1
        else:
            if array[mid] <= interval:
                return mid + 1

        if array[mid] <= interval:
            start = mid + 1
        else:
            stop = mid - 1
    return 0


n, m, g = map(int, input().split(' '))

times = list(map(int, input().split(' ')))

intervals = [times[i] - times[i - 1] for i in range(1, len(times))]

clothes = list(map(int, input().split(' ')))

clothes = sorted(clothes)
intervals = sorted(intervals, reverse=True)

count = 0
clothes_count = 0
for interval in intervals:
    index = binary_search(clothes, m, 0, m - 1, interval)
    if index != -1 and clothes_count < index:
        clothes_count = index
        count += 1
    if count == g:
        break
    if clothes_count == m:
        break
print(clothes_count)
