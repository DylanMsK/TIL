import sys
sys.stdin = open('input.txt', 'r')


def find_wormhole(table):
    wormhole = {}
    for y in range(len(table)):
        for x in range(len(table)):
            # if table[y][x] in [6, 7, 8, 9, 10]:
            if table[y][x] in ['6', '7', '8', '9', '10']:
                if table[y][x] in wormhole:
                    wormhole[table[y][x]].append((x, y))
                else:
                    wormhole[table[y][x]] = [(x, y)]
    return wormhole


def start(x, y, direction):
    global table, N, wormhole, max_
    block1 = {'right': 'left', 'up': 'down', 'left': 'up', 'down': 'right'}
    block2 = {'right': 'left', 'up': 'right', 'left': 'down', 'down': 'up'}
    block3 = {'right': 'down', 'up': 'left', 'left': 'right', 'down': 'up'}
    block4 = {'right': 'up', 'up': 'down', 'left': 'right', 'down': 'left'}
    block5 = {'right': 'left', 'up': 'down', 'left': 'right', 'down': 'up'}
    init = (x, y)
    sum_ = 0
    while 1:
        # 방향
        if direction == 'up':
            y -= 1
        elif direction == 'right':
            x += 1
        elif direction == 'down':
            y += 1
        else:
            direction == 'left'
            x -= 1
        
        if (x, y) == init:
            if sum_ > max_:
                max_ = sum_
            break

        # 이동
        if x < 0:
            direction = 'right'
            sum_ += 1
            continue
        elif y < 0:
            direction = 'down'
            sum_ += 1
            continue
        elif x >= N:
            direction = 'left'
            sum_ += 1
            continue
        elif y >= N:
            direction = 'up'
            sum_ += 1
            continue
        # elif table[y][x] == 1:
        elif table[y][x] == '1':
            direction = block1[direction]
            sum_ += 1
            continue
        # elif table[y][x] == 2:
        elif table[y][x] == '2':
            direction = block2[direction]
            sum_ += 1
            continue
        # elif table[y][x] == 3:
        elif table[y][x] == '3':
            direction = block3[direction]
            sum_ += 1
            continue
        # elif table[y][x] == 4:
        elif table[y][x] == '4':
            direction = block4[direction]
            sum_ += 1
            continue
        # elif table[y][x] == 5:
        elif table[y][x] == '5':
            direction = block5[direction]
            sum_ += 1
            continue
        # elif table[y][x] == -1:
        elif table[y][x] == '-1':
            if sum_ > max_:
                max_ = sum_
            break
        # elif table[y][x] in [6, 7, 8, 9, 10]:
        elif table[y][x] in ['6', '7', '8', '9', '10']:
            num_wormhole = table[y][x]
            if wormhole[num_wormhole][0] == (x, y):
                x, y = wormhole[num_wormhole][1]
            else:
                x, y = wormhole[num_wormhole][0]
            continue


for tc in range(int(input())):
    N = int(input())
    # table = [list(map(int, input().split())) for _ in range(N)]
    table = [input().split() for _ in range(N)]
    wormhole = find_wormhole(table)
    max_ = 0
    for y in range(N):
        for x in range(N):
            if table[y][x] == '0':
                start(x, y, 'right')
                start(x, y, 'left')
                start(x, y, 'up')
                start(x, y, 'down')
    print(f'#{tc+1} {max_}')