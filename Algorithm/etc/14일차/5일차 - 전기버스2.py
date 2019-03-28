def backtrack(now, cnt):
    global min_
    if cnt >= min_:
        return

    if now >= N-1:
        if cnt < min_:
            min_ = cnt
    else:
        prob = stations[now]
        for i in range(now+prob, now, -1):
            backtrack(i, cnt+1)


for _ in range(int(input())):
    temp = list(map(int, input().split()))
    N = temp[0]
    stations = temp[1:]

    min_ = N
    backtrack(0, -1)

    print(f'#{_+1} {min_}')