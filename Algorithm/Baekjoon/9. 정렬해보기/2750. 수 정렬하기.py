# url = 'https://www.acmicpc.net/problem/2750'
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

# Bubble sorting
for i in range(n-1):
    for j in range(i+1, n):
        if nums[j] < nums[i]:
            nums[i], nums[j] = nums[j], nums[i]

for i in nums:
    print(i)


# Insertion sorting
for i in range(1, n):
    for j in range(i, 0, -1):
        print(nums)
        if nums[j] < nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
        else:
            break

for i in nums:
    print(i)