# url = 'https://www.acmicpc.net/problem/2675'


n = int(input())

for i in range(n):
    x = input().split()
    r, s = int(x[0]), x[-1]
    
    result = ''
    for j in s:
        result += j*r

    print(result)