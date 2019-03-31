# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV_6mRsasV8DFAWS&categoryId=AV_6mRsasV8DFAWS&categoryType=CODE'

lst = [i if i != 1 else 0 for i in range(1000001)]
for i in range(int(len(lst) ** 0.5)):
    if lst[i] == 0:
        continue
    for j in range(i+i, len(lst), i):
        lst[j] = 0

for i in lst:
    if i:
        print(i, end=' ')
print()