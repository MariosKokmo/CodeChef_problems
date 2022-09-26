t = int(input())

for _ in range(t):
    n,k = [int(i) for i in input().split()]
    # least common multiple n*k/gcd(n,k)
    r = 0
    if n >= k:
        a,b = n,k
        while (a%b)>0:
            r = a%b
            a = b
            b = r
        gcd = b
    else:
        a,b = k,n
        while (a%b)>0:
            r = a%b
            a = b
            b = r
        gcd = b
    o = n/gcd
    print(int(o))