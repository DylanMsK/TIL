# url = 'https://www.acmicpc.net/problem/1874'

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

stack = []
result = []
num = 0
flag = True
for i in lst:
    if stack:
        if i < stack[-1]:
            flag = False
            print('NO')
            break
        if stack[-1] == i:
            result.append('-')
            stack.pop()
            continue
        else:
            while 1:
                num += 1
                stack.append(num)
                result.append('+')
                if stack[-1] == i:
                    result.append('-')
                    stack.pop()
                    break
    else:
        while 1:
            num += 1
            stack.append(num)
            result.append('+')
            if stack[-1] == i:
                result.append('-')
                stack.pop()
                break

if flag:
    for i in result:
        print(i)
