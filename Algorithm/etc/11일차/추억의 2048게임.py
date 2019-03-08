# import sys
# sys.stdin = open('C:\\Users\\student\\Desktop\\github\\TIL\\Algorithm\\etc\\11일차\\s_input.txt', 'r')



def left():
    for y in range(N):
        stack = []
        flag = True
        for x in range(N):
            if arr[y][x]:
                if stack:
                    if stack[-1] == arr[y][x] and flag:
                        stack[-1] += arr[y][x]
                        flag = False
                    else:
                        stack.append(arr[y][x])
                        flag = True
                else:
                    stack.append(arr[y][x])
                    flag = True
        for x in range(N):
            if x >= len(stack):
                arr[y][x] = 0
            else:
                arr[y][x] = stack[x]

def right():
    for y in range(N):
        stack = []
        flag = True
        for x in range(N-1, -1, -1):
            if arr[y][x]:
                if stack:
                    if stack[-1] == arr[y][x] and flag:
                        stack[-1] += arr[y][x]
                        flag = False
                    else:
                        stack.append(arr[y][x])
                        flag = True
                else:
                    stack.append(arr[y][x])
                    flag = True
        for x in range(N-1, -1, -1):
            if x < N - len(stack):
                arr[y][x] = 0
            else:
                arr[y][x] = stack[N-1-x]

def up():
    for x in range(N):
        stack = []
        flag = True
        for y in range(N):
            if arr[y][x]:
                if stack:
                    if stack[-1] == arr[y][x] and flag:
                        stack[-1] += arr[y][x]
                        flag = False
                    else:
                        stack.append(arr[y][x])
                        flag = True
                else:
                    stack.append(arr[y][x])
                    flag = True
        for y in range(N):
            if y >= len(stack):
                arr[y][x] = 0
            else:
                arr[y][x] = stack[y]

def down():
    for x in range(N):
        stack = []
        flag = True
        for y in range(N-1, -1, -1):
            if arr[y][x]:
                if stack:
                    if stack[-1] == arr[y][x] and flag:
                        stack[-1] += arr[y][x]
                        flag = False
                    else:
                        stack.append(arr[y][x])
                        flag = True
                else:
                    stack.append(arr[y][x])
                    flag = True
        for y in range(N-1, -1, -1):
            if y < N - len(stack):
                arr[y][x] = 0
            else:
                arr[y][x] = stack[N-1-y]

for _ in range(int(input())):
    temp = input().split()
    N, cmd = int(temp[0]), temp[1]
    arr = [list(map(int, input().split())) for i in range(int(N))]
    if cmd == 'up':
        up()
    elif cmd == 'down':
        down()
    elif cmd == 'right':
        right()
    else:
        left()

    print("#{}".format(_+1))
    for i in arr:
        for j in i:
            print(j, end=' ')
        print()
