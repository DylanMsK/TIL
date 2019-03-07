# url = 'https://www.acmicpc.net/problem/2636'

def DFS(x, y):
    if not 0 <= x < row+2 or not 0 <= y < col+2 or arr[y][x] == 2:
        return
    if arr[y][x] == 1:
        arr[y][x] = -1
        return
    if arr[y][x] == 0:
        arr[y][x] = 2
        DFS(x, y+1)
        DFS(x+1, y)
        DFS(x-1, y)
        DFS(x, y-1)


col, row = map(int, input().split())
arr = [[0] + list(map(int, input().split())) + [0] for i in range(col)]
arr.insert(0, [0] * (row+2))
arr.append([0] * (row+2))

result = []
while 1:
    x, y = 0, 0
    cnt = 0
    DFS(x, y)

    for y in range(col+2):
        for x in range(row+2):
            if arr[y][x] == -1:
                cnt += 1
                arr[y][x] = 0
            elif arr[y][x] == 2:
                arr[y][x] = 0

    if cnt == 0:
        break
    result.append(cnt)

print(len(result))
print(result[-1])