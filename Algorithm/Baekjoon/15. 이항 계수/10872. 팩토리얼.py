# url = 'https://www.acmicpc.net/problem/10872'

N = int(input())
res = 1
for i in range(N, 1, -1):
    res *= i
print(res)