def danjo(num):
    s_num = str(num)
    for i in range(1, len(s_num)):
        if int(s_num[i]) < int(s_num[i-1]):
            return False
    return True


for _ in range(int(input())):
    N = int(input())
    lst = sorted(list(map(int, input().split())))
    max_ = -1
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            mul = lst[i] * lst[j]
            if danjo(mul):
                if mul > max_:
                    max_ = mul
                    break

    print('#{} {}'.format(_+1, max_))