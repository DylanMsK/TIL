def my_int(string):
    sum_ = 0
    cnt = 0
    for s in string[::-1]:
        sum_ += (ord(s)-ord('0')) * (10**cnt)
        cnt += 1
    return sum_

for _ in range(my_int(input())):
    s1 = {}
    for i in input():
        if i not in s1:
            s1[i] = 0

    s2 = input()
    for s in s2:
        if s in s1:
            s1[s] += 1

    max_ = 0
    for val in s1.values():
        if val > max_:
            max_ = val

    print(f'#{_+1} {max_}')