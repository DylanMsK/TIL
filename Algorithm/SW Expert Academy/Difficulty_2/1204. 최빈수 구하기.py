# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13zo1KAAACFAYh&categoryId=AV13zo1KAAACFAYh&categoryType=CODE'

import sys
sys.stdin = open('input.txt', 'r')


for _ in range(int(input())):
    T = int(input())
    lst = list(map(int, input().split()))
    # scores = {i: 0 for i in range(101)}
    # for i in lst:
    #     scores[i] += 1
    score = max(lst, key=lst.count)
    # max_ = 0
    # for score, cnt in scores.items():
    #     if cnt >= max_:
    #         max_ = cnt
    #         result = score
    # break
    print(f'#{T} {score}')
