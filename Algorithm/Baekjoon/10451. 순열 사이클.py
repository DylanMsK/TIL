# url = 'https://www.acmicpc.net/problem/10451'

for _ in range(int(input())):
    N = int(input())
    nums = list(range(1, N+1))
    squence = {k: 0 for k in nums}
    lst = list(map(int, input().split()))
    for i in nums:
        squence[i] = lst[i-1]

    cnt = 0
    for i in range(N):
        if nums[i]:
            cnt += 1
            temp = [nums[i]]
            while 1:
                nxt = squence[temp[-1]]
                if nxt == temp[0]:
                    break
                nums[nxt-1] = 0
                temp.append(nxt)
    print(cnt)