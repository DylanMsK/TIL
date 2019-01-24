n = int(input())
 
nums = []
for i in range(n):
    nums.append(list(map(int, input().split())))
 
for idx, num in enumerate(nums):
    print('#{} {}'.format(idx+1, max(num)))