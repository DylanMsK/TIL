for _ in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()

    cnt = 0
    for num in B:
        l, r = 0, N-1
        flag = False
        # m = (l + r) // 2
        # if A[m] > num:
        #     now = 1
        # elif A[m] < num:
        #     now = -1
        # else:
        #     cnt += 1
        #     continue

        while 1:
            m = (l + r) // 2
            if A[m] > num:
                if now > 0:
                    now *= -1
                    r = m - 1
                else:
                    break
            elif A[m] < num:
                if now < 0:
                    now *= -1
                    l = m + 1
                else:
                    break
            else:
                flag = True
                break
        if flag:
            cnt += 1
        
    print(f'#{_+1} {cnt}')