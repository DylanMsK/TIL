# url = 'https://www.acmicpc.net/problem/1065'

def h(n):
    if n < 100:
        return 1
    s = str(n)
    dif = []
    for i in range(len(s)-1):
        dif.append(int(s[i])-int(s[i+1]))
    if len(set(dif)) == 1:
        return 1
    return 0

n = int(input())
cnt = 0
for i in range(1, n+1):
    if h(i):
        cnt += 1

print(cnt)