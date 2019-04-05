import itertools


def protect(array, K):
    for y in range(len(array)):
        flag = False
        for x in range(len(array[0])-K+1):
            sum_ = sum(array[y][x:x+K])
            if sum_ == 0 or sum_ == K:
                flag = True
                break
        if not flag:
            return flag
    return flag


def test(brr, K, idxs):
    global D
    if idxs:
        crr = [brr[row][:] for row in range(W)]
        for idx in idxs:
            crr[idx] = [0] * D
            # for row in crr:
            #     row = [0] * D
        print('{} crr'.format(idxs))
        for i in crr:
            print(i)
        drr = [brr[row][:] for row in range(W)]
        for idx in idxs:
            drr[idx] = [0] * D
            # for row in drr:
                # row[idx] = 1
        print('{} drr'.format(idxs))
        for i in drr:
            print(i)
        return protect(crr, K) and protect(drr, K)
    else:
        for i in brr:
            print(i)
        return protect(brr, K)
                

for tc in range(int(input())):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]
    brr = [[0]*D for _ in range(W)]
    for y in range(D):
        for x in range(W):
            brr[x][y] = arr[y][x]
    
    cnt = -1
    depth_idx = list(range(D))
    flag = False
    while 1:
        cnt += 1
        print('+++++++++++++{}+++++++++++++'.format(cnt))
        for idxs in itertools.combinations(depth_idx, cnt):
            if test(brr, K, idxs):
                print(idxs, cnt)
                flag = True
                break
        if flag:
            break


    print('#{} {}'.format(tc+1, cnt))