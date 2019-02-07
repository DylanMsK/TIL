# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpoFaAS4DFAUq&categoryId=AV5PpoFaAS4DFAUq&categoryType=CODE'

import sys
sys.stdin = open('input.txt', 'r')


for _ in range(int(input())):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if N > M:
        a, b = b, a
        N, M = M, N

    max_ = 0
    for i in range(M-N+1):
        sum_ = 0
        for j in range(N):
            sum_ += a[j] * b[i+j]
        if sum_ > max_:
            max_ = sum_

    print(f'#{_+1} {max_}')