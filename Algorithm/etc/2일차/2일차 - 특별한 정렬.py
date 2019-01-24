# url = 'https://www.swexpertacademy.com/main/learn/course/lectureProblemViewer.do'

import sys
sys.stdin = open('특이한_정렬_input.txt', 'r')

for _ in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    for idx in range(10):
        if idx % 2 == 0:
            max_ = idx
            for j in range(idx+1, N):
                if lst[j] >= lst[max_]:
                    max_ = j
            lst[idx], lst[max_] = lst[max_], lst[idx]
        else:
            min_ = idx
            for j in range(idx+1, N):
                if lst[j] <= lst[min_]:
                    min_ = j
            lst[idx], lst[min_] = lst[min_], lst[idx]
    print(f'#{_+1} {" ".join(str(i) for i in lst[:10])}')