t = int(input())

for _ in range(t):
    a,b,p,q = [int(i) for i in input().split()]
    
    #alice n , bob n+1
    alice = p/a
    bob = q/b
    
    if alice!=p//a or bob!=q//b:
        print('NO')
    else:
        if abs(bob - alice)<=1:
            print('YES')
        else:
            print('NO')