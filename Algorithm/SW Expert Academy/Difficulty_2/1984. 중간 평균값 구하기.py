# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pw_-KAdcDFAUq&categoryId=AV5Pw_-KAdcDFAUq&categoryType=CODE'

import sys
sys.stdin = open('input.txt', 'r')

for _ in range(int(input())):

    lst = list(map(int, input().split()))
    med_lst = sorted(lst)[1:-1]
    avg = sum(med_lst) / len(med_lst)


    print(f'#{_+1} {round(avg)}')