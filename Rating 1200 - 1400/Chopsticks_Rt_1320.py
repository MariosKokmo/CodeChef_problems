n , d = [int(i) for i in input().split()]
L = []
for _ in range(n):
    L.append(int(input()))
L.sort(reverse=True)
count = 0
i = 0
while i < n-1:
    if L[i] - L[i+1] <= d:
        count += 1
        i += 2
    else:
        i += 1

print(count)