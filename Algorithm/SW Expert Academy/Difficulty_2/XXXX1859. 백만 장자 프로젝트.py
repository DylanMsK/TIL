# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE'


for _ in range(int(input())):
    days = int(input())
    lst = list(map(int, input().split()))

    idx, temp_idx = 0, 0
    temp =[]
    sum_ = 0
    while 1:
        if lst[temp_idx] <= lst[temp_idx+1]:
            temp.append(lst[temp_idx])
            temp_idx += 1
        else:
            sum_ = sum(temp)


    for i in range(len(lst)):
        idx = i
        now = lst[idx]
        while 1:
            idx += 1
            if lst[idx]


    print(f'#{_+1} {}')