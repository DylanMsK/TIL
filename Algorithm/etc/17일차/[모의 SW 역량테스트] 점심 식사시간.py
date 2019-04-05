def permutation(K):
    lst = [[1], [2]]
    while 1:
        temp = []
        for i in lst:
            temp.append(i+[1])
            temp.append(i+[2])

        lst = temp
        if len(temp[0]) == K:
            break
    return lst

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    stairs = {1: [], 2: []}
    people = []
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 1:
                people.append([x, y])
            elif arr[y][x]:
                if stairs[2]:
                    stairs[1] = (arr[y][x], (x, y))
                else:
                    stairs[2] = (arr[y][x], (x, y))

    print(stairs)
    print(people)

    perm = permutation(len(people))
    for test in perm:
        p = people[:]
        distance = {1: [], 2: []}
        for i, j in zip(p, test):
            if j == 1:
                distance[1].append(abs(i[0]-stairs[1][0]) + abs(i[1]-stairs[1][1]))
            else:
                distance[2].append(abs(i[0]-stairs[2][0]) + abs(i[1]-stairs[2][1]))
        time = 0
        stack = []
        while 1:
            if 0 not in distance[1]:
                time += min(distance[1])
                continue

    print('#{}'.format(tc+1))