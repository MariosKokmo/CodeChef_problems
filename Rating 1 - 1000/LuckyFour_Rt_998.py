t = int(input())

for _ in range(t):
    number = str(input())
    count = 0
    for n in number:
        if n == '4':
            count += 1
    print(count)