# url = 'https://www.swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AWhVVhNaS8EDFAW_&contestProbId=AV14ABYKADACFAYh&probBoxId=AWjlXu8a4U0DFAVT+&type=PROBLEM&problemBoxTitle=7%EC%9D%BC%EC%B0%A8%282%EC%9B%9413%EC%9D%BC%29&problemBoxCnt=++1+'

import sys
sys.stdin = open('/Users/dylan/Desktop/github/TIL/Algorithm/etc/4일차/input.txt', 'r')

for _ in range(10):
    TC = input()
    arr = [input().split() for i in range(100)]
    
    x, y = arr[-1].index('2'), 99
    dx = [1, -1, 0]
    dy = [0, 0, -1]
    while 1:
        for diff in range(3):
            next_x, next_y = x + dx[diff], y + dy[diff]
            if (next_x < 0) or (next_x > 99):
                continue
            if arr[next_y][next_x] == '1':
                arr[y][x] = '2'
                x, y = next_x, next_y
                break
        if next_y == 0:
            print(f'#{TC} {next_x}')
            break