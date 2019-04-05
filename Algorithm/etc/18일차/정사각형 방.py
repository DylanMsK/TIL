# dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
# for tc in range(int(input())):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]

#     min_, max_ = 1000000, 0
#     for y in range(N):
#         for x in range(N):
#             visited = [0] * (N**2)
#             visited[0] = (x, y)
#             cnt = 1
#             while 1:
#                 now = visited[cnt-1]
#                 for diff in range(4):
#                     if 0 <= now[0]+dx[diff] < N and 0 <= now[1]+dy[diff] < N and abs(arr[now[1]+dy[diff]][now[0]+dx[diff]] - arr[now[1]][now[0]]) == 1\
#                         and (now[0]+dx[diff], now[1]+dy[diff]) not in visited:
#                         visited[cnt] = (x+dx[diff], y+dy[diff])
#                         cnt += 1
#                         break
#                 else:
#                     if cnt > max_:
#                         max_ = cnt
#                         if arr[visited[0][1]][visited[0][0]] < min_:
#                             min_ = arr[visited[0][1]][visited[0][0]]
#                     break

#     print('#{} {} {}'.format(tc+1, min_, max_))

def find_minimum(arr, N):
    min_ = N**2+1
    loc = ()
    for y in range(N):
        for x in range(N):
            if arr[y][x] == -1:
                continue
            if arr[y][x] < min_:
                min_ = arr[y][x]
                loc = (x, y)
    return loc, min_


def move(x, y):
    global arr, N, dx, dy
    sum_ = 0
    while 1:
        for diff in range(4):
            if 0 <= x+dx[diff] < N and 0 <= y+dy[diff] < N and arr[y+dy[diff]][x+dx[diff]] != -1 and arr[y+dy[diff]][x+dx[diff]] - arr[y][x] == 1:
                arr[y][x] = -1
                x, y = x+dx[diff], y+dy[diff]
                sum_ += 1
                break
        else:
            arr[y][x] = -1
            sum_ += 1
            break
    return sum_


dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_ = 1000000
    max_ = 0
    while 1:
        loc, val = find_minimum(arr, N)
        if loc:
            sum_ = move(loc[0], loc[1])
            if sum_ > max_:
                max_ = sum_
                min_ = val
        else:
            break

    print('#{} {} {}'.format(tc+1, min_, max_))