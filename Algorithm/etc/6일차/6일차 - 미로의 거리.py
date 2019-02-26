import sys
sys.stdin = open('C:\\Users\\student\\Desktop\\github\\TIL\\Algorithm\\etc\\6일차\\미로_input.txt', 'r')


def BFS(x, y, cnt):
    global arr, res
    if not 0 <= x < N or not 0 <= y < N or res or arr[y][x] == '1':
        pass
    else:
        if arr[y][x] == '3':
            res = cnt-1
            return 

        arr[y][x] = '1'
        BFS(x+1, y, cnt+1)
        BFS(x-1, y, cnt+1)
        BFS(x, y+1, cnt+1)
        BFS(x, y-1, cnt+1)

for _ in range(int(input())):
    N = int(input())
    arr = [list(input()) for i in range(N)]
    for y in range(N):
        for x in range(N):
            if arr[y][x] == '2':
                start = (x, y)
                break
    
    cnt = res = 0
    BFS(start[0], start[1], cnt)

    print(f'#{_+1} {res}')