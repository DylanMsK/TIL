# url = 'https://www.acmicpc.net/problem/1316'

n = int(input())

cnt = 0
for i in range(n):
    string = input()
    wordset = []
    flag = True
    for idx, j in enumerate(string):
        if idx == 0:
            wordset.append(j)
            continue
        if (j != wordset[-1]) & (j in wordset):
            flag = False
            break
        wordset.append(j)    
    if flag:
        cnt += 1

print(cnt)