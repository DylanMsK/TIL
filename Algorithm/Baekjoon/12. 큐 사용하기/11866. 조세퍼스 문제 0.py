# url = 'https://www.acmicpc.net/problem/11866'

N, M = map(int, input().split())
init = list(range(1, N+1))
idx = 1
result = []
while init:
    temp = init.pop(0)
    if idx % M == 0:
        result.append(temp)
        idx = 1
        continue
    init.append(temp)
    idx += 1

print('<' + ', '.join([str(i) for i in result]) + '>')