t = int(input())

for _ in range(t):
    n,x = [int(i) for i in input().split()]
    max_rate = 0
    for _ in range(n):
        s, r = [int(i) for i in input().split()]
        if r >= max_rate:
            if s <= x:
                max_rate = r
    print(max_rate)  