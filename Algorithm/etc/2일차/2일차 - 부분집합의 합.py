# url = 'https://www.swexpertacademy.com/main/learn/course/lectureProblemViewer.do'

import sys
sys.stdin = open('부분집합의_합_input.txt', 'r')

arr = list(range(1, 13))
for _ in range(int(input())):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1 << 12):
        temp = []
        for j in range(12):
            if i & (1 << j):
                temp.append(arr[j])
        if len(temp) == N and sum(temp) == K:
            cnt += 1
    print(f'#{_+1} {cnt}')