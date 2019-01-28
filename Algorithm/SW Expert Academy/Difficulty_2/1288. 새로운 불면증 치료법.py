# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18_yw6I9MCFAZN&categoryId=AV18_yw6I9MCFAZN&categoryType=CODE'

for _ in range(int(input())):
    N = int(input())
    lst = list(str(i) for i in range(10))
    cnt = 0
    while len(lst):
        cnt += 1
        for i in str(N*cnt):
            if i in lst:
                lst.remove(i)
    print(f'#{_+1} {N*cnt}')