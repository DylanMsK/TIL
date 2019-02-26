import sys
sys.stdin = open('C:\\Users\\student\\Desktop\\github\\TIL\\Algorithm\\etc\\6일차\\노드_input.txt', 'r')

for _ in range(int(input())):
    V, E = map(int, input().split())
    arr = [[0]*V for i in range(V)]
    for i in range(E):
        a, b = map(int, input().split())
        arr[a-1][b-1] = 1
        arr[b-1][a-1] = 1
    S, G = map(int, input().split())

    q = [S]
    visited = [0] * (V+1)
    visited[S] = 1
    cnt = 0
    while q:
        cnt += 1
        nxt = []
        for i in range(len(q)):
            temp = q.pop(0)
            visited[temp] = 1
            for i in range(V):
                if arr[temp-1][i] and not visited[i+1]:
                    nxt.append(i+1)

        if G in nxt:
            break
        if not nxt:
            cnt = 0
            break

        q = nxt[::]

    print(f'#{_+1} {cnt}')