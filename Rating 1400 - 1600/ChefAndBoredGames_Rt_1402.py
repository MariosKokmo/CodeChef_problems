t = int(input())
for _ in range(t):
    n = int(input())
    total = 0
    i = 1
    while i <= n:
        no_strides = n - i + 1
        total += no_strides**2
        i += 2
    print(total)