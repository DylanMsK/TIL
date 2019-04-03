# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWGsRbk6AQIDFAVW&categoryId=AWGsRbk6AQIDFAVW&categoryType=CODE'

for tc in range(int(input())):
    N = int(input())
    lst = input().split()
    if N % 2:
        a, b = lst[:N//2+1], lst[N//2+1:]
    else:
        a, b = lst[:N//2], lst[N//2:]
    res = []
    while len(a) > 0 and len(b) > 0:
        res.append(a.pop(0))
        res.append(b.pop(0))
    if len(a):
        res += a
    else:
        res += b
    print('#{} {}'.format(tc+1, ' '.join(res)))