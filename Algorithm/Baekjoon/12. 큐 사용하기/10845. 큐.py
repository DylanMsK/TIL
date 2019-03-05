# url = 'https://www.acmicpc.net/problem/10845'

def push(num):
    q.append(int(num))
    return q


def front():
    if len(q) > 0:
        return q[0]
    return -1


def back():
    if len(q) > 0:
        return q[-1]
    return -1


def empty():
    if len(q):
        return 0
    return 1


def pop():
    if len(q) > 0:
        return q.pop(0)
    return -1


def size():
    return len(q)


N = int(input())
q = []
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        push(cmd[1])
    elif cmd[0] == 'front':
        print(front())
    elif cmd[0] == 'back':
        print(back())
    elif cmd[0] == 'size':
        print(size())
    elif cmd[0] == 'empty':
        print(empty())
    elif cmd[0] == 'pop':
        print(pop())
    else:
        print('error')

