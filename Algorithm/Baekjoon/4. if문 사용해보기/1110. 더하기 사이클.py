# url = 'https://www.acmicpc.net/problem/1110'

init = input()
if len(init) == 1:
    init = '0' + init
cnt = 0
temp = init
while 1:
    cnt += 1
    sum_ = str(int(temp[0]) + int(temp[-1]))
    nxt = temp[-1] + sum_[-1]
    if nxt == init:
        break
    temp = nxt
print(cnt)