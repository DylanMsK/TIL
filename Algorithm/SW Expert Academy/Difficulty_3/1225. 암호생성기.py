# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14uWl6AF0CFAYD&categoryId=AV14uWl6AF0CFAYD&categoryType=CODE'

for _ in range(10):
    tc = input()
    lst = list(map(int, input().split()))
    flag = False
    while lst[-1] != 0:
        temp = 1
        while temp <= 5:
            last = lst[0] - temp
            lst = lst[1:] + [last]
            if last <= 0:
                lst[-1] = 0
                flag = True
                break
            temp += 1
        if flag:
            break
    print(f'#{tc} {" ".join(list(str(i) for i in lst))}')