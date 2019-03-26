# url = 'https://www.acmicpc.net/problem/11047'

N, K = map(int, input().split())
money = []
for _ in range(N):
    money.append(int(input()))

cnt = 0
for i in money[::-1]:
    if K >= i:
        cnt += K // i
        K = K % i
    else:
        continue
    if K == 0:
        break
        
print(cnt)