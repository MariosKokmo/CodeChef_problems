t = int(input())

for _ in range(t):
    a,b,a1,b1,a2,b2 = [int(i) for i in input().split()]
    
    ab = sorted([a,b])
    a1b1 = sorted([a1,b1])
    a2b2 = sorted([a2,b2])
    
    if ab[0] == a1b1[0]:
        if ab[1] == a1b1[1]:
            print(1)
            continue
    if ab[0] == a2b2[0]:
        if ab[1] == a2b2[1]:
            print(2)
            continue
    print(0)