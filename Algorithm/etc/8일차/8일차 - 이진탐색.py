def in_order(node):
    global init
    if node > N:
        return
    in_order(node*2)
    edge[node] = init
    init += 1
    in_order(node*2+1)


for _ in range(int(input())):
    N = int(input())
    edge = [0] * (N+1)
    init = 1
    in_order(1)

    print("#{} {} {}".format(_+1, edge[1], edge[N//2]))