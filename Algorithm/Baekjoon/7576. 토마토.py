# url = 'https://www.acmicpc.net/problem/7576'

import sys


M, N = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while 1:
    

















# cnt = 0
# while 1:
#     temp = []
#     for y in range(N):
#         for x in range(M):
#             if arr[y][x] == 1:
#                 temp.append((y, x))
#     flag = True
#     for tup in temp:
#         y, x = tup[0], tup[1]
#         for diff in range(4):
#             nxt_y, nxt_x = y + dy[diff], x + dx[diff]
#             if (nxt_y not in range(N)) or (nxt_x not in range(M)):
#                 continue
#             if arr[nxt_y][nxt_x] == -1:
#                 continue
#             elif arr[nxt_y][nxt_x] == 0:
#                 flag = False
#                 arr[nxt_y][nxt_x] = 1
#         arr[y][x] = 2
    
#     if flag:
#         for row in arr:
#             if (0 in row):
#                 cnt = -1
#                 break
#         break

#     cnt += 1

# print(cnt)