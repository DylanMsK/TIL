# url = 'https://www.acmicpc.net/problem/2108'


def avg(nums):
    print(round(sum(nums)/n))

def med(nums):
    nums
    print(nums[n//2])

def mode(nums):
    nums_dict = {k: 0 for k in set(nums)}
    for num in nums:
        nums_dict[num] += 1
    
    max_ = 0
    max_list = []
    for i in nums_dict:
        if nums_dict[i] > max_:
            max_ = nums_dict[i]

    for num in nums_dict:
        if nums_dict[num] == max_:
            max_list.append(num)
    max_list.sort()
    if len(max_list) == 1:
        print(max_list[0])
    else:
        print(max_list[1])

def min_max(nums):
    print(max(nums) - min(nums))


n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()

avg(nums)
med(nums)
mode(nums)
min_max(nums)