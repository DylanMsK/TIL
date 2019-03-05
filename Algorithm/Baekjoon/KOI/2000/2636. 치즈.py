# url = 'https://www.acmicpc.net/problem/2636'
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(x, y):
    if not 0 <= x < row or not 0 <= y < col:
        return
    if arr[y][x] == 2:
        return
    elif arr[y][x] == 1:
        arr[y][x] = -1
    elif arr[y][x] == -1:
        return

    arr[y][x] = 2
    DFS(x, y+1)
    # return
    DFS(x+1, y)
    DFS(x-1, y)
    DFS(x, y-1)





def find_edge(arr):
    for y in range(col):
        for x in range(row):
            if arr[y][x] == 0:
                return x, y
    return None


col, row = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(col)]
x, y = find_edge(arr)
# print(x, y)
# DFS(x, y)
for i in arr:
    print(i)
# time = 0