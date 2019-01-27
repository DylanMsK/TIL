# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq&categoryId=AV5Pq-OKAVYDFAUq&categoryType=CODE'

import sys
sys.stdin = open('input.txt', 'r')


for _ in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]

    brr = crr = drr = arr[::]
    for y in range(N):
        for x in range(N):
            brr[y][x] = brr[x][y]

    for i in arr:
        print(i)

    print()
    for i in brr:
        print(i)

    # print(f'#{_+1}')
    break