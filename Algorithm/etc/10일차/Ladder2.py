import sys
sys.stdin = open('C:\\Users\\student\\Desktop\\github\\TIL\\Algorithm\\etc\\10일차\\Ladder2_input.txt', 'r')


def go(x, y):
    dx = [1, -1, 0]
    dy = [0, 0, 1]
    cnt, visited = 0, []
    while 1:
        if y == 99:
            break
        visited.append((x, y))
        for diff in range(3):
            nxt_x, nxt_y = x + dx[diff], y + dy[diff]
            if 0 <= nxt_x < 100 and 0 <= nxt_y < 100 and not (nxt_x, nxt_y) in visited and arr[nxt_y][nxt_x]:
                x, y = nxt_x, nxt_y
                cnt += 1
                if diff == 2:
                    visited = []
                break
    return cnt


for _ in range(10):
    tc = input()
    arr = [list(map(int, input().split())) for i in range(100)]

    min_ = 100000
    min_idx = 0
    for idx in range(100):
        if arr[0][idx]:
            cnt = go(idx, 0)
            if cnt < min_:
                min_ = cnt
                min_idx = idx

    print("#{} {}".format(_+1, min_idx))