for _ in range(int(input())):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))

    sum_ = sum(lst)
    for i in range(1 << N):
        temp = 0
        for j in range(N):
            if i & 1 << j:
                temp += lst[j]
        if temp >= B:
            if temp == B:
                sum_ = temp
                break
            elif temp < sum_:
                sum_ = temp
    print(f'#{_+1} {sum_ - B}')
    

