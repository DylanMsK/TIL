# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PjMgaALgDFAUq&categoryId=AV5PjMgaALgDFAUq&categoryType=CODE'

for _ in range(int(input())):
    N = int(input())
    x, v = 0, 0
    for i in range(N):
        temp = input():
        if temp[0] == 1:
            v += int(temp[-1])
            x += v
        elif temp[0] == 2:
            if int(temp[-1]) > v:
                x += 
                v = 0
            v -= int(temp[-1])

    print(f'#{_+1} {}')