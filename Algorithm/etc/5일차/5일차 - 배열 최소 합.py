import sys
sys.stdin = open('C:\\Users\\student\\PycharmProjects\\TT\\python5\\합_input.txt', 'r')

def find_next(arr, y, N, c):
    in_perm = [False] * N

    for i in range(1, y):
        in_perm[arr[i]] = True

    n = 0
    for i in range(1, N+1):
        if in_perm[i-1] == False:
            c[n] = i
            n += 1
    return n


def backtrack(arr, y, N):
    global min_
    c = [0] * N     # 노드들의 value

    if y == N:
        if sum(c) < min_:
            min_ = sum(c)
        # sum이 들어올 곳
        # sum < minvalue: minvalue = sum 업데이트
        # for i in range(1, y+1):
        #     print(c)
    else:
        y += 1
        # 다음 자식 노드를 찾음
        n = find_next(arr, y, N, c)
        # 자식 노드를 돌면서

        for i in range(n):
            # 다음 자식 노드들을 데리고 backtracking을 이어서 함 - sum이 계속 누적되어서 가야함
            if sum(c) > min_:
                return
            backtrack(arr, y, N)



for _ in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    min_ = 100
    backtrack([0], 0, N)
    break


