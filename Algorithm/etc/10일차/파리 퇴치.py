for _ in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    max_ = 0
    for y in range(N-(M-1)):
        for x in range(N-(M-1)):
            sum_ = 0
            for i in range(M):
                sum_ += sum(arr[y+i][x:x+M])
            if sum_ > max_:
                max_ = sum_

    print("#{} {}".format(_+1, max_))