def GCD(lst):
    if 1 in lst:
        return 1

    for i in range(min(lst), 0, -1):
        temp = []
        for j in lst:
            if j % i == 0:
                temp.append(j)
            else:
                break
        if len(temp) == len(lst):
            gcd = i
            break
        
    return gcd


def LCM(lst):
    for i in range(2, max(lst)):
        common = 1
        cnt = 0
        for j in lst:
            if j == 1:
                continue
            if j % i == 0:
                cnt += 1
        if cnt >= 2:
            common = i
            next_lst = [e // i if e % i == 0 else e for e in lst]
            break
    if cnt < 2:
        last = 1
        for i in lst:
            last = last * i
        return last
    return common * LCM(next_lst)
        

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(GCD(lst))
print(LCM(lst))
