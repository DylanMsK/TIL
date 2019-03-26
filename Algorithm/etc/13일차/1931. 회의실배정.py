# url = 'https://www.acmicpc.net/problem/1931'

N = int(input())
lst = []
for i in range(N):
    lst.append(tuple(map(int, input().split())))

lst = sorted(lst, key=lambda x: (x[1], x[0]))

start = lst[0]
cnt = 1
idx = 1
while idx < N:
    if lst[idx][0] >= start[1]:
        start = lst[idx]
        cnt += 1
    idx += 1
print(cnt)