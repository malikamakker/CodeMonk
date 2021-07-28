'''
Monk's best friend Micro, who happen to be an awesome programmer,
got him an integer matrix M of size N  x N for his birthday.
Monk is taking coding classes from Micro.
They have just completed array inversions and Monk was successful in
writing a program to count the number of inversions in an array.
Now, Micro has asked Monk to find out the number of inversion in the matrix M.
Number of inversions, in a matrix is defined as the number of unordered pairs
of cells {(i,j),(p,q)} such that M[i][j]>M[p][q] and i<=p and j<=q.

Monk is facing a little trouble with this task and since you did not
got him any birthday gift, you need to help him with this task.

Sample Input
2
3
1 2 3
4 5 6
7 8 9
2
4 3
1 4

Sample Output
0
2
'''

def find_inversions(num, j, k, matrix, min_row_wise, min_of_min_cols):
    count = 0

    if j > 0 and num < min_of_min_cols[j][k + 1]:
        count += (j) * (k + 1)
    elif j > 0:
        count += find_inversions(num, j - 1, k, matrix, min_row_wise, min_of_min_cols)

    if k >= 0 and num < min_row_wise[j + 1][k+1]:
        count += k + 1
    elif k >= 0:
        while (k >= 0):
            if num < min_row_wise[j + 1][k+1]:
                count += k + 1
                break
            else:
                if num < matrix[j][k]:
                    count += 1
            k = k - 1
    return count

for i in range(int(input())):
    n = int(input())

    min_row_wise = [[1001 for j in range(n+1)] for j in range(n+1)]
    min_of_min_cols = [[1001 for j in range(n+1)] for j in range(n+1)]
    matrix = []

    count = 0

    for j in range(n):
        arr = list(map(int, input().split(' ')))
        matrix.append(arr)

        for k in range(n):
            if matrix[j][k] < min_row_wise[j + 1][k]:
                min_row_wise[j + 1][k + 1] = matrix[j][k]
            else:
                min_row_wise[j + 1][k + 1] = min_row_wise[j + 1][k]
            if min_row_wise[j + 1][k + 1] < min_of_min_cols[j][k + 1]:
                min_of_min_cols[j + 1][k + 1] = min_row_wise[j + 1][k + 1]
            else:
                min_of_min_cols[j + 1][k + 1] = min_of_min_cols[j][k + 1]
            count += find_inversions(matrix[j][k], j, k, matrix, min_row_wise, min_of_min_cols)
    print(count)
