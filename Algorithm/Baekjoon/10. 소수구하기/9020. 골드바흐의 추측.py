# url = 'https://www.acmicpc.net/problem/9020'

for _ in range(int(input())):
    n = int(input())
    nums = [i if i not in [0, 1] else 0 for i in range(n)]

    for i in range(2, n):
        if nums[i] == 0:
            continue
        for j in range(i+i, n, i):
            nums[j] = 0

    result = [i for i in nums if i != 0]
    length = len(result)
    idx = -1
    for i in result:
        if i > n // 2:
            break
        idx += 1
        
    flag = False
    for i in range(idx, -1, -1):
        for j in range(idx, length):
            if result[i] + result[j] == n:
                flag = True
                print(result[i], result[j])
                break
        if flag:
            break