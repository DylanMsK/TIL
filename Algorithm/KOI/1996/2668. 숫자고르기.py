# url = 'https://www.acmicpc.net/problem/2668'

N = int(input())
num_dic = {i: 0 for i in range(1, N+1)}
for i in range(N):
    num_dic[i+1] = int(input())

result = []
start = 1
for i in range(1, N+1):
    if i in result:
        continue

    if num_dic[i] == i:
        result.append(i)
    else:
        temp = [i]
        cnt = 1
        while cnt <= N:
            t = num_dic[temp[-1]]
            if t == temp[0]:
                for j in temp:
                    result.append(j)
                break
            temp.append(t)
            cnt += 1

print(len(result))
for i in sorted(result):
    print(i)
