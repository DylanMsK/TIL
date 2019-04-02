# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWGsRbk6AQIDFAVW&categoryId=AWGsRbk6AQIDFAVW&categoryType=CODE'

for tc in range(int(input())):
    N = int(input())
    lst = input().split()
    if N % 2:
        m = N // 2
        for i in range(1, N, 2):
            lst[i], lst[i+m] = lst[i+m], lst[i]
    else:
        m = N // 2
        for i in range(1, N+1, 2):
            print(lst)
            lst[i], lst[i-1+m] = lst[i-1+m], lst[i]
    # print(f'#{tc+1} {lst}')