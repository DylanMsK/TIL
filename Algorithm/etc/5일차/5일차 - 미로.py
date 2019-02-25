# import sys
# sys.stdin = open('C:\\Users\\student\\PycharmProjects\\TT\\python5\\미로_input.txt', 'r')

# def find_in_out(arr):
#     end = [0, 0]
#     start = [0, 0]
#     eflag = 0
#     sflag = 0
#     for y in range(len(arr)):
#         for x in range(len(arr[0])):
#             if arr[y][x] == '2':
#                 start[0], start[1] = x, y
#                 sflag = 1
#             elif arr[y][x] == '3':
#                 end[0], end[1] = x, y
#                 eflag = 1
#             if eflag and sflag:
#                 return start, end


# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# for _ in range(int(input())):
#     N = int(input())
#     arr = [input() for i in range(N)]
#     start, end = find_in_out(arr)
#     now = start
#     stack = [now]
#     visited = [now]
#     res = 0
#     while 1:
#         flag = False
#         for diff in range(4):
#             nxt_x, nxt_y = stack[-1][0] + dx[diff], stack[-1][1] + dy[diff]
#             if 0 <= nxt_x < N and 0 <= nxt_y < N:
#                 if [nxt_x, nxt_y] == end:
#                     res = 1
#                     break
#                 if arr[nxt_y][nxt_x] == '0' and [nxt_x, nxt_y] not in visited:
#                     flag = True
#                     break
#             else:
#                 continue
#         if res:
#             break

#         if flag:
#             now = [nxt_x, nxt_y]
#             stack.append(now)
#             visited.append(now)
#         else:
#             now = stack.pop()

#         if not stack:
#             break

#     print(f'#{_+1} {res}')



# 재귀

def DFSr(x, y):
    global res
    if not 0 <= x < N or not 0 <= y < N or res or arr[y][x] == '1':
        return
    
    if arr[y][x] == '3':
        res = 1
        return
    
    arr[y][x] = '1'
    DFSr(x, y+1)
    DFSr(x, y-1)
    DFSr(x+1, y)
    DFSr(x-1, y)


for _ in range(int(input())):
    N = int(input())
    arr = [list(input()) for i in range(N)]
    start = (0, 0)
    for y in range(N):
        for x in range(N):
            if arr[y][x] == '2':
                start = (x, y)
                break
    res = 0
    DFSr(start[0], start[1])
    print(f'#{_+1} {res}')