t = int(input())
for _ in range(t):
    n, s = [int(i) for i in input().split()]
    if n >= s:
        print(s)
    else:
        s1 = n
        s2 = s-n
        print(s1-s2)