t = int(input())
for _ in range(t):
    d, l, r = [int(i) for i in input().split()]
    if d<l:
        print('Too Early')
    elif d>r:
        print('Too Late')
    else:
        print('Take second dose now')