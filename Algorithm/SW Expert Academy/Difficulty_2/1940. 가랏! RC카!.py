# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PjMgaALgDFAUq&categoryId=AV5PjMgaALgDFAUq&categoryType=CODE'

for _ in range(int(input())):
    N = int(input())
    x = v = 0
    for i in range(N):
        state = list(map(int, input().split()))

        if state[0] == 0:
            x += v
        else:
            if state[0] == 1:
                v += state[1]
                x += v
            else:
                v = max(0, v-state[1])
                x += v
        # print(x, v)
    print(f'#{_+1} {x}')