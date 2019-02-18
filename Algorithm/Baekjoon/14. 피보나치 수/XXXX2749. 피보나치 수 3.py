# url = 'https://www.acmicpc.net/problem/2749'

n = int(input())
if n <= 1:
    print(n)
else:
    a, b = 1, 1
    for i in range(n-2):
        a, b = b, a + b

print(str(b)[-6:])