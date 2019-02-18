# url = 'https://www.acmicpc.net/problem/1012'
import sys
sys.setrecursionlimit(100000)

def find(arr):
    for y in range(N):
        for x in range(M):
            if arr[y+1][x+1]:
                return x+1, y+1
    return

def change(x, y):
    for i in range(4):
        nxt_x, nxt_y = x + dx[i], y + dy[i]
        if arr[nxt_y][nxt_x]:
            if (nxt_x, nxt_y) in lst:
                continue
            lst.append((nxt_x, nxt_y))
            return change(nxt_x, nxt_y)

result = []
tc = int(sys.stdin.readline())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(tc):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0] * (M+2) for i in range(N+2)]
    for i in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        arr[Y+1][X+1] = 1
    # arr = [
    #     [0, 0, 0, 0],
    #     [0, 1, 1, 0],
    #     [0, 0, 1, 0],
    #     [0, 1, 1, 0],
    #     [0, 0, 0, 0]
    # ]
    cnt = 0
    while 1:
        nxt = find(arr)
        if not nxt:
            break
        cnt += 1
        lst = [nxt]
        change(nxt[0], nxt[1])
        for i in lst:
            arr[i[1]][i[0]] = 0

    # print(cnt)
    result.append(cnt)

for i in result:
    print(i)