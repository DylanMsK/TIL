import sys
sys.stdin = open('input.txt', 'r')


def mask_generator(K):
    l = 2*K-1
    mask = [[0]*(l) for _ in range(l)]
    mid = (l)//2
    for y in range(l):
        if y <= mid:
            for x in range(l):
                if mid-y <= x < mid+1+y:
                    mask[y][x] = 1
        else:
            for x in range(l):
                if mid-(l-1-y) <= x < mid+1+(l-1-y):
                    mask[y][x] = 1
    
    relative_location = []
    for y in range(l):
        for x in range(l):
            if mask[y][x]:
                relative_location.append((x-mid, y-mid))
    
    return (K*K+(K-1)*(K-1), relative_location)


for tc in range(int(input())):
    N, M = map(int, input().split())
    target = [list(map(int, input().split())) for _ in range(N)]
    num_house = 0
    for i in target:
        num_house += sum(i)

    max_ = 0
    for k in range(N+1, 0, -1):
        if num_house*M - (k**2+(k-1)**2) < 0:
            continue
        profit, mask = mask_generator(k)
        for y in range(N):
            for x in range(N):
                sum_ = 0
                for point in mask:
                    if 0 <= x+point[0] < N and 0 <= y+point[1] < N and target[y+point[1]][x+point[0]]:
                        sum_ += 1
                if M*sum_ - profit >= 0 and sum_ > max_:
                    max_ = sum_

    print(f'#{tc+1} {max_}')