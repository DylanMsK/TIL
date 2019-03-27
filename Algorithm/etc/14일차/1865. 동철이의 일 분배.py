def promiss(x_idx, y, N, candis):
    visited = [0] * N

    # 이미 한 작업
    for idx in range(1, y):
        visited[x_idx[idx]] = 1

    # 확률이 0인거 제거
    for idx in range(N):
        if work[y-1][idx] == 0:
            visited[idx] = 1
    
    n = 0
    for idx in range(N):
        if visited[idx] == 0:
            candis[n] = idx
            n += 1
    return n
    
def backtrack(x_idx, y, N, prob):
    global max_
    candis = [0] * N
    if prob < max_:
        return
    if y == N:
        if prob > max_:
            max_ = prob
    else:
        y += 1
        n = promiss(x_idx, y, N, candis)
        for i in range(n):
            x_idx[y] = candis[i]
            backtrack(x_idx, y, N, prob * work[y-1][x_idx[y]])

for _ in range(int(input())):
    N = int(input())
    work = []
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(len(temp)):
            temp[j] /= 100
        work.append(temp)

    max_ = 0
    x_idx = [-1] * (N+1)
    backtrack(x_idx, 0, N, 1)

    print('#%d %.6f'%(_+1, max_*100)) 