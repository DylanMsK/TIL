# url = 'https://www.acmicpc.net/problem/2775'


t = int(input())

for i in range(t):
    k, n = int(input()), int(input())
    lst = [l for l in range(1, n+1)] + [0]
    for j in range(1, k+1):
        temp = []
        for m in range(n):
            temp.append(sum(lst[:m+1]))
        lst = temp + [0]
    print(lst[-2]) 