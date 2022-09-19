t = int(input())

for _ in range(t):
    u,v,a,s = [int(i) for i in input().split()]
    entering_u = (u**2 - 2*a*s)
    if entering_u > v**2:
        print('No')
    else:
        print('Yes')