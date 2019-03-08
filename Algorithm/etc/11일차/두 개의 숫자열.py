for _ in range(int(input())):
    N, M = map(int, input().split())
    N_lst = list(map(int, input().split()))
    M_lst = list(map(int, input().split()))

    max_ = 0
    if M >= N:
        for i in range(M-N+1):
            sum_ = 0
            for j in range(N):
                sum_ += M_lst[i+j] * N_lst[j]
            if sum_ > max_:
                max_ = sum_
    else:
        for i in range(N-M+1):
            sum_ = 0
            for j in range(M):
                sum_ += N_lst[i+j] * M_lst[j]
            if sum_ > max_:
                max_ = sum_

    print("#{} {}".format(_+1, max_))