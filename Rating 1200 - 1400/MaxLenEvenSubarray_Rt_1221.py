t = int(input())
for _ in range(t):
    n = int(input())
    odds = 0
    if n%2:
        odds = int(n//2 + 1)
    else:
        odds = n//2
    if odds%2:
        print(n-1)
    else:
        print(n)