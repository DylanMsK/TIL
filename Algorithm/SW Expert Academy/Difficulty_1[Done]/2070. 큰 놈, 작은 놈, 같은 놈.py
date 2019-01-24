n = int(input())
 
nums = []
for i in range(n):
    nums.append(list(map(int, input().split())))
     
for idx, num in enumerate(nums):
    if num[0] < num[-1]:
        res = '<'
    elif num[0] == num[-1]:
        res = '='
    else:
        res = '>'
    print('#{} {}'.format(idx+1, res))