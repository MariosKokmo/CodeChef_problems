t = int(input())
for _ in range(t):
    a,b,c,d,k = [int(i) for i in input().split()]
    # it is all about the manhattan distance
    diff = abs(c-a)+abs(d-b)
    if (k == diff):
        print('YES')
        continue
    if k>diff:
        if (k-diff)%2 == 0: #excess number of steps is even
            print('YES')
        else:
            print('NO')
        continue
    print('NO')