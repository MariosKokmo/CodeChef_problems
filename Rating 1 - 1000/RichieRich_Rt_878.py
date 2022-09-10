t = int(input())
for _ in range(t):
    a,b,x = [int(i) for i in input().split()]
    print(int((b-a)/x))