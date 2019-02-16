# url = 'https://www.acmicpc.net/problem/1929'

M, N = map(int, input().split())

nums = list(i if i not in [0, 1] else 0 for i in range(N+1))
for i in range(2, N+1):
    if i == 0:
        continue
    for j in range(i+i, N+1, i):
        nums[j] = 0

for i in range(M, N+1):
    if nums[i]:
        print(nums[i])
