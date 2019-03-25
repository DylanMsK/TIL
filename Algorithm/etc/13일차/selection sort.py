import time
import random

L = list(range(10000))
random.shuffle(L)
lst = L[:]

start = time.time()
# 재귀
def selecting_sort(lst, idx):
    if idx == len(lst)-1:
        return lst
    
    min_idx = lst.index(min(lst[idx:]))
    if lst[idx] > lst[min_idx]:
        lst[idx], lst[min_idx] = lst[min_idx], lst[idx]
    return selecting_sort(lst, idx+1)

# lst = [5, 4, 3, 2, 1]
print(time.time()-start)
print(selecting_sort(lst, 0))


# lst = [5, 4, 3, 2, 1]
lst = L[:]
start = time.time()
# 반복문
for i in range(len(lst)-1):
    min_ = i
    for j in range(i+1, len(lst)):
        if lst[j] < lst[min_]:
            min_ = j
    lst[min_], lst[i] = lst[i], lst[min_]

print(time.time()-start)
print(lst)