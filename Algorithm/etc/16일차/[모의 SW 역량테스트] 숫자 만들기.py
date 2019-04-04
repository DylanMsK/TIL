for tc in range(int(input())):
    N = int(input())
    operators = list(map(int, input().split()))
    operands = list(map(int, input().split()))

    min_, max_ = 100000000, -100000000
    stack = [(operands[0], 1, operators[0], operators[1], operators[2], operators[3])]
    while stack:
        cal = stack.pop()
        if not -100000000 <= cal[0] <= 100000000:
            continue
        if cal[1] == N:
            if cal[0] > max_:
                max_ = cal[0]
            if cal[0] < min_:
                min_ = cal[0]
            continue
        if cal[2]:
            stack.append((cal[0] + operands[cal[1]], cal[1]+1, cal[2]-1, cal[3], cal[4], cal[5]))
        if cal[3]:
            stack.append((cal[0] - operands[cal[1]], cal[1]+1, cal[2], cal[3]-1, cal[4], cal[5]))
        if cal[4]:
            stack.append((cal[0] * operands[cal[1]], cal[1]+1, cal[2], cal[3], cal[4]-1, cal[5]))
        if cal[5]:
            stack.append((int(cal[0] / operands[cal[1]]), cal[1]+1, cal[2], cal[3], cal[4], cal[5]-1))
    print(f'#{tc+1} {max_-min_}')