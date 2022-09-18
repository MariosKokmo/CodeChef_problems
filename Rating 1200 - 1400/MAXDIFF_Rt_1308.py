t = int(input())
for _ in range(t):
    n,k = [int(i) for i in input().split()]
    w = [int(i) for i in input().split()]
    w.sort()
    if k>n//2:
        print(sum(w[n-k:]) - sum(w[:n-k]))
    else:
        print(sum(w[k:]) - sum(w[:k]))