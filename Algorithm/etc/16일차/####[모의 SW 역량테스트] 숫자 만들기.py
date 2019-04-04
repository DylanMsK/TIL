from itertools import permutations

def get_operator(op_nums):
    operators = []
    for num, op in zip(op_nums, given_ops):
        if num:
            operators += [op] * num
    return operators

def unique_permutations(iterable, r=None):
    previous = tuple()
    for p in permutations(iterable, r):
        if p > previous:
            previous = p
            yield p

given_ops = ['+', '-', '*', '/']
for tc in range(int(input())):
    N = int(input())

    op_nums = list(map(int, input().split()))
    operator s = get_operator(op_nums)

    nums = list(map(int, input().split()))
    # result = []
    min_, max_ = 9 ** N, -(9 ** N)
    for ops in unique_permutations(operators):
        res = nums[0]
        flag = True
        for i in range(N-1):
            if ops[i] == '+':
                res += nums[i+1]
            elif ops[i] == '-':
                res -= nums[i+1]
            elif ops[i] == '*':
                res *= nums[i+1]
            else:
                res //= nums[i+1]
                if res < 0:
                    res += 1
            if not -100000000 <= res <= 100000000:
                flag = False
                break
        # result.append(res)
        # print(ops, res, max_, min_)
        if flag:
            if res > max_:
                max_ = res
            if res < min_:
                min_ = res
    # print(f'#{tc+1} {max(result)-min(result)}')
    print(f'#{tc+1} {max_-min_}')