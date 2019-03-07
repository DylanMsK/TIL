# url = 'https://www.acmicpc.net/problem/2658'

def eliminateZero(counts):
    for i in range(len(counts)):
        if counts[0] == '1':
            break
        counts.pop(0)
    for j in range(len(counts)):
        if counts[-1] == '1':
            break
        counts.pop()
    return counts

def isPal(counts):
    t = len(counts) // 2
    start = 1
    flag = True
    if t % 2 == 0:
        return False

    for i in range(t):
        if counts[i] == start and counts(-(i+1)) == start:
            start += 1
        else:
            flag = False
    if counts[t] != start:
        flag = False
    if flag:
        return flag
    return flag

def squence(counts):
    if len(counts) <= 1:
        return False

    temp = counts[0] - counts[1]
    for i in range(len(counts)-1):
        if counts[i] - counts[i+1] != temp:
            return False
    return True



arr = [list(input()) for i in range(10)]
counts = [0] * 10
for y in range(10):
    cnt = 0
    for x in range(10):
        if arr[y][x] == '1':
            cnt += 1
    counts[y] = cnt

counts = eliminateZero(counts)
flag = True
if isPal(counts) and squence(counts):
    flag = False

if flag:
    print(0)
    print(counts)
else:
    print('dzdz')
    # if isPal(counts):
    #     for y in range(10):
    #         if arr[y].count('1') == 1:
    #             for x in range(10):
    #                 if arr[y][x] == '1':

        
