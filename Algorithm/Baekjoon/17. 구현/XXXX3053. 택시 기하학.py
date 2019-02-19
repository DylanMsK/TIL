# url = 'https://www.acmicpc.net/problem/3053'
import math

r = int(input())

perimeter = 0
start = [0, 1]
x, y = 0, 1
degree = 0
while degree < 360:
    print(x, y)
    nxt_x, nxt_y = r * math.cos(math.radians(degree)), r * math.sin(math.radians(degree))
    perimeter += ((nxt_x-x)**2 + (nxt_y-y)**2) ** 0.5
    x, y = nxt_x, nxt_y
    degree += 1

# for degree in range(0, 360, 0.5):
#     nxt_x, nxt_y = r * math.cos(math.radians(degree)), r * math.sin(math.radians(degree))
#     perimeter += ((nxt_x-x)**2 + (nxt_y-y)**2) ** 0.5
#     x, y = nxt_x, nxt_y
print(perimeter/2)