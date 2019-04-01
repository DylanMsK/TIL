# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWl0ZQ8qn7UDFAXz&categoryId=AWl0ZQ8qn7UDFAXz&categoryType=CODE'

one = 'ADOPQR'
two = 'B'

for tc in range(int(input())):
    res = [0]*3
    a, b = input().split()
    flag = 0
    if len(a) == len(b):
        for i, j in zip(a, b):
            if i in one:
                res[1] += 1
            elif i in two:
                res[2] += 1
            else:
                res[0] += 1

            if j in one:
                res[1] -= 1
            elif j in two:
                res[2] -= 1
            else:
                res[0] -= 1
        if res.count(0) == 3:
            flag = 1

    if flag:
        print('#{} SAME'.format(tc+1))
    else:
        print('#{} DIFF'.format(tc+1))
