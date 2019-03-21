for _ in range(int(input())):
    num = float(input())
    binary = ''
    while 1:
        num *= 2
        if num >= 1:
            binary += '1'
            num -= 1
        else:
            binary += '0'
        if num == 0:
            break
        if len(binary) == 13:
            binary = 'overflow'
            break

    print(f'#{_+1} {binary}')