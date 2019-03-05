def complete(node):
    global sum_
    if node > N:
        return
    complete(node * 2)
    complete(node * 2 + 1)
    sum_ += edge[node]

for _ in range(int(input())):
    N, M, L = map(int, input().split())
    edge = [0 for i in range(N+1)]
    for i in range(M):
        node, num = map(int, input().split())
        edge[node] = num

    sum_ = 0
    complete(L)

    print("#{} {}".format(_+1, sum_))