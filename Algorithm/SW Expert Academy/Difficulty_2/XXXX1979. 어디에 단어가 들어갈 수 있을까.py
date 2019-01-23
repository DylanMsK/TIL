# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq&categoryId=AV5PuPq6AaQDFAUq&categoryType=CODE'
import sys
sys.stdin = open('input.txt', 'r')

def f(arr, K):
    cnt = 0
    for i in arr:
        if sum(i) < K:
            continue
        temp = 0
        for j in i:
            if j:
                temp += 1
            else:
                temp = 0
            if temp == K:
                cnt += 1
            elif temp > K:
                cnt -= 1
                temp = 0
        print(cnt)
    return cnt

for _ in range(int(input())):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    cnt = f(arr, K)
    print(cnt)
    for i in range(K):
        for j in range(K):
            if i > j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    cnt += f(arr, K)

    print(cnt)
    # for i in range(N):
    #     if sum(arr[i]) < K:
    #         continue
    #     temp = 0
    #     for j in range(N):
    #         arr[i][j]
    # print(cnt)

    # print(f'#{_+1} {}')