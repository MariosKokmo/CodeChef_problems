n, m, k = [int(i) for i in input().split()]
total = 0
for _ in range(n):
    tq = [int(i) for i in input().split()]
    t = tq[:-1]
    q = tq[-1]
    if sum(t)>= m and q<=10:
        total += 1
        
print(total)