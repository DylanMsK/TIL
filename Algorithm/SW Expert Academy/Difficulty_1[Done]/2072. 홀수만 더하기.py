n = int(input())
 
nums = []
for i in range(n):
    nums.append(list(map(int, input().split())))
     
for idx, num in enumerate(nums):
    sum = 0
    for i in num:
        if i % 2 == 1:
            sum += i
    print('#{} {}'.format(idx+1, sum))