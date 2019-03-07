# url = 'https://www.acmicpc.net/problem/2628'

def find_area(direction, index):
    global squares
    next = []
    while squares:
        square = squares.pop(0)
        # print(square)
        if direction == 1:
            if square[0][0] < index < square[1][0]:
                next.append([square[0], [index, square[1][1]], square[2], [index, square[3][1]]])
                next.append([[index, square[0][1]], square[1], [index, square[2][1]], square[3]])
            else:
                next.append(square)
        else:
            if square[0][1] < index < square[2][1]:
                next.append([square[0], square[1], [square[2][0], index], [square[3][0], index]])
                next.append([[square[0][0], index], [square[1][0], index], square[2], square[3]])
            else:
                next.append(square)
    squares = next[:]


def max_square(squares):
    max_ = 0
    for square in squares:
        area = (square[1][0] - square[0][0]) * (square[3][1] - square[1][1])
        if area > max_:
            max_ = area
    return max_


row, col = map(int, input().split())
N = int(input())
squares = [[[0, 0], [row, 0], [0, col], [row, col]]]
for i in range(N):
    d, idx = map(int, input().split())
    find_area(d, idx)

print(max_square(squares))