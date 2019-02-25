# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14zIwqAHwCFAYD&categoryId=AV14zIwqAHwCFAYD&categoryType=CODE'

import sys
sys.stdin = open('input.txt', 'r')

def insert(lst, x, y, s):
    lst = lst[:x] + s + lst[x:]
    return lst


for _ in range(10):
    N = int(input())
    lst = list(map(int, input().split()))
    num_cmd = int(input())
    cmd = input().split()
    idx = 0
    while  idx < len(cmd):
        if cmd[idx] == 'I':
            x = int(cmd[idx+1])
            y = int(cmd[idx+2])
            s = cmd[idx+3:idx+3+y]
            lst = insert(lst, x, y, s)
            idx += 3 + y

    print(f'#{_+1} {" ".join([str(i) for i in lst[:10]])}')