# url = 'https://www.acmicpc.net/problem/2981'

nums = []
max_ = 1
for _ in range(int(input())):
    temp = int(input())
    nums.append(temp)
    if temp > max_:
        max_ = temp

result = []
for i in range(max_, 1, -1):
    flag = True
    left = nums[0] % i
    for j in nums[1:]:
        if j % i != left:
            flag = False
            break
    if flag:
        result.append(i)

print(' '.join([str(i) for i in sorted(result)]))