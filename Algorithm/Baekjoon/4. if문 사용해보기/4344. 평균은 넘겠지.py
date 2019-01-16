# url = 'https://www.acmicpc.net/problem/4344'

T = int(input())

for _ in range(T):
    temp = list(map(int, input().split()))
    N, nums = temp[0], temp[1:]
    l = len([i for i in nums if i > sum(nums)/N])
    print("%.3f"%(l/N*100) + '%')