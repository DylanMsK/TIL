def post_order(node):
    if node:
        node = int(node)
        post_order(edge[node][1])
        post_order(edge[node][2])
        post.append(edge[node][0])

for _ in range(10):
    N = int(input())
    edge = [[0, 0, 0] for i in range(N+1)]

    for i in range(N):
        temp = list(input().split())
        idx = int(temp[0])
        for j in range(len(temp)-1):
            edge[idx][j] = temp[j+1]
    post = []
    post_order('1')
    stack = []
    while 1:
        if len(post) == 0:
            break
        temp = post.pop(0)
        if temp == '-':
            stack.append(stack.pop(-2) - stack.pop())

        elif temp == '/':
            stack.append(stack.pop(-2) / stack.pop())

        elif temp == '*':
            stack.append(stack.pop() * stack.pop())

        elif temp == '+':
            stack.append(stack.pop() + stack.pop())
        else:
            stack.append(int(temp))

    print("#{} {}".format(_+1, int(stack[0])))