# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    C = [int(i) for i in input().split()]
    A=[]
    B=[]

    if n<=1:
        print(-1)
        continue
    
    # find position of maximum
    maximum = C[0]
    max_index = 0
    for i in range(n):
        if C[i]>maximum:
            maximum = C[i]
            max_index = i
    
    if max_index != 0:
        A = C[:max_index]
        B= C[max_index:]
    else:
        print(-1)
        continue
    
    if len(A) + len(B) == n:
        print(len(A))
        print(' '.join([str(i) for i in A]))
        print(len(B))
        print(' '.join([str(i) for i in B]))
    else:
        print(-1)
        
""" 
Problem
Chef initially had two non-empty arrays A and B, where both arrays contain distinct elements. Moreover, there is no common element in the arrays A and B.

Chef forms another array C from the arrays A and B using the following process :

Let X denote the leftmost element of array A and Y denote the leftmost element of array BB.
If Y is smaller than X, delete Y from B and append it to the end of C.
If X is smaller than Y, delete X from A and append it to the end of C.
If either array A or B becomes empty, append all the remaining elements of the other array to the end of C.
Chef forgot the arrays A and B but remembers the array C. Find any two valid non-empty arrays A and B that will yield the given array C. If it is not possible, print -1.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains a space-separated integer N — the number of elements in array C.
The next line contains N space-separated integers denoting the elements of the array C.
Output Format
For each test case, if a solutions exists, print any two valid arrays AA and BB along with their lengths respectively . For example, if A= [1,7] and B=[4,10,2], then print it as :

2 
1 7
3
4 10 2
Else, if answer doesn't exist, print −1 in a single line.

Constraints
1 <= T <= 100
1 <= N <= 10^5 
 
-10^5 <= C[i] <= 10^5 
 
The sum of N over all test cases won't exceed 10^6 
Sample 1:
Input
2
6
7 6 3 8 2 9
2
2 1

output
3
7 6 3
3
8 2 9
-1




Solution idea:
We are interested in any two arrays A and B that satisfy the above.
The idea is to simply find the maximum and its index.
If the maximum does not occur at the very first position
then we can always split our arrays where the maximum occurs.
A will be the array up to but not including the maximum
and B will be the array starting at the maximum till the end


"""