node = '1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7'
node = list(map(int, node.split(', ')))
arr = [[0] * 7 for i in range(7)]

for i in range(0, len(node), 2):
    arr[node[i]-1][node[i+1]-1] = 1
    arr[node[i+1]-1][node[i]-1] = 1

start = 1
visited = []
# visited.append(start)
# q = [0] * 14
q = []
q.append(start)
while len(visited) < 7:
    for i in range(7):
        if arr[q[0]-1][i] != 0:
            if i+1 in visited:
                continue
            else:
                q.append(i+1)
    visited.append(q.pop(0))
print(visited)
    
    