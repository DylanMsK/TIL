# import sys
# sys.stdin = open('C:\\Users\\student\\Desktop\\github\\TIL\\Algorithm\\etc\\5일차\\합_input.txt', 'r')


def candidates(x_idx, nxt_y, N, candis):
    visited = [False] * N

    for idx in range(1, nxt_y):
        visited[x_idx[idx]] = True
    
    n = 0
    for idx in range(N):
        if visited[idx] == False:
            candis[n] = idx
            n += 1
    return n
    

def backtrack(x_idx, y, N, sum_):
    global arr, min_
    candis = [0] * N        # index가 들어감
    
    if y == N:
        if sum_ < min_:
            min_ = sum_
    
    else:
        y += 1
        n = candidates(x_idx, y, N, candis)

        if sum_ < min_:
            for i in range(n):
                x_idx[y] = candis[i]
                backtrack(x_idx, y, N, sum_+arr[y-1][x_idx[y]])


for _ in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    min_ = 100
    x_idx = [0] * (N+1)
    backtrack(x_idx, 0, N, 0)
    print(f'#{_+1} {min_}')