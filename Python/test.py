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


def merge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right

    return result


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


lst = [69, 10, 30, 2, 16, 8, 31, 22]

print(merge_sort(lst))