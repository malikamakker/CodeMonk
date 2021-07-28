from sys import stdin, stdout
import io, os

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

const = 100000


def count_sort(arr, digit):
    freq = [0 for i in range(100000)]

    for num in arr:
        freq[int(num / digit) % const] += 1

    for i in range(1, len(freq)):
        freq[i] += freq[i - 1]

    new = [0 for i in range(len(arr))]

    for num in reversed(arr):
        new[freq[int(num / digit) % const] - 1] = num
        freq[int(num / digit) % const] -= 1
    return new


n = int(input().decode().strip())
arr = list(map(int, input().decode().strip().split(' ')))

maxx = 0
maxx = max(arr, key=lambda x: len(str(x)))
maxx = len(str(maxx))

if maxx % 5 == 0:
    iterations = int(maxx / 5)
else:
    iterations = int(maxx / 5) + 1
digit = 1
for j in range(iterations):
    arr = count_sort(arr, digit)
    digit = digit * const
    stdout.write(' '.join(map(str, arr)) + "\n")