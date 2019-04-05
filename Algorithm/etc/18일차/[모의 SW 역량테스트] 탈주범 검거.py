import sys
sys.stdin = open('input.txt', 'r')


pipe_to = {1: ['right', 'down', 'left', 'up'],
        2: ['up', 'down'],
        3: ['right', 'left'],
        4: ['up', 'right'],
        5: ['right', 'down'],
        6: ['left', 'down'],
        7: ['up', 'left']}
pipe_from = {1: ['right', 'down', 'left', 'up'],
        2: ['up', 'down'],
        3: ['right', 'left'],
        4: ['down', 'left'],
        5: ['left', 'up'],
        6: ['right', 'up'],
        7: ['down', 'right']}

for tc in range(int(input())):
    N, M, y, x, L = map(int, input().split())
    base = [list(map(int, input().split())) for _ in range(N)]
    
    visited = [(x, y)]
    stack = [(x, y, 1)]
    while stack:
        # print(stack[-1])
        x, y, time = stack.pop()
        if time == L:
            continue

        now = base[y][x]
        directions = pipe_to[now]
        for direction in directions:
            nxt_x, nxt_y = x, y
            if direction == 'right':
                nxt_x += 1
            elif direction == 'down':
                nxt_y += 1
            elif direction == 'left':
                nxt_x -= 1
            else:
                nxt_y -= 1

            if not 0 <= nxt_x < M or not 0 <= nxt_y < N or not base[nxt_y][nxt_x]:
                continue
            if direction in pipe_from[base[nxt_y][nxt_x]] and (nxt_x, nxt_y) not in visited:
                visited.append((nxt_x, nxt_y))
                stack.append((nxt_x, nxt_y, time+1))
    print(visited)
    print('#{} {}'.format(tc+1, len(visited)))