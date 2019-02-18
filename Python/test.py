# lst = [1, 2, 3, 4]
# n = len(lst)
# for i in range(1 << n):
#     temp = [0] * n
#     cnt = 0
#     for j in range(n):
#         if i & 1 << j:
#             temp[cnt] = lst[j]
#             cnt += 1
#     if cnt == 3:
#         print(temp[:3])


# def combination(arr, r, M):
#     arr = sorted(arr)
#     def generate(chosen):
#         flag = True
#         if len(chosen) == r:
#             flag = False
#             return

#         start = arr.index(chosen[-1]) + 1 if chosen else 0
#         for nxt in range(start, len(arr)):
#             chosen.append(arr[nxt])
#             generate(chosen)
#             if flag:
#                 if sum(chosen) == M:
#                     break
#             chosen.pop()
#         return chosen
#     result = generate([])
#     return result
# print(combination([5, 6, 7, 8, 9], 3, 21))
