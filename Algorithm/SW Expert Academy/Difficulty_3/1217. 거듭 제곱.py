# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14dUIaAAUCFAYD&categoryId=AV14dUIaAAUCFAYD&categoryType=CODE'

def my_pow(N, M):
    if M == 1:
        return N
    return N * my_pow(N, M-1)

for _ in range(10):
    t = input()
    N, M = map(int, input().split())
    print(f'#{t} {my_pow(N, M)}')
