# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWBnA2jaxDsDFAWr&categoryId=AWBnA2jaxDsDFAWr&categoryType=CODE'

for tc in range(int(input())):
    nums = list(map(int, input().split()))
    nums = [i if i >= 40 else 40 for i in nums]
    print(f'#{tc+1} {sum(nums)//len(nums)}')