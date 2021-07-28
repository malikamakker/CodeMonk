# mem = [[0 for i in range(1000000009)] for j in range(100000)]

def combos(pos, n, count, target):
    ctr = 0
    if (pos+2)==n:
        return 1
    elif (pos+2)>n:
        return 0
    else:
        if count==target:
            return n-(pos+1)
        else:
            for i in range(pos, n):
                ctr = ctr + combos(pos+2, n+1, count+1, target)
    return ctr

for i in range(int(input())):
    total = 0
    n = int(input())

    for j in range(1, n):
        count = combos(0, n, 1, j)
        total = total + count
        if count==1:
            break
    print((10**n - total)%1000000009)
