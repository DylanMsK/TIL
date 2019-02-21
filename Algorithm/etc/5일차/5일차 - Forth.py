import sys
sys.stdin = open('C:\\Users\\student\\PycharmProjects\\TT\\python5\\Forth_input.txt', 'r')


for _ in range(int(input())):
    string = input().split()
    stack = []
    flag = True
    for s in string:
        if s.isdigit():
            stack.append(int(s))
            continue
        if s == '.':
            break
        if len(stack) < 2:
            flag = False
            break
        if s == '+':
            stack.append(stack.pop() + stack.pop())
        elif s == '*':
            stack.append(stack.pop() * stack.pop())
        elif s == '/':
            stack.append(stack.pop(-2) // stack.pop())
        else:
            stack.append(stack.pop(-2) - stack.pop())

    if flag:
        if len(stack) == 1:
            res = stack[0]
        else:
            res = 'error'
    else:
        res = 'error'

    print(f'#{_+1} {res}')
