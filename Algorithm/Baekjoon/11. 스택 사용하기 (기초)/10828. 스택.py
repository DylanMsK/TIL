# url = 'https://www.acmicpc.net/problem/10828'

def push(num):
    stack.append(num)

def pop():
    global stack
    temp = -1
    if stack:
        temp = stack[-1]
        stack = stack[:-1]
    return temp

def size():
    cnt = 0
    for i in stack:
        if i == 0:
            break
        cnt += 1
    return cnt

def empty():
    if stack:
        return 0
    return 1

def top():
    if stack:
        return stack[-1]
    return -1

stack = []
for _ in range(int(input())):
    cmd = input().split()

    if cmd[0] == 'push':
        push(int(cmd[1]))

    elif cmd[0] == 'top':
        print(top())
    
    elif cmd[0] == 'size':
        print(size())
    
    elif cmd[0] == 'empty':
        print(empty())
    else:
        print(pop())