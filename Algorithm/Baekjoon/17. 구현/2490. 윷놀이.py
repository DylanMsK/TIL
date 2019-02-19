# url = 'https://www.acmicpc.net/problem/2490'

import sys

for _ in range(3):
    lst = list(map(int, sys.stdin.readline().split()))
    sum_ = sum(lst)
    if sum_ > 3:
        print('E')
    elif sum_ > 2:
        print('A')
    elif sum_ > 1:
        print('B')
    elif sum_ > 0:
        print('C')
    else:
        print('D')