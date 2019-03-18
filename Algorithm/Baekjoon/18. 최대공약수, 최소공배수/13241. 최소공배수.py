# url = 'https://www.acmicpc.net/problem/13241'

A, B = map(int, input().split())
com = 1
for i in range(min(A, B), 1, -1):
    if A % i == 0 and B % i == 0:
        com = i
        A //= i
        B //= i
        break
print(com * A * B)