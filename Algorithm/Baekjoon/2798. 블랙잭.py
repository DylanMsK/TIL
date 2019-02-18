# url = 'https://www.acmicpc.net/problem/2798'

N, M = map(int, input().split())
lst = list(map(int, input().split()))
result = []
temp = [0] * 3
for i in range(N):
    temp[0] = lst[i]
    for j in range(i+1, N):
        temp[1] = lst[j]
        for k in range(j+1, N):
            temp[2] = lst[k]
            sum_ = sum(temp)
            if sum_ > M:
                continue
            result.append(sum_)
print(max(result))
            


# for i in range(1 << N):
#     tot = 0
#     temp = [0] * N
#     idx = 0
#     for j in range(N):
#         if i & 1 << j:
#             temp[idx] = lst[j]
#             idx += 1
#     if idx == 3:
#         if sum(temp[:idx]) == M:
#             print(M)
#             break