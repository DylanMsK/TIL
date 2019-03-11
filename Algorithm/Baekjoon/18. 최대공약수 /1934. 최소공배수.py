# url = 'https://www.acmicpc.net/problem/1934'

for _ in range(int(input())):
    A, B = map(int, input().split())
    com = 1
    for i in range(min(A, B), 1, -1):
        if A % i == 0 and B % i == 0:
            com = i
            A //= i
            B //= i
            break
    print(com * A * B)