def backtrack(work, tot, visited):
    global min_

    work += 1
    if tot >= min_:
        return

    if len(visited) == N+1:
        distance = abs(visited[-1][0]-home[0]) + abs(visited[-1][1]-home[1])
        tot += distance
        if tot < min_:
            min_ = tot
    else:
        for i in range(N):
            if orders[i] == 0:
                orders[i] = 1
                distance = abs(visited[-1][0]-works[i][0]) + abs(visited[-1][1]-works[i][1])
                tot += distance
                visited.append(works[i])
                backtrack(i, tot, visited)
                # visited = visited[:-1]
                visited.pop()
                tot -= distance
                orders[i] = 0



for _ in range(int(input())):
    N = int(input())
    init = list(map(int, input().split()))
    company = (init[0], init[1])
    home = (init[2], init[3])
    works = [(init[i], init[i+1]) for i in range(4, 2*N+4, 2)]

    orders = [0] * N
    min_ = 200 * (N+2)
    backtrack(-1, 0, [company])

    print(f'#{_+1} {min_}')