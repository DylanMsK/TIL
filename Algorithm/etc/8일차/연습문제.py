def pre_order(node):
    if node:
        print(node, end=' ')
        pre_order(arr[node][0])
        pre_order(arr[node][1])

def post_order(node):
    if node:
        post_order(arr[node][0])
        post_order(arr[node][1])
        print(node, end=' ')

def in_order(node):
    if node:
        in_order(arr[node][0])
        print(node, end=' ')
        in_order(arr[node][1])


edge = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
edge = list(map(int, edge.split()))

arr = [[0, 0, 0] for i in range((max(edge) + 1))]

for i in range(0, len(edge), 2):
    if arr[edge[i]][0]:
        arr[edge[i]][1] = edge[i+1]
    else:
        arr[edge[i]][0] = edge[i+1]
        arr[edge[i]][2] = edge[i]


pre_order(1)
print()
post_order(1)
print()
in_order(1)
