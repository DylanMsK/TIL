# url = 'https://www.acmicpc.net/problem/2747'

n = int(input())
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(n))

# n = int(input())
# if n <= 1:
#     print(n)
# else:
#     a1, a2 = 1, 1
#     for i in range(n-2):
#         a1, a2 = a2, a1 + a2
#     print(a2)