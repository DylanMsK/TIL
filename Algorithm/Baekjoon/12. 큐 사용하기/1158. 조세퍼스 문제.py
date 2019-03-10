# url = 'https://www.acmicpc.net/problem/1158'

N, M = map(int, input().split())
init = list(range(1, N+1))
num = M - 1
idx = 0
result = [0] * N
while 1:
    temp = init.pop(num)
    result[idx] = temp
    if len(init) == 0:
        break
    idx += 1
    num += M - 1
    if num >= len(init):
        num %= len(init)
    
print('<' + ', '.join([str(i) for i in result]) + '>')