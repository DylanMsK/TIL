import sys
sys.stdin = open('괄호검사_input.txt', 'r')


for _ in range(int(input())):
    string = input()
    stack = []

    flag = 1
    for s in string:
        if s == '(':
            stack.append(1)
        elif s == ')':
            if stack:
                if stack[-1] == 1:
                    stack.pop()
                else:
                    flag = 0
                    break
            else:
                flag = 0
                break

        if s == '{':
            stack.append(2)
        elif s == '}':
            if stack:
                if stack[-1] == 2:
                    stack.pop()
                else:
                    flag = 0
                    break
            else:
                flag = 0
                break
    if stack:
        flag = 0

    print(f'#{_+1} {flag}')