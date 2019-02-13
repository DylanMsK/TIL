# url = 'https://www.acmicpc.net/problem/2750'


# Bubble sorting
nums = []
n = int(input())
for _ in range(n):
    nums.append(int(input()))

for i in range(n-1):
    for j in range(i+1, n):
        if nums[j] < nums[i]:
            nums[i], nums[j] = nums[j], nums[i]

for i in nums:
    print(i)