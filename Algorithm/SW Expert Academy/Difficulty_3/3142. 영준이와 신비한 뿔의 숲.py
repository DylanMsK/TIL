# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV_6xWk6sbADFAWS&categoryId=AV_6xWk6sbADFAWS&categoryType=CODE'

for tc in range(int(input())):
    N, M = map(int, input().split())
    y = N - M
    x = N - (2 * y)
    print(f'#{tc+1} {x} {y}')