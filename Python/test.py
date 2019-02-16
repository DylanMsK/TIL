import time

n = 100000

# 1. break 없이
# start = time.time()
# temp = []
# for i in range(2, n+1):
#     flag = True
#     for j in range(2, i):
#         if i % j == 0:
#             flag = False
#     if flag:
#         temp.append(i)
#         # print(i)
# # print(temp)
# print(len(temp))
# print(time.time() - start)


# 2. break 추가
start = time.time()
temp = []
for i in range(2, n+1):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        temp.append(i)
        # print(i)
# print(temp)
print(len(temp))
print(time.time() - start)


# 3. 소수로 안나눠지는 수
start = time.time()
temp = [2, 3, 5, 7]
for i in range(8, n+1):
    flag = True
    for j in temp:
        if i % j == 0:
            flag = False
            break
    if flag:
        temp.append(i)
# print(temp)
print(len(temp))
print(time.time() - start)


# 4. 에라토스테네스의 체
start = time.time()
temp = list(0 if i in [0, 1] else i for i in range(n+1))
for i in range(2, round((n+1)**0.5)):
    if i == 0:
        continue
    for j in range(i*2, n+1, i):
        temp[j] = 0

result = [i for i in temp if i != 0]
# print(result)
print(len(result))
print(time.time() - start)