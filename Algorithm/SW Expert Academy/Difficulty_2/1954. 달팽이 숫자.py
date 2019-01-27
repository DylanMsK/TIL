# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE'


for _ in range(int(input())):
    N = int(input())
    arr = [i for i in range(1, N**2+1)]
    te, be, re, le = -1, N, N, -1
    x, y = -1, 0
    dx, dy = 1, 0
    brr = [[0]*N for i in range(N)]
    for i in arr:
        y, x = y+dy, x+dx
        brr[y][x] = i
        nxt_y, nxt_x = y, x
        if nxt_x + dx == re:
            dx, dy = 0, 1
            te += 1
        if nxt_y + dy == be:
            dx, dy = -1, 0
            re -= 1
        if nxt_x + dx == le:
            dx, dy = 0, -1
            be -= 1
        if nxt_y + dy == te:
            dx, dy = 1, 0
            le += 1

    print(f'#{_+1}')
    for i in brr:
        print(' '.join([str(j) for j in i]))