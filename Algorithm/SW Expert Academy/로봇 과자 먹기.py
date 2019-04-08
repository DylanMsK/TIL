from itertools import permutations

for tc in range(int(input())):
    N = int(input())
    s_init = list(map(int, input().split()))
    r_init = list(map(int, input().split()))
    snacks = []
    robots = []
    for i in range(0, 2*N, 2):
        snacks.append((s_init[i], s_init[i+1]))
        robots.append((r_init[i], r_init[i+1]))
    
    min_ = float('inf')
    for i in permutations(list(range(N))):
        sum_ = 0
        for idx, j in enumerate(i):
            sum_ += abs(snacks[idx][0] - robots[j][0]) + abs(snacks[idx][1] - robots[j][1])
        if sum_ < min_:
            min_ = sum_

    print('#{} {}'.format(tc+1, min_))