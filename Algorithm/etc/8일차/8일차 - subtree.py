def count(node):
    global cnt
    if node:
        cnt += 1
        count(edge[node][0])
        count(edge[node][1])


for _ in range(int(input())):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    edge = [[0, 0] for i in range(max(lst) + 1)]
    for i in range(0, 2*E, 2):
        if edge[lst[i]][0]:
            edge[lst[i]][1] = lst[i+1]
        else:
            edge[lst[i]][0] = lst[i+1]
    
    cnt = 0
    count(N)

    print(f'#{_+1} {cnt}')