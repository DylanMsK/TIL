# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18TrIqIwUCFAZN&categoryId=AV18TrIqIwUCFAZN&categoryType=CODE'

def find_next():
    for now in range(1, V+1):
        if work[now][0] == 0:
            return now
 
 
for _ in range(10):
    V, E = map(int, input().split())
    work = {k: [0, []] for k in range(1, V+1)}
 
    lines = list(map(int, input().split()))
    for i in range(0, len(lines), 2):
        work[lines[i]][1].append(lines[i+1])
        work[lines[i+1]][0] += 1
 
    order = []
 
    while 1:
        now = find_next()
        if now == None:
            break
        order.append(now)
        work[now][0] -= 1
        for next in work[now][1]:
            work[next][0] -= 1
 
    print(f'#{_+1} {" ".join([str(i) for i in order])}')