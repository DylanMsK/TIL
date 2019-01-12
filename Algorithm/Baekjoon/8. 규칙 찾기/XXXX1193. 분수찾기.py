# url = 'https://www.acmicpc.net/problem/1193'

n = int(input())

cnt = 1
temp = n
while temp >= cnt:
    temp = temp - cnt
    cnt += 1

print(n, cnt, temp)
if cnt % 2 == 0:
    print(f'{temp+1}/{cnt+1-temp}')
else:
    print(f'{cnt-(temp+1)}/{temp+1}')
