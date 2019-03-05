for _ in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    edge = [0] * (N+1)
    for node in range(1, N+1):
        edge[node] = lst[node-1]
        if node > 1:
            while node > 1:
                if edge[node//2] > edge[node]:
                    edge[node // 2], edge[node] = edge[node], edge[node // 2]
                if edge[node//2] > edge[(node//2)*2]:
                    edge[node // 2], edge[(node // 2) * 2] = edge[(node//2)*2], edge[node//2]
                node = node // 2
    sum_ = 0
    while N >= 1:
        N = N // 2
        sum_ += edge[N]

    print("#{} {}".format(_+1, sum_))