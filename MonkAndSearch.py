def binary_search(arr, n, start, stop, target, q):
    if start < n and stop >= 0 and start <= stop:
        mid = (int((start + stop) / 2))

        if mid == 0:
            if q == 0:
                if arr[mid] >= target:
                    return mid
            if q == 1:
                if arr[mid] > target:
                    return mid

        elif mid < (n - 1):
            if q == 0:
                if arr[mid] < target and arr[mid + 1] >= target:
                    return mid + 1
            if q == 1:
                if arr[mid] <= target and arr[mid + 1] > target:
                    return mid + 1

        if q == 0:
            if arr[mid] < target:
                return binary_search(arr, n, mid + 1, stop, target, q)
            else:
                return binary_search(arr, n, start, mid - 1, target, q)

        if q == 1:
            if arr[mid] <= target:
                return binary_search(arr, n, mid + 1, stop, target, q)
            else:
                return binary_search(arr, n, start, mid - 1, target, q)
    return -1


n = 100
arr = "6279 2839 9035 1581 7907 1984 3803 6723 9182 2613 5310 9270 5806 668 6759 1807 5799 7694 397 7420 1882 5958 4790 5015 9545 2029 1618 6418 8643 5923 8794 4921 8761 4180 2853 3020 6164 6655 9742 5345 5619 5051 4614 7776 5718 1373 5934 7868 5418 6330 6655 6279 6655 8643 1807 4180 6723 2853 6279 6330 6723 7776 5958 7694 5015 5015 9742 9742 5923 5923 8761 5418 8761 5418 2029 6330 4790 2613 7420 5345 9742 9182 5345 2029 6164 3803 9182 1373 5051 9270 5934 6279 7907 7694 7420 5923 5619 9182 7694 4790"
arr = list(map(int, arr.split(' ')))
arr = sorted(arr)

for i in range(1):
    query ="1 465"
    query = list(map(int, query.split(' ')))
    num = binary_search(arr, n, 0, n - 1, query[1], query[0])
    print(num)
    if num == -1:
        print(0)
    else:
        print(n - num)
