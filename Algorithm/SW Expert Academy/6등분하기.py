def calc(row, col1, col2):
    global arr, max_
    nums = [0] * 6
    for y in range(N):
        for x in range(M):
            if y < row and x < col1:
                nums[0] += arr[y][x]
            elif y < row and col1 <= x < col2:
                nums[1] += arr[y][x]
            elif y < row and col2 <= x:
                nums[2] += arr[y][x]
            elif y >= row and x < col1:
                nums[3] += arr[y][x]
            elif y >= row and col1 <= x < col2:
                nums[4] += arr[y][x]
            elif y >= row and col2 <= x:
                nums[5] += arr[y][x]
            else:
                print('?????')

    for i in range(4):
        for j in range(i+1, 5):
            for k in range(j+1, 6):
                sum_ = abs(nums[i]-nums[j]) + abs(nums[i]-nums[k]) + abs(nums[j]-nums[k])
                if sum_ > max_:
                    max_ = sum_


for _ in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]

    max_ = 0
    for row in range(1, N):
        for col1 in range(1, M-1):
            for col2 in range(col1+1, M):
                calc(row, col1, col2)

    print(f'#{_+1} {max_}')