"""def find(x, y, visited, cnt):
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

    print('#{} {}'.format(_+1, min_))"""


dx, dy = (2, 3, 3, 2, -2, -3, -3, -2), (-3, -2, 2, 3, 3, 2, -2, -3)

for tc in range(int(input())):
    N = int(input())
    x, y, tx, ty = map(int, input().split())
    min_ = float('Inf')
    q = [[(x, y)]]
    while q:
        visited = q.pop(0)

        if len(visited)-1 > min_:
            continue

        if visited[-1] == (tx, ty):
            if len(visited)-1 < min_:
                min_ = len(visited)-1
            continue

        x, y = visited[-1][0], visited[-1][1]
        for diff in range(8):
            if 0 <= x + dx[diff] < N and 0 <= y + dy[diff] < N and (x+dx[diff], y+dy[diff]) not in visited:
                nxt = visited[:]
                nxt.append((x+dx[diff], y+dy[diff]))
                q.append(nxt)

    print('#{} {}'.format(tc+1, min_))


