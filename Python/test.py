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


# def combination(arr, r):
#     arr = sorted(arr)
#     def generate(chosen):
#         if len(chosen) == r:
#             print(chosen)
#             return

#         start = arr.index(chosen[-1]) + 1 if chosen else 0
#         for nxt in range(start, len(arr)):
#             chosen.append(arr[nxt])
#             generate(chosen)
#             chosen.pop()
#         return chosen
#     generate([])

# print(combination([5, 6, 7, 8, 9], 3))


arr = [i for i in range(1, 11)]
result = []
def powerset(arr, k):
    def backtrack(chosen):
        global cnt
        cnt += 1
        if sum(chosen) > k:
            return
        elif sum(chosen) == k:
            result.append(chosen[::])
            return
        else:
            start = arr.index(chosen[-1])+1 if chosen else 0
            for idx in range(start, len(arr)):
                chosen.append(arr[idx])
                backtrack(chosen)
                chosen.pop()
            return chosen
    backtrack([])

cnt = 0
powerset(arr, 10)
print(result, cnt)
