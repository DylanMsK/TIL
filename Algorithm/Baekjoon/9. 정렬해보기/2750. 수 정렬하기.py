# url = 'https://www.acmicpc.net/problem/2750'

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

print('\n'.join([str(i) for i in sorted(arr)]))