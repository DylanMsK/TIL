# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE'

for _ in range(int(input())):
    days = int(input())
    lst = list(map(int, input().split()))
    
    sum_ = 0
    cnt = 0
    while lst:
        cnt += 1
        max_ = lst.index(max(lst))
        temp = sum(lst[:max_])
        sum_ += lst[max_] * max_ - temp
        lst = lst[max_+1:]

    print("#{} {}".format(_+1, sum_))