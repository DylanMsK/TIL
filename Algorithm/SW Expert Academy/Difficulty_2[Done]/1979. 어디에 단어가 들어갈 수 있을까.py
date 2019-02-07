# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq&categoryId=AV5PuPq6AaQDFAUq&categoryType=CODE'
import sys
sys.stdin = open('input.txt', 'r')


def check_K(arr):
    cnt = 0
    for i in arr:
        if sum(i) < K:
            continue
        sum_ = 0
        for j in i:
            if j:
                sum_ += j
            else:
                if sum_ == K:
                    cnt += 1
                sum_ = 0
        if sum_ == K:
            cnt += 1
    return cnt
        
for _ in range(int(input())):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]

    cnt = 0
    cnt += check_K(arr)
    for y in range(N):
        for x in range(N):
            if x > y:
                arr[y][x], arr[x][y] = arr[x][y], arr[y][x]
    cnt += check_K(arr)

    print(f'#{_+1} {cnt}')