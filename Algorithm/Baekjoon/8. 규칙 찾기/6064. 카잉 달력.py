# url = 'https://www.acmicpc.net/problem/6064'

# 다른사람
# T = int(input())
# for t in range(T):
#     M, N, x, y = map(int, input().split())
#     for i in range(0, M*N+1, M):
#         n = i + x-1
#         if n%N == y-1:
#             print(n+1)
#             break
#     if n%N != y-1:
#         print(-1)

t = int(input())

for _ in range(t):
    M, N, x, y = map(int, input().split())
    for i in range(min(M, N), 0, -1):
        if (M % i == 0) & (N % i == 0):
            com = i
            break
    tot = com * (M//com) * (N//com)
    if (M == x) & (N == y):
        print(tot)
    else:
        if M > N:
            M, N, x, y = N, M, y, x
        flag = False
        for i in range((tot//N)):
            temp = (N * i) + y
            if temp % M == x % M:
                result = temp
                flag = True
                break
        if flag:
            print(result)
        else:
            print(-1)


# 시간초과         
# for _ in range(t):
#     M, N, x, y = map(int, input().split())
  
#     cnt = 0
#     m, n = 0, 0
#     while 1:
#         cnt += 1
#         if m < M:
#             m += 1
#         else:
#             m = 1
#         if n < N:
#             n += 1
#         else:
#             n = 1

#         if (m == x) & (n == y):
#             print(cnt)
#             break
    
#         if (m == M) & (n == N):
#             print(-1)
#             break