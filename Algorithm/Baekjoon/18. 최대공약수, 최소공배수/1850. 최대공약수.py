# url = 'https://www.acmicpc.net/problem/1850'

a, b = map(int, input().split())
for i in range(2, 8):
    if a % i == 0 and b % i == 0:
        r = i
print('1' * r)