# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GKs06AU0DFAXB&categoryId=AV7GKs06AU0DFAXB&categoryType=CODE'
def promissing(x_idx, y, N, candidates):
    visited = [0] * N

    for idx in range(1, y):
        visited[x_idx[idx]] = 1
    
    cross = [0] * N
    for idx in range(1, y):
        x1 = x_idx[idx] - abs(y-idx)
        x2 = x_idx[idx] + abs(y-idx)
        if 0 <= x1 < N:
            cross[x1] = 1
        if 0 <= x2 < N:
            cross[x2] = 1

    promiss = [0] * N
    for i in range(N):
        if visited[i] or cross[i]:
            promiss[i] = 1

    n = 0
    for idx in range(N):
        if promiss[idx] == 0:
            candidates[n] = idx
            n += 1
    return n


def DFS(x_idx, y, N):
    global cnt
    candidates = [0] * N

    if y == N:
        # print(x_idx)
        cnt += 1

    else:
        y += 1
        n = promissing(x_idx, y, N, candidates)
        for i in range(n):
            x_idx[y] = candidates[i]
            DFS(x_idx, y, N)


def queen(N):
    x_idx = [-1] * (N+1)
    DFS(x_idx, 0, N)


for _ in range(int(input())):
    N = int(input())
    cnt = 0
    queen(N)
    print(f'#{_+1} {cnt}')