t = int(input())

for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    C = {i:0 for i in range(1,101)}
    for a in A:
        C[a] += 1
    out = []
    for i in range(1,101):
        while C[i]!=0:
            out.append(i)
            C[i] -= 1
    print(' '.join([str(i) for i in out]))