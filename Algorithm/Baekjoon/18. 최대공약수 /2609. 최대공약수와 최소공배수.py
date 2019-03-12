# url = 'https://www.acmicpc.net/problem/2609'

A, B = map(int, input().split())
com = 1
for i in range(min(A, B), 1, -1):
    if A % i == 0 and B % i == 0:
        com = i
        A = A // i
        B = B // i
        break
print(com)
print(com * A * B)