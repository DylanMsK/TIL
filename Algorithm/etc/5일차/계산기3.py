import sys
sys.stdin = open('C:\\Users\\student\\PycharmProjects\\TT\\python5\\계산기3_input.txt', 'r')

for _ in range(10):
    l = int(input())
    string = input()
    stack = [0] * l
    post = [0] * l
    pdx = 0
    sdx = 0
    for s in range(l):
        if '0' <= string[s] <= '9':
            post[pdx] = string[s]
            pdx += 1
            continue
        if string[s] == '(':
            stack[sdx] = string[s]
            sdx += 1
        elif string[s] == ')':
            while 1:
                sdx -= 1
                if stack[sdx] == '(':
                    stack[sdx] = 0
                    break
                post[pdx] = stack[sdx]
                stack[sdx] = 0
                pdx += 1
        elif string[s] == '*':
            if stack[sdx-1] == '*':
                sdx -= 1
                post[pdx] = stack[sdx]
                stack[sdx] = 0
                pdx += 1
            stack[sdx] = string[s]
            sdx += 1
        else:
            if stack[sdx-1] == '*':
                sdx -= 1
                post[pdx] = stack[sdx]
                stack[sdx] = 0
                pdx += 1
            stack[sdx] = string[s]
            sdx += 1

    for s in post:
        if s:
            if '0' <= s <= '9':
                stack[sdx] = s
                sdx += 1
                continue
            if s == '*':
                sdx -= 1
                stack[sdx-1] = int(stack[sdx]) * int(stack[sdx-1])
                stack[sdx] = 0
            else:
                sdx -= 1
                stack[sdx-1] = int(stack[sdx]) + int(stack[sdx-1])
                stack[sdx] = 0

    print(f'#{_+1} {stack[0]}')