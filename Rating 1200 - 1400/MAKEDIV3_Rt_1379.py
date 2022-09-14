t = int(input())

for _ in range(t):
    n = int(input())
    if n==1:
        print(3)
    else:
        print('1'+'0'*(n-2)+'5')