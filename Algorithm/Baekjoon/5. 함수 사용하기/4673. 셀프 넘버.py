# url = 'https://www.acmicpc.net/problem/4673'
def d(n):
    return n + sum([int(i) for i in str(n)])

lst = [i for i in range(1, 10001)]
for i in range(1, 10001):
    if d(i) in lst:
        lst.remove(d(i))

print('\n'.join([str(i) for i in lst]))