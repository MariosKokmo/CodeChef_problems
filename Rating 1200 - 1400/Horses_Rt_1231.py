t = int(input())

for _ in range(t):
    n = int(input())
    s = [int(i) for i in input().split()]
    s.sort()
    diff = [s[i] - s[i-1] for i in range(1,n)]
    print(min(diff))