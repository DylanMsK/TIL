# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PrmyKAWEDFAUq&categoryId=AV5PrmyKAWEDFAUq&categoryType=CODE'

for _ in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(N):
        min_ = i
        for j in range(i+1, N):
            if nums[j] < nums[min_]:
                min_ = j
        nums[i], nums[min_] = nums[min_], nums[i]


    print(f'#{_+1} {" ".join([str(i) for i in nums])}')