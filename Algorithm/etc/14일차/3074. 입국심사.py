def min_com(lst):
    min_ = min(lst)
    com = 1
    for i in range(min_, 1, -1):
        flag = True
        for j in lst:
            if j % i != 0:
                flag = False
                break
        if flag:
            com = i
            break
    min_com = com
    for i in lst:
        min_com *= i // com
    return min_com


for _ in range(int(input())):
    N, M = map(int, input().split())
    lst = []
    for i in range(N):
        lst.append(int(input()))

    # time = 0    
    # com = min_com(lst)
    # if M >= com:
    #     num_per_cycle = 0
    #     for i in lst:
    #         num_per_cycle += com // i
    #     time += num_per_cycle * (M // com)
    #     M = com % num_per_cycle
    
    time = 0
    temp = lst[:]
    while M > 0:
        min_ = min(temp)
        time += min_
        M -= temp.count(min_)
        for i in range(N):
            temp[i] -= min_
            if temp[i] == 0:
                temp[i] = lst[i]
    print(f'#{_+1} {time}')
    
