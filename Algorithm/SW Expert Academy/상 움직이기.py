def find(x, y, visited, cnt):
    global min_

    if cnt > min_ or x < 0 or x >= N or y < 0 or y >= N or (x, y) in visited:
        return

    if (x, y) == (tx, ty):
        if cnt < min_:
            min_ = cnt
    else:
        visited.append((x, y))
        find(x+2, y-3, visited, cnt+1)
        visited.pop()
        visited.append((x,y))
        find(x+3, y-2, visited, cnt+1)
        visited.pop()
        visited.append((x, y))
        find(x-2, y-3, visited, cnt+1)
        visited.pop()
        visited.append((x, y))
        find(x-3, y-2, visited, cnt+1)
        visited.pop()
        visited.append((x, y))
        find(x+2, y+3, visited, cnt+1)
        visited.pop()
        visited.append((x, y))
        find(x+3, y+2, visited, cnt+1)
        visited.pop()
        visited.append((x, y))
        find(x-2, y+3, visited, cnt+1)
        visited.pop()
        visited.append((x, y))
        find(x-3, y+2, visited, cnt+1)
        visited.pop()


for _ in range(int(input())):
    N = int(input())
    n = N
    init = list(map(int, input().split()))
    x, y = init[:2]
    tx, ty = init[2:]
    min_ = 20 ** 2
    find(x, y, [], 0)

    print(f'#{_+1} {min_}')


"""
def find(x, y, cnt):
    global min_

    if cnt > min_ or x < 0 or x >= N or y < 0 or y >= N or visited[x][y]==False:
        return

    if (x, y) == (tx, ty):
        if cnt < min_:
            min_ = cnt
    else:
        visited.append((x, y))
        find(x+2, y-3, cnt+1)
        find(x+3, y-2, visited, cnt+1)
        find(x-2, y-3, visited, cnt+1)
        find(x-3, y-2, visited, cnt+1)
        find(x+2, y+3, visited, cnt+1)
        find(x+3, y+2, visited, cnt+1)
        find(x-2, y+3, visited, cnt+1)
        find(x-3, y+2, visited, cnt+1)


for _ in range(int(input())):
    N = int(input())
    n = N
    init = list(map(int, input().split()))
    x, y = init[:2]
    tx, ty = init[2:]
    min_ = 20 ** 2
    find(x, y, [], 0)
    visited = [[False for _ in range(N)] for __ in range(N)]
    print(f'#{_+1} {min_}')
"""
"""
def find(x, y, visited, cnt):
    global min_

    if cnt > min_ or x < 0 or x >= N or y < 0 or y >= N or (x, y) in visited:
        return

    if (x, y) == (tx, ty):
        if cnt < min_:
            min_ = cnt
    else:
        visited.append((x, y))
        find(x+2, y-3, visited, cnt+1)
        find(x+3, y-2, visited, cnt+1)
        find(x-2, y-3, visited, cnt+1)
        find(x-3, y-2, visited, cnt+1)
        find(x+2, y+3, visited, cnt+1)
        find(x+3, y+2, visited, cnt+1)
        find(x-2, y+3, visited, cnt+1)
        find(x-3, y+2, visited, cnt+1)


for _ in range(int(input())):
    N = int(input())
    n = N
    init = list(map(int, input().split()))
    x, y = init[:2]
    tx, ty = init[2:]
    min_ = 20 ** 2
    find(x, y, [], 0)

    print(f'#{_+1} {min_}')

"""