# url = 'https://www.acmicpc.net/problem/1966'

for _ in range(int(input())):
    N, M = map(int, input().split())
    lst = [[idx, w] for idx, w in zip(range(N), list(map(int, input().split())))]

    cnt = 0
    while 1:
        max_ = max(lst, key=lambda x: x[1])[1]
        first = lst.pop(0)
        if first[1] >= max_:
            cnt += 1
            if first[0] == M:
                break
        else:
            lst.append(first)

    print('{}'.format(cnt))