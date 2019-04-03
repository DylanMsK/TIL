def dfs(month, sum_, buy):
    global min_, d1, m1, m3

    if month > 11:
        if sum_ < min_:
            min_ = sum_
        return

    if days[month] == 0:
        dfs(month+1, sum_, buy)
    else:
        dfs(month+1, sum_+(d1*days[month]), buy+[d1])
        dfs(month+1, sum_+m1, buy+[m1])
        dfs(month+1, sum_+m3, buy+[m3])
        dfs(month+2, sum_+m3, buy+[m3])
        dfs(month+3, sum_+m3, buy+[m3])


for tc in range(int(input())):
    d1, m1, m3, y1 = map(int, input().split())
    days = list(map(int, input().split()))
    min_ = y1
    dfs(0, 0, [])

    # day = 0
    # q = []
    # while day != 11:
    #     if days[day]:
    #         if q:
    #             nxt = []
    #             while q:
    #                 temp = q.pop(0)
    #                 nxt += [temp, temp+(d1*days[day]), temp+m1, temp+m3]
    #         else:
    #             q += [d1*days[day], m1, m3]
    #     days += 1




    print(f'#{tc+1} {min_}')