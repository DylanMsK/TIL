# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14_DEKAJcCFAYD&categoryId=AV14_DEKAJcCFAYD&categoryType=CODE'

for _ in range(10):
    N, nums = input().split()

    stack = [0] * int(N)
    result = ''
    idx = 0
    for i in nums:
        if idx == 0:
            stack[idx] = i
            idx += 1

        else:
            if stack[idx-1] == i:
                idx -= 1
                stack[idx] = 0
            else:
                stack[idx] = i
                idx += 1
    print(f'#{_+1} {"".join(stack[:idx])}')