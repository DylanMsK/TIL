# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWD3Y27q3QIDFAUZ&categoryId=AWD3Y27q3QIDFAUZ&categoryType=CODE'

init = [0, 1, 1, 1, 2, 2]
nums = init + [0] * (101-len(init))
for i in range(len(init), 101):
    nums[i] = nums[i-1] + nums[i-5]
    
for tc in range(int(input())):
    N = int(input())
    print('#{} {}'.format(tc+1, nums[N]))