# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18-stqI8oCFAZN&categoryId=AV18-stqI8oCFAZN&categoryType=CODE'

for _ in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    lst = [abs(i) for i in lst]
    min_ = min(lst)
    cnt = lst.count(min_)

    print('#{} {} {}'.format(_+1, min_, cnt))