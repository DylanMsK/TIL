# import sys
# sys.stdin = open('C:\\Users\\student\\Desktop\\github\\TIL\\Algorithm\\etc\\11일차\\input.txt', 'r')

def find(arr, K):
    cnt = 0
    for i in range(N):
        row = 0
        for j in range(N):
            if arr[i][j]:
                row += 1
                if j == N-1 and row == K:
                    cnt += 1
            else:
                if row == K:
                    cnt += 1
                row = 0
    return cnt


def T(arr):
    for y in range(N):
        for x in range(N):
            if x > y:
                arr[y][x], arr[x][y] = arr[x][y], arr[y][x]
    return arr


for _ in range(int(input())):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    cnt = find(arr, K)
    arr = T(arr)
    cnt += find(arr, K)
    print("#{} {}".format(_+1, cnt))