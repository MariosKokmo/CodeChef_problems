t = int(input())

for _ in range(t):
    n, p, x, y = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    j = 1
    total = 0
    while j < p+1:
        if arr[j-1] == 0:
            total += x
        else:
            total += y
        j += 1
    print(total)