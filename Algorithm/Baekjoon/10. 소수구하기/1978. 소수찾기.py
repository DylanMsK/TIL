# url = 'https://www.acmicpc.net/problem/1978'

n = int(input())
lst = list(map(int, input().split()))
cnt = 0
for num in lst:
    if num == 1:
        continue
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    if flag:
        cnt += 1
print(cnt)