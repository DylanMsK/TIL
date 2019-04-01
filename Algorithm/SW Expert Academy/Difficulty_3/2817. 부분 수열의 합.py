# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7IzvG6EksDFAXB&categoryId=AV7IzvG6EksDFAXB&categoryType=CODE'

for tc in range(int(input())):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst = [i for i in lst if i <= K]
    cnt = 0
    for i in range(1 << len(lst)):
        sum_ = 0
        for j in range(len(lst)):
            if i & 1 << j:
                sum_ += lst[j]
                if sum_ > K:
                    break
        if sum_ == K:
            cnt += 1
    print('#{} {}'.format(tc+1, cnt))