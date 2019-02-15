# url = 'https://www.acmicpc.net/problem/2581'

M = int(input())
N = int(input())

lst = []
for i in range(M, N+1):
    if i == 1:
        continue
    else:
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag:
            lst.append(i)

if lst:
    print(sum(lst))
    print(lst[0])
else:
    print(-1)