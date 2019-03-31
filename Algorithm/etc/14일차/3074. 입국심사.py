for _ in range(int(input())):
    N, M = map(int, input().split())
    lst = []
    for i in range(N):
        lst.append(int(input()))

    l, r = 1, max(lst) * M
    while 1:
        sum_ = 0
        m = (l+r)//2
        for time in lst:
            sum_ += (m // time)
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
    
