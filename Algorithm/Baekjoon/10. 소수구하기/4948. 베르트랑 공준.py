# url = 'https://www.acmicpc.net/problem/4948'

while 1:
    n = int(input())
    if n == 0:
        break
    nums = [i if i not in [0, 1] else 0 for i in range((2*n) + 1)]
    cnt = 0
    for i in range(2, 2*n+1):
        if not i:
            continue
        if nums[i] > n:
            cnt += 1
        for j in range(i+i, 2*n+1, i):
            nums[j] = 0
    print(cnt)