import sys
sys.stdin = open('그래프 경로_input.txt', 'r')


for _ in range(int(input())):
    V, E = map(int, input().split())
    route = {k: [] for k in range(1, V+1)}
    for path in range(E):
        i, o = map(int, input().split())
        route[o].append(i)
    start, end = map(int, input().split())

    visited = [0] * (V+1)
    v = end
    visited[v] = 1
    stack = [v]

    flag = 0
    while stack:
        if v == start:
            flag = 1
            break

        if route[stack[-1]]:
            temp = 0
            for i in route[stack[-1]]:
                if visited[i]:
                    continue
                else:
                    temp += 1
                    v = i
                    stack.append(v)
                    visited[v] = 1
                    break
            if temp == 0:
                stack.pop()

        else:
            stack.pop()

    print(f'#{_+1} {flag}')


