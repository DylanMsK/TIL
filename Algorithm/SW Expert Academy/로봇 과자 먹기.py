
def backtrack(idx, sum_):
    global min_

    idx += 1
    if sum_ >= min_:
        return
    else:
        if idx == N:
            if sum_ < min_:
                min_ = sum_
        else:
            rx, ry = robots[idx][0], robots[idx][1]
            for i in range(N):
                if visited[i] == 0:
                    sx, sy = snacks[i][0], snacks[i][1]
                    distance = abs(rx-sx) + abs(ry-sy)
                    visited[i] = 1
                    backtrack(i, sum_+distance)
                    visited[i] = 0


for _ in range(int(input())):
    N = int(input())
    r_init = list(map(int, input().split()))
    s_init = list(map(int, input().split()))
    robots = list((r_init[i], r_init[i+1]) for i in range(0, 2*N, 2))
    snacks = list((s_init[i], s_init[i+1]) for i in range(0, 2*N, 2))

    visited = [0] * N
    min_ = 9999999
    backtrack(-1, 0)

    print(f'#{_+1} {min_}')