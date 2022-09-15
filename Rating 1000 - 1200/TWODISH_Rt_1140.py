t = int(input())

for _ in range(t):
    n,a,b,c = [int(i) for i in input().split()]
    if b<n:
        print('NO')
    else:
        if (a+c)<n:
            print('NO')
        else:
            print('YES')