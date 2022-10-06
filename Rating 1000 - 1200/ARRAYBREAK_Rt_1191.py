t = int(input())

for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    even = 0
    odd = 0
    ones = 0
    for a in A:
        if a%2:
            odd += 1
        else:
            even += 1
    if odd==0 or even==0:
        print(0)
    else:
        print(even)