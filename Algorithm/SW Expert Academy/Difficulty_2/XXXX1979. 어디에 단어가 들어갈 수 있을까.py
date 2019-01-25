# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq&categoryId=AV5PuPq6AaQDFAUq&categoryType=CODE'
import sys
sys.stdin = open('input.txt', 'r')


def check_K(lst):
    sum_ = 0
    cnt = 0
    for i in lst:
        if i:
            sum_ += i
        else:
            if sum_ == K:
                cnt += 1
            sum_ = 0
    return cnt
        
for _ in range(int(input())):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]

    cnt = 0
    for i in arr:
        if sum(i) < K:
            continue
        cnt += check_K(i)
    for i in arr:
        print(i)
    print(cnt)
    for y in range(N):
        for x in range(N):
            if y != x:
                arr[y][x] = arr[x][y]
    print()
    for i in arr:
        print(i)
    # print(arr)
    for i in arr:
        if sum(i) < K:
            continue
        cnt += check_K(i)
    print(cnt)

    # print(f'#{_+1} {cnt}')
    break