t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    dic = {}
    for a in A:
        if a not in dic.keys():
            dic[a] = 1
        else:
            dic[a] += 1
    m = max(dic.values())
    print(n - m)