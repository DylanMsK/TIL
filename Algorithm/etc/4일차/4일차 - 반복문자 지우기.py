import sys
sys.stdin = open('반복문자 지우기_input.txt', 'r')

for _ in range(int(input())):
    string = input()
    length = len(string)
    stack = [''] * length
    stack[0] = string[0]
    idx = 0
    for i in range(1, length):
        if string[i] == stack[idx]:
            stack.pop(idx)
            idx -= 1
            continue
        else:
            idx += 1
            stack[idx] = string[i]
    cnt = 0
    for i in stack:
        if i:
            cnt += 1
        else:
            break
    print(f'#{_+1} {cnt}')

