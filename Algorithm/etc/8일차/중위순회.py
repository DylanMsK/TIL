def in_order(node):
    if node:
        node = int(node)
        in_order(edge[node][1])
        result.append(edge[node][0])
        in_order(edge[node][2])


for _ in range(10):
    N = int(input())
    edge = [['', '', ''] for i in range(N+1)]
    for i in range(N):
        temp = list(input().split())
        idx = int(temp[0])
        for j in range(len(temp)-1):
            edge[idx][j] = temp[j+1]
    result = []
    in_order('1')
    print("#{} {}".format(_+1, "".join(result)))