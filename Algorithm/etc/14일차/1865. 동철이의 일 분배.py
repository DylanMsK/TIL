def promiss(x_idx, y, N, candis):
    visited = [0] * N

    # 이미 한 작업
    for idx in range(1, y):
        visited[x_idx[idx]] = 1

    n = 0
    for idx in range(N):
        if visited[idx] == 0:
            candis[n] = idx
            n += 1
    return n
    

def backtrack(x_idx, y, N, prob):
    global max_
    candis = [0] * N
    if prob == 0 or prob < max_:
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






def best_percent(depth, percent):
    global best
    depth += 1
    if depth == N:
        if best < percent:
            best = percent

    elif best > percent:
        return

    elif percent == 0:
        return

    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                best_percent(depth, percent*percent_arr[depth][i]*0.01)
                visited[i] = 0

 
TC = int(input())
for t in range(1, TC+1):
    N = int(input())
    percent_arr = []
    for _ in range(N):
        percent_arr.append(list(map(int, input().split())))
    visited = [0] * N
 
    best = -1
    best_percent(-1, 1)
    print(f"#{t} %f" %round(best*100, 6))