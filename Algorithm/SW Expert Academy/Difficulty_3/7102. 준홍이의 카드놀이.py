# url = 'https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWkIlHWqBYcDFAXC&categoryId=AWkIlHWqBYcDFAXC&categoryType=CODE'

for _ in range(int(input())):
    N, M = map(int, input().split())
    nums = []
    for i in range(1, N+1):
        for j in range(1, M+1):
            nums.append([i, j])

    num_dict = {}
    for num in nums:
        sum_ = sum(num)
        if sum_ not in num_dict:
            num_dict[sum_] = 0
        num_dict[sum_] += 1

    max_ = max(num_dict.values())
    result = []
    for key in num_dict:
        if num_dict[key] == max_:
            result.append(key)

    print("#{} {}".format(_+1, " ".join([str(i) for i in result])))