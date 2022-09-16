t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    median = a[n//2]
    cnt = 0
    for s in a:
        if s>=median:
            cnt += 1
    print(cnt)