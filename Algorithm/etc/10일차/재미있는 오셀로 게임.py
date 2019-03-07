def init():
    arr[N//2-1][N//2-1] = 2
    arr[N//2-1][N//2] = 1
    arr[N//2][N//2-1] = 1
    arr[N//2][N//2] = 2


def put(init_x, init_y, S):
    arr[init_y-1][init_x-1] = S
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]
    for diff in range(8):
        visited = []
        x, y = init_x-1, init_y-1
        while 1:
            x, y = x + dx[diff], y + dy[diff]
            if not 0 <= x < N or not 0 <= y < N:
                break

            if arr[y][x] == 0:
                break

            if arr[y][x] == S:
                for v in visited:
                    arr[v[1]][v[0]] = S
                break

            visited.append((x, y))


for _ in range(int(input())):
    N, M = map(int, input().split())
    arr = [[0] * N for i in range(N)]
    init()

    for cmd in range(M):
        x, y, S = map(int, input().split())
        put(x, y, S)

    B, W = 0, 0
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 1:
                B += 1
            elif arr[y][x] == 2:
                W += 1

    print('#{} {} {}'.format(_+1, B, W))