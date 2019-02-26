# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD&categoryId=AV15B1cKAKwCFAYD&categoryType=CODE'

import sys
sys.stdin = open('Contact_input.txt', 'r')

for _ in range(10):
    tot, start = map(int, input().split())
    lst = list(map(int, input().split()))

    emg_dict = {}
    for i in range(0, tot, 2):
        if lst[i] in emg_dict:
            emg_dict[lst[i]].append(lst[i+1])
        else:
            emg_dict[lst[i]] = [lst[i+1]]

    visited = []
    idx = 0
    q = [start]
    while 1:
        max_ = max(q)
        for i in q:
            if i in visited:
                continue
            else:
                visited.append(i)
        temp = []
        for i in q:
            if i in emg_dict:
                for j in emg_dict[i]:
                    if j not in visited:
                        temp.append(j)
            else:
                continue

        q = temp[::]
        if not temp:
            break

    print(f'#{_+1} {max_}')