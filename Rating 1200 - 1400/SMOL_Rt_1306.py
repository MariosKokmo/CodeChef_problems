t = int(input())

for _ in range(t):
    n,k = [int(i) for i in input().split()]
    if k==0:
        print(n)
    else:
        print(n%k)