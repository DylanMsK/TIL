# url = 'https://www.acmicpc.net/problem/2669'

arr = [[0] * 100 for i in range(100)]
cnt = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            if arr[y][x] == 1:
                continue
            else:
                arr[y][x] = 1
                cnt += 1

print(cnt)
