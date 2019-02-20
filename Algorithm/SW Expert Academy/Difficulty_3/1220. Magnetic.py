# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14hwZqABsCFAYD&categoryId=AV14hwZqABsCFAYD&categoryType=CODE'
import sys
sys.stdin = open('C:\\Users\\student\\Desktop\\github\\TIL\\Algorithm\\SW Expert Academy\\Difficulty_3\\input.txt', 'r')

for _ in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    cnt = 0
    for x in range(N):
        min_, max_ = 0, N-1
        for y in range(max_+1):
            if arr[y][x] == 1:
                min_ = y
                break
        for y in range(max_, min_-1, -1):
            if arr[y][x] == 2:
                max_ = y
                break

        flag = 1
        for y in range(min_+1, max_+1):
            if arr[y][x]:
                if arr[y][x] == 1:
                    flag = 1
                elif flag:
                    cnt += 1
                    flag = 0
    print(f'#{_+1} {cnt}')
