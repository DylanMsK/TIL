def my_int(string):
    sum_ = 0
    cnt = 0
    for s in string[::-1]:
        sum_ += (ord(s)-ord('0')) * (10**cnt)
        cnt += 1
    return sum_


def my_in(iterator, target):
    flag = False
    for i in iterator:
        if target == i:
            flag = True
            break
    return flag

for _ in range(my_int(input())):
    T = input().split()
    print(f'#{_+1}', end=' ')
    sub = list(map(my_int, input().split()))

    for i in range(1, my_int(T[0])+1):
        if not my_in(sub, i):
            print(i, end=' ')
    print()
