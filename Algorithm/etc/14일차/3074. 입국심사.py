for _ in range(int(input())):
    N, M = map(int, input().split())
    times = {}
    for i in range(N):
        temp = int(input())
        if temp not in times:
            times[temp] = 1
        else:
            times[temp] += 1

    l, r = 1, max(times.keys()) * M
    while 1:
        sum_ = 0
        m = (l+r)//2
        for time in times:
            sum_ += (m // time) * times[time]
        if sum_ == M:
            break
        elif sum_ > M:
            r = m
        else:
            l = m
            if r - l == 1:
                m = r
                break
    print(f'#{_+1} {m}')
    
