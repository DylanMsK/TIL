# url = 'https://www.swexpertacademy.com/main/learn/course/lectureProblemViewer.do'
import sys
sys.stdin = open("전기버스_input.txt", 'r')

T = int(input())
for _ in range(T):
    K, N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    x, cnt = 0, 0
    while x < N:
        if x + K in nums:
            x += K
            cnt += 1
        else:
            if x + K >= N:
                break
            else:
                flag = 1
                for i in range(x+K-1, x, -1):
                    if i in nums:
                        x += i-x
                        cnt += 1
                        flag = 0
                        break
                if flag:
                    cnt = 0
                    break

    print(f'#{_+1} {cnt}')