# url = 'https://www.swexpertacademy.com/main/learn/course/lectureProblemViewer.do'

import sys
sys.stdin = open('min_max_input.txt', 'r')

T = int(input())
for _ in range(T):
    N = int(input())
    a = sorted(list(map(int, input().split())))
    print(f'#{_+1} {a[-1] - a[0]}')