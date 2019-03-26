# url = 'https://www.acmicpc.net/problem/1038'

N = int(input())

if N >= 1023:
    print(-1)
else:
    init = list(range(10))
    nums = []
    for i in range(1, 1 << 10):
        temp = ''
        for j in range(10):
            if i & (1 << j):
                temp += str(init[j])
        nums.append(int(temp[::-1]))
    nums.sort()
    print(int(nums[N]))