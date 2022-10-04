t = int(input())
for _ in range(t):
    L, R = [int(i) for i in input().split()]
    
    d = R-L+1 # distinct numbers, make a 2D table to see  the distinct sums
    print(2*d - 1)