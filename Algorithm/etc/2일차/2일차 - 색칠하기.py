# url = 'https://www.swexpertacademy.com/main/learn/course/lectureProblemViewer.do'

import sys
sys.stdin = open('색칠하기_input.txt', 'r')

for _ in range(int(input())):
    N = int(input())
    color_temp = [list(map(int, input().split())) for _ in range(N)]
    area = [[0]*10 for i in range(10)]

    for color in color_temp:
        for y in range(color[1], color[3]+1):
            for x in range(color[0], color[2]+1):
                area[y][x] += color[-1]

    cnt = 0
    for y in range(len(area)):
        for x in range(len(area[0])):
            if area[y][x] == 3:
                cnt += 1

    print(f'#{_+1} {cnt}')









# for _ in range(int(input())):
#     N = int(input())
#     color_temp = [list(map(int, input().split())) for _ in range(N)]
#     colors = {1: [], 2: []}
#     for color in color_temp:
#         if color[-1] == 1:
#             colors[1].append(color[:-1])
#         else:
#             colors[2].append(color[:-1])
#     sum_ = 0
#     for r in colors[1]:
#         for b in colors[2]:
#             row = col = 0
#             if b[0] in range(r[0], r[2]+1):
#                 if b[2] >= r[2]:
#                     row = r[2]+1 - b[0]
#                 else:
#                     row = b[2]+1 - b[0]
#             elif b[2] in range(r[0], r[2]+1):
#                 row = b[2]+1 - r[0]
#             if b[1] in range(r[1], r[3]+1):
#                 col = r[3]+1 - b[1]
#             elif b[3] in range(r[1], r[3]+1):
#                 col = b[3]+1 - r[1]
#             sum_ += row * col
#     print(f'#{_+1} {sum_}')