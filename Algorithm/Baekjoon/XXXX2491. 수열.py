# url = 'https://www.acmicpc.net/problem/2491'

N = int(input())
lst = list(map(int, input().split()))
# stack = [lst[0]]
now = lst[0]
cnt = 1
max_ = 1
flag = True
for idx in range(1, N):
    if lst[idx] >= now and flag:
        cnt += 1
        now = lst[idx]
        continue
    elif lst[idx] < now and flag:
        flag = False
        if idx == 1:
            cnt += 1
        if cnt > max_:
            max_ = cnt
        cnt = 2
        now = lst[idx]
        continue
    elif lst[idx] <= now and not flag:
        cnt += 1
        now = lst[idx]
        continue
    elif lst[idx] > now and not flag:
        flag = True
        if cnt > max_:
            max_ = cnt
        cnt = 2
        now = lst[idx]
        continue
    else:
        print('error')
print(max_)


