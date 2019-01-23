arr = list(range(1, 26))
brr = [[0]*5 for _ in range(5)]

x, y = -1, 0
dx, dy = 1, 0
l_end, t_end, r_end, b_end = -1, -1, 5, 5

for i in arr:
    x, y = x+dx, y+dy
    brr[y][x] = i
    nxt_x, nxt_y = x + dx, y + dy
    if nxt_x == r_end:
        dx, dy = 0, 1
        t_end += 1
    elif nxt_y == b_end:
        dx, dy = -1, 0
        r_end -= 1
    elif nxt_x == l_end:
        dx, dy = 0, 1
        b_end -= 1
    elif nxt_y == t_end:
        dx, dy = 1, 0
        l_end += 1

print(brr)