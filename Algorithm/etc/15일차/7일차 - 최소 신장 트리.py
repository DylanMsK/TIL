def make_set(v):
    p[v] = v


def find(v):
    if v != p[v]:
        p[v] = find(p[v])
    return p[v]


def union(v, u):
    root1 = find(v)
    root2 = find(u)

    p[root1] = root2


for tc in range(int(input())):
    V, E = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x: x[2])

    p = {}
    mst = []
    cost = 0
    for i in range(V+1):
        make_set(i)
    
    for edge in edges:
        u, v, wt = edge
        if find(u) != find(v):
            union(u, v)
            mst.append(edge)
            cost += wt

    print('#{} {}'.format(tc+1, cost))