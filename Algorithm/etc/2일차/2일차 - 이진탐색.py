# url = 'https://www.swexpertacademy.com/main/learn/course/lectureProblemViewer.do'

import sys
sys.stdin = open('이진탐색_input.txt', 'r')


def binary(X):
    cnt = 0
    l, r = 1, P
    c = 0
    while X != c:
        cnt += 1
        c = int((l + r) / 2)
        if X >= c:
            l = c
            continue
        r = c
    return cnt


for _ in range(int(input())):
    P, A, B = map(int, input().split())
    cntA = binary(A)
    cntB = binary(B)
    if cntA < cntB:
        res = 'A'
    elif cntA > cntB:
        res = 'B'
    else:
        res = 0
    print(f'#{_+1} {res}')