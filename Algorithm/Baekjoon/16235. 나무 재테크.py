def spring_summer():
    global bab, trees, N
    for x in range(N):
        for y in range(N):
            if trees[y][x]:
                trees[y][x].sort()

                q = trees[y][x]
                get_old = []
                while q:
                    tree = q.pop(0)
                    if tree <= bab[y][x]:
                        bab[y][x] -= tree
                        get_old.append(tree+1)
                    else:
                        q.append(tree)
                        break

                for tree in q:
                    bab[y][x] += tree // 2

                trees[y][x] = get_old        


def fall_winter():
    global bab, s2d2, trees, N
    dx = (1, 1, 1, 0, -1, -1, -1, 0)
    dy = (-1, 0, 1, 1, 1, 0, -1, -1)
    for x in range(N):
        for y in range(N):
            bab[y][x] += s2d2[y][x]
            if trees[y][x]:
                for tree in trees[y][x]:
                    if tree % 5 == 0:
                        for diff in range(8):
                            if 0 <= x+dx[diff] < N and 0 <= y+dy[diff] < N:
                                trees[y+dy[diff]][x+dx[diff]].append(1)


def winter():
    global bab, trees, N
    for x in range(N):
        for y in range(N):
            bab[y][x] += s2d2[y][x]


N, M, K = map(int, input().split())
s2d2 = [list(map(int, input().split())) for _ in range(N)]
tree_init = [tuple(map(int, input().split())) for _ in range(M)]

# K년 후 양분
bab = [[5]*N for _ in range(N)]

# 나무 초기화
trees = [[[] for _ in range(N)] for __ in range(N)]
for tree in tree_init:
    trees[tree[0]-1][tree[1]-1].append(tree[2])

# 나무 성장
for year in range(K):
    spring_summer()
    fall_winter()
    # winter()

sum_ = 0
for y in range(N):
    for x in range(N):
        sum_ += len(trees[y][x])
print(sum_)