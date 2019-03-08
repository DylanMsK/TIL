# url = 'https://www.acmicpc.net/problem/2304'

N = int(input())
lst = sorted([list(map(int, input().split())) for i in range(N)], key=lambda x: x[0])
print(lst)
max_ = max(lst, key=lambda x: x[1])[0]
# print(max_)
sum_ = 0
now = 0
for i in range(, max_):
    if lst[i][1] > now:
        now = lst[i][1]
    print(now)
    sum_ += now
print(sum_)