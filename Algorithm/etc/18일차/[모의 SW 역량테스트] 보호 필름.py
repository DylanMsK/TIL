import itertools
import sys
sys.stdin = open('film_input.txt', 'r')

def test(brr, K, idxs):
    global D, W
    if idxs:
        crr = [brr[row][:] for row in range(W)]

        for y in range(W):
            flag = True
            for x in range(D-K+1):
                for idx in idxs:
                    crr[y][idx] = 0
                if sum(crr[y][x:x+K]) in [0, K]:
                    flag = False
                    break
            if flag:
                break
        if not flag:
            return True

        for y in range(W):
            flag = True
            for x in range(D-K+1):
                for idx in idxs:
                    crr[y][idx] = 1
                if sum(crr[y][x:x+K]) in [0, K]:
                    flag = False
                    break
            if flag:
                return False
        return True
    else:
        for y in range(W):
            flag = True
            for x in range(D-K+1):
                if sum(brr[y][x:x+K]) in [0, K]:
                    flag = False
                    break
            if flag:
                return False
        return True
                

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
        for idxs in itertools.combinations(depth_idx, cnt):
            if test(brr, K, idxs):
                flag = True
                break
        if flag:
            break

    print('#{} {}'.format(tc+1, cnt))




# def protect(array, K):
#     for y in range(len(array)):
#         flag = False
#         for x in range(len(array[0])-K+1):
#             sum_ = sum(array[y][x:x+K])
#             if sum_ == 0 or sum_ == K:
#                 flag = True
#                 break
#         if not flag:
#             return flag
#     return flag


# def test(brr, K, idxs):
#     if idxs:
#         crr = [brr[row][:] for row in range(W)]
#         for row in crr:
#             for idx in idxs:
#                 row[idx] = 0
#         if protect(crr, K):
#             return True
#         for row in crr:
#             for idx in idxs:
#                 row[idx] = 1
#         if protect(crr, K):
#             return True
#         return False
#     else:
#         return protect(brr, K)
                

# for tc in range(int(input())):
#     D, W, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(D)]
#     brr = [[0]*D for _ in range(W)]
#     for y in range(D):
#         for x in range(W):
#             brr[x][y] = arr[y][x]
    
#     cnt = -1
#     depth_idx = list(range(D))
#     flag = False
#     while 1:
#         cnt += 1
#         for idxs in itertools.combinations(depth_idx, cnt):
#             if test(brr, K, idxs):
#                 flag = True
#                 break
#         if flag:
#             break

#     print('#{} {}'.format(tc+1, cnt))