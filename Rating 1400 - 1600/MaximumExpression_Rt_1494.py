t = int(input())

for _ in range(t):
    n = int(input())
    S = input()
    symb = []
    numb = []
    for s in S:
        if s == '+' or s == '-':
            symb.append(s)
        else:
            numb.append(s)
    symb.sort(reverse=True)
    numb.sort(reverse=False)
    out = []
    for i in range(len(symb)):
        out.append(numb[i])
        out.append(symb[i])
    out = out + numb[len(symb):]
    print(''.join([str(o) for o in out[::-1]]))