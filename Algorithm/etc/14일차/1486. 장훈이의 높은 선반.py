for _ in range(int(input())):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))

    sum_ = sum(lst)
    for i in range(1 << N):
        temp_sum = 0
        for j in range(N):
            if i & 1 << j:
                temp_sum += lst[j]
        if temp_sum >= B:
            if temp_sum == B:
                sum_ = temp_sum
                break
            elif temp_sum < sum_:
                sum_ = temp_sum
    print(f'#{_+1} {sum_ - B}')
    

