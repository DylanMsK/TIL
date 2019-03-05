# url = 'https://www.acmicpc.net/problem/2635'

N = int(input())
second = N

max_ = 0
lst = []
while second >= 0:
    temp = [N, second]
    next = temp[-2] - temp[-1]
    while 1:
        if next < 0:
            break
        temp.append(next)
        next = temp[-2] - temp[-1]
    # print(temp)
    if len(temp) > max_:
        max_ = len(temp)
        lst = temp
    second -= 1

print(max_)
print(" ".join(str(i) for i in lst))

