# url = 'https://www.acmicpc.net/problem/9012'

for _ in range(int(input())):
    ps = input()
    stack = [0] * len(ps)
    idx = 0
    flag = True
    for s in ps:
        if s == '(':
            stack[idx] = 1
            idx += 1
        else:
            if stack[0]:
                idx -= 1
                stack[idx] = 0
            else:
                flag = False

    if flag and stack[0] == 0:
        print('YES')
    else:
        print('NO')