# url = 'https://www.acmicpc.net/problem/1977'

def ceil(num):
    if num - int(num) > 0:
        num = int(num) + 1
    return int(num)
    

M = int(input())
N = int(input())
min_, sum_ = 0, 0
for idx, num in enumerate(range(ceil(M**0.5), int(N**0.5)+1)):
    if idx == 0:
        min_ = num ** 2
    sum_ += num ** 2

if sum_:
    print(sum_)
    print(min_)
else:
    print(-1)