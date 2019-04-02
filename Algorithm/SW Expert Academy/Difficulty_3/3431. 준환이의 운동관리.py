# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWE_ZXcqAAMDFAV2&categoryId=AWE_ZXcqAAMDFAV2&categoryType=CODE'

for tc in range(int(input())):
    L, U, X = map(int, input().split())
    res = 0
    if X > U:
        res = -1
    elif X < L:
        res = L - X
    print(f'#{tc+1} {res}')