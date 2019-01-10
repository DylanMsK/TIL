# url = 'https://www.acmicpc.net/problem/2908'

x = input().split()
a, b = int(x[0][::-1]), int(x[-1][::-1])
print(a) if a > b else print(b)

print(max([int(i[::-1])for i in input().split()]))