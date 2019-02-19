# url = 'https://www.acmicpc.net/problem/10871'
import sys

N, X = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
# for i in lst:
#     if i < X:
#         print(i, end=' ')
# print()


print(' '.join([str(i) for i in lst if i < X]))