# url = 'https://www.acmicpc.net/problem/2504'

ps = input()
tot = 1
stack = [0] * len(ps)
idx = 0
flag = True
for s in ps:
    if s == '(':
        temp = 1
        stack[idx] = 2
        idx += 1
    elif s == '[':
        temp = 1 
        stack[idx] = 3
        idx += 1

    elif s == ')':
        if stack[0]:
            idx -= 1
            if stack[idx] == 2:
                stack[idx] = 0
                temp = temp * 2
                
                continue
            elif stack[idx] == 3:
                flag = False
                break
            else:
                flag = False
                break
        else:
            flag = False
            break
    elif s == ']':
        if stack[0]:
            idx -= 1
            if stack[idx] == 3:
                stack[idx] = 0
                tot = tot * 3
                continue
            elif stack[idx] == 2:
                flag = False
                break
            else:
                flag = False
                break
        else:
            flag = False
            break
if flag:
    print(tot)
else:
    print(0)