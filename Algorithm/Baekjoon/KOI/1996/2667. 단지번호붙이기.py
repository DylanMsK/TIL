# url = 'https://www.acmicpc.net/problem/2667'

def find(arr):
    for y in range(N):
        for x in range(N):
            if arr[y][x] == '1':
                return (x, y)
    return None

def dangi(x, y):
    global cnt
    if not 0 <= x < N or not 0 <= y < N or arr[y][x] == '0':
        return
    else:
        cnt += 1
        arr[y][x] = '0'
        dangi(x+1, y)
        dangi(x-1, y)
        dangi(x, y+1)
        dangi(x, y-1)

N = int(input())
arr = [list(input()) for _ in range(N)]
dangis = []
while find(arr):
    cnt = 0
    x, y = find(arr)
    dangi(x, y)
    dangis.append(cnt)

print(len(dangis))
for i in sorted(dangis):
    print(i)