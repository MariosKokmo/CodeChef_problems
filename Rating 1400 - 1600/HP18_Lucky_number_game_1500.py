# cook your dish here
t = int(input())

for _ in range(t):
    bob_count = 0
    alice_count = 0
    N, a, b = [int(i) for i in input().split(' ')]
    # read the data
    nn = [int(i) for i in input().split(' ')]
    for j in nn:
        if j % a == 0 and j>=a:
            bob_count += 1
            continue
        if j % b == 0 and j>=b:
            alice_count += 1
    if bob_count > alice_count:
        print('BOB')
    else:
        print('ALICE')