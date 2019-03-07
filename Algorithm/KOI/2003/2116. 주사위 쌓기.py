# url = 'https://www.acmicpc.net/problem/2116'

find_top = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

N = int(input())
cubic = [list(map(int, input().split())) for i in range(N)]
result = 0
for num in range(1, 7):
    sum_ = 0
    top_num = num
    for c in cubic:
        bottom = c.index(top_num)
        top = find_top[bottom]
        top_num = c[top]
        max_ = 0
        for i in c:
            if i in [c[top], c[bottom]]:
                continue
            if i > max_:
                max_ = i
        sum_ += max_
    if sum_ > result:
        result = sum_
print(result)