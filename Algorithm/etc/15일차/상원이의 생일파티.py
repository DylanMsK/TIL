for tc in range(int(input())):
    N, M = map(int, input().split())

    friends = {k: [] for k in range(1, N+1)}
    for _ in range(M):
        a, b = map(int, input().split())
        if b not in friends[a]:
            friends[a].append(b)
        if a not in friends[b]:
            friends[b].append(a)

    invite = [0] * (N+1)
    for i in friends[1]:
        invite[i] = 1
        for j in friends[i]:
            invite[j] = 1
    invite[1] = 0

    print('#{} {}'.format(tc+1, sum(invite)))