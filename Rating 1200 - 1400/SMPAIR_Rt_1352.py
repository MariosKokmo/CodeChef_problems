t = int(input())
for _ in range(t):
    n = int(input())
    numbers = [int(i) for i in input().split(" ")]
    min1 = min(numbers)
    numbers.remove(min1)
    min2 = min(numbers)
    print(min1+min2)