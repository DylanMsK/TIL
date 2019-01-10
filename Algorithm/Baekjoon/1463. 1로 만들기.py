# url = 'https://www.acmicpc.net/problem/1463'


x = int(input())

cnt = 0


while x != 1:
    cnt += 1
    if x & (x-1) == 0:
        x = x // 2
    if x % 3 == 0:
        x = x // 3
        print(f'횟수: {cnt}, x: {x}')
    elif (x+1) % 3 == 0:
        x -= 1
        print(f'횟수: {cnt}, x: {x}')
    elif ((x+2) % 3) == 0 & ((x+2) % 2 == 0):
        x -= 1
        print(f'횟수: {cnt}, x: {x}')
    else:
        x = x / 2
        print(f'횟수: {cnt}, x: {x}')

print(cnt)