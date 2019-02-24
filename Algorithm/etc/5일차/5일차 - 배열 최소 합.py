import sys
sys.stdin = open('/Users/dylan/Desktop/github/TIL/Algorithm/etc/5일차/합_input.txt', 'r')

def find_idx(x_idx, y):
    promissing = [False] * N
    for idx in range(N):
        if x_idx[idx] == -1:
            promissing[idx] = True
    return promissing




def backtrack(x_idx, y):
    global min_, arr, N

    if y == N:
        print(x_idx)
    else:
        promissing = find_idx(x_idx, y)      # 처음: x_idx = [-1, -1, -1], y = 0
        y += 1
        for idx in range(N):
            if promissing[idx]:
                x_idx[idx] = idx
                backtrack(x_idx, y)

for _ in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    min_ = 100
    backtrack([-1]*N, 0)
    break


