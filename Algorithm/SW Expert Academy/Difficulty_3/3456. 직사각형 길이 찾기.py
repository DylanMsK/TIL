# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWFPmsqqALwDFAV0&categoryId=AWFPmsqqALwDFAV0&categoryType=CODE'

for tc in range(int(input())):
    lst = list(map(int, input().split()))
    if len(set(lst)) == 2:
        res = sum(set(lst)) * 2 - sum(lst)
    else:
        res = lst[0]
    print(f'#{tc+1} {res}')