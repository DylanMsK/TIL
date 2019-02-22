# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXGEbd6cjMDFAUo&categoryId=AWXGEbd6cjMDFAUo&categoryType=CODE'


for _ in range(int(input())):
    N = int(input())
    sum_ = 0
    lst = []
    for i in range(N):
        temp = int(input())
        sum_ += temp
        lst.append(temp)
    avg = sum_ // N
    cnt = 0
    for i in lst:
        if i > avg:
            cnt += i - avg

    print(f'#{_+1} {cnt}')