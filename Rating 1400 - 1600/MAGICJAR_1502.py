# cook your dish here
t = int(input())

for _ in range(t):
    N = int(input())
    A = [int(a) for a in input().split()]
    # worst case we need the sum of all
    # we need at every step at least one
    # chef to be able to finish. We can subtract 1 jar from each chef
    # except for the one that needs to be able to finish
    print(sum(A)-N+1)