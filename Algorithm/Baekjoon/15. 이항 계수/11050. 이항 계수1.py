# url = 'https://www.acmicpc.net/problem/11050'

N, K = map(int, input().split())
res = 1
for i in range(N, N-K, -1):
    res *= i
for i in range(K, 1, -1):
    res //= i
print(res)