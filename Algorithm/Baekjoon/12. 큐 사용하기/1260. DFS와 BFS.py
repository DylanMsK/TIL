# url = 'https://www.acmicpc.net/problem/1260'

def DFS(now):
    if visited[now]:
        return
    stack.append(now)
    visited[now] = 1
    next = sorted(edge[now])
    for i in next:
        DFS(i)


def BFS(node):
    q = [node]

    while len(q) > 0:
        x = q.pop(0)
        stack.append(x)
        next = sorted(edge[x])
        for i in next:
            if i not in stack and i not in q:
                q.append(i)


N, M, V = map(int, input().split())
edge = {k: [] for k in range(1, N+1)}
for i in range(M):
    a, b = map(int, input().split())
    if b not in edge[a]:
        edge[a].append(b)
    if a not in edge[b]:
        edge[b].append(a)

visited = [0] * (N+1)
stack = []
DFS(V)
print(" ".join(str(i) for i in stack))

stack = []
BFS(V)
print(" ".join(str(i) for i in stack))
