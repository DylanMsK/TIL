# url = 'https://www.acmicpc.net/problem/2504'

ps = input()
stack = []
flag = True
for bracket in ps:
    if bracket in ['(', '[']:
        stack.append(bracket)
    else:               # 닫는 괄호
        if stack:       # 열린 괄호가 있을때
            if bracket == ')':
                if stack[-1] == '(':
                    stack[-1] = 2
                elif isinstance(stack[-1], int):
                    temp = 0
                    while 1:
                        temp += stack.pop()
                        if stack:
                            if isinstance(stack[-1], int):
                                continue
                            elif stack[-1] == '(':
                                stack[-1] = temp * 2
                                break
                            else:
                                flag = False
                                break
                        else:
                            flag = False
                            break
                else:
                    flag = False
                    break

            elif bracket == ']':
                if stack[-1] == '[':
                    stack[-1] = 3
                elif isinstance(stack[-1], int):
                    temp = 0
                    while 1:
                        temp += stack.pop()
                        if stack:
                            if isinstance(stack[-1], int):
                                continue
                            elif stack[-1] == '[':
                                stack[-1] = temp * 3
                                break
                            else:
                                flag = False
                                break
                        else:
                            flag = False
                            break
                else:
                    flag = False
                    break

        else:           # 열린 괄호가 없을때
            flag = False
            break

    if flag:
        continue
    else:
        flag = False
        break

for i in stack:
    if not isinstance(i, int):
        flag = False
        break

if flag:
    print(sum(stack))
else:
    print(0)


# tot = 1
# stack = [0] * len(ps)
# idx = 0
# flag = True
# for s in ps:
#     if s == '(':
#         temp = 1
#         stack[idx] = 2
#         idx += 1
#     elif s == '[':
#         temp = 1 
#         stack[idx] = 3
#         idx += 1

#     elif s == ')':
#         if stack[0]:
#             idx -= 1
#             if stack[idx] == 2:
#                 stack[idx] = 0
#                 temp = temp * 2

#                 continue
#             elif stack[idx] == 3:
#                 flag = False
#                 break
#             else:
#                 flag = False
#                 break
#         else:
#             flag = False
#             break
#     elif s == ']':
#         if stack[0]:
#             idx -= 1
#             if stack[idx] == 3:
#                 stack[idx] = 0
#                 tot = tot * 3
#                 continue
#             elif stack[idx] == 2:
#                 flag = False
#                 break
#             else:
#                 flag = False
#                 break
#         else:
#             flag = False
#             break
# if flag:
#     print(tot)
# else:
#     print(0)