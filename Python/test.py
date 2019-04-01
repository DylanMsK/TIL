# lst = [1, 2, 3, 4]
# n = len(lst)
# for i in range(1 << n):
#     temp = [0] * n
#     cnt = 0
#     for j in range(n):
#         if i & 1 << j:
#             temp[cnt] = lst[j]
#             cnt += 1
#     if cnt == 3:
#         print(temp[:3])


# def combination(arr, r):
#     arr = sorted(arr)
#     def generate(chosen):
#         if len(chosen) == r:
#             print(chosen)
#             return

#         start = arr.index(chosen[-1]) + 1 if chosen else 0
#         for nxt in range(start, len(arr)):
#             chosen.append(arr[nxt])
#             generate(chosen)
#             chosen.pop()
#         return chosen
#     generate([])

# print(combination([5, 6, 7, 8, 9], 3))


# def merge(left, right):
#     result = []

#     while len(left) > 0 and len(right) > 0:
#         if left[0] > right[0]:
#             result.append(right.pop(0))
#         else:
#             result.append(left.pop(0))
    
#     if len(left) > 0:
#         result += left
#     if len(right) > 0:
#         result += right

#     return result


# def merge_sort(lst):
#     if len(lst) <= 1:
#         return lst

#     mid = len(lst) // 2
#     left = lst[:mid]
#     right = lst[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     return merge(left, right)


# lst = [69, 10, 30, 2, 16, 8, 31, 22]

# print(merge_sort(lst))


# def binary(string):

#     lst = []    
#     for i in range(0, len(string), 7):
#         temp = 0
#         for p, j in enumerate(range(6, -1, -1)):
#             if string[i + j] == '1':
#                 temp += 2 ** p
#         lst.append(temp)
#     return lst    

# string = '00000010001101'
# print(binary(string))

# lst = list(range(1, 11))

# for i in range(1 << 10):
#     temp = []
#     for j in range(10):
#         if i & 1 << j:
#             temp.append(lst[j])
#     if sum(temp) == 10:
#         print(temp)



# def backtrack(ary, k, n, sum_):
#     if sum_ > 10:
#         return

#     if k == n:
#         if sum_ == 10:
#             for i in range(n):
#                 if chk[i]:
#                     print(ary[i], end=' ')
#             print()
#         return
    
#     k += 1

#     chk[k-1] = 1
#     backtrack(ary, k, n, sum_+ary[k-1])
#     chk[k-1] = 0
#     backtrack(ary, k, n, sum_)

# arr = list(range(1, 11))
# chk = [0] * 10
# backtrack(arr, 0, 10, 0)
# aaa = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'

# def pre_order(node):
#     print(node, end=' ')
#     if edge[node][0]:
#         pre_order(edge[node][0])
#     if edge[node][1]:
#         pre_order(edge[node][1])

# def in_order(node):
#     if edge[node][0]:
#         pre_order(edge[node][0])
#     print(node, end=' ')
#     if edge[node][1]:
#         pre_order(edge[node][1])

# def post_order(node):
#     if edge[node][0]:
#         pre_order(edge[node][0])
#     if edge[node][1]:
#         pre_order(edge[node][1])
#     print(node, end=' ')


# N = int(input())
# lst = list(map(int, input().split()))
# edge = [[0, 0] for _ in range(N+2)]

# for i in range(0, 2*N, 2):
#     if edge[lst[i]][0]:
#         edge[lst[i]][1] = lst[i+1]
#     else:
#         edge[lst[i]][0] = lst[i+1]

# print('---pre_order---')
# pre_order(1)
# print()
# print('---in_order---')
# in_order(1)
# print()
# print('---post_order---')
# post_order(1)




# for _ in range(int(input())):
#     N, M = map(int, input().split())
#     lst = []
#     for i in range(N):
#         lst.append(int(input()))

#     temp = lst[:]
#     time = 0
#     while M > 0:
#         min_ = min(temp)
#         time += min_
#         M -= temp.count(min_)
#         # print(temp, M, time)
#         for i in range(N):
#             temp[i] -= min_
#             if temp[i] == 0:
#                 temp[i] = lst[i]
#     print(f'#{_+1} {time}')

def dfs(node, visited):
    visited.append(node)
    if node in edge:
        for i in edge[node]:
            if i not in visited:
                dfs(i, visited)


def bfs(node, visited):
    q = [node]

    while q:
        nxt = q.pop(0)
        visited.append(nxt)
        if nxt in edge:
            for i in edge[nxt]:
                if i in visited+q:
                    continue
                q.append(i)
        # print(visited)

init = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
init = list(map(int, init.split(' ')))
edge = {}
for i in range(0, len(init), 2):
    if init[i] in edge:
        edge[init[i]].append(init[i+1])
    else:
        edge[init[i]] = [init[i+1]]
        
visited = []
# dfs(1, visited)
bfs(1, visited)
print(visited)



