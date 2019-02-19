# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14hwZqABsCFAYD&categoryId=AV14hwZqABsCFAYD&categoryType=CODE'
import sys
sys.stdin = open('/Users/dylan/Desktop/github/TIL/Algorithm/SW Expert Academy/Difficulty_3/input.txt', 'r')

for _ in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    # N = 5
    # arr = [
    #     [0, 1, 2, 0, 1],
    #     [2, 2, 2, 1, 2],
    #     [1, 2, 1, 0, 0],
    #     [0, 0, 0, 2, 0],
    #     [1, 2, 1, 1, 1]
    # ]
    cnt = 0 
    for x in range(N):
        min_, max_ = 0, N-1
        while min_ <= max_:
            temp = arr[min_][x]
            if temp:
                if temp == 1:
                    break
                else:
                    arr[min_][x] = 0
            min_ += 1

        while max_ >= min_:
            temp = arr[max_][x]
            if temp:
                if temp == 2:
                    break
                else:
                    arr[max_][x] = 0
            max_ -= 1

        if max_ == min_:
            continue

        stack = []
        for y in range(min_, max_+1):
            if arr[y][x]:
                if stack:
                    if stack[-1] == 0:
                        stack[-1] = arr[y][x]
                        continue
                    if stack[-1] != arr[y][x]:
                        cnt += 1
                        stack.append(arr[y][x])
                        stack.append(0)
                    else:
                        stack.append(arr[y][x])
                else:
                    stack.append(arr[y][x])

    print(f'#{_+1} {cnt}')
    # break