# url = 'https://www.acmicpc.net/problem/15552'

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(a+b)+'\n')