import sys
sys.stdin = open('피자_input.txt', 'r')


for _ in range(int(input())):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    pizza = [[num, piz] for num, piz in zip(range(1, M+1), pizza)]
    now, pizza = pizza[:N], pizza[N:]
    while 1:
        if len(now) == 1:
            res = now[0][0]
            break

        if now[0][1] // 2 == 0:
            now.pop(0)
            if pizza:
                now.append(pizza.pop(0))
        else:
            now = now[1:] + [[now[0][0], now[0][1]//2]]

    print(f'#{_+1} {res}')