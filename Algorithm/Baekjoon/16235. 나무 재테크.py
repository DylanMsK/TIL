# N, M, K = map(int, input().split())
# s2d2 = [[0] + list(map(int, input().split())) for _ in range(N)]
# s2d2 = [[0]*(N+1)] + s2d2
# init_tree = [tuple(map(int, input().split())) for _ in range(M)]

# arr = [[0]*(N+1) if i == 0 else [0]+[5]*N for i in range(N+1)]
# trees = {k: [] for k in range(1, N**2+1)}
# for tree in init_tree:
#     trees[N*(tree[0]-1) + tree[1]].append(tree[2])

# for year in range(K):
#     # 봄
#     idx = 0
#     for y in range(1, N+1):
#         for x in range(1, N+1):
#             idx += 1
#             if trees[idx]:
#                 nxt = 0
#                 for age in range(len(trees[idx])-1, -1, -1):
#                     if arr[y][x] - trees[idx][age] >= 0:
#                         arr[y][x] -= trees[idx][age]
#                         trees[idx][age] += 1
#                     else:
#                         nxt = age+1
#                         break
#                 remove_tree = trees[idx][:nxt]
#                 trees[idx] = trees[idx][nxt:]
#                 for i in remove_tree:
#                     arr[y][x] += i//2

#     # 가을
#     idx = 0
#     diff = [-5, 1, 5, -1, -4, 6, 4, -6]
#     dx = (0, 1, 0, -1, 1, 1, -1, -1)
#     dy = (-1, 0, 1, 0, -1, 1, 1, -1)
#     for y in range(1, N+1):
#         for x in range(1, N+1):
#             idx += 1
#             if trees[idx]:
#                 for tree in trees[idx]:
#                     if tree % 5 == 0:
#                         for i in range(8):
#                             if 0 < idx + diff[i] <= N**2 and 0 < x+dx[i] <= N and 0 < y+dy[i] <= N:
#                                 trees[idx+diff[i]].append(1)
    
#     # 겨울
#     for y in range(1, N+1):
#         for x in range(1, N+1):
#             arr[y][x] += s2d2[y][x]

# sum_ = 0
# for tree in trees:
#     sum_ += len(trees[tree])

# print(sum_)


def spring_spring():
    global bab, trees, N
    for y in range(N):
        for x in range(N):
            if trees[y][x]:
                trees[y][x].sort()
                # 나무에 양분주고 못먹는애 찾기
                idx = len(trees[y][x])
                for tree in range(idx):
                    if trees[y][x][tree] <= bab[y][x]:
                        bab[y][x] -= trees[y][x][tree]
                        trees[y][x][tree] += 1
                    else:
                        idx = tree
                        break
                # 죽은나무 양분 추가
                for tree in trees[y][x][idx:]:
                    bab[y][x] += tree // 2


def fall():
    global bab, trees, N
    dx = (1, 1, 1, 0, -1, -1, -1, 0)
    dy = (-1, 0, 1, 1, 1, 0, -1, -1)
    for y in range(N):
        for x in range(N):
            if trees[y][x]:
                for tree in trees[y][x]:
                    if tree % 5 == 0:
                        for diff in range(8):
                            if 0 <= x+dx[diff] < N and 0 <= y+dy[diff] < N:
                                trees[y+dy[diff]][x+dx[diff]].append(1)


def winter():
    global bab, trees, N
    for y in range(N):
        for x in range(N):
            bab[y][x] += s2d2[y][x]



N, M, K = map(int, input().split())
s2d2 = [list(map(int, input().split())) for _ in range(N)]
tree_init = [tuple(map(int, input().split())) for _ in range(M)]

# K년 후 양분
bab = [[5]*N for _ in range(N)]
# for y in range(N):
#     for x in range(N):
#         bab[y][x] += K * s2d2[y][x]

# 나무 초기화
trees = [[[] for _ in range(N)] for __ in range(N)]
for tree in tree_init:
    trees[tree[0]-1][tree[1]-1].append(tree[2])

# 나무 성장
for year in range(K):
    spring_spring()
    fall()
    winter()

sum_ = 0
for y in range(N):
    for x in range(N):
        sum_ += len(trees[y][x])
print(sum_)