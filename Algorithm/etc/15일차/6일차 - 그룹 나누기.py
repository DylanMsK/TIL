def dfs(node, visited):
    visited.append(node)
    for i in jos[node]:
        if i not in visited:
            dfs(i, visited)


def make_set(x):
    p[x] = x


def find_set(x):
    if x == p[x]:
        return x
    return find_set(x)


def union_set(x, y):
    a = find_set(x)
    b = find_set(y)
    p[a] = b
    for i in range(len(p)):
        if p[i] == a:
            p[i] = b


for tc in range(int(input())):
    N, M = map(int, input().split())
    # jos = {i: [] for i in range(1, N+1)}
    # temp = list(map(int, input().split()))
    # for i in range(0, len(temp), 2):
    #     jos[temp[i]].append(temp[i+1])
    #     jos[temp[i+1]].append(temp[i])

    # jo_lst = list(jos.keys())
    # cnt = 0
    # while jo_lst:
    #     visited = []
    #     dfs(jo_lst[0], visited)
    #     for i in visited:
    #         jo_lst.remove(i)
    #     cnt += 1

    jos = list(map(int, input().split()))
    p = [0] * N
    for i in range(N):
        make_set(i)
    print(p)
    print(jos)
    cnt = 0
    for i in range(0, len(jos), 2):
        union_set(jos[i]-1, jos[i+1]-1)
    

    print('#{} {}'.format(tc+1, len(set(p))))