# url = 'https://www.swexpertacademy.com/main/learn/course/lectureProblemViewer.do'
import sys
sys.stdin = open('구간합_input.txt', 'r')

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    sum_ = []
    for i in range(N-M+1):
        sum_.append(sum(a[i:i+M]))
    sum_.sort()

    print(f'#{_+1} {sum_[-1]-sum_[0]}')