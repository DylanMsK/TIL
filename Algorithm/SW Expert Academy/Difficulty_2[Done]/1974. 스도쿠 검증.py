# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq&categoryId=AV5Psz16AYEDFAUq&categoryType=CODE'

import sys
sys.stdin = open('input.txt', 'r')

for _ in range(int(input())):
    arr = [list(map(int, input().split())) for _ in range(9)]

    flag = 1
    for i in range(9):
        row = []
        col = []
        for j in range(9):
            row.append(arr[i][j])
            col.append(arr[j][i])
        if (len(set(row)) != 9) | (len(set(col)) != 9):
            flag = 0
            break
    
    if flag:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if len(set(arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3])) != 9:
                    flag = 0
                    break
            if not flag:
                break
    print(f'#{_+1} {flag}')