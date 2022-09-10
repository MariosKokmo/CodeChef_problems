t = int(input())
for _ in range(t):
    numbers = [int(i) for i in input().split()]
    sums = [numbers[i] + numbers[j] for i in range(1,4) for j in range(i+1,4)]
    sums = sums + [numbers[1] + numbers[3] + numbers[2]]
    sums = sums + numbers[1:]
    if numbers[0] not in sums:
        print('NO')
        continue
    print('YES')