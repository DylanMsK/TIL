def backtrack(v, sum_):
    global min_

    v += 1

    if sum_ >= min_:
        return

    if v == N:
        if sum_ < min_:
            min_ = sum_
    
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                backtrack(v, sum_+arr[v][i])
                visited[i] = 0


for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_ = 99 * N
    visited = [0] * N
    backtrack(-1, 0)
    print('#{} {}'.format(tc+1, min_))
