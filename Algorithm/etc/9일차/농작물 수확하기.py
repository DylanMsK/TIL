# url = 'https://www.acmicpc.net/problem/2636'

for _ in range(int(input())):
    N = int(input())
    arr = [list(map(int, list(input()))) for i in range(N)]

    mid = N // 2
    diff = -1
    sum_ = 0
    for y in range(N):
        if y > mid:
            diff -= 1
        else:
            diff += 1

        sum_ += sum(arr[y][mid-diff:mid+1+diff])

    print("#{} {}".format(_+1, sum_))