# url = 'https://www.acmicpc.net/problem/10866'

def push_front(X):
    global lst
    lst = [X] + lst

def push_back(X):
    global lst
    lst += [X]

def pop_front():
    global lst
    if len(lst):
        print(lst.pop(0))
    else:
        print(-1)

def pop_back():
    global lst
    if len(lst):
        print(lst.pop())
    else:
        print(-1)

def size():
    global lst
    print(len(lst))

def empty():
    global lst
    if len(lst):
        print(0)
    else:
        print(1)

def front():
    global lst
    if len(lst):
        print(lst[0])
    else:
        print(-1)

def back():
    global lst
    if len(lst):
        print(lst[-1])
    else:
        print(-1)

# cmd_dict = {
#     'push_front': push_front(cmd[1]),
#     'push_back': push_back(cmd[1]),
#     'pop_front': pop_front(),
#     'pop_back': pop_back(),
#     'size': size(),
#     'empty': empty(),
#     'front': front(),
#     'back': back()
# }

lst = []
for i in range(int(input())):
    cmd = input().split()
    if cmd[0] == 'push_front':
        push_front(cmd[1])
    elif cmd[0] == 'push_back':
        push_back(cmd[1])
    elif cmd[0] == 'pop_front':
        pop_front()
    elif cmd[0] == 'pop_back':
        pop_back()
    elif cmd[0] == 'size':
        size()
    elif cmd[0] == 'empty':
        empty()
    elif cmd[0] == 'front':
        front()
    else:
        back()


